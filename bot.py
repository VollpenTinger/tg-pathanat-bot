import asyncio
import os
import random
import re
from typing import List, Dict, Any

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton,
    FSInputFile
)

# ======================================================
# НАСТРОЙКА ТОКЕНА
# ======================================================

# ⚠️ Для простоты токен сейчас захардкожен.
# Перед финальным публичным использованием лучше:
# 1) сгенерировать новый токен в @BotFather
# 2) читать его из переменной окружения BOT_TOKEN.
BOT_TOKEN = "8245340349:AAF2sB8Gn5dXiqQQ1ldxAHqk_wpsdcLrH2c"

if not BOT_TOKEN:
    raise RuntimeError("Не указан BOT_TOKEN")

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Папка с файлами препаратов
PREPARATS_DIR = "preparats"

# Список препаратов будем заполнять автоматически
SPECIMENS: List[Dict[str, Any]] = []

# user_id -> состояние
user_state: Dict[int, Dict[str, Any]] = {}


# ======================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ======================================================

def normalize_text(text: str) -> str:
    """Упростить строку для сравнения ответов."""
    return (
        text.strip()
        .lower()
        .replace("ё", "е")
    )


def humanize_name(base: str) -> str:
    """
    Делает человеческое название из имени файла:
    'amiloidoz_pecheni' -> 'Amiloidoz pecheni'
    'serozno_gemorragicheskaya_pnevmoniya' -> 'Serozno gemorragicheskaya pnevmoniya'
    """
    name = base.replace("_", " ").strip(" .")
    if not name:
        return "Neizvestnyi preparat"
    return name[0].upper() + name[1:]


def load_specimens_from_folder(folder: str = PREPARATS_DIR) -> List[Dict[str, Any]]:
    """
    Сканирует папку с файлами:
    - берёт только .jpg/.jpeg/.png
    - группирует картинки по базе имени БЕЗ номера в конце.
    Пример:
        'amiloidoz_pecheni_1.jpeg'
        'amiloidoz_pecheni_2.jpeg'
    -> база: 'amiloidoz_pecheni'
    """
    if not os.path.exists(folder):
        print(f"Папка '{folder}' не найдена, создаю пустую.")
        os.makedirs(folder, exist_ok=True)
        return []

    groups: Dict[str, List[str]] = {}

    for fname in os.listdir(folder):
        if fname.startswith("."):
            continue

        lower = fname.lower()
        if not (lower.endswith(".jpg") or lower.endswith(".jpeg") or lower.endswith(".png")):
            continue

        full_path = os.path.join(folder, fname)
        stem, _ext = os.path.splitext(fname)
        stem = stem.strip()

        # отрезаем номер в конце: *_1, *_2, *_3 и т.п.
        m = re.match(r"^(.*?)[ _\.-]?(\d+)$", stem)
        if m:
            base = m.group(1)
        else:
            base = stem

        base = base.strip(" _.-")
        if not base:
            base = stem

        groups.setdefault(base, []).append(full_path)

    specimens: List[Dict[str, Any]] = []
    current_id = 1

    for base_name in sorted(groups.keys(), key=lambda x: x.lower()):
        images = sorted(groups[base_name])
        display_name = humanize_name(base_name)

        specimen = {
            "id": current_id,
            "name": display_name,
            "difficulty": "easy",  # пока все easy; позже можно разделить
            "aliases": [
                display_name,
                display_name.lower(),
            ],
            "images": images,
        }
        specimens.append(specimen)
        current_id += 1

    print(f"Загружено препаратов: {len(specimens)}")
    return specimens


def get_specimens_by_difficulty(diff: str | None):
    if diff is None:
        return SPECIMENS
    sel = [s for s in SPECIMENS if s.get("difficulty") == diff]
    return sel or SPECIMENS


def get_random_specimen(diff: str | None = None):
    items = get_specimens_by_difficulty(diff)
    return random.choice(items)


def get_specimen_by_id(spec_id: int):
    for s in SPECIMENS:
        if s["id"] == spec_id:
            return s
    return None


# ======================================================
# КЛАВИАТУРЫ
# ======================================================

def main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Обучение")],
            [
                KeyboardButton(text="🧪 Тест (лёгкий)"),
                KeyboardButton(text="🔥 Тест (сложный)")
            ]
        ],
        resize_keyboard=True
    )


def next_button_keyboard(mode: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="➡️ Далее",
                    callback_data=f"next:{mode}"
                )
            ]
        ]
    )


# ======================================================
# ОТПРАВКА ИЗОБРАЖЕНИЙ
# ======================================================

async def send_specimen_image(chat_id: int, specimen: Dict[str, Any],
                              text: str, kb: InlineKeyboardMarkup | None = None):
    images = specimen.get("images") or []
    if not images:
        await bot.send_message(chat_id, text + "\n(картинка не найдена)", reply_markup=kb)
        return

    img_path = random.choice(images)
    if os.path.exists(img_path):
        await bot.send_photo(
            chat_id,
            FSInputFile(img_path),
            caption=text,
            reply_markup=kb
        )
    else:
        await bot.send_message(chat_id, text, reply_markup=kb)


# ======================================================
# ХЕНДЛЕРЫ
# ======================================================

@dp.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer(
        "Привет! 👋\n"
        "Я бот для тренировки микропрепаратов по патанатомии.\n\n"
        "Режимы:\n"
        "• 📚 Обучение — картинка + название\n"
        "• 🧪 Тест (лёгкий) — картинка + варианты ответов\n"
        "• 🔥 Тест (сложный) — картинка, ответ нужно вписать самому\n\n"
        "Выбери режим на клавиатуре 👇",
        reply_markup=main_menu_keyboard()
    )


@dp.message(Command("menu"))
async def cmd_menu(msg: Message):
    await msg.answer("Выбери режим:", reply_markup=main_menu_keyboard())


# ---------- ОБУЧЕНИЕ ----------

@dp.message(F.text == "📚 Обучение")
async def training(msg: Message):
    specimen = get_random_specimen()
    text = f"<b>{specimen['name']}</b>"
    await send_specimen_image(
        msg.chat.id, specimen, text, next_button_keyboard("train")
    )


# ---------- ЛЁГКИЙ ТЕСТ (ВАРИАНТЫ) ----------

@dp.message(F.text == "🧪 Тест (лёгкий)")
async def easy_test(msg: Message):
    specimen = get_random_specimen("easy")

    others = [s for s in SPECIMENS if s["id"] != specimen["id"]]
    distractors = random.sample(others, k=min(3, len(others))) if others else []

    options = [specimen["name"]] + [s["name"] for s in distractors]
    random.shuffle(options)

    user_state[msg.from_user.id] = {
        "mode": "easy",
        "specimen_id": specimen["id"],
        "options": options,
        "correct": specimen["name"],
    }

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=o, callback_data=f"opt:{i}")]
            for i, o in enumerate(options)
        ]
    )

    await send_specimen_image(
        msg.chat.id, specimen, "Выбери правильный вариант:", kb
    )


@dp.callback_query(F.data.startswith("opt:"))
async def easy_answer(cb: CallbackQuery):
    state = user_state.get(cb.from_user.id)
    if not state or state.get("mode") != "easy":
        await cb.answer("Начни тест заново: выбери 🧪 Тест (лёгкий)")
        return

    idx = int(cb.data.split(":")[1])
    options = state["options"]
    if idx < 0 or idx >= len(options):
        await cb.answer("Что-то пошло не так, попробуй ещё раз")
        return

    chosen = options[idx]
    correct = state["correct"]

    if chosen == correct:
        text = f"✅ Верно!\n<b>{correct}</b>"
    else:
        text = (
            f"❌ Неверно.\n"
            f"Ты выбрала: <b>{chosen}</b>\n"
            f"Правильный ответ: <b>{correct}</b>"
        )

    await cb.message.answer(text, reply_markup=next_button_keyboard("easy"))
    await cb.answer()


# ---------- СЛОЖНЫЙ ТЕСТ (ВПИСАТЬ ОТВЕТ) ----------

@dp.message(F.text == "🔥 Тест (сложный)")
async def hard_test(msg: Message):
    specimen = get_random_specimen(None)  # пока используем все препараты
    user_state[msg.from_user.id] = {
        "mode": "hard",
        "specimen_id": specimen["id"],
    }

    await send_specimen_image(
        msg.chat.id,
        specimen,
        "Напиши <b>точное название</b> препарата (можно без регистра):"
    )


@dp.message()  # все остальные текстовые сообщения
async def hard_answer(msg: Message):
    state = user_state.get(msg.from_user.id)
    if not state or state.get("mode") != "hard":
        return

    specimen = get_specimen_by_id(state["specimen_id"])
    if not specimen:
        await msg.answer("Ошибка данных, попробуй начать тест заново 🙈")
        return

    user_text = normalize_text(msg.text)
    candidates = [normalize_text(specimen["name"])] + [
        normalize_text(a) for a in specimen.get("aliases", [])
    ]

    ok = any(
        user_text == c or user_text in c or c in user_text
        for c in candidates
    )

    if ok:
        text = f"✅ Верно! Это <b>{specimen['name']}</b>"
    else:
        text = f"❌ Неверно.\nПравильный ответ: <b>{specimen['name']}</b>"

    await msg.answer(text, reply_markup=next_button_keyboard("hard"))


# ---------- КНОПКА "ДАЛЕЕ" ----------

@dp.callback_query(F.data.startswith("next:"))
async def next_cb(cb: CallbackQuery):
    mode = cb.data.split(":", 1)[1]
    if mode == "train":
        await training(cb.message)
    elif mode == "easy":
        await easy_test(cb.message)
    elif mode == "hard":
        await hard_test(cb.message)
    await cb.answer()


# ======================================================
# MAIN
# ======================================================

async def main():
    global SPECIMENS
    SPECIMENS = load_specimens_from_folder(PREPARATS_DIR)
    if not SPECIMENS:
        print("⚠ ВНИМАНИЕ: не найдено ни одного препарата в папке 'preparats'")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
