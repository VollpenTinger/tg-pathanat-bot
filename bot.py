import telebot
from telebot import types
import os
import random
import json

# ======================
#   НАСТРОЙКИ
# ======================

TOKEN = "8245340349:AAF2sB8Gn5dXiqQQ1ldxAHqk_wpsdcLrH2c"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# Папка с препаратами
PREP_DIR = "preparats"

# Один JSON файл для всех пользователей
DATA_FILE = "user_data.json"

# Если файла нет — создаём пустую структуру
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False, indent=2)


# =========================================
#   ЗАГРУЗКА / СОХРАНЕНИЕ ДАННЫХ ПОЛЬЗОВАТЕЛЕЙ
# =========================================

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_user(user_id):
    data = load_data()
    if str(user_id) not in data:
        data[str(user_id)] = {
            "stats": {"total": 0, "correct": 0, "wrong": 0},
            "errors": [],
            "mode": None,
            "current_prep": None,
            "current_answer": None,
        }
        save_data(data)
    return data[str(user_id)]


# ======================
#   ЗАГРУЗКА ПРЕПАРАТОВ
# ======================

def load_preparats():
    preparats = {}

    for folder in os.listdir(PREP_DIR):
        folder_path = os.path.join(PREP_DIR, folder)
        if os.path.isdir(folder_path):
            images = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
                      if f.lower().endswith((".jpg", ".jpeg", ".png"))]

            if images:
                preparats[folder] = images

    return preparats


PREPS = load_preparats()


# ======================
#   КЛАВИАТУРЫ
# ======================

def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📚 Обучение")
    kb.row("🎲 Тест (варианты)", "⌨️ Тест (ввод)")
    kb.row("📊 Статистика", "🔁 Повтор ошибок")
    return kb


def test_navigation():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("Ещё вопрос", "Закончить")
    return kb


# ======================
#   ОБРАБОТЧИК СТАРТА
# ======================

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Ну что же поучим препараты 🤓😜",
        reply_markup=main_menu()
    )


# ======================
#     ОБУЧЕНИЕ
# ======================

@bot.message_handler(func=lambda m: m.text == "📚 Обучение")
def learning(message):
    prep = random.choice(list(PREPS.keys()))
    send_learning_prep(message.chat.id, prep)


def send_learning_prep(chat_id, prep):
    bot.send_message(chat_id, f"📖 <b>{prep}</b>")

    for img_path in PREPS[prep]:
        with open(img_path, "rb") as img:
            bot.send_photo(chat_id, img)

    bot.send_message(chat_id, "Готово! Выбирай следующее 👇", reply_markup=main_menu())


# ======================
#     ТЕСТ: ВАРИАНТЫ
# ======================

@bot.message_handler(func=lambda m: m.text == "🎲 Тест (варианты)")
def test_variants_start(message):
    user = get_user(message.chat.id)
    user["mode"] = "test_variants"
    save_user = load_data()
    save_user[str(message.chat.id)] = user
    save_data(save_user)

    send_test_question(message.chat.id, variants=True)


# ======================
#     ТЕСТ: ВВОД ТЕКСТОМ
# ======================

@bot.message_handler(func=lambda m: m.text == "⌨️ Тест (ввод)")
def test_input_start(message):
    user = get_user(message.chat.id)
    user["mode"] = "test_input"
    save_data({**load_data(), str(message.chat.id): user})

    send_test_question(message.chat.id, variants=False)


# ======================
#     СОЗДАНИЕ ВОПРОСА
# ======================

def send_test_question(chat_id, variants=True):
    user = get_user(chat_id)

    prep = random.choice(list(PREPS.keys()))
    user["current_prep"] = prep
    user["current_answer"] = prep

    data = load_data()
    data[str(chat_id)] = user
    save_data(data)

    # Отправляем первое фото препарата
    first_img = PREPS[prep][0]
    with open(first_img, "rb") as img:
        bot.send_photo(chat_id, img, caption="Что за препарат?")

    # ВАРИАНТЫ ОТВЕТА
    if variants:
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

        options = random.sample(list(PREPS.keys()), 3)
        if prep not in options:
            options[random.randint(0, 2)] = prep

        random.shuffle(options)

        for o in options:
            kb.row(o)

        kb.row("Ещё вопрос", "Закончить")
        bot.send_message(chat_id, "Выбери ответ:", reply_markup=kb)

    else:
        bot.send_message(chat_id, "Введи правильный ответ:", reply_markup=test_navigation())


# ======================
#     ПОВТОР ОШИБОК
# ======================

@bot.message_handler(func=lambda m: m.text == "🔁 Повтор ошибок")
def repeat_errors(message):
    user = get_user(message.chat.id)

    if not user["errors"]:
        bot.send_message(message.chat.id, "У тебя нет ошибок! 🤩", reply_markup=main_menu())
        return

    prep = random.choice(user["errors"])
    user["current_prep"] = prep
    user["current_answer"] = prep
    user["mode"] = "repeat"

    save_data({**load_data(), str(message.chat.id): user})

    img = PREPS[prep][0]
    with open(img, "rb") as im:
        bot.send_photo(message.chat.id, im, caption="Попробуй снова 😉")

    bot.send_message(message.chat.id, "Твой ответ?", reply_markup=test_navigation())


# ======================
#     ОБРАБОТКА ВСЕХ ОТВЕТОВ
# ======================

@bot.message_handler(func=lambda m: True)
def answer_handler(message):
    user = get_user(message.chat.id)
    mode = user["mode"]

    # кнопка "Ещё вопрос"
    if message.text == "Ещё вопрос":
        if mode == "test_variants":
            send_test_question(message.chat.id, variants=True)
        elif mode == "test_input":
            send_test_question(message.chat.id, variants=False)
        elif mode == "repeat":
            repeat_errors(message)
        return

    # кнопка "Закончить"
    if message.text == "Закончить":
        bot.send_message(message.chat.id, "Хорошо, завершаем ✔️", reply_markup=main_menu())
        return

    # тестовые режимы
    if mode in ("test_variants", "test_input", "repeat"):
        correct = user["current_answer"]

        user["stats"]["total"] += 1

        if message.text.lower().strip() == correct.lower().strip():
            bot.send_message(message.chat.id, "Молодец 🥳")
            user["stats"]["correct"] += 1
            if mode == "repeat" and correct in user["errors"]:
                user["errors"].remove(correct)
        else:
            bot.send_message(message.chat.id, "Всё фигня, переделывай 🤨🤡")
            user["stats"]["wrong"] += 1
            if correct not in user["errors"]:
                user["errors"].append(correct)

        save_data({**load_data(), str(message.chat.id): user})
        return


# ======================
#     СТАТИСТИКА
# ======================

@bot.message_handler(func=lambda m: m.text == "📊 Статистика")
def stats(message):
    user = get_user(message.chat.id)
    s = user["stats"]

    text = (
        "📊 <b>Твоя статистика:</b>\n\n"
        f"Всего вопросов: <b>{s['total']}</b>\n"
        f"Правильных: 🟢 <b>{s['correct']}</b>\n"
        f"Ошибок: 🔴 <b>{s['wrong']}</b>\n\n"
        f"Ошибок в списке повтора: <b>{len(user['errors'])}</b>"
    )

    bot.send_message(message.chat.id, text, reply_markup=main_menu())


# ======================
#     ЗАПУСК БОТА
# ======================

bot.infinity_polling()
