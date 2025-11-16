import asyncio
import os
import random
import re
from difflib import SequenceMatcher

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import (
    Message, CallbackQuery,
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton,
    FSInputFile,
)

# ===================== НАСТРОЙКИ =====================

# Можно оставить как есть, а можно вынести токен в переменную окружения BOT_TOKEN на Render
BOT_TOKEN = os.getenv(
    "BOT_TOKEN",
    "8245340349:AAF2sB8Gn5dXiqQQ1ldxAHqk_wpsdcLrH2c"  # твой токен; лучше потом заменить на env
)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

PREP_DIR = "preparats"

# user_id -> правильный ответ для сложного уровня
hard_answers: dict[int, str] = {}

# ===================== КАТЕГОРИИ =====================

CATEGORIES = {
    "Дистрофии": [
        "zernistaya_distrofiya_pochki",
        "zernistaya_distrofiya_pecheni",
        "gialinovo_kapelnaya_distrofiya_pochki",
        "vakuolnaya_distrofiya_pochki",
        "zhirovaia_distrofiya_pecheni",
        "kolloidnaya_distrofiya_shchitovidnoi",
    ],
    "Воспаления": [
        "ostryi_seroznyi_gastrit",
        "seroznoe_vosp_legkikh",
        "serozno_gemorragicheskaya_pnevmoniya",
        "gemorragicheskoe_vospalenie_kishechnika",
        "difteriticheskii_enterit",
        "gnoinyi_nefrit",
        "khronicheskii_kataralnyi_enterit_ge",
        "khronicheskii_kataralnyi_enterit_sudan",
        "khronicheskii_abscess_pecheni",
    ],
    "Некрозы": [
        "nekroticheskii_nefroz",
        "tsenkerovskii_voskovidnyi_nekroz_myshc",
        "tvorozhistyi_nekroz_legkikh_tb",
        "tvorozhistyi_nekroz_lymph_tb",
    ],
    "Амилоидозы": [
        "amiloidoz_pecheni",
        "amiloidoz_pochki",
        "amiloidoz_selezenki_sagovaya",
        "amiloidoz_selezenki_salnaya",
    ],
    "Гемосидероз": [
        "hemosideroz_pecheni",
        "hemosideroz_pecheni_muskatnaya",
        "hemosideroz_selezenki_ge",
        "hemosideroz_selezenki_perls",
    ],
    "Гиперемия / застой": [
        "ostraya_zastoynaya_giperemiya_otek_legkikh",
        "ostraya_zastoynaya_venoznaya_giperemiya_pecheni",
        "khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen",
    ],
    "Инфаркты": [
        "ishemicheskii_infarkt_pochki",
        "ishemicheskii_infarkt_selezenki",
        "gemorragicheskii_infarkt_pochki",
        "gemorragicheskii_infarkt_legkogo",
    ],
    "Индурации": [
        "buraya_induratsiya_legkogo",
        "buraya_induratsiya_pecheni",
    ],
    "Пневмонии": [
        "krupoznaya_pnevmoniya",
        "serozno_gemorragicheskaya_pnevmoniya",
    ],
    "Прочее": [
        "smeshannyi_tromb",
        "antrakoz_legkikh",
    ],
}

# ===================== РУССКИЕ НАЗВАНИЯ =====================

RUS_NAMES = {
    "zernistaya_distrofiya_pochki": "Зернистая дистрофия почки",
    "zernistaya_distrofiya_pecheni": "Зернистая дистрофия печени",
    "gialinovo_kapelnaya_distrofiya_pochki": "Гиалиново-капельная дистрофия почки",
    "vakuolnaya_distrofiya_pochki": "Вакуольная дистрофия почки",
    "zhirovaia_distrofiya_pecheni": "Жировая дистрофия печени",
    "kolloidnaya_distrofiya_shchitovidnoi": "Коллоидная дистрофия щитовидной железы",

    "ostryi_seroznyi_gastrit": "Острый серозный гастрит",
    "seroznoe_vosp_legkikh": "Серозное воспаление лёгких",
    "serozno_gemorragicheskaya_pnevmoniya": "Серозно-геморрагическая пневмония",
    "gemorragicheskoe_vospalenie_kishechnika": "Геморрагическое воспаление кишечника",
    "difteriticheskii_enterit": "Дифтеритический энтерит",
    "gnoinyi_nefrit": "Гнойный нефрит",
    "khronicheskii_kataralnyi_enterit_ge": "Хронический катаральный энтерит (ГЭ)",
    "khronicheskii_kataralnyi_enterit_sudan": "Хронический катаральный энтерит (Судан III)",
    "khronicheskii_abscess_pecheni": "Хронический абсцесс печени",

    "nekroticheskii_nefroz": "Некротический нефроз",
    "tsenkerovskii_voskovidnyi_nekroz_myshc": "Ценкеровский (восковидный) некроз мышц",
    "tvorozhistyi_nekroz_legkikh_tb": "Творожистый некроз лёгких при туберкулёзе",
    "tvorozhistyi_nekroz_lymph_tb": "Творожистый (казеозный) некроз лимфоузла при туберкулёзе",

    "amiloidoz_pecheni": "Амилоидоз печени",
    "amiloidoz_pochki": "Амилоидоз почки",
    "amiloidoz_selezenki_sagovaya": "Амилоидоз селезёнки (саговая форма)",
    "amiloidoz_selezenki_salnaya": "Амилоидоз селезёнки (сальная форма)",

    "hemosideroz_pecheni": "Гемосидероз печени",
    "hemosideroz_pecheni_muskatnaya": "Гемосидероз печени (мускатная печень)",
    "hemosideroz_selezenki_ge": "Гемосидероз селезёнки (ГЭ)",
    "hemosideroz_selezenki_perls": "Гемосидероз селезёнки (Перлс)",

    "ostraya_zastoynaya_giperemiya_otek_legkikh": "Острая застойная гиперемия и отёк лёгких",
    "ostraya_zastoynaya_venoznaya_giperemiya_pecheni": "Острая застойная венозная гиперемия печени",
    "khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen": "Хроническое венозное полнокровие (мускатная печень)",

    "ishemicheskii_infarkt_pochki": "Ишемический инфаркт почки",
    "ishemicheskii_infarkt_selezenki": "Ишемический инфаркт селезёнки",
    "gemorragicheskii_infarkt_pochki": "Геморрагический инфаркт почки",
    "gemorragicheskii_infarkt_legkogo": "Геморрагический инфаркт лёгкого",

    "buraya_induratsiya_legkogo": "Бурая индурация лёгкого",
    "buraya_induratsiya_pecheni": "Бурая индурация печени",

    "krupoznaya_pnevmoniya": "Крупозная пневмония",

    "smeshannyi_tromb": "Смешанный тромб",
    "antrakoz_legkikh": "Антракоз лёгких",
}

# ===================== ЗАГРУЗКА КАРТИНОК =====================

# base_name -> [список путей к файлам]
SPECIMENS: dict[str, list[str]] = {}


def load_all_files():
    if not os.path.isdir(PREP_DIR):
        print(f"Папка {PREP_DIR} не найдена")
        return

    for fname in os.listdir(PREP_DIR):
        lower = fname.lower()
        if not lower.endswith((".jpg", ".jpeg", ".png")):
            continue

        stem = os.path.splitext(fname)[0]
        # убираем номер в конце _1, _2 и т.д.
        base = re.sub(r"[_\.\- ]?\d+$", "", stem)
        path = os.path.join(PREP_DIR, fname)

        SPECIMENS.setdefault(base, []).append(path)

    print(f"Загружено баз: {len(SPECIMENS)}")


# ===================== КЛАВИАТУРЫ =====================

def main_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Обучение")],
            [
                KeyboardButton(text="🟡 Лёгкий уровень"),
                KeyboardButton(text="🔴 Сложный уровень"),
            ],
        ],
        resize_keyboard=True,
    )


def categories_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=cat, callback_data=f"cat:{cat}")]
            for cat in CATEGORIES.keys()
        ]
    )


def diagnoses_kb(cat: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=RUS_NAMES.get(base, base),
                    callback_data=f"diag:{base}",
                )
            ]
            for base in CATEGORIES.get(cat, [])
        ]
    )


# ===================== ОБУЧЕНИЕ =====================

@dp.message(F.text == "📚 Обучение")
async def learning(msg: Message):
    await msg.answer("Выбери категорию:", reply_markup=categories_kb())


@dp.callback_query(F.data.startswith("cat:"))
async def category_select(cb: CallbackQuery):
    cat = cb.data.split(":", 1)[1]
    await cb.message.answer(
        f"Выбери диагноз в категории <b>{cat}</b>:",
        reply_markup=diagnoses_kb(cat),
    )
    await cb.answer()


@dp.callback_query(F.data.startswith("diag:"))
async def diagnosis_show(cb: CallbackQuery):
    base = cb.data.split(":", 1)[1]
    name = RUS_NAMES.get(base, base)
    images = SPECIMENS.get(base, [])

    if not images:
        await cb.message.answer(f"Нет изображений для: <b>{name}</b>")
        await cb.answer()
        return

    # отправляем ВСЕ изображения препарата
    for img in sorted(images):
        await cb.message.answer_photo(FSInputFile(img))

    await cb.message.answer(f"<b>{name}</b>")
    await cb.answer()


# ===================== ЛЁГКИЙ ТЕСТ =====================

@dp.message(F.text == "🟡 Лёгкий уровень")
async def easy_test(msg: Message):
    if not SPECIMENS:
        await msg.answer("Нет загруженных препаратов.")
        return

    base = random.choice(list(SPECIMENS.keys()))
    correct = RUS_NAMES.get(base, base)
    img = random.choice(SPECIMENS[base])

    # варианты отвелов
    others = [b for b in SPECIMENS.keys() if b != base]
    other_names = [RUS_NAMES.get(b, b) for b in others]
    if len(other_names) >= 3:
        wrong = random.sample(other_names, 3)
    else:
        wrong = other_names

    variants = wrong + [correct]
    random.shuffle(variants)

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=v,
                    callback_data=f"ans:{v}|{correct}",
                )
            ]
            for v in variants
        ]
    )

    await msg.answer_photo(
        FSInputFile(img),
        caption="Выбери правильный вариант:",
        reply_markup=kb,
    )


@dp.callback_query(F.data.startswith("ans:"))
async def easy_answer(cb: CallbackQuery):
    payload = cb.data.split(":", 1)[1]
    chosen, correct = payload.split("|", 1)

    if chosen == correct:
        text = f"✅ Верно! Это <b>{correct}</b>"
    else:
        text = f"❌ Неверно.\nПравильный ответ: <b>{correct}</b>"

    await cb.message.answer(text)
    await cb.answer()


# ===================== СЛОЖНЫЙ ТЕСТ =====================

def fuzzy_ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


@dp.message(F.text == "🔴 Сложный уровень")
async def hard_start(msg: Message):
    if not SPECIMENS:
        await msg.answer("Нет загруженных препаратов.")
        return

    base = random.choice(list(SPECIMENS.keys()))
    img = random.choice(SPECIMENS[base])
    correct = RUS_NAMES.get(base, base).lower()

    hard_answers[msg.from_user.id] = correct

    await msg.answer_photo(
        FSInputFile(img),
        caption="Напиши название препарата (можно без строгого совпадения):",
    )


@dp.message()
async def hard_check(msg: Message):
    # если пользователь не в режиме сложного уровня — игнорируем
    if msg.from_user.id not in hard_answers:
        return

    correct = hard_answers[msg.from_user.id]
    user_answer = msg.text.lower().strip()

    score = fuzzy_ratio(user_answer, correct)

    if score >= 0.7:
        text = f"✅ Верно! Это <b>{correct}</b>\n(совпадение: {score:.2f})"
    else:
        text = (
            f"❌ Неверно.\n"
            f"Твой ответ: <b>{msg.text}</b>\n"
            f"Правильный: <b>{correct}</b>\n"
            f"(совпадение: {score:.2f})"
        )

    await msg.answer(text)
    # сбрасываем состояние
    del hard_answers[msg.from_user.id]


# ===================== START / MAIN =====================

@dp.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer(
        "Привет! Я бот для тренировки микропрепаратов по патанатомии.\n\n"
        "Режимы:\n"
        "📚 Обучение — категории → диагноз → все фото\n"
        "🟡 Лёгкий уровень — картинка + 4 варианта\n"
        "🔴 Сложный уровень — картинка, ответ пишешь сам",
        reply_markup=main_menu(),
    )


async def main():
    load_all_files()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

