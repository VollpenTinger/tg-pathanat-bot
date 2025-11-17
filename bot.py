import telebot
from telebot import types
import os
import random

# ==========================
# ⭐ ВСТАВЬ СВОЙ ТОКЕН СЮДА
# ==========================
BOT_TOKEN "8245340349:AAF2sB8Gn5dXiqQQ1ldxAHqk_wpsdcLrH2c"

bot = telebot.TeleBot(BOT_TOKEN)

# ==========================
#   ИМПОРТ ВСЕХ ПРЕПАРАТОВ
# ==========================

PREPARATS = {
    # ---------- Амилоидозы ----------
    "Амилоидоз печени": [
        "amiloidoz_pecheni_1.jpeg",
        "amiloidoz_pecheni_2.jpeg",
        "amiloidoz_pecheni_3.jpeg",
    ],
    "Амилоидоз почки": [
        "amiloidoz_pochki_1.jpeg",
        "amiloidoz_pochki_2.jpeg",
    ],
    "Амилоидоз селезёнки (саговая форма)": [
        "amiloidoz_selezenki_sagovaya_1.jpeg",
        "amiloidoz_selezenki_sagovaya_2.jpeg",
    ],
    "Амилоидоз селезёнки (сальная форма)": [
        "amiloidoz_selezenki_salnaya_1.jpeg",
        "amiloidoz_selezenki_salnaya_2.jpeg",
        "amiloidoz_selezenki_salnaya_3.jpeg",
    ],

    # ---------- Воспаления ----------
    "Антракоз лёгких": [
        "antrakoz_legkikh_1.jpeg",
        "antrakoz_legkikh_2.jpeg",
        "antrakoz_legkikh_3.jpeg",
    ],
    "Острый серозный гастрит": [
        "ostryi_seroznyi_gastrit_1.jpeg",
        "ostryi_seroznyi_gastrit_2.jpeg",
        "ostryi_seroznyi_gastrit_3.jpeg",
        "ostryi_seroznyi_gastrit_4.jpeg",
    ],
    "Серозно-геморрагическая пневмония": [
        "serozno_gemorragicheskaya_pnevmoniya_1.jpeg",
        "serozno_gemorragicheskaya_pnevmoniya_2.jpeg",
        "serozno_gemorragicheskaya_pnevmoniya_3.jpeg",
    ],
    "Серозное воспаление лёгких": [
        "seroznoe_vosp_legkikh_1.jpeg",
        "seroznoe_vosp_legkikh_2.jpeg",
        "seroznoe_vosp_legkikh_3.jpeg",
    ],
    "Крупозная пневмония": [
        "krupoznaya_pnevmoniya_1.jpeg",
        "krupoznaya_pnevmoniya_2.jpeg",
    ],
    "Фибринозный перикардит": [
        "fibrinoznyi_perikardit_1.jpeg",
        "fibrinoznyi_perikardit_2.jpeg",
        "fibrinoznyi_perikardit_3.jpeg",
    ],
    "Дифтеритический энтерит": [
        "difteriticheskii_enterit_1.jpeg",
        "difteriticheskii_enterit_2.jpeg",
    ],
    "Геморрагическое воспаление кишечника": [
        "gemorragicheskoe_vospalenie_kishechnika_1.jpeg",
        "gemorragicheskoe_vospalenie_kishechnika_2.jpeg",
        "gemorragicheskoe_vospalenie_kishechnika_3.jpeg",
    ],
    "Гнойный нефрит": [
        "gnoinyi_nefrit_1.jpeg",
        "gnoinyi_nefrit_2.jpeg",
        "gnoinyi_nefrit_3.jpeg",
        "gnoinyi_nefrit_4.jpeg",
    ],
    "Хронический абсцесс печени": [
        "khronicheskii_abscess_pecheni_1.jpeg",
    ],
    "Хронический катаральный энтерит (ГЭ)": [
        "khronicheskii_kataralnyi_enterit_ge_1.jpeg",
        "khronicheskii_kataralnyi_enterit_ge_2.jpeg",
        "khronicheskii_kataralnyi_enterit_ge_3.jpeg",
        "khronicheskii_kataralnyi_enterit_ge_4.jpeg",
    ],
    "Хронический катаральный энтерит (Судан III)": [
        "khronicheskii_kataralnyi_enterit_sudan_1.jpeg",
        "khronicheskii_kataralnyi_enterit_sudan_2.jpeg",
        "khronicheskii_kataralnyi_enterit_sudan_3.jpeg",
    ],

    # ---------- Дистрофии ----------
    "Зернистая дистрофия почки": [
        "zernistaya_distrofiya_pochki_1.jpeg",
        "zernistaya_distrofiya_pochki_2.jpeg",
    ],
    "Зернистая дистрофия печени": [
        "zernistaya_distrofiya_pecheni_1.jpeg",
        "zernistaya_distrofiya_pecheni_2.jpeg",
    ],
    "Гиалиново-капельная дистрофия почки": [
        "gialinovo_kapelnaya_distrofiya_pochki_1.jpeg",
        "gialinovo_kapelnaya_distrofiya_pochki_2.jpeg",
        "gialinovo_kapelnaya_distrofiya_pochki_3.jpeg",
    ],
    "Вакуольная дистрофия почки": [
        "vakuolnaya_distrofiya_pochki_1.jpeg",
    ],
    "Коллоидная дистрофия щитовидной железы": [
        "kolloidnaya_distrofiya_shchitovidnoi_1.jpeg",
        "kolloidnaya_distrofiya_shchitovidnoi_2.jpeg",
    ],
    "Жировая дистрофия печени": [
        "zhirovaia_distrofiya_pecheni_1.jpeg",
        "zhirovaia_distrofiya_pecheni_2.jpeg",
    ],

    # ---------- Гиалиноз ----------
    "Гиалиноз селезёнки": [
        "gialinoz_selezenki_1.jpeg",
        "gialinoz_selezenki_2.jpeg",
        "gialinoz_selezenki_3.jpeg",
    ],
    "Гиалиноз стенки сосуда матки": [
        "gialinoz_stenki_sosuda_matki_1.jpeg",
        "gialinoz_stenki_sosuda_matki_2.jpeg",
        "gialinoz_stenki_sosuda_matki_3.jpeg",
    ],

    # ---------- Пигменты и пылевые ----------
    "Гемосидероз печени": [
        "hemosideroz_pecheni_1.jpeg",
        "hemosideroz_pecheni_2.jpeg",
    ],
    "Гемосидероз печени (мускатная печень)": [
        "hemosideroz_pecheni_muskatnaya_1.jpeg",
        "hemosideroz_pecheni_muskatnaya_2.jpeg",
        "hemosideroz_pecheni_muskatnaya_3.jpeg",
    ],
    "Гемосидероз селезёнки (ГЭ)": [
        "hemosideroz_selezenki_ge_1.jpeg",
        "hemosideroz_selezenki_ge_2.jpeg",
        "hemosideroz_selezenki_ge_3.jpeg",
        "hemosideroz_selezenki_ge_4.jpeg",
    ],
    "Гемосидероз селезёнки (Перлс)": [
        "hemosideroz_selezenki_perls_1.jpeg",
        "hemosideroz_selezenki_perls_2.jpeg",
        "hemosideroz_selezenki_perls_3.jpeg",
        "hemosideroz_selezenki_perls_4.jpeg",
    ],
    "Меланоз печени": [
        "melanoz_pecheni_1.jpeg",
        "melanoz_pecheni_2.jpeg",
        "melanoz_pecheni_3.jpeg",
    ],
    "Антракоз лёгких": [
        "antrakoz_legkikh_1.jpeg",
        "antrakoz_legkikh_2.jpeg",
        "antrakoz_legkikh_3.jpeg",
    ],

    # ---------- Некрозы ----------
    "Некротический нефроз": [
        "nekroticheskii_nefroz_1.jpeg",
        "nekroticheskii_nefroz_2.jpeg",
        "nekroticheskii_nefroz_3.jpeg",
    ],
    "Творожистый некроз лёгких при туберкулёзе": [
        "tvorozhistyi_nekroz_legkikh_tb_1.jpeg",
        "tvorozhistyi_nekroz_legkikh_tb_2.jpeg",
    ],
    "Творожистый некроз лимфоузла при туберкулёзе": [
        "tvorozhistyi_nekroz_lymph_tb_1.jpeg",
        "tvorozhistyi_nekroz_lymph_tb_2.jpeg",
    ],
    "Ценкеровский восковидный некроз мышц": [
        "tsenkerovskii_voskovidnyi_nekroz_myshc_1.jpeg",
        "tsenkerovskii_voskovidnyi_nekroz_myshc_2.jpeg",
    ],

    # ---------- Инфаркты ----------
    "Ишемический инфаркт почки": [
        "ishemicheskii_infarkt_pochki_1.jpeg",
        "ishemicheskii_infarkt_pochki_2.jpeg",
    ],
    "Ишемический инфаркт селезёнки": [
        "ishemicheskii_infarkt_selezenki_1.jpeg",
        "ishemicheskii_infarkt_selezenki_2.jpeg",
    ],
    "Геморрагический инфаркт почки": [
        "gemorragicheskii_infarkt_pochki_1.jpeg",
        "gemorragicheskii_infarkt_pochki_2.jpeg",
        "gemorragicheskii_infarkt_pochki_3.jpeg",
    ],
    "Геморрагический инфаркт лёгкого": [
        "gemorragicheskii_infarkt_legkogo_1.jpeg",
        "gemorragicheskii_infarkt_legkogo_2.jpeg",
    ],

    # ---------- Кровообращение ----------
    "Бурая индурация печени": [
        "buraya_induratsiya_pecheni_1.jpeg",
        "buraya_induratsiya_pecheni_2.jpeg",
    ],
    "Бурая индурация лёгкого": [
        "buraya_induratsiya_legkogo_1.jpeg",
        "buraya_induratsiya_legkogo_2.jpeg",
    ],
    "Острая застойная венозная гиперемия печени": [
        "ostraya_zastoynaya_venoznaya_giperemiya_pecheni_1.jpeg",
        "ostraya_zastoynaya_venoznaya_giperemiya_pecheni_2.jpeg",
    ],
    "Острая застойная гиперемия и отёк лёгких": [
        "ostraya_zastoynaya_giperemiya_otek_legkikh_1.jpeg",
        "ostraya_zastoynaya_giperemiya_otek_legkikh_2.jpeg",
    ],
    "Хроническое венозное полнокровие (мускатная печень)": [
        "khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen_1.jpeg",
        "khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen_2.jpeg",
    ],

    # ---------- Тромбы ----------
    "Смешанный тромб": [
        "smeshannyi_tromb_1.jpeg",
        "smeshannyi_tromb_2.jpeg",
    ],
}


# ======================================
#              ЛОГИКА БОТА
# ======================================

USER_STATE = {}  # user_id: {"mode": "...", "correct": "..."}


# ---------------- КНОПКИ ----------------

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📚 Обучение")
    markup.row("❓ Тест (варианты)", "⌨️ Тест (ввод)")
    return markup


# ---------------- ОБУЧЕНИЕ ----------------

@bot.message_handler(func=lambda m: m.text == "📚 Обучение")
def send_training(message):
    name = random.choice(list(PREPARATS.keys()))
    photos = PREPARATS[name]

    bot.send_message(message.chat.id, f"📌 <b>{name}</b>", parse_mode="HTML")

    for p in photos:
        path = os.path.join("preparats", p)
        bot.send_photo(message.chat.id, open(path, "rb"))


# ---------------- ТЕСТ (ВАРИАНТЫ) ----------------

@bot.message_handler(func=lambda m: m.text == "❓ Тест (варианты)")
def test_mcq(message):
    name = random.choice(list(PREPARATS.keys()))
    correct = name
    photos = PREPARATS[name]

    USER_STATE[message.chat.id] = {"mode": "mcq", "correct": correct}

    first_photo = os.path.join("preparats", photos[0])
    bot.send_photo(message.chat.id, open(first_photo, "rb"), caption="Что за препарат?")

    options = random.sample(list(PREPARATS.keys()), 4)
    if correct not in options:
        options[0] = correct
    random.shuffle(options)

    markup = types.InlineKeyboardMarkup()
    for opt in options:
        markup.add(types.InlineKeyboardButton(text=opt, callback_data=f"ans:{opt}"))

    bot.send_message(message.chat.id, "Выбери правильный ответ:", reply_markup=markup)


@bot.callback_query_handler(func=lambda c: c.data.startswith("ans:"))
def handle_mcq_answer(call):
    chosen = call.data.split(":", 1)[1]
    correct = USER_STATE.get(call.message.chat.id, {}).get("correct")

    if chosen == correct:
        bot.answer_callback_query(call.id, "Верно! ✅")
        bot.send_message(call.message.chat.id, f"Правильный ответ: <b>{correct}</b>", parse_mode="HTML")
    else:
        bot.answer_callback_query(call.id, "Неверно ❌")
        bot.send_message(call.message.chat.id, f"Неверно.\nПравильный ответ: <b>{correct}</b>", parse_mode="HTML")

    test_mcq(call.message)


# ---------------- ТЕСТ (ВВОД) ----------------

@bot.message_handler(func=lambda m: m.text == "⌨️ Тест (ввод)")
def test_typing(message):
    name = random.choice(list(PREPARATS.keys()))
    USER_STATE[message.chat.id] = {"mode": "typing", "correct": name}

    photos = PREPARATS[name]
    first_photo = os.path.join("preparats", photos[0])

    bot.send_photo(message.chat.id, open(first_photo, "rb"))
    bot.send_message(message.chat.id, "Напиши название препарата:")


@bot.message_handler(func=lambda m: m.chat.id in USER_STATE and USER_STATE[m.chat.id]["mode"] == "typing")
def receive_typing(message):
    correct = USER_STATE[message.chat.id]["correct"]
    user_text = message.text.lower().replace("ё", "е")

    correct_norm = correct.lower().replace("ё", "е")

    if any(word in user_text for word in correct_norm.split()):
        bot.send_message(message.chat.id, f"Верно! ✅ Это <b>{correct}</b>", parse_mode="HTML")
    else:
        bot.send_message(message.chat.id, f"❌ Неверно.\nПравильный ответ: <b>{correct}</b>", parse_mode="HTML")

    test_typing(message)


# ---------------- СТАРТ ----------------

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,
                     "Привет! 👋 Я бот для изучения микропрепаратов.\n\n"
                     "Выбери режим:",
                     reply_markup=main_menu())


# ---------------- ЗАПУСК ----------------

print("Бот запущен!")
bot.infinity_polling()

    
