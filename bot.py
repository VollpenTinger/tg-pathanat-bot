import os
import random
from dataclasses import dataclass
from typing import List, Dict

import telebot
from telebot import types

# =========================
# НАСТРОЙКИ БОТА
# =========================

# ТВОЙ ТОКЕН
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
        files=[
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
        files=[
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

# специальный ключ для "Случайных препаратов"
RANDOM_CATEGORY_KEY = "__random__"

# ========== СОСТОЯНИЯ И СТАТИСТИКА ==========

user_state: Dict[int, Dict] = {}     # {user_id: {...}}
user_stats: Dict[int, Dict] = {}     # {user_id: {"total": int, "correct": int, "wrong": int, "errors": set()}}
user_test_pool: Dict[int, List[str]] = {}  # для тестов без повторов


def get_user_stats(user_id: int) -> Dict:
    if user_id not in user_stats:
        user_stats[user_id] = {
            "total": 0,
            "correct": 0,
            "wrong": 0,
            "errors": set(),
        }
    return user_stats[user_id]


# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ КЛАВИАТУР ==========

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


def training_nav_keyboard() -> types.ReplyKeyboardMarkup:
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(types.KeyboardButton("➡️ Следующий"))
    kb.row(types.KeyboardButton("⬅️ Назад к разделам"))
    kb.row(types.KeyboardButton("🏠 Выйти в меню"))   # ← ДОБАВИТЬ ЭТУ СТРОКУ
    return kb


# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ЛОГИКИ ==========

def get_or_reset_test_pool(user_id: int) -> List[str]:
    pool = user_test_pool.get(user_id)
    if not pool:
        pool = [p.id for p in PREPARATS]
        random.shuffle(pool)
        user_test_pool[user_id] = pool
    return pool


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


def send_preparat_training(chat_id: int, prep: Preparat, with_keyboard: bool = False):
    if with_keyboard:
        bot.send_message(chat_id, f"<b>{prep.name}</b>", reply_markup=training_nav_keyboard())
    else:
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
        pool = get_or_reset_test_pool(user_id)
        if not pool:
            pool = [p.id for p in PREPARATS]
            random.shuffle(pool)
            user_test_pool[user_id] = pool
        prep_id = pool.pop()
        user_test_pool[user_id] = pool
        prep = PREP_BY_ID[prep_id]
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
        pool = get_or_reset_test_pool(user_id)
        if not pool:
            pool = [p.id for p in PREPARATS]
            random.shuffle(pool)
            user_test_pool[user_id] = pool
        prep_id = pool.pop()
        user_test_pool[user_id] = pool
        prep = PREP_BY_ID[prep_id]
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


def get_training_list_for_user(user_id: int, category_key: str) -> List[str]:
    """
    category_key:
      - одно из названий категорий
      - или RANDOM_CATEGORY_KEY для случайных из всех
    """
    if category_key == RANDOM_CATEGORY_KEY:
        ids = [p.id for p in PREPARATS]
    else:
        ids = [p.id for p in PREPARATS if p.category == category_key]
    random.shuffle(ids)
    # сохраним в user_state
    if user_id not in user_state:
        user_state[user_id] = {}
    user_state[user_id]["train_category"] = category_key
    user_state[user_id]["train_remaining"] = ids
    return ids


def pick_next_training_prep(user_id: int) -> Preparat | None:
    st = user_state.get(user_id)
    if not st or st.get("mode") != "train":
        return None

    category_key = st.get("train_category")
    remaining = st.get("train_remaining", [])

    if not remaining:
        remaining = get_training_list_for_user(user_id, category_key)

    if not remaining:
        return None

    prep_id = remaining.pop()
    st["train_remaining"] = remaining
    st["train_current_id"] = prep_id
    return PREP_BY_ID[prep_id]


# ========== ХЕНДЛЕРЫ ==========

@bot.message_handler(commands=["start"])
def cmd_start(message: types.Message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот для отработки микропрепаратов по патанатомии.\n\n"
        "Режимы:\n"
        "• <b>Обучение</b> – показываю препарат и его название (по разделам).\n"
        "• <b>Случайные препараты</b> – обучение на всех препаратах вперемешку.\n"
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
    # кнопка случайных препаратов
    kb.add(
        types.InlineKeyboardButton(
            text="Случайные препараты",
            callback_data=f"cat:{RANDOM_CATEGORY_KEY}",
        )
    )
    bot.send_message(
        message.chat.id,
        "Выбери раздел для обучения:",
        reply_markup=kb,
    )


@bot.callback_query_handler(func=lambda c: c.data.startswith("cat:"))
def handle_training_category(callback: types.CallbackQuery):
    _, category_key = callback.data.split(":", 1)
    user_id = callback.from_user.id
    chat_id = callback.message.chat.id

    ids = get_training_list_for_user(user_id, category_key)
    if not ids:
        bot.answer_callback_query(callback.id, "В этом разделе пока нет препаратов.")
        bot.send_message(chat_id, "В этом разделе пока нет препаратов.", reply_markup=main_keyboard())
        return

    user_state[user_id]["mode"] = "train"
    prep_id = user_state[user_id]["train_remaining"].pop()
    user_state[user_id]["train_current_id"] = prep_id

    cat_name = "Случайные препараты" if category_key == RANDOM_CATEGORY_KEY else category_key

    bot.answer_callback_query(callback.id, f"Раздел: {cat_name}")
    send_preparat_training(chat_id, PREP_BY_ID[prep_id], with_keyboard=True)


# ---------- ВЫХОД И ВОЗВРАТ ----------

@bot.message_handler(func=lambda m: m.text == "🔙 Назад к разделам")
def handle_training_back(message: types.Message):
    st = user_state.get(message.from_user.id)
    if st:
        st.pop("mode", None)
        st.pop("train_category", None)
        st.pop("train_remaining", None)
        st.pop("train_current_id", None)

    handle_training_menu(message)


@bot.message_handler(func=lambda m: m.text == "🏁 Выйти")
def handle_training_exit(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_state:
        user_state.pop(user_id)

    bot.send_message(
        message.chat.id,
        "Ты вышел из режима обучения 👌",
        reply_markup=main_keyboard()
    )


# ---------- ОБУЧЕНИЕ: НАВИГАЦИЯ ----------

@bot.message_handler(func=lambda m: m.text == "➡️ Следующий")
def handle_training_next(message: types.Message):
    user_id = message.from_user.id
    st = user_state.get(user_id)

    if not st or st.get("mode") != "train":
        bot.send_message(
            message.chat.id,
            "Сначала выбери раздел обучения через кнопку «📚 Обучение».",
            reply_markup=main_keyboard(),
        )
        return

    prep = pick_next_training_prep(user_id)
    if not prep:
        bot.send_message(
            message.chat.id,
            "В этом разделе закончились препараты 😊",
            reply_markup=main_keyboard(),
        )
        return

    send_preparat_training(message.chat.id, prep, with_keyboard=True)
