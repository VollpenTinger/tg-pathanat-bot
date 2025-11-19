import os
import random
from dataclasses import dataclass
from typing import List, Dict, Optional

import telebot
from telebot import types

# =========================
# НАСТРОЙКИ
# =========================

BOT_TOKEN = "8245340349:AAF2sB8Gn5dXiqQQ1ldxAHqk_wpsdcLrH2c"
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# =========================
# ДАННЫЕ О ПРЕПАРАТАХ
# =========================

@dataclass
class Preparat:
    id: str
    name: str
    category: str
    files: List[str]


# === ПОЛНЫЙ СПИСОК ПРЕПАРАТОВ ===

PREPARATS: List[Preparat] = [
    Preparat("amiloidoz_pecheni", "Амилоидоз печени", "Амилоидозы",
             ["amiloidoz_pecheni_1.jpeg", "amiloidoz_pecheni_2.jpeg", "amiloidoz_pecheni_3.jpeg"]),

    Preparat("amiloidoz_pochki", "Амилоидоз почки", "Амилоидозы",
             ["amiloidoz_pochki_1.jpeg", "amiloidoz_pochki_2.jpeg"]),

    Preparat("amiloidoz_selezenki_sagovaya", "Амилоидоз селезёнки («саговая» форма)", "Амилоидозы",
             ["amiloidoz_selezenki_sagovaya_1.jpeg", "amiloidoz_selezenki_sagovaya_2.jpeg"]),

    Preparat("amiloidoz_selezenki_salnaya", "Амилоидоз селезёнки («сальная» форма)", "Амилоидозы",
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

    Preparat("khronicheskii_kataralnyi_enterit_ge", "Хронический катаральный энтерит (гематоксилин-эозин)", "Воспаление",
             ["khronicheskii_kataralnyi_enterit_ge_1.jpeg",
              "khronicheskii_kataralnyi_enterit_ge_2.jpeg",
              "khronicheskii_kataralnyi_enterit_ge_3.jpeg",
              "khronicheskii_kataralnyi_enterit_ge_4.jpeg"]),

    Preparat("khronicheskii_kataralnyi_enterit_sudan", "Хронический катаральный энтерит (Судан III)", "Воспаление",
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

    # --- Гиалинозы ---
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

    Preparat("hemosideroz_selezenki_ge", "Гемосидероз селезёнки (гематоксилин-эозин)", "Пигменты",
             ["hemosideroz_selezenki_ge_1.jpeg",
              "hemosideroz_selezenki_ge_2.jpeg",
              "hemosideroz_selezenki_ge_3.jpeg",
              "hemosideroz_selezenki_ge_4.jpeg"]),

    Preparat("hemosideroz_selezenki_perls", "Гемосидероз селезёнки (реакция Перлса)", "Пигменты",
             ["hemosideroz_selezenki_perls_1.jpeg",
              "hemosideroz_selezenki_perls_2.jpeg",
              "hemosideroz_selezenki_perls_3.jpeg",
              "hemosideroz_selezenki_perls_4.jpeg"]),

    Preparat("melanoz_pecheni", "Меланоз печени", "Пигменты",
             ["melanoz_pecheni_1.jpeg", "melanoz_pecheni_2.jpeg", "melanoz_pecheni_3.jpeg"]),

    Preparat("antrakoz_legkikh", "Антракоз лёгких", "Пигменты",
             ["antrakoz_legkikh_1.jpeg", "antrakoz_legkikh_2.jpeg", "antrakoz_legkikh_3.jpeg"]),

    # --- Некроз ---
    Preparat("nekroticheskii_nefroz", "Некротический нефроз", "Некроз",
             ["nekroticheskii_nefroz_1.jpeg",
              "nekroticheskii_nefroz_2.jpeg",
              "nekroticheskii_nefroz_3.jpeg"]),

    Preparat("tvorozhistyi_nekroz_lymph_tb", "Творожистый некроз лимфоузла (туберкулёз)", "Некроз",
             ["tvorozhistyi_nekroz_lymph_tb_1.jpeg", "tvorozhistyi_nekroz_lymph_tb_2.jpeg"]),

    Preparat("tsenkerovskii_voskovidnyi_nekroz_myshc", "Ценкеровский некроз мышц", "Некроз",
             ["tsenkerovskii_voskovidnyi_nekroz_myshc_1.jpeg",
              "tsenkerovskii_voskovidnyi_nekroz_myshc_2.jpeg"]),

    Preparat("tvorozhistyi_nekroz_legkikh_tb", "Творожистый некроз лёгких (туберкулёз)", "Некроз",
             ["tvorozhistyi_nekroz_legkikh_tb_1.jpeg",
              "tvorozhistyi_nekroz_legkikh_tb_2.jpeg"]),

    # --- Кровообращение ---
    Preparat("buraya_induratsiya_pecheni", "Бурая индурация печени", "Кровообращение",
             ["buraya_induratsiya_pecheni_1.jpeg", "buraya_induratsiya_pecheni_2.jpeg"]),

    Preparat("ostraya_zastoynaya_venoznaya_giperemiya_pecheni",
             "Острая застойная венозная гиперемия печени",
             "Кровообращение",
             ["ostraya_zastoynaya_venoznaya_giperemiya_pecheni_1.jpeg",
              "ostraya_zastoynaya_venoznaya_giperemiya_pecheni_2.jpeg"]),

    Preparat("khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen",
             "Хроническое венозное полнокровие печени («мускатная печень»)",
             "Кровообращение",
             ["khronicheskoe_venoznoe_polnokrovie_musкатная_peчен_1.jpeg",
              "khronicheskoe_venoznoe_polнокровие_musкатная_peчен_2.jpeg"]),

    Preparat("ostraya_zastoynaya_giperemiya_otek_legkikh",
             "Острая застойная гиперемия и отёк лёгких",
             "Кровообращение",
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

# словари
PREP_BY_ID: Dict[str, Preparat] = {p.id: p for p in PREPARATS}

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

# для случайных препаратов
RANDOM_CATEGORY_KEY = "__random__"

# состояние пользователя
user_state: Dict[int, Dict] = {}
user_stats: Dict[int, Dict] = {}
user_test_pool: Dict[int, List[str]] = {}


# ============================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================

def get_user_stats(user_id: int) -> Dict:
    if user_id not in user_stats:
        user_stats[user_id] = {
            "total": 0,
            "correct": 0,
            "wrong": 0,
            "errors": set(),
        }
    return user_stats[user_id]


def main_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📚 Обучение")
    kb.row("❓ Тест (варианты)", "⌨️ Тест (ввод)")
    kb.row("📊 Статистика", "🔁 Повторить ошибки")
    return kb


def training_nav_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("➡️ Следующий")
    kb.row("⬅️ Назад к разделам")
    kb.row("🏁 Выйти")
    return kb


def normalize(text: str) -> str:
    return text.lower().replace("ё", "е").strip()


# ==========================================================
# ОБУЧЕНИЕ
# ==========================================================

def start_training_for_user(user_id: int, category_key: str):
    """Создаёт новый список препаров и перемешивает."""
    if category_key == RANDOM_CATEGORY_KEY:
        ids = [p.id for p in PREPARATS]
    else:
        ids = [p.id for p in PREPARATS if p.category == category_key]

    random.shuffle(ids)

    user_state[user_id] = {
        "mode": "train",
        "train_category": category_key,
        "train_remaining": ids.copy(),
        "train_current_id": None,
    }

    return ids


def get_next_training_prep(user_id: int) -> Optional[Preparat]:
    st = user_state.get(user_id)
    if not st or st.get("mode") != "train":
        return None

    if not st["train_remaining"]:
        return None

    prep_id = st["train_remaining"].pop()
    st["train_current_id"] = prep_id

    return PREP_BY_ID[prep_id]


def send_preparat_training(chat_id: int, prep: Preparat, with_keyboard=True):
    kb = training_nav_keyboard() if with_keyboard else None
    bot.send_message(chat_id, f"<b>{prep.name}</b>", reply_markup=kb)

    for filename in prep.files:
        path = os.path.join("preparats", filename)
        if os.path.exists(path):
            with open(path, "rb") as photo:
                bot.send_photo(chat_id, photo)
        else:
            bot.send_message(chat_id, f"Файл отсутствует: {path}")


# ==========================================================
# РАЗДЕЛЫ ОБУЧЕНИЯ
# ==========================================================

@bot.message_handler(func=lambda m: m.text == "📚 Обучение")
def handle_training_menu(message):
    kb = types.InlineKeyboardMarkup()
    for cat in CATEGORIES_ORDERED:
        kb.add(types.InlineKeyboardButton(text=cat, callback_data=f"cat:{cat}"))
    kb.add(types.InlineKeyboardButton(text="Случайные препараты",
                                      callback_data=f"cat:{RANDOM_CATEGORY_KEY}"))
    bot.send_message(message.chat.id, "Выбери раздел:", reply_markup=kb)


@bot.callback_query_handler(func=lambda c: c.data.startswith("cat:"))
def handle_training_category(callback):
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id

    _, category_key = callback.data.split(":", 1)

    ids = start_training_for_user(user_id, category_key)

    if not ids:
        bot.answer_callback_query(callback.id, "Пусто")
        return

    prep = get_next_training_prep(user_id)
    bot.answer_callback_query(callback.id)
    send_preparat_training(chat_id, prep, with_keyboard=True)


@bot.message_handler(func=lambda m: m.text == "➡️ Следующий")
def handle_training_next(message):
    user_id = message.from_user.id

    prep = get_next_training_prep(user_id)
    if not prep:
        bot.send_message(message.chat.id, "Все препараты просмотрены 🎉", reply_markup=main_keyboard())
        return

    send_preparat_training(message.chat.id, prep, with_keyboard=True)


@bot.message_handler(func=lambda m: m.text == "⬅️ Назад к разделам")
def handle_training_back(message):
    user_state.pop(message.from_user.id, None)
    handle_training_menu(message)


@bot.message_handler(func=lambda m: m.text == "🏁 Выйти")
def handle_training_exit(message):
    user_state.pop(message.from_user.id, None)
    bot.send_message(message.chat.id, "Готово! Ты в меню.", reply_markup=main_keyboard())


# ==========================================================
# ТЕСТ (ВАРИАНТЫ)
# ==========================================================

def get_or_reset_mcq_pool(user_id: int):
    pool = user_test_pool.get(user_id)
    if not pool:
        pool = [p.id for p in PREPARATS]
        random.shuffle(pool)
        user_test_pool[user_id] = pool
    return pool


def build_options(correct: Preparat):
    others = [p for p in PREPARATS if p.id != correct.id]
    random.shuffle(others)
    opts = [correct] + others[:3]
    random.shuffle(opts)
    return opts


def send_mcq_question(chat_id, user_id, only_errors=False):
    stats = get_user_stats(user_id)

    if only_errors:
        if not stats["errors"]:
            bot.send_message(chat_id, "Нет ошибок 😊", reply_markup=main_keyboard())
            return
        prep_id = random.choice(list(stats["errors"]))
        prep = PREP_BY_ID[prep_id]
        from_errors = True
    else:
        pool = get_or_reset_mcq_pool(user_id)
        prep_id = pool.pop()
        user_test_pool[user_id] = pool
        prep = PREP_BY_ID[prep_id]
        from_errors = False

    user_state[user_id] = {
        "mode": "mcq",
        "correct_id": prep.id,
        "from_errors": from_errors,
    }

    photo_path = os.path.join("preparats", prep.files[0])
    kb = types.InlineKeyboardMarkup()
    for option in build_options(prep):
        kb.add(types.InlineKeyboardButton(text=option.name, callback_data=f"ans:{option.id}"))

    with open(photo_path, "rb") as photo:
        bot.send_photo(chat_id, photo, caption="Что за препарат?", reply_markup=kb)


@bot.message_handler(func=lambda m: m.text == "❓ Тест (варианты)")
def test_mcq(message):
    send_mcq_question(message.chat.id, message.from_user.id, only_errors=False)


@bot.message_handler(func=lambda m: m.text == "🔁 Повторить ошибки")
def test_errors(message):
    send_mcq_question(message.chat.id, message.from_user.id, only_errors=True)


@bot.callback_query_handler(func=lambda c: c.data.startswith("ans:"))
def handle_mcq_answer(callback):
    user_id = callback.from_user.id
    st = user_state.get(user_id)

    if not st or st["mode"] != "mcq":
        bot.answer_callback_query(callback.id, "Устарело")
        return

    chosen = callback.data.split(":", 1)[1]
    correct = st["correct_id"]

    stats = get_user_stats(user_id)
    stats["total"] += 1

    if chosen == correct:
        stats["correct"] += 1
        stats["errors"].discard(correct)
        bot.send_message(callback.message.chat.id, f"✅ Верно!\n<b>{PREP_BY_ID[correct].name}</b>")
    else:
        stats["wrong"] += 1
        stats["errors"].add(correct)
        bot.send_message(callback.message.chat.id,
                         f"❌ Неверно.\nПравильно: <b>{PREP_BY_ID[correct].name}</b>")

    bot.answer_callback_query(callback.id)
    send_mcq_question(callback.message.chat.id, user_id, only_errors=st["from_errors"])


# ==========================================================
# ТЕСТ (ВВОД)
# ==========================================================

def send_typing_question(chat_id, user_id, only_errors=False):
    stats = get_user_stats(user_id)

    if only_errors and not stats["errors"]:
        bot.send_message(chat_id, "Нет ошибок 😊", reply_markup=main_keyboard())
        return

    if only_errors:
        prep_id = random.choice(list(stats["errors"]))
        from_errors = True
    else:
        pool = get_or_reset_mcq_pool(user_id)
        prep_id = pool.pop()
        user_test_pool[user_id] = pool
        from_errors = False

    prep = PREP_BY_ID[prep_id]

    user_state[user_id] = {
        "mode": "typing",
        "correct_id": prep.id,
        "from_errors": from_errors,
    }

    photo_path = os.path.join("preparats", prep.files[0])
    with open(photo_path, "rb") as photo:
        bot.send_photo(chat_id, photo)

    bot.send_message(chat_id, "Напиши название препарата:")


@bot.message_handler(func=lambda m: m.text == "⌨️ Тест (ввод)")
def handle_typing_test(message):
    send_typing_question(message.chat.id, message.from_user.id, only_errors=False)


@bot.message_handler(
    func=lambda m: m.text not in [
        "📚 Обучение", "❓ Тест (варианты)", "⌨️ Тест (ввод)",
        "📊 Статистика", "🔁 Повторить ошибки",
        "➡️ Следующий", "⬅️ Назад к разделам", "🏁 Выйти"
    ]
)
def handle_typing_answer(message):
    user_id = message.from_user.id
    st = user_state.get(user_id)

    if not st or st["mode"] != "typing":
        return

    correct = PREP_BY_ID[st["correct_id"]]
    stats = get_user_stats(user_id)
    stats["total"] += 1

    user_text = normalize(message.text)
    correct_words = normalize(correct.name).split()

    if any(w for w in correct_words if len(w) > 4 and w in user_text):
        stats["correct"] += 1
        stats["errors"].discard(correct.id)
        bot.send_message(message.chat.id, f"✅ Верно! Это <b>{correct.name}</b>.")
    else:
        stats["wrong"] += 1
        stats["errors"].add(correct.id)
        bot.send_message(message.chat.id, f"❌ Неверно.\nПравильно: <b>{correct.name}</b>.")

    send_typing_question(message.chat.id, user_id, only_errors=st["from_errors"])


# ==========================================================
# СТАТИСТИКА
# ==========================================================

@bot.message_handler(func=lambda m: m.text == "📊 Статистика")
def handle_stats(message):
    st = get_user_stats(message.from_user.id)

    total = st["total"]
    correct = st["correct"]
    wrong = st["wrong"]
    acc = round(correct * 100 / total, 1) if total else 0

    bot.send_message(
        message.chat.id,
        f"<b>Статистика:</b>\n"
        f"Всего вопросов: <b>{total}</b>\n"
        f"Правильных: <b>{correct}</b>\n"
        f"Ошибок: <b>{wrong}</b>\n"
        f"Точность: <b>{acc}%</b>\n"
        f"В списке ошибок: <b>{len(st['errors'])}</b>",
        reply_markup=main_keyboard(),
    )


# ==========================================================
# СТАРТ
# ==========================================================

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот по микропрепаратам 😊",
        reply_markup=main_keyboard(),
    )


if __name__ == "__main__":
    print("Бот запущен 🎉")
    bot.infinity_polling()