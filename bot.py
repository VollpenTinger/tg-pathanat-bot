import os
import random
from dataclasses import dataclass
from typing import List, Dict

import telebot
from telebot import types


# =========================
# НАСТРОЙКИ
# =========================

BOT_TOKEN = "8245340349:AAF2sB8Gn5dXiqQQ1ldxAHqk_wpsdcLrH2c"
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")


# =========================
# МОДЕЛЬ ПРЕПАРАТА
# =========================

@dataclass
class Preparat:
    id: str
    name: str
    category: str
    files: List[str]


# =========================
# СПИСОК ПРЕПАРАТОВ
# =========================

# (вставлены ВСЕ препараты из твоей папки GitHub)
PREPARATS: List[Preparat] = [

    # --- Амилоидозы ---
    Preparat("amiloidoz_pecheni",
             "Амилоидоз печени", "Амилоидозы",
             ["amiloidoz_pecheni_1.jpeg", "amiloidoz_pecheni_2.jpeg", "amiloidoz_pecheni_3.jpeg"]),

    Preparat("amiloidoz_pochki",
             "Амилоидоз почки", "Амилоидозы",
             ["amiloidoz_pochki_1.jpeg", "amiloidoz_pochki_2.jpeg"]),

    Preparat("amiloidoz_selezenki_sagovaya",
             "Амилоидоз селезёнки («саговая» форма)", "Амилоидозы",
             ["amiloidoz_selezenki_sagovaya_1.jpeg", "amiloidoz_selezenki_sagovaya_2.jpeg"]),

    Preparat("amiloidoz_selezenki_salnaya",
             "Амилоидоз селезёнки («сальная» форма)", "Амилоидозы",
             ["amiloidoz_selezenki_salnaya_1.jpeg", "amiloidoz_selezenki_salnaya_2.jpeg", "amiloidoz_selezenki_salnaya_3.jpeg"]),

    # --- Воспаление ---
    Preparat("serozno_gemorragicheskaya_pnevmoniya",
             "Серозно-геморрагическая пневмония", "Воспаление",
             ["serozno_gemorragicheskaya_pnevmoniya_1.jpeg",
              "serozno_gemorragicheskaya_pnevmoniya_2.jpeg",
              "serozno_gemorragicheskaya_pnevmoniya_3.jpeg"]),

    Preparat("seroznoe_vosp_legkikh",
             "Серозное воспаление лёгких", "Воспаление",
             ["seroznoe_vosp_legkikh_1.jpeg",
              "seroznoe_vosp_legkikh_2.jpeg",
              "seroznoe_vosp_legkikh_3.jpeg"]),

    Preparat("ostryi_seroznyi_gastrit",
             "Острый серозный гастрит", "Воспаление",
             ["ostryi_seroznyi_gastrit_1.jpeg",
              "ostryi_seroznyi_gastrit_2.jpeg",
              "ostryi_seroznyi_gastrit_3.jpeg",
              "ostryi_seroznyi_gastrit_4.jpeg"]),

    Preparat("krupoznaya_pnevmoniya",
             "Крупозная пневмония", "Воспаление",
             ["krupoznaya_pnevmoniya_1.jpeg", "krupoznaya_pnevmoniya_2.jpeg"]),

    Preparat("fibrinoznyi_perikardit",
             "Фибринозный перикардит", "Воспаление",
             ["fibrinoznyi_perikardit_1.jpeg",
              "fibrinoznyi_perikardit_2.jpeg",
              "fibrinoznyi_perikardit_3.jpeg"]),

    Preparat("difteriticheskii_enterit",
             "Дифтеритический энтерит", "Воспаление",
             ["difteriticheskii_enterit_1.jpeg", "difteriticheskii_enterit_2.jpeg"]),

    Preparat("gemorragicheskoe_vospalenie_kishechnika",
             "Геморрагическое воспаление кишечника", "Воспаление",
             ["gemorragicheskoe_vospalenie_kishechnika_1.jpeg",
              "gemorragicheskoe_vospalenie_kishechnika_2.jpeg",
              "gemorragicheskoe_vospalenie_kishechnika_3.jpeg"]),

    Preparat("gnoinyi_nefrit", "Гнойный нефрит", "Воспаление",
             ["gnoinyi_nefrit_1.jpeg", "gnoinyi_nefrit_2.jpeg", "gnoinyi_nefrit_3.jpeg", "gnoinyi_nefrit_4.jpeg"]),

    Preparat("khronicheskii_abscess_pecheni",
             "Хронический абсцесс печени", "Воспаление",
             ["khronicheskii_abscess_pecheni_1.jpeg"]),

    Preparat("khronicheskii_kataralnyi_enterit_ge",
             "Хронический катаральный энтерит (гематоксилин-эозин)", "Воспаление",
             ["khronicheskii_kataralnyi_enterit_ge_1.jpeg",
              "khronicheskii_kataralnyi_enterit_ge_2.jpeg",
              "khronicheskii_kataralnyi_enterit_ge_3.jpeg",
              "khronicheskii_kataralnyi_enterit_ge_4.jpeg"]),

    Preparat("khronicheskii_kataralnyi_enterit_sudan",
             "Хронический катаральный энтерит (Судан III)", "Воспаление",
             ["khronicheskii_kataralnyi_enterit_sudan_1.jpeg",
              "khronicheskii_kataralnyi_enterit_sudan_2.jpeg",
              "khronicheskii_kataralnyi_enterit_sudan_3.jpeg"]),

    # --- Дистрофии ---
    Preparat("zernistaya_distrofiya_pochki",
             "Зернистая дистрофия почки", "Дистрофии",
             ["zernistaya_distrofiya_pochki_1.jpeg", "zernistaya_distrofiya_pochki_2.jpeg"]),

    Preparat("zernistaya_distrofiya_pecheni",
             "Зернистая дистрофия печени", "Дистрофии",
             ["zernistaya_distrofiya_pecheni_1.jpeg", "zernistaya_distrofiya_pecheni_2.jpeg"]),

    Preparat("gialinovo_kapelnaya_distrofiya_pochki",
             "Гиалиново-капельная дистрофия почки", "Дистрофии",
             ["gialinovo_kapelnaya_distrofiya_pochki_1.jpeg",
              "gialinovo_kapelnaya_distrofiya_pochki_2.jpeg",
              "gialinovo_kapelnaya_distrofiya_pochki_3.jpeg"]),

    Preparat("vakuolnaya_distrofiya_pochki",
             "Вакуольная дистрофия почки", "Дистрофии",
             ["vakuolnaya_distrofiya_pochki_1.jpeg"]),

    Preparat("kolloidnaya_distrofiya_shchitovidnoi",
             "Коллоидная дистрофия щитовидной железы", "Дистрофии",
             ["kolloidnaya_distrofiya_shchitovidnoi_1.jpeg",
              "kolloidnaya_distrofiya_shchitovidnoi_2.jpeg"]),

    Preparat("zhirovaia_distrofiya_pecheni",
             "Жировая дистрофия печени", "Дистрофии",
             ["zhirovaia_distrofiya_pecheni_1.jpeg",
              "zhirovaia_distrofiya_pecheni_2.jpeg"]),

    # --- Гиалинозы ---
    Preparat("gialinoz_stenki_sosuda_matki",
             "Гиалиноз стенки сосуда матки", "Гиалинозы",
             ["gialinoz_stenki_sosuda_matki_1.jpeg",
              "gialinoz_stenki_sosuda_matki_2.jpeg",
              "gialinoz_stenki_sosuda_matki_3.jpeg"]),

    Preparat("gialinoz_selezenki",
             "Гиалиноз селезёнки", "Гиалинозы",
             ["gialinoz_selezenki_1.jpeg",
              "gialinoz_selezenki_2.jpeg",
              "gialinoz_selezenki_3.jpeg"]),

    # --- Пигменты ---
    Preparat("hemosideroz_pecheni",
             "Гемосидероз печени", "Пигменты",
             ["hemosideroz_pecheni_1.jpeg",
              "hemosideroz_pecheni_2.jpeg"]),

    Preparat("hemosideroz_pecheni_muskatnaya",
             "Гемосидероз печени («мускатная печень»)", "Пигменты",
             ["hemosideroz_pecheni_muskatnaya_1.jpeg",
              "hemosideroz_pecheni_muskatnaya_2.jpeg",
              "hemosideroz_pecheni_muskatnaya_3.jpeg"]),

    Preparat("hemosideroz_selezenki_ge",
             "Гемосидероз селезёнки (Г-Э)", "Пигменты",
             ["hemosideroz_selezenki_ge_1.jpeg",
              "hemosideroz_selezenki_ge_2.jpeg",
              "hemosideroz_selezenki_ge_3.jpeg",
              "hemosideroz_selezenki_ge_4.jpeg"]),

    Preparat("hemosideroz_selezenki_perls",
             "Гемосидероз селезёнки (реакция Перлса)", "Пигменты",
             ["hemosideroz_selezenki_perls_1.jpeg",
              "hemosideroz_selezenki_perls_2.jpeg",
              "hemosideroz_selezenki_perls_3.jpeg",
              "hemosideroz_selezenki_perls_4.jpeg"]),

    Preparat("melanoz_pecheni",
             "Меланоз печени", "Пигменты",
             ["melanoz_pecheni_1.jpeg",
              "melanoz_pecheni_2.jpeg",
              "melanoz_pecheni_3.jpeg"]),

    Preparat("antrakoz_legkikh",
             "Антракоз лёгких", "Пигменты",
             ["antrakoz_legkikh_1.jpeg",
              "antrakoz_legkikh_2.jpeg",
              "antrakoz_legkikh_3.jpeg"]),

    # --- Некрозы ---
    Preparat("nekroticheskii_nefroz",
             "Некротический нефроз", "Некроз",
             ["nekroticheskii_nefroz_1.jpeg",
              "nekroticheskii_nefroz_2.jpeg",
              "nekroticheskii_nefroz_3.jpeg"]),

    Preparat("tvorozhistyi_nekroz_lymph_tb",
             "Казеозный некроз лимфоузла (туберкулёз)", "Некроз",
             ["tvorozhistyi_nekroz_lymph_tb_1.jpeg",
              "tvorozhistyi_nekroz_lymph_tb_2.jpeg"]),

    Preparat("tsenkerovskii_voskovidnyi_nekroz_myshc",
             "Ценкеровский (восковидный) некроз мышц", "Некроз",
             ["tsenkerovskii_voskovidnyi_nekroz_myshc_1.jpeg",
              "tsenkerovskii_voskovidnyi_nekroz_myshc_2.jpeg"]),

    Preparat("tvorozhistyi_nekroz_legkikh_tb",
             "Казеозный некроз лёгких (туберкулёз)", "Некроз",
             ["tvorozhistyi_nekroz_legkikh_tb_1.jpeg",
              "tvorozhistyi_nekroz_legkikh_tb_2.jpeg"]),

    # --- Кровообращение ---
    Preparat("buraya_induratsiya_pecheni",
             "Бурая индурация печени", "Кровообращение",
             ["buraya_induratsiya_pecheni_1.jpeg",
              "buraya_induratsiya_pecheni_2.jpeg"]),

    Preparat("ostraya_zastoynaya_venoznaya_giperemiya_pecheni",
             "Острая застойная венозная гиперемия печени", "Кровообращение",
             ["ostraya_zastoynaya_venoznaya_giperemiya_pecheni_1.jpeg",
              "ostraya_zastoynaya_venoznaya_giperemiya_pecheni_2.jpeg"]),

    Preparat("khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen",
             "Хроническое венозное полнокровие (мускатная печень)", "Кровообращение",
             ["khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen_1.jpeg",
              "khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen_2.jpeg"]),

    Preparat("ostraya_zastoynaya_giperemiya_otek_legkikh",
             "Острая застойная гиперемия и отёк лёгких", "Кровообращение",
             ["ostraya_zastoynaya_giperemiya_otek_legkikh_1.jpeg",
              "ostraya_zastoynaya_giperemiya_otek_legkikh_2.jpeg"]),

    Preparat("buraya_induratsiya_legkogo",
             "Бурая индурация лёгкого", "Кровообращение",
             ["buraya_induratsiya_legkogo_1.jpeg",
              "buraya_induratsiya_legkogo_2.jpeg"]),

    # --- Инфаркты ---
    Preparat("ishemicheskii_infarkt_pochki",
             "Ишемический инфаркт почки", "Инфаркты",
             ["ishemicheskii_infarkt_pochki_1.jpeg",
              "ishemicheskii_infarkt_pochki_2.jpeg"]),

    Preparat("ishemicheskii_infarkt_selezenki",
             "Ишемический инфаркт селезёнки", "Инфаркты",
             ["ishemicheskii_infarkt_selezenki_1.jpeg",
              "ishemicheskii_infarkt_selezenki_2.jpeg"]),

    Preparat("gemorragicheskii_infarkt_pochki",
             "Геморрагический инфаркт почки", "Инфаркты",
             ["gemorragicheskii_infarkt_pochki_1.jpeg",
              "gemorragicheskii_infarkt_pochki_2.jpeg",
              "gemorragicheskii_infarkt_pochki_3.jpeg"]),

    Preparat("gemorragicheskii_infarkt_legkogo",
             "Геморрагический инфаркт лёгкого", "Инфаркты",
             ["gemorragicheskii_infarkt_legkogo_1.jpeg",
              "gemorragicheskii_infarkt_legkogo_2.jpeg"]),

    # --- Тромбоз ---
    Preparat("smeshannyi_tromb",
             "Смешанный тромб", "Тромбоз",
             ["smeshannyi_tromb_1.jpeg", "smeshannyi_tromb_2.jpeg"]),
]


# Быстрая таблица доступа
PREP_BY_ID = {p.id: p for p in PREPARATS}


# =========================
# КАТЕГОРИИ
# =========================

CATEGORIES = [
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


# =========================
# СОСТОЯНИЕ ПОЛЬЗОВАТЕЛЕЙ
# =========================

user_state: Dict[int, Dict] = {}
user_stats: Dict[int, Dict] = {}


def get_stats(uid):
    if uid not in user_stats:
        user_stats[uid] = {"total": 0, "correct": 0, "wrong": 0, "errors": set()}
    return user_stats[uid]


# =========================
# КЛАВИАТУРЫ
# =========================

def main_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📚 Обучение")
    kb.row("❓ Тест (варианты)", "⌨️ Тест (ввод)")
    kb.row("📊 Статистика", "🔁 Повторить ошибки")
    return kb


def training_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("➡️ Следующий")
    kb.row("🔙 Назад к разделам")
    kb.row("🏠 В меню")
    return kb


# =========================
# ВСПОМОГАТЕЛЬНЫЕ
# =========================

def send_preparat(chat_id, prep: Preparat):
    bot.send_message(chat_id, f"<b>{prep.name}</b>")

    for f in prep.files:
        path = os.path.join("preparats", f)
        if os.path.exists(path):
            with open(path, "rb") as ph:
                bot.send_photo(chat_id, ph)


# =========================
# ОТДЕЛ: ОБУЧЕНИЕ
# =========================

def start_training(uid, category):
    ids = [p.id for p in PREPARATS if p.category == category]
    random.shuffle(ids)
    user_state[uid] = {
        "mode": "train",
        "category": category,
        "list": ids
    }


def next_training(uid):
    st = user_state.get(uid)
    if not st or st["mode"] != "train":
        return None

    if not st["list"]:
        return None

    pid = st["list"].pop()
    return PREP_BY_ID[pid]


# =========================
# ТЕСТЫ
# =========================

def build_mcq(prep):
    others = [p for p in PREPARATS if p.id != prep.id]
    random.shuffle(others)
    opts = [prep] + others[:3]
    random.shuffle(opts)
    return opts


def normalize(t):
    return t.lower().replace("ё", "е").strip()


# =========================
# ХЕНДЛЕРЫ
# =========================

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,
                     "Привет! Готов учить патан 🔬❤️",
                     reply_markup=main_kb())


# --- ОБУЧЕНИЕ ---

@bot.message_handler(func=lambda m: m.text == "📚 Обучение")
def training_menu(m):
    kb = types.InlineKeyboardMarkup()
    for c in CATEGORIES:
        kb.add(types.InlineKeyboardButton(c, callback_data=f"cat:{c}"))
    bot.send_message(m.chat.id, "Выбери раздел:", reply_markup=kb)


@bot.callback_query_handler(func=lambda c: c.data.startswith("cat:"))
def training_start(cb):
    _, cat = cb.data.split(":", 1)
    uid = cb.from_user.id

    start_training(uid, cat)

    prep = next_training(uid)
    bot.answer_callback_query(cb.id, f"Раздел: {cat}")

    send_preparat(cb.message.chat.id, prep)
    bot.send_message(cb.message.chat.id, "⬇️ Дальше:", reply_markup=training_kb())


@bot.message_handler(func=lambda m: m.text == "➡️ Следующий")
def training_next(m):
    uid = m.from_user.id
    prep = next_training(uid)

    if not prep:
        bot.send_message(m.chat.id,
                         "🎉 Все препараты раздела просмотрены!",
                         reply_markup=main_kb())
        return

    send_preparat(m.chat.id, prep)


@bot.message_handler(func=lambda m: m.text == "🔙 Назад к разделам")
def back_to_sections(m):
    if m.from_user.id in user_state:
        user_state.pop(m.from_user.id)

    training_menu(m)


@bot.message_handler(func=lambda m: m.text == "🏠 В меню")
def to_menu(m):
    if m.from_user.id in user_state:
        user_state.pop(m.from_user.id)
    bot.send_message(m.chat.id, "Главное меню:", reply_markup=main_kb())


# --- ТЕСТ: ВАРИАНТЫ ---

@bot.message_handler(func=lambda m: m.text == "❓ Тест (варианты)")
def test_mcq(m):
    uid = m.from_user.id
    prep = random.choice(PREPARATS)

    user_state[uid] = {"mode": "mcq", "correct": prep.id}

    opts = build_mcq(prep)

    kb = types.InlineKeyboardMarkup()
    for o in opts:
        kb.add(types.InlineKeyboardButton(o.name, callback_data=f"ans:{o.id}"))

    with open(os.path.join("preparats", prep.files[0]), "rb") as ph:
        bot.send_photo(m.chat.id, ph, caption="Что за препарат?", reply_markup=kb)


@bot.callback_query_handler(func=lambda c: c.data.startswith("ans:"))
def mcq_ans(cb):
    uid = cb.from_user.id
    st = user_state.get(uid)

    if not st or st["mode"] != "mcq":
        bot.answer_callback_query(cb.id, "Вопрос устарел")
        return

    chosen = cb.data.split(":", 1)[1]
    correct = st["correct"]

    stats = get_stats(uid)
    stats["total"] += 1

    if chosen == correct:
        stats["correct"] += 1
        txt = f"✅ Верно! Это <b>{PREP_BY_ID[correct].name}</b>"
    else:
        stats["wrong"] += 1
        stats["errors"].add(correct)
        txt = (f"❌ Неверно.\n"
               f"Правильный ответ: <b>{PREP_BY_ID[correct].name}</b>")

    bot.send_message(cb.message.chat.id, txt)
    bot.answer_callback_query(cb.id)

    test_mcq(cb.message)


# --- ТЕСТ: ВВОД ---

@bot.message_handler(func=lambda m: m.text == "⌨️ Тест (ввод)")
def test_typing(m):
    uid = m.from_user.id
    prep = random.choice(PREPARATS)

    user_state[uid] = {"mode": "typing", "correct": prep.id}

    with open(os.path.join("preparats", prep.files[0]), "rb") as ph:
        bot.send_photo(m.chat.id, ph)

    bot.send_message(m.chat.id, "Напиши название препарата:")


@bot.message_handler(func=lambda m: user_state.get(m.from_user.id, {}).get("mode") == "typing")
def typing_answer(m):
    uid = m.from_user.id
    st = user_state[uid]
    correct = PREP_BY_ID[st["correct"]]

    user = normalize(m.text)
    right = normalize(correct.name)

    stats = get_stats(uid)
    stats["total"] += 1

    key_words = [w for w in right.split() if len(w) > 3]

    if any(w in user for w in key_words):
        stats["correct"] += 1
        txt = f"✅ Верно! Это <b>{correct.name}</b>"
    else:
        stats["wrong"] += 1
        stats["errors"].add(correct.id)
        txt = f"❌ Неверно!\nПравильный ответ: <b>{correct.name}</b>"

    bot.send_message(m.chat.id, txt)
    test_typing(m)


# --- СТАТИСТИКА ---

@bot.message_handler(func=lambda m: m.text == "📊 Статистика")
def stats_handler(m):
    st = get_stats(m.from_user.id)

    total = st["total"]
    acc = round(st["correct"] * 100 / total, 1) if total else 0

    bot.send_message(m.chat.id,
                     f"<b>Статистика:</b>\n"
                     f"Всего вопросов: {total}\n"
                     f"Правильных: {st['correct']}\n"
                     f"Неправильных: {st['wrong']}\n"
                     f"Точность: {acc}%\n"
                     f"Ошибок: {len(st['errors'])}",
                     reply_markup=main_kb())


# =========================
# ЗАПУСК
# =========================

print("Бот работает…")
bot.infinity_polling()
    
