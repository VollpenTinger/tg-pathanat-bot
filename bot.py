import os
import random
from dataclasses import dataclass
from typing import List, Dict, Set
import telebot
from telebot import types

# ============================================================
#   НАСТРОЙКИ
# ============================================================

BOT_TOKEN = "ВАШ_ТОКЕН_СЮДА"
BASE_URL = "https://raw.githubusercontent.com/lapinaalina845-ux/tg-pathanat-bot/main/preparats/"

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# ============================================================
#   ДАННЫЕ
# ============================================================

@dataclass
class Preparat:
    id: str
    name: str
    category: str
    files: List[str]

# ============================================================
#   СПИСОК ПРЕПАРАТОВ (ВСЕ)
# ============================================================

PREPARATS: List[Preparat] = [

    # --- Амилоидозы ---
    Preparat("amiloidoz_pecheni", "Амилоидоз печени", "Амилоидозы",
             ["amiloidoz_pecheni_1.jpeg", "amiloidoz_pecheni_2.jpeg", "amiloidoz_pecheni_3.jpeg"]),
    Preparat("amiloidoz_pochki", "Амилоидоз почки", "Амилоидозы",
             ["amiloidoz_pochki_1.jpeg", "amiloidoz_pochki_2.jpeg"]),
    Preparat("amiloidoz_selezenki_sagovaya", "Амилоидоз селезёнки («саговая форма»)", "Амилоидозы",
             ["amiloidoz_selezenki_sagovaya_1.jpeg", "amiloidoz_selezenki_sagovaya_2.jpeg"]),
    Preparat("amiloidoz_selezenki_salnaya", "Амилоидоз селезёнки («сальная форма»)", "Амилоидозы",
             ["amiloidoz_selezenki_salnaya_1.jpeg", "amiloidoz_selezenki_salnaya_2.jpeg", "amiloidoz_selezenki_salnaya_3.jpeg"]),

    # --- Воспаление ---
    Preparat("serozno_gemorragicheskaya_pnevmoniya", "Серозно-геморрагическая пневмония", "Воспаление",
             ["serozno_gemorragicheskaya_pnevmoniya_1.jpeg",
              "serozno_gemorragicheskaya_pnevmoniya_2.jpeg",
              "serozno_gemorragicheskaya_pnevmoniya_3.jpeg"]),
    Preparat("seroznoe_vosp_legkikh", "Серозное воспаление лёгких", "Воспаление",
             ["seroznoe_vosp_legkikh_1.jpeg", "seroznoe_vosp_legkikh_2.jpeg", "seroznoe_vosp_legkikh_3.jpeg"]),
    Preparat("ostryi_seroznyi_gastrit", "Острый серозный гастрит", "Воспаление",
             ["ostryi_seroznyi_gastrit_1.jpeg", "ostryi_seroznyi_gastrit_2.jpeg",
              "ostryi_seroznyi_gastrit_3.jpeg", "ostryi_seroznyi_gastrit_4.jpeg"]),
    Preparat("krupoznaya_pnevmoniya", "Крупозная пневмония", "Воспаление",
             ["krupoznaya_pnevmoniya_1.jpeg", "krupoznaya_pnevmoniya_2.jpeg"]),
    Preparat("fibrinoznyi_perikardit", "Фибринозный перикардит", "Воспаление",
             ["fibrinoznyi_perikardit_1.jpeg", "fibrinoznyi_perikardit_2.jpeg", "fibrinoznyi_perikardit_3.jpeg"]),
    Preparat("difteriticheskii_enterit", "Дифтеритический энтерит", "Воспаление",
             ["difteriticheskii_enterit_1.jpeg", "difteriticheskii_enterit_2.jpeg"]),
    Preparat("gemorragicheskoe_vospalenie_kishechnika", "Геморрагическое воспаление кишечника", "Воспаление",
             ["gemorragicheskoe_vospalenie_kishechnika_1.jpeg",
              "gemorragicheskoe_vospalenie_kishechnika_2.jpeg",
              "gemorragicheskoe_vospalenie_kishechnika_3.jpeg"]),
    Preparat("gnoinyi_nefrit", "Гнойный нефрит", "Воспаление",
             ["gnoinyi_nefrit_1.jpeg", "gnoinyi_nefrit_2.jpeg",
              "gnoinyi_nefrit_3.jpeg", "gnoinyi_nefrit_4.jpeg"]),
    Preparat("khronicheskii_abscess_pecheni", "Хронический абсцесс печени", "Воспаление",
             ["khronicheskii_abscess_pecheni_1.jpeg"]),
    Preparat("khronicheskii_kataralnyi_enterit_ge", "Хр. катаральный энтерит (Г-Э)", "Воспаление",
             ["khronicheskii_kataralnyi_enterit_ge_1.jpeg",
              "khronicheskii_kataralnyi_enterit_ge_2.jpeg",
              "khronicheskii_kataralnyi_enterit_ge_3.jpeg",
              "khronicheskii_kataralnyi_enterit_ge_4.jpeg"]),
    Preparat("khronicheskii_kataralnyi_enterit_sudan", "Хр. катаральный энтерит (Судан III)", "Воспаление",
             ["khronicheskii_kataralnyi_enterit_sudan_1.jpeg",
              "khronicheskii_kataralnyi_enterit_sudan_2.jpeg",
              "khronicheskii_kataralnyi_enterit_sudan_3.jpeg"]),

    # --- Дистрофии ---
    Preparat("zernistaya_distrofiya_pochki", "Зернистая дистрофия почки", "Дистрофии",
             ["zernistaya_distrofiya_pochki_1.jpeg", "zernistaya_distrofiya_pochki_2.jpeg"]),
    Preparat("zernistaya_distrofiya_pecheni", "Зернистая дистрофия печени", "Дистрофии",
             ["zernistaya_distrofiya_pecheni_1.jpeg", "zernistaya_distrofiya_pecheni_2.jpeg"]),
    Preparat("gialinovo_kapelnaya_distrofiya_pochki", "Гиалиново-капельная дистрофия почки", "Дистрофии",
             ["gialinovo_kapelnaya_distrofiya_pochki_1.jpeg",
              "gialinovo_kapelnaya_distrofiya_pochki_2.jpeg",
              "gialinovo_kapelnaya_distrofiya_pochki_3.jpeg"]),
    Preparat("vakuolnaya_distrofiya_pochki", "Вакуольная дистрофия почки", "Дистрофии",
             ["vakuolnaya_distrofiya_pochki_1.jpeg"]),
    Preparat("kolloidnaya_distrofiya_shchitovidnoi", "Коллоидная дистрофия щитовидной железы", "Дистрофии",
             ["kolloidnaya_distrofiya_shchitovidnoi_1.jpeg",
              "kolloidnaya_distrofiya_shchitovidnoi_2.jpeg"]),
    Preparat("zhirovaia_distrofiya_pecheni", "Жировая дистрофия печени", "Дистрофии",
             ["zhirovaia_distrofiya_pecheni_1.jpeg", "zhirovaia_distrofiya_pecheni_2.jpeg"]),

    # --- Гиалиноз ---
    Preparat("gialinoz_stenki_sosuda_matki", "Гиалиноз стенки сосуда матки", "Гиалинозы",
             ["gialinoz_stenki_sosuda_matki_1.jpeg",
              "gialinoz_stenki_sosuda_matki_2.jpeg",
              "gialinoz_stenki_sosuda_matki_3.jpeg"]),
    Preparat("gialinoz_selezenki", "Гиалиноз селезёнки", "Гиалинозы",
             ["gialinoz_selezenki_1.jpeg", "gialinoz_selezenki_2.jpeg", "gialinoz_selezenki_3.jpeg"]),

    # --- Пигменты ---
    Preparat("hemosideroz_pecheni", "Гемосидероз печени", "Пигменты",
             ["hemosideroz_pecheni_1.jpeg", "hemosideroz_pecheni_2.jpeg"]),
    Preparat("hemosideroz_pecheni_muskatnaya", "Гемосидероз печени («мускатная печень»)", "Пигменты",
             ["hemosideroz_pecheni_muskatnaya_1.jpeg",
              "hemosideroz_pecheni_muskatnaya_2.jpeg",
              "hemosideroz_pecheni_muskatnaya_3.jpeg"]),
    Preparat("hemosideroz_selezenki_ge", "Гемосидероз селезёнки (Г-Э)", "Пигменты",
             ["hemosideroz_selezenki_ge_1.jpeg", "hemosideroz_selezenki_ge_2.jpeg",
              "hemosideroz_selezenki_ge_3.jpeg", "hemosideroz_selezenki_ge_4.jpeg"]),
    Preparat("hemosideroz_selezenki_perls", "Гемосидероз селезёнки (Перлс)", "Пигменты",
             ["hemosideroz_selezenki_perls_1.jpeg", "hemosideroz_selezenki_perls_2.jpeg",
              "hemosideroz_selezenki_perls_3.jpeg", "hemosideroz_selezenki_perls_4.jpeg"]),
    Preparat("melanoz_pecheni", "Меланоз печени", "Пигменты",
             ["melanoz_pecheni_1.jpeg", "melanoz_pecheni_2.jpeg", "melanoz_pecheni_3.jpeg"]),
    Preparat("antrakoz_legkikh", "Антракоз лёгких", "Пигменты",
             ["antrakoz_legkikh_1.jpeg", "antrakoz_legkikh_2.jpeg", "antrakoz_legkikh_3.jpeg"]),

    # --- Некроз ---
    Preparat("nekroticheskii_nefroz", "Некротический нефроз", "Некроз",
             ["nekroticheskii_nefroz_1.jpeg", "nekroticheskii_nefroz_2.jpeg", "nekroticheskii_nefroz_3.jpeg"]),
    Preparat("tvorozhistyi_nekroz_lymph_tb", "Творожистый некроз лимфоузла (ТБ)", "Некроз",
             ["tvorozhistyi_nekroz_lymph_tb_1.jpeg", "tvorozhistyi_nekroz_lymph_tb_2.jpeg"]),
    Preparat("tsenkerovskii_voskovidnyi_nekroz_myshc", "Ценкеровский некроз мышц", "Некроз",
             ["tsenkerovskii_voskovidnyi_nekroz_myshc_1.jpeg",
              "tsenkerovskii_voskovidnyi_nekroz_myshc_2.jpeg"]),
    Preparat("tvorozhistyi_nekroz_legkikh_tb", "Творожистый некроз лёгких (ТБ)", "Некроз",
             ["tvorozhistyi_nekroz_legkikh_tb_1.jpeg", "tvorozhistyi_nekroz_legkikh_tb_2.jpeg"]),

    # --- Кровообращение ---
    Preparat("buraya_induratsiya_pecheni", "Бурая индурация печени", "Кровообращение",
             ["buraya_induratsiya_pecheni_1.jpeg", "buraya_induratsiya_pecheni_2.jpeg"]),
    Preparat("ostraya_zastoynaya_venoznaya_giperemiya_pecheni",
             "Острая застойная венозная гиперемия печени", "Кровообращение",
             ["ostraya_zastoynaya_venoznaya_giperemiya_pecheni_1.jpeg",
              "ostraya_zastoynaya_venoznaya_giperemiya_pecheni_2.jpeg"]),
    Preparat("khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen",
             "Хроническое венозное полнокровие печени («мускатная печень»)", "Кровообращение",
             ["khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen_1.jpeg",
              "khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen_2.jpeg"]),
    Preparat("ostraya_zastoynaya_giperemiya_otek_legkikh",
             "Острая застойная гиперемия и отёк лёгких", "Кровообращение",
             ["ostraya_zastoynaya_giperemiya_otek_legkikh_1.jpeg",
              "ostraya_zastoynaya_giperemiya_otek_legkikh_2.jpeg"]),
    Preparat("buraya_induratsiya_legkogo", "Бурая индурация лёгкого", "Кровообращение",
             ["buraya_induratsiya_legkogo_1.jpeg", "buraya_induratsiya_legkogo_2.jpeg"]),

    # --- Инфаркты ---
    Preparat("ishemicheskii_infarkt_pochki", "Ишемический инфаркт почки", "Инфаркты",
             ["ishemicheskii_infarkt_pochki_1.jpeg", "ishemicheskii_infarkt_pochki_2.jpeg"]),
    Preparat("ishemicheskii_infarkt_selezenki", "Ишемический инфаркт селезёнки", "Инфаркты",
             ["ishemicheskii_infarkt_selezenki_1.jpeg", "ishemicheskii_infarkt_selezenki_2.jpeg"]),
    Preparat("gemorragicheskii_infarkt_pochki", "Геморрагический инфаркт почки", "Инфаркты",
             ["gemorragicheskii_infarkt_pochki_1.jpeg",
              "gemorragicheskii_infarkt_pochki_2.jpeg",
              "gemorragicheskii_infarkt_pochki_3.jpeg"]),
    Preparat("gemorragicheskii_infarkt_legkogo", "Геморрагический инфаркт лёгкого", "Инфаркты",
             ["gemorragicheskii_infarkt_legkogo_1.jpeg",
              "gemorragicheskii_infarkt_legkogo_2.jpeg"]),

    # --- Тромбоз ---
    Preparat("smeshannyi_tromb", "Смешанный тромб", "Тромбоз",
             ["smeshannyi_tromb_1.jpeg", "smeshannyi_tromb_2.jpeg"]),
]

PREP_BY_ID = {p.id: p for p in PREPARATS}

CATEGORIES = sorted(list(set(p.category for p in PREPARATS)))

# ============================================================
#   СОСТОЯНИЯ ПОЛЬЗОВАТЕЛЕЙ
# ============================================================

STATE = {}   # user_id: {mode, section, remaining, current, errors}

def get_state(uid):
    if uid not in STATE:
        STATE[uid] = {
            "mode": None,
            "section": None,
            "remaining": [],
            "current": None,
            "errors": set(),
        }
    return STATE[uid]

# ============================================================
#   КЛАВИАТУРЫ
# ============================================================

def main_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📚 Обучение", "🎲 Случайные препараты")
    kb.row("❓ Тест (варианты)", "⌨️ Тест (ввод)")
    kb.row("🔁 Повторить ошибки", "📊 Статистика")
    return kb


def train_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("➡️ Следующий")
    kb.row("🔙 Назад к разделам")
    kb.row("🏠 Домой")
    return kb


# ============================================================
#   ПОМОЩНИКИ
# ============================================================

def send_all_photos(chat_id, prep: Preparat, caption=None):
    for i, file in enumerate(prep.files):
        url = BASE_URL + file
        if i == 0:
            bot.send_photo(chat_id, url, caption=caption)
        else:
            bot.send_photo(chat_id, url)


# ============================================================
#   /start
# ============================================================

@bot.message_handler(commands=["start"])
def start_cmd(msg):
    bot.send_message(msg.chat.id, "Привет! Выбери режим:", reply_markup=main_kb())

# ============================================================
#   ОБУЧЕНИЕ
# ============================================================

@bot.message_handler(func=lambda m: m.text == "📚 Обучение")
def learn(msg):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for c in CATEGORIES:
        kb.row(c)
    kb.row("🏠 Домой")
    bot.send_message(msg.chat.id, "Выбери раздел:", reply_markup=kb)


@bot.message_handler(func=lambda m: m.text in CATEGORIES)
def learn_section(msg):
    uid = msg.from_user.id
    st = get_state(uid)

    st["mode"] = "learn"
    st["section"] = msg.text
    items = [p for p in PREPARATS if p.category == msg.text]
    random.shuffle(items)
    st["remaining"] = items
    st["current"] = None

    handle_next(msg)


@bot.message_handler(func=lambda m: m.text == "➡️ Следующий")
def handle_next(msg):
    uid = msg.from_user.id
    st = get_state(uid)

    if st["mode"] != "learn":
        bot.send_message(msg.chat.id, "Сперва выбери раздел обучения.")
        return

    if not st["remaining"]:
        bot.send_message(msg.chat.id, "Раздел пройден! 🎉", reply_markup=main_kb())
        return

    prep = st["remaining"].pop(0)
    st["current"] = prep.id

    send_all_photos(msg.chat.id, prep, caption=f"<b>{prep.name}</b>")
    bot.send_message(msg.chat.id, "👇 Продолжай обучение:", reply_markup=train_kb())


@bot.message_handler(func=lambda m: m.text == "🔙 Назад к разделам")
def back_to_sections(msg):
    learn(msg)


@bot.message_handler(func=lambda m: m.text == "🏠 Домой")
def home(msg):
    bot.send_message(msg.chat.id, "Главное меню:", reply_markup=main_kb())

# ============================================================
#   СЛУЧАЙНЫЙ ПРОСМОТР БЕЗ ПОВТОРОВ
# ============================================================

@bot.message_handler(func=lambda m: m.text == "🎲 Случайные препараты")
def random_view(msg):
    uid = msg.from_user.id
    st = get_state(uid)

    if "random_used" not in st:
        st["random_used"] = set()

    available = [p for p in PREPARATS if p.id not in st["random_used"]]

    if not available:
        st["random_used"] = set()
        available = PREPARATS.copy()

    prep = random.choice(available)
    st["random_used"].add(prep.id)

    send_all_photos(msg.chat.id, prep, f"<b>{prep.name}</b>")

# ============================================================
#   ТЕСТ (ВАРИАНТЫ)
# ============================================================

@bot.message_handler(func=lambda m: m.text == "❓ Тест (варианты)")
def test_variants(msg):
    uid = msg.from_user.id
    st = get_state(uid)

    target = random.choice(PREPARATS)
    st["mode"] = "mcq"
    st["current"] = target.id

    variants = {target.id}
    while len(variants) < 4:
        variants.add(random.choice(PREPARATS).id)

    variants = list(variants)
    random.shuffle(variants)

    kb = types.InlineKeyboardMarkup()
    for vid in variants:
        kb.add(types.InlineKeyboardButton(text=PREP_BY_ID[vid].name, callback_data=f"ans:{vid}"))

    kb.add(types.InlineKeyboardButton(text="Домой", callback_data="home"))

    url = BASE_URL + random.choice(target.files)
    bot.send_photo(msg.chat.id, url, caption="Что за препарат?", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data.startswith("ans:"))
def check_answer(call):
    uid = call.from_user.id
    st = get_state(uid)

    chosen = call.data.split(":")[1]
    correct = st["current"]

    if chosen == correct:
        text = "✅ Верно!"
    else:
        text = f"❌ Неверно!\nПравильный ответ: <b>{PREP_BY_ID[correct].name}</b>"
        st["errors"].add(correct)

    bot.edit_message_caption(
        caption=text,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    bot.answer_callback_query(call.id)

# ============================================================
#   ТЕСТ (ВВОД)
# ============================================================

@bot.message_handler(func=lambda m: m.text == "⌨️ Тест (ввод)")
def typing_test(msg):
    uid = msg.from_user.id
    st = get_state(uid)

    target = random.choice(PREPARATS)
    st["mode"] = "typing"
    st["current"] = target.id

    url = BASE_URL + random.choice(target.files)
    bot.send_photo(msg.chat.id, url)
    bot.send_message(msg.chat.id, "Введите название препарата:")

@bot.message_handler(func=lambda m: True)
def check_typing(msg):
    uid = msg.from_user.id
    st = get_state(uid)

    if st["mode"] != "typing":
        return

    target = PREP_BY_ID[st["current"]]

    user = msg.text.lower()
    correct = target.name.lower()

    ok = sum(w in user for w in correct.split() if len(w) > 4) >= 1

    if ok:
        bot.send_message(msg.chat.id, "✅ Верно!", reply_markup=main_kb())
    else:
        bot.send_message(msg.chat.id, f"❌ Неверно!\nПравильный ответ: <b>{target.name}</b>", reply_markup=main_kb())
        st["errors"].add(target.id)

    st["mode"] = None

# ============================================================
#   ПОВТОР ОШИБОК
# ============================================================

@bot.message_handler(func=lambda m: m.text == "🔁 Повторить ошибки")
def repeat_errors(msg):
    uid = msg.from_user.id
    st = get_state(uid)

    if not st["errors"]:
        bot.send_message(msg.chat.id, "Ошибок нет — молодец! 🎉")
        return

    prep_id = random.choice(list(st["errors"]))
    prep = PREP_BY_ID[prep_id]

    send_all_photos(msg.chat.id, prep, f"Повтор ошибки:\n<b>{prep.name}</b>")

# ============================================================
#   СТАТИСТИКА
# ============================================================

@bot.message_handler(func=lambda m: m.text == "📊 Статистика")
def stats(msg):
    uid = msg.from_user.id
    st = get_state(uid)

    bot.send_message(
        msg.chat.id,
        f"Ошибок всего: {len(st['errors'])}",
        reply_markup=main_kb()
    )

# ============================================================
#   ЗАПУСК
# ============================================================

print("Бот запущен!")
bot.infinity_polling()
