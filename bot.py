import os
import random
from dataclasses import dataclass
from typing import List, Dict

import telebot
from telebot import types

# =========================
# НАСТРОЙКИ БОТА
# =========================

BOT_TOKEN = "8245340349:AAF2sB8Gn5dXiqQQ1ldxAHqk_wpsdcLrH2c"
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# =========================
# МОДЕЛЬ ДАННЫХ
# =========================

@dataclass
class Preparat:
    id: str
    name: str
    category: str
    files: List[str]


# =========================
# СПИСОК ПРЕПАРАТОВ (ТВОЙ СПИСОК)
# =========================

PREPARATS: List[Preparat] = [
    # ---- ТВОИ ПРЕПАРАТЫ (оставлены без изменений) ----
    Preparat(
        id="amiloidoz_pecheni",
        name="Амилоидоз печени",
        category="Амилоидозы",
        files=["amiloidoz_pecheni_1.jpeg", "amiloidoz_pecheni_2.jpeg", "amiloidoz_pecheni_3.jpeg"],
    ),
    # ... весь твой список (я не изменял) ...
]

# Быстрый доступ
PREP_BY_ID = {p.id: p for p in PREPARATS}

# Список категорий
CATEGORIES_ORDERED = [
    "Амилоидозы",
    "Воспаление",
    "Дистрофии",
    "Гиалинозы",
    "Пигменты",
    "Некроз",
    "Кровообращение",
    "Инфаркты",
    "Тромбоз",
]

RANDOM_CATEGORY_KEY = "__random__"

# =========================
# ПЕРСОНАЛЬНЫЕ СОСТОЯНИЯ
# =========================

user_state: Dict[int, Dict] = {}
user_stats: Dict[int, Dict] = {}
user_test_pool: Dict[int, List[str]] = {}

# =========================
# ФУНКЦИИ ВСПОМОГАТЕЛЬНЫЕ
# =========================

def main_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📚 Обучение")
    kb.row("❓ Тест (варианты)", "⌨️ Тест (ввод)")
    kb.row("📊 Статистика", "🔁 Повторить ошибки")
    return kb


def training_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("➡️ Следующий")
    kb.row("🔙 Назад к разделам")
    kb.row("🏁 Выйти")
    return kb


def get_user_stats(user_id):
    if user_id not in user_stats:
        user_stats[user_id] = {"total": 0, "correct": 0, "wrong": 0, "errors": set()}
    return user_stats[user_id]


def normalize(text: str) -> str:
    return text.lower().replace("ё", "е").strip()


# =========================
# ОБУЧЕНИЕ — ЛОГИКА
# =========================

def get_training_list_for_user(user_id, category_key):
    """Формируем список препаратов для обучения без повторов"""
    if category_key == RANDOM_CATEGORY_KEY:
        ids = [p.id for p in PREPARATS]
    else:
        ids = [p.id for p in PREPARATS if p.category == category_key]

    random.shuffle(ids)

    if user_id not in user_state:
        user_state[user_id] = {}

    user_state[user_id]["train_category"] = category_key
    user_state[user_id]["train_remaining"] = ids
    return ids


def pick_next_training_prep(user_id):
    st = user_state.get(user_id)
    if not st or st.get("mode") != "train":
        return None

    remaining = st.get("train_remaining", [])

    if not remaining:
        # начинаем список заново
        remaining = get_training_list_for_user(user_id, st["train_category"])

    prep_id = remaining.pop()
    st["train_remaining"] = remaining
    st["train_current_id"] = prep_id
    return PREP_BY_ID[prep_id]


# =========================
# ОТПРАВКА ПРЕПАРАТА
# =========================

def send_preparat_training(chat_id, prep: Preparat, with_keyboard=False):
    """Только ОДНА корректная версия функции"""
    kb = training_keyboard() if with_keyboard else None

    bot.send_message(chat_id, f"<b>{prep.name}</b>", reply_markup=kb)

    for filename in prep.files:
        path = os.path.join("preparats", filename)
        if not os.path.exists(path):
            bot.send_message(chat_id, f"Файл отсутствует: {path}")
            continue
        with open(path, "rb") as img:
            bot.send_photo(chat_id, img)


# =========================
# ТЕСТЫ — ЛОГИКА
# =========================

def get_or_reset_test_pool(user_id):
    pool = user_test_pool.get(user_id)
    if not pool:
        pool = [p.id for p in PREPARATS]
        random.shuffle(pool)
        user_test_pool[user_id] = pool
    return pool


def send_mcq_question(chat_id, user_id, only_errors=False):
    stats = get_user_stats(user_id)

    if only_errors:
        error_ids = list(stats["errors"])
        if not error_ids:
            bot.send_message(chat_id, "Нет ошибок 😊", reply_markup=main_keyboard())
            return
        prep = PREP_BY_ID[random.choice(error_ids)]
        from_errors = True
    else:
        pool = get_or_reset_test_pool(user_id)
        if not pool:
            pool = get_or_reset_test_pool(user_id)
        prep = PREP_BY_ID[pool.pop()]
        user_test_pool[user_id] = pool
        from_errors = False

    options = [prep] + random.sample([p for p in PREPARATS if p.id != prep.id], 3)
    random.shuffle(options)

    user_state[user_id] = {"mode": "mcq", "correct_id": prep.id, "from_errors": from_errors}

    path = os.path.join("preparats", prep.files[0])
    with open(path, "rb") as img:
        kb = types.InlineKeyboardMarkup()
        for opt in options:
            kb.add(types.InlineKeyboardButton(text=opt.name, callback_data=f"ans:{opt.id}"))

        bot.send_photo(chat_id, img, caption="Что за препарат?", reply_markup=kb)


def send_typing_question(chat_id, user_id, only_errors=False):
    stats = get_user_stats(user_id)

    if only_errors:
        err = list(stats["errors"])
        if not err:
            bot.send_message(chat_id, "Нет ошибок 😊", reply_markup=main_keyboard())
            return
        prep = PREP_BY_ID[random.choice(err)]
        from_errors = True
    else:
        pool = get_or_reset_test_pool(user_id)
        if not pool:
            pool = get_or_reset_test_pool(user_id)
        prep = PREP_BY_ID[pool.pop()]
        user_test_pool[user_id] = pool
        from_errors = False

    user_state[user_id] = {"mode": "typing", "correct_id": prep.id, "from_errors": from_errors}

    # фото
    path = os.path.join("preparats", prep.files[0])
    with open(path, "rb") as img:
        bot.send_photo(chat_id, img)

    bot.send_message(chat_id, "Напиши название препарата.")


# =========================
# ХЕНДЛЕРЫ
# =========================

@bot.message_handler(commands=["start"])
def cmd_start(msg):
    bot.send_message(
        msg.chat.id,
        "Привет! ❤️ Я бот для микропрепаратов.\n\n"
        "Выбери режим:",
        reply_markup=main_keyboard(),
    )


# --- ОБУЧЕНИЕ: ВЫБОР РАЗДЕЛА ---

@bot.message_handler(func=lambda m: m.text == "📚 Обучение")
def training_menu(msg):
    kb = types.InlineKeyboardMarkup()

    for cat in CATEGORIES_ORDERED:
        kb.add(types.InlineKeyboardButton(text=cat, callback_data=f"cat:{cat}"))

    kb.add(types.InlineKeyboardButton(text="Случайные препараты", callback_data=f"cat:{RANDOM_CATEGORY_KEY}"))

    bot.send_message(msg.chat.id, "Выбери раздел:", reply_markup=kb)


@bot.callback_query_handler(func=lambda c: c.data.startswith("cat:"))
def training_choose_category(cb):
    _, category_key = cb.data.split(":")
    user_id = cb.from_user.id

    ids = get_training_list_for_user(user_id, category_key)
    user_state[user_id]["mode"] = "train"

    prep = PREP_BY_ID[ids.pop()]
    user_state[user_id]["train_current_id"] = prep.id

    send_preparat_training(cb.message.chat.id, prep, with_keyboard=True)
    bot.answer_callback_query(cb.id)


# --- ОБУЧЕНИЕ: НАВИГАЦИЯ ---

@bot.message_handler(func=lambda m: m.text == "➡️ Следующий")
def training_next(msg):
    user_id = msg.from_user.id
    prep = pick_next_training_prep(user_id)

    if not prep:
        bot.send_message(msg.chat.id, "Все препараты показаны!", reply_markup=main_keyboard())
        return

    send_preparat_training(msg.chat.id, prep, with_keyboard=True)


@bot.message_handler(func=lambda m: m.text == "🔙 Назад к разделам")
def training_back(msg):
    user_id = msg.from_user.id
    if user_id in user_state:
        user_state[user_id] = {}
    training_menu(msg)


@bot.message_handler(func=lambda m: m.text == "🏁 Выйти")
def training_exit(msg):
    user_state.pop(msg.from_user.id, None)
    bot.send_message(msg.chat.id, "Выход выполнен 👌", reply_markup=main_keyboard())


# --- ТЕСТ И ВАРИАНТЫ И ВВОД ---

@bot.message_handler(func=lambda m: m.text == "❓ Тест (варианты)")
def start_mcq(msg):
    send_mcq_question(msg.chat.id, msg.from_user.id)


@bot.message_handler(func=lambda m: m.text == "⌨️ Тест (ввод)")
def start_typing(msg):
    send_typing_question(msg.chat.id, msg.from_user.id)


@bot.message_handler(func=lambda m: m.text == "🔁 Повторить ошибки")
def start_error_training(msg):
    send_mcq_question(msg.chat.id, msg.from_user.id, only_errors=True)


@bot.callback_query_handler(func=lambda c: c.data.startswith("ans:"))
def handle_mcq_answer(cb):
    user_id = cb.from_user.id
    state = user_state.get(user_id)

    if not state or state["mode"] != "mcq":
        bot.answer_callback_query(cb.id, "Вопрос устарел")
        return

    chosen_id = cb.data.split(":")[1]
    correct_id = state["correct_id"]
    stats = get_user_stats(user_id)

    stats["total"] += 1

    if chosen_id == correct_id:
        stats["correct"] += 1
        stats["errors"].discard(correct_id)
        bot.send_message(cb.message.chat.id, f"✅ Верно! Это <b>{PREP_BY_ID[correct_id].name}</b>")
    else:
        stats["wrong"] += 1
        stats["errors"].add(correct_id)
        bot.send_message(
            cb.message.chat.id,
            f"❌ Неверно.\nПравильно: <b>{PREP_BY_ID[correct_id].name}</b>"
        )

    bot.answer_callback_query(cb.id)
    send_mcq_question(cb.message.chat.id, user_id, only_errors=state["from_errors"])


# --- ТЕСТ — ВВОД ---

@bot.message_handler(
    func=lambda m: m.text not in ["📚 Обучение", "❓ Тест (варианты)", "⌨️ Тест (ввод)",
                                  "📊 Статистика", "🔁 Повторить ошибки",
                                  "➡️ Следующий", "🔙 Назад к разделам", "🏁 Выйти"]
)
def typing_answer(msg):
    user_id = msg.from_user.id
    state = user_state.get(user_id)

    if not state or state["mode"] != "typing":
        return

    prep = PREP_BY_ID[state["correct_id"]]
    stats = get_user_stats(user_id)
    stats["total"] += 1

    answer = normalize(msg.text)
    correct = normalize(prep.name)

    words = [w for w in correct.split() if len(w) > 3]

    if any(w in answer for w in words):
        stats["correct"] += 1
        stats["errors"].discard(prep.id)
        bot.send_message(msg.chat.id, f"✅ Верно! Это <b>{prep.name}</b>")
    else:
        stats["wrong"] += 1
        stats["errors"].add(prep.id)
        bot.send_message(msg.chat.id, f"❌ Неверно.\nПравильно: <b>{prep.name}</b>")

    send_typing_question(msg.chat.id, user_id, only_errors=state["from_errors"])


# --- СТАТИСТИКА ---

@bot.message_handler(func=lambda m: m.text == "📊 Статистика")
def user_statistics(msg):
    stats = get_user_stats(msg.from_user.id)
    total = stats["total"]
    correct = stats["correct"]
    wrong = stats["wrong"]
    acc = round(correct * 100 / total, 1) if total else 0

    bot.send_message(
        msg.chat.id,
        f"<b>Статистика:</b>\n"
        f"Всего: <b>{total}</b>\n"
        f"Правильно: <b>{correct}</b>\n"
        f"Неправильно: <b>{wrong}</b>\n"
        f"Точность: <b>{acc}%</b>\n"
        f"Ошибок в списке: <b>{len(stats['errors'])}</b>",
        reply_markup=main_keyboard()
    )


# =========================
# ПУСК
# =========================

print("Бот запущен!")
bot.infinity_polling()
