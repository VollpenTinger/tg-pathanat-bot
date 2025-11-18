import os
import random
from dataclasses import dataclass
from typing import List, Dict

import telebot
from telebot import types

# =========================
# НАСТРОЙКИ БОТА
# =========================

# ВСТАВЬ СЮДА СВОЙ ТОКЕН В КАВЫЧКАХ
BOT_TOKEN = "8245340349:AAF2sB8Gn5dXiqQQ1ldxAHqk_wpsdcLrH2c"

if BOT_TOKEN == "PASTE_YOUR_TOKEN_HERE":
    raise RuntimeError("Не забудь вставить настоящий токен бота в BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# =========================
# МОДЕЛЬ ДАННЫХ
# =========================

@dataclass
class Preparat:
    id: str           # внутренний id (короткий)
    name: str         # полное название по-русски
    category: str     # категория (для обучения)
    files: List[str]  # имена файлов из папки preparats/


# ---------- СПИСОК ПРЕПАРАТОВ ----------

PREPARATS: List[Preparat] = [
    # --- Амилоидозы ---
    Preparat(
        id="amiloidoz_pecheni",
        name="Амилоидоз печени",
        category="Амилоидозы",
        files=[
            "amiloidoz_pecheni_1.jpeg",
            "amiloidoz_pecheni_2.jpeg",
            "amiloidoz_pecheni_3.jpeg",
        ],
    ),
    Preparat(
        id="amiloidoz_pochki",
        name="Амилоидоз почки",
        category="Амилоидозы",
        files=[
            "amiloidoz_pochki_1.jpeg",
            "amiloidoz_pochki_2.jpeg",
        ],
    ),
    Preparat(
        id="amiloidoz_selezenki_sagovaya",
        name="Амилоидоз селезёнки («саговая» форма)",
        category="Амилоидозы",
        files=[
            "amiloidoz_selezenki_sagovaya_1.jpeg",
            "amiloidoz_selezenki_sagovaya_2.jpeg",
        ],
    ),
    Preparat(
        id="amiloidoz_selezenki_salnaya",
        name="Амилоидоз селезёнки («сальная» форма)",
        category="Амилоидозы",
        files=[
            "amiloidoz_selezenki_salnaya_1.jpeg",
            "amiloidoz_selezenki_salnaya_2.jpeg",
            "amiloidoz_selezenki_salnaya_3.jpeg",
        ],
    ),

    # --- Воспаление ---
    Preparat(
        id="serozno_gemorragicheskaya_pnevmoniya",
        name="Серозно-геморрагическая пневмония",
        category="Воспаление",
        files=[
            "serozno_gemorragicheskaya_pnevmoniya_1.jpeg",
            "serozno_gemorragicheskaya_pnevmoniya_2.jpeg",
            "serozno_gemorragicheskaya_pnevmoniya_3.jpeg",
        ],
    ),
    Preparat(
        id="seroznoe_vosp_legkikh",
        name="Серозное воспаление лёгких",
        category="Воспаление",
        files=[
            "seroznoe_vosp_legkikh_1.jpeg",
            "seroznoe_vosp_legkikh_2.jpeg",
            "seroznoe_vosp_legkikh_3.jpeg",
        ],
    ),
    Preparat(
        id="ostryi_seroznyi_gastrit",
        name="Острый серозный гастрит",
        category="Воспаление",
        files=[
            "ostryi_seroznyi_gastrit_1.jpeg",
            "ostryi_seroznyi_gastrit_2.jpeg",
            "ostryi_seroznyi_gastrit_3.jpeg",
            "ostryi_seroznyi_gastrit_4.jpeg",
        ],
    ),
    Preparat(
        id="krupoznaya_pnevmoniya",
        name="Крупозная пневмония",
        category="Воспаление",
        files=[
            "krupoznaya_pnevmoniya_1.jpeg",
            "krupoznaya_pnevmoniya_2.jpeg",
        ],
    ),
    Preparat(
        id="fibrinoznyi_perikardit",
        name="Фибринозный перикардит",
        category="Воспаление",
        files=[
            "fibrinoznyi_perikardit_1.jpeg",
            "fibrinoznyi_perikardit_2.jpeg",
            "fibrinoznyi_perikardit_3.jpeg",
        ],
    ),
    Preparat(
        id="difteriticheskii_enterit",
        name="Дифтеритический энтерит",
        category="Воспаление",
        files=[
            "difteriticheskii_enterit_1.jpeg",
            "difteriticheskii_enterit_2.jpeg",
        ],
    ),
    Preparat(
        id="gemorragicheskoe_vospalenie_kishechnika",
        name="Геморрагическое воспаление кишечника",
        category="Воспаление",
        files=[
            "gemorragicheskoe_vospalenie_kishechnika_1.jpeg",
            "gemorragicheskoe_vospalenie_kishechnika_2.jpeg",
            "gemorragicheskoe_vospalenie_kishechnika_3.jpeg",
        ],
    ),
    Preparat(
        id="gnoinyi_nefrit",
        name="Гнойный нефрит",
        category="Воспаление",
        files=[
            "gnoinyi_nefrit_1.jpeg",
            "gnoinyi_nefrit_2.jpeg",
            "gnoinyi_nefrit_3.jpeg",
            "gnoinyi_nefrit_4.jpeg",
        ],
    ),
    Preparat(
        id="khronicheskii_abscess_pecheni",
        name="Хронический абсцесс печени",
        category="Воспаление",
        files=[
            "khronicheskii_abscess_pecheni_1.jpeg",
        ],
    ),
    Preparat(
        id="khronicheskii_kataralnyi_enterit_ge",
        name="Хронический катаральный энтерит (гематоксилин-эозин)",
        category="Воспаление",
        files=[
            "khronicheskii_kataralnyi_enterit_ge_1.jpeg",
            "khronicheskii_kataralnyi_enterit_ge_2.jpeg",
            "khronicheskii_kataralnyi_enterit_ge_3.jpeg",
            "khronicheskii_kataralnyi_enterit_ge_4.jpeg",
        ],
    ),
    Preparat(
        id="khronicheskii_kataralnyi_enterit_sudan",
        name="Хронический катаральный энтерит (Судан III)",
        category="Воспаление",
        files=[
            "khronicheskii_kataralnyi_enterit_sudan_1.jpeg",
            "khronicheskii_kataralnyi_enterit_sudan_2.jpeg",
            "khronicheskii_kataralnyi_enterit_sudan_3.jpeg",
        ],
    ),

    # --- Дистрофии ---
    Preparat(
        id="zernistaya_distrofiya_pochki",
        name="Зернистая дистрофия почки",
        category="Дистрофии",
        files=[
            "zernistaya_distrofiya_pochki_1.jpeg",
            "zernistaya_distrofiya_pochki_2.jpeg",
        ],
    ),
    Preparat(
        id="zernistaya_distrofiya_pecheni",
        name="Зернистая дистрофия печени",
        category="Дистрофии",
        files=[
            "zernistaya_distrofiya_pecheni_1.jpeg",
            "zernistaya_distrofiya_pecheni_2.jpeg",
        ],
    ),
    Preparat(
        id="gialinovo_kapelnaya_distrofiya_pochki",
        name="Гиалиново-капельная дистрофия почки",
        category="Дистрофии",
        files=[
            "gialinovo_kapelnaya_distrofiya_pochki_1.jpeg",
            "gialinovo_kapelnaya_distrofiya_pochki_2.jpeg",
            "gialinovo_kapelnaya_distrofiya_pochki_3.jpeg",
        ],
    ),
    Preparat(
        id="vakuolnaya_distrofiya_pochki",
        name="Вакуольная дистрофия почки",
        category="Дистрофии",
        files=[
            "vakuolnaya_distrofiya_pochki_1.jpeg",
        ],
    ),
    Preparat(
        id="kolloidnaya_distrofiya_shchitovidnoi",
        name="Коллоидная дистрофия щитовидной железы",
        category="Дистрофии",
        files=[
            "kolloidnaya_distrofiya_shchitovidnoi_1.jpeg",
            "kolloidnaya_distrofiya_shchitovidnoi_2.jpeg",
        ],
    ),
    Preparat(
        id="zhirovaia_distrofiya_pecheni",
        name="Жировая дистрофия печени",
        category="Дистрофии",
        files=[
            "zhirovaia_distrofiya_pecheni_1.jpeg",
            "zhirovaia_distrofiya_pecheni_2.jpeg",
        ],
    ),

    # --- Гиалиноз ---
    Preparat(
        id="gialinoz_stenki_sosuda_matki",
        name="Гиалиноз стенки сосуда матки",
        category="Гиалинозы",
        files=[
            "gialinoz_stenki_sosuda_matki_1.jpeg",
            "gialinoz_stenki_sosuda_matki_2.jpeg",
            "gialinoz_stenki_sosuda_matki_3.jpeg",
        ],
    ),
    Preparat(
        id="gialinoz_selezenki",
        name="Гиалиноз селезёнки",
        category="Гиалинозы",
        files=[
            "gialinoz_selezenki_1.jpeg",
            "gialinoz_selezenki_2.jpeg",
            "gialinoz_selezenki_3.jpeg",
        ],
    ),

    # --- Пигменты (включая антракоз) ---
    Preparat(
        id="hemosideroz_pecheni",
        name="Гемосидероз печени",
        category="Пигменты",
        files=[
            "hemosideroz_pecheni_1.jpeg",
            "hemosideroz_pecheni_2.jpeg",
        ],
    ),
    Preparat(
        id="hemosideroz_pecheni_muskatnaya",
        name="Гемосидероз печени («мускатная печень»)",
        category="Пигменты",
        files=[
            "hemosideroz_pecheni_muskatnaya_1.jpeg",
            "hemosideroz_pecheni_muskatnaya_2.jpeg",
            "hemosideroz_pecheni_muskatnaya_3.jpeg",
        ],
    ),
    Preparat(
        id="hemosideroz_selezenki_ge",
        name="Гемосидероз селезёнки (гематоксилин-эозин)",
        category="Пигменты",
        files=[
            "hemosideroz_selezenki_ge_1.jpeg",
            "hemosideroz_selezenki_ge_2.jpeg",
            "hemosideroz_selezenki_ge_3.jpeg",
            "hemosideroz_selezenki_ge_4.jpeg",
        ],
    ),
    Preparat(
        id="hemosideroz_selezenki_perls",
        name="Гемосидероз селезёнки (реакция Перлса)",
        category="Пигменты",
        files=[
            "hemosideroz_selezenki_perls_1.jpeg",
            "hemosideroz_selezenki_perls_2.jpeg",
            "hemosideroz_selezenki_perls_3.jpeg",
            "hemosideroz_selezenki_perls_4.jpeg",
        ],
    ),
    Preparat(
        id="melanoz_pecheni",
        name="Меланоз печени",
        category="Пигменты",
        files=[
            "melanoz_pecheni_1.jpeg",
            "melanoz_pecheni_2.jpeg",
            "melanoz_pecheni_3.jpeg",
        ],
    ),
    Preparat(
        id="antrakoz_legkikh",
        name="Антракоз лёгких",
        category="Пигменты",
        files=[
            "antrakoz_legkikh_1.jpeg",
            "antrakoz_legkikh_2.jpeg",
            "antrakoz_legkikh_3.jpeg",
        ],
    ),

    # --- Некрозы ---
    Preparat(
        id="nekroticheskii_nefroz",
        name="Некротический нефроз",
        category="Некроз",
        files=[
            "nekroticheskii_nefroz_1.jpeg",
            "nekroticheskii_nefroz_2.jpeg",
            "nekroticheskii_nefroz_3.jpeg",
        ],
    ),
    Preparat(
        id="tvorozhistyi_nekroz_lymph_tb",
        name="Творожистый (казеозный) некроз лимфатического узла при туберкулёзе",
        category="Некроз",
        files=[
            "tvorozhistyi_nekroz_lymph_tb_1.jpeg",
            "tvorozhistyi_nekroz_lymph_tb_2.jpeg",
        ],
    ),
    Preparat(
        id="tsenkerovskii_voskovidnyi_nekroz_myshc",
        name="Ценкеровский (восковидный) некроз скелетной мускулатуры",
        category="Некроз",
        files=[
            "tsenkerovskii_voskovidnyi_nekroz_myshc_1.jpeg",
            "tsenkerovskii_voskovidnyi_nekroz_myshc_2.jpeg",
        ],
    ),
    Preparat(
        id="tvorozhistyi_nekroz_legkikh_tb",
        name="Творожистый некроз в лёгких при туберкулёзе",
        category="Некроз",
        files=[
            "tvorozhistyi_nekroz_legkikh_tb_1.jpeg",
            "tvorozhistyi_nekroz_legkikh_tb_2.jpeg",
        ],
    ),

    # --- Кровообращение ---
    Preparat(
        id="buraya_induratsiya_pecheni",
        name="Бурая индурация печени",
        category="Кровообращение",
        files=[
            "buraya_induratsiya_pecheni_1.jpeg",
            "buraya_induratsiya_pecheni_2.jpeg",
        ],
    ),
    Preparat(
        id="ostraya_zastoynaya_venoznaya_giperemiya_pecheni",
        name="Острая застойная венозная гиперемия печени",
        category="Кровообращение",
        files=[
            "ostraya_zastoynaya_venoznaya_giperemiya_pecheni_1.jpeg",
            "ostraya_zastoynaya_venoznaya_giperemiya_pecheni_2.jpeg",
        ],
    ),
    Preparat(
        id="khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen",
        name="Хроническое венозное полнокровие печени («мускатная печень»)",
        category="Кровообращение",
        files=[
            "khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen_1.jpeg",
            "khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen_2.jpeg",
        ],
    ),
    Preparat(
        id="ostraya_zastoynaya_giperemiya_otek_legkikh",
        name="Острая застойная гиперемия и отёк лёгких",
        category="Кровообращение",
        files[
            "ostraya_zastoynaya_giperemiya_otek_legkikh_1.jpeg",
            "ostraya_zastoynaya_giperemiya_otek_legkikh_2.jpeg",
        ],
    ),
    Preparat(
        id="buraya_induratsiya_legkogo",
        name="Бурая индурация лёгкого",
        category="Кровообращение",
        files=[
            "buraya_induratsiya_legkogo_1.jpeg",
            "buraya_induratsiya_legkogo_2.jpeg",
        ],
    ),

    # --- Инфаркты ---
    Preparat(
        id="ishemicheskii_infarkt_pochki",
        name="Ишемический инфаркт почки",
        category="Инфаркты",
        files=[
            "ishemicheskii_infarkt_pochki_1.jpeg",
            "ishemicheskii_infarkt_pochki_2.jpeg",
        ],
    ),
    Preparat(
        id="ishemicheskii_infarkt_selezenki",
        name="Ишемический инфаркт селезёнки",
        category="Инфаркты",
        files=[
            "ishemicheskii_infarkt_selezenki_1.jpeg",
            "ishemicheskii_infarkt_selezenki_2.jpeg",
        ],
    ),
    Preparat(
        id="gemorragicheskii_infarkt_pochki",
        name="Геморрагический инфаркт почки",
        category="Инфаркты",
        files=[
            "gemorragicheskii_infarkt_pochki_1.jpeg",
            "gemorragicheskii_infarkt_pochki_2.jpeg",
            "gemorragicheskii_infarkt_pochki_3.jpeg",
        ],
    ),
    Preparat(
        id="gemorragicheskii_infarkt_legkogo",
        name="Геморрагический инфаркт лёгкого",
        category="Инфаркты",
        files[
            "gemorragicheskii_infarkt_legkogo_1.jpeg",
            "gemorragicheskii_infarkt_legkogo_2.jpeg",
        ],
    ),

    # --- Тромбоз ---
    Preparat(
        id="smeshannyi_tromb",
        name="Смешанный тромб",
        category="Тромбоз",
        files=[
            "smeshannyi_tromb_1.jpeg",
            "smeshannyi_tromb_2.jpeg",
        ],
    ),
]

# Быстрый доступ
PREP_BY_ID: Dict[str, Preparat] = {p.id: p for p in PREPARATS}

# Список категорий в удобном порядке
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

# ========== СОСТОЯНИЯ И СТАТИСТИКА ==========

user_state: Dict[int, Dict] = {}     # {user_id: {"mode": "...", "correct_id": "...", "from_errors": bool}}
user_stats: Dict[int, Dict] = {}     # {user_id: {"total": int, "correct": int, "wrong": int, "errors": set()}}


def get_user_stats(user_id: int) -> Dict:
    if user_id not in user_stats:
        user_stats[user_id] = {
            "total": 0,
            "correct": 0,
            "wrong": 0,
            "errors": set(),
        }
    return user_stats[user_id]


# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==========

def main_keyboard() -> types.ReplyKeyboardMarkup:
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(types.KeyboardButton("📚 Обучение"))
    kb.row(
        types.KeyboardButton("❓ Тест (варианты)"),
        types.KeyboardButton("⌨️ Тест (ввод)"),
    )
    kb.row(
        types.KeyboardButton("📊 Статистика"),
        types.KeyboardButton("🔁 Повторить ошибки"),
    )
    return kb


def get_random_preparat() -> Preparat:
    return random.choice(PREPARATS)


def get_random_preparat_from_category(category: str) -> Preparat:
    candidates = [p for p in PREPARATS if p.category == category]
    return random.choice(candidates)


def get_random_preparat_from_errors(user_id: int):
    stats = get_user_stats(user_id)
    ids = list(stats["errors"])
    if not ids:
        return None
    prep_ids = [pid for pid in ids if pid in PREP_BY_ID]
    if not prep_ids:
        return None
    return PREP_BY_ID[random.choice(prep_ids)]


def build_options(correct: Preparat, count: int = 4) -> List[Preparat]:
    others = [p for p in PREPARATS if p.id != correct.id]
    random.shuffle(others)
    options = [correct] + others[: count - 1]
    random.shuffle(options)
    return options


def send_preparat_training(chat_id: int, prep: Preparat):
    bot.send_message(chat_id, f"<b>{prep.name}</b>")
    for filename in prep.files:
        photo_path = os.path.join("preparats", filename)
        if not os.path.exists(photo_path):
            bot.send_message(chat_id, f"Файл не найден: {photo_path}")
            continue
        with open(photo_path, "rb") as photo:
            bot.send_photo(chat_id, photo)


def send_mcq_question(chat_id: int, user_id: int, only_errors: bool = False):
    if only_errors:
        prep = get_random_preparat_from_errors(user_id)
        if prep is None:
            bot.send_message(chat_id, "Пока нет ошибок для повторения 😊", reply_markup=main_keyboard())
            return
        from_errors = True
    else:
        prep = get_random_preparat()
        from_errors = False

    options = build_options(prep)

    user_state[user_id] = {
        "mode": "mcq",
        "correct_id": prep.id,
        "from_errors": from_errors,
    }

    photo_path = os.path.join("preparats", prep.files[0])
    if not os.path.exists(photo_path):
        bot.send_message(chat_id, f"Файл не найден: {photo_path}")
    else:
        with open(photo_path, "rb") as photo:
            kb = types.InlineKeyboardMarkup()
            for p in options:
                kb.add(
                    types.InlineKeyboardButton(
                        text=p.name,
                        callback_data=f"ans:{p.id}",
                    )
                )
            bot.send_photo(
                chat_id,
                photo,
                caption="Что за препарат?",
                reply_markup=kb,
            )


def send_typing_question(chat_id: int, user_id: int, only_errors: bool = False):
    if only_errors:
        prep = get_random_preparat_from_errors(user_id)
        if prep is None:
            bot.send_message(chat_id, "Пока нет ошибок для повторения 😊", reply_markup=main_keyboard())
            return
        from_errors = True
    else:
        prep = get_random_preparat()
        from_errors = False

    user_state[user_id] = {
        "mode": "typing",
        "correct_id": prep.id,
        "from_errors": from_errors,
    }

    photo_path = os.path.join("preparats", prep.files[0])
    if not os.path.exists(photo_path):
        bot.send_message(chat_id, f"Файл не найден: {photo_path}")
    else:
        with open(photo_path, "rb") as photo:
            bot.send_photo(chat_id, photo)

    bot.send_message(
        chat_id,
        "Напиши название препарата (можно не слово в слово, главное – смысл).",
    )


def normalize(text: str) -> str:
    return text.lower().replace("ё", "е").strip()


# ========== ХЕНДЛЕРЫ ==========

@bot.message_handler(commands=["start"])
def cmd_start(message: types.Message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот для отработки микропрепаратов по патанатомии.\n\n"
        "Режимы:\n"
        "• <b>Обучение</b> – показываю препарат и его название (по разделам).\n"
        "• <b>Тест (варианты)</b> – выбираешь правильный ответ из списка.\n"
        "• <b>Тест (ввод)</b> – сам вписываешь ответ.\n"
        "• <b>Статистика</b> – твои результаты.\n"
        "• <b>Повторить ошибки</b> – тренировка по сложным препаратам.\n",
        reply_markup=main_keyboard(),
    )


# ---------- ОБУЧЕНИЕ: ВЫБОР РАЗДЕЛА ----------

@bot.message_handler(func=lambda m: m.text == "📚 Обучение")
def handle_training_menu(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    for cat in CATEGORIES_ORDERED:
        kb.add(
            types.InlineKeyboardButton(
                text=cat,
                callback_data=f"cat:{cat}",
            )
        )
    bot.send_message(
        message.chat.id,
        "Выбери раздел для обучения:",
        reply_markup=kb,
    )


@bot.callback_query_handler(func=lambda c: c.data.startswith("cat:"))
def handle_training_category(callback: types.CallbackQuery):
    _, category = callback.data.split(":", 1)
    # category — это строка, как в CATEGORIES_ORDERED и в Preparat.category
    prep = get_random_preparat_from_category(category)
    bot.answer_callback_query(callback.id, f"Раздел: {category}")
    send_preparat_training(callback.message.chat.id, prep)


# ---------- ТЕСТ (ВАРИАНТЫ) ----------

@bot.message_handler(func=lambda m: m.text == "❓ Тест (варианты)")
def handle_test_mcq(message: types.Message):
    send_mcq_question(message.chat.id, message.from_user.id, only_errors=False)


@bot.message_handler(func=lambda m: m.text == "🔁 Повторить ошибки")
def handle_test_mcq_errors(message: types.Message):
    send_mcq_question(message.chat.id, message.from_user.id, only_errors=True)


@bot.callback_query_handler(func=lambda c: c.data.startswith("ans:"))
def handle_answer(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    data = user_state.get(user_id)

    if not data or data.get("mode") != "mcq":
        bot.answer_callback_query(callback.id, "Этот вопрос уже устарел. Нажми «Тест (варианты)».", show_alert=True)
        return

    chosen_id = callback.data.split(":", 1)[1]
    correct_id = data["correct_id"]
    from_errors = data.get("from_errors", False)
    correct_prep = PREP_BY_ID[correct_id]

    stats = get_user_stats(user_id)
    stats["total"] += 1

    if chosen_id == correct_id:
        stats["correct"] += 1
        # можно убрать из списка ошибок, если один раз ответили верно
        if correct_id in stats["errors"]:
            stats["errors"].remove(correct_id)
        text = f"✅ Верно! Это <b>{correct_prep.name}</b>."
    else:
        stats["wrong"] += 1
        stats["errors"].add(correct_id)
        chosen_prep = PREP_BY_ID.get(chosen_id)
        chosen_name = chosen_prep.name if chosen_prep else "—"
        text = (
            f"❌ Неверно.\n"
            f"Ты выбрал: <b>{chosen_name}</b>\n"
            f"Правильный ответ: <b>{correct_prep.name}</b>."
        )

    bot.send_message(callback.message.chat.id, text)
    bot.answer_callback_query(callback.id)

    # новый вопрос — либо снова из ошибок, либо обычный
    send_mcq_question(callback.message.chat.id, user_id, only_errors=from_errors)


# ---------- ТЕСТ (ВВОД) ----------

@bot.message_handler(func=lambda m: m.text == "⌨️ Тест (ввод)")
def handle_test_typing(message: types.Message):
    send_typing_question(message.chat.id, message.from_user.id, only_errors=False)


@bot.message_handler(func=lambda m: m.text and m.text not in ["📚 Обучение", "❓ Тест (варианты)", "⌨️ Тест (ввод)", "📊 Статистика", "🔁 Повторить ошибки"])
def handle_typing_answer(message: types.Message):
    user_id = message.from_user.id
    data = user_state.get(user_id)

    # если пользователь сейчас не в режиме "ввод", игнорируем (чтобы не ловить любое сообщение)
    if not data or data.get("mode") != "typing":
        return

    correct_prep = PREP_BY_ID[data["correct_id"]]
    from_errors = data.get("from_errors", False)

    user_text = normalize(message.text)
    correct_name_norm = normalize(correct_prep.name)

    stats = get_user_stats(user_id)
    stats["total"] += 1

    # очень простая проверка: хотя бы одно "значимое" слово содержится в ответе
    words = [w for w in correct_name_norm.split() if len(w) > 3]
    if any(w in user_text for w in words):
        stats["correct"] += 1
        if correct_prep.id in stats["errors"]:
            stats["errors"].remove(correct_prep.id)
        text = f"✅ Верно! Это <b>{correct_prep.name}</b>."
    else:
        stats["wrong"] += 1
        stats["errors"].add(correct_prep.id)
        text = (
            f"❌ Не совсем.\n"
            f"Правильный ответ: <b>{correct_prep.name}</b>."
        )

    bot.send_message(message.chat.id, text)
    # сразу новый вопрос (из ошибок или общий)
    send_typing_question(message.chat.id, user_id, only_errors=from_errors)


# ---------- СТАТИСТИКА ----------

@bot.message_handler(func=lambda m: m.text == "📊 Статистика")
def handle_stats(message: types.Message):
    stats = get_user_stats(message.from_user.id)
    total = stats["total"]
    correct = stats["correct"]
    wrong = stats["wrong"]
    if total > 0:
        acc = round(correct * 100 / total, 1)
    else:
        acc = 0.0

    errors_count = len(stats["errors"])

    text = (
        "<b>Твоя статистика:</b>\n"
        f"• Всего вопросов: <b>{total}</b>\n"
        f"• Правильных ответов: <b>{correct}</b>\n"
        f"• Неправильных ответов: <b>{wrong}</b>\n"
        f"• Точность: <b>{acc}%</b>\n"
        f"• Препаратов в списке ошибок: <b>{errors_count}</b>\n"
        "\nСовет: используй режим «🔁 Повторить ошибки», чтобы добить сложные препараты 😊"
    )
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())


# ========== ЗАПУСК ==========

if __name__ == "__main__":
    print("Бот запущен (polling)...")
    bot.infinity_polling()
