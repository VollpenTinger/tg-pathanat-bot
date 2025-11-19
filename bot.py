import os
import random
from dataclasses import dataclass
from typing import List, Dict, Optional

import telebot
from telebot import types

# =========================
# НАСТРОЙКИ БОТА
# =========================

# Можешь оставить этот токен или вставить свой
BOT_TOKEN = "8245340349:AAF2sB8Gn5dXiqQQ1ldxAHqk_wpsdcLrH2c"

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# =========================
# ДАННЫЕ О ПРЕПАРАТАХ
# =========================

@dataclass
class Preparat:
    id: str           # внутренний id
    name: str         # название
    category: str     # раздел
    files: List[str]  # файлы в папке preparats/


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

    # --- Гиалинозы ---
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

    # --- Пигменты ---
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

    # --- Некроз ---
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

# специальная "категория" для случайных в обучении
RANDOM_CATEGORY_KEY = "__random__"

# =========================
# СОСТОЯНИЕ ПОЛЬЗОВАТЕЛЕЙ
# =========================

user_state: Dict[int, Dict] = {}
user_stats: Dict[int, Dict] = {}
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


# =========================
# КЛАВИАТУРЫ
# =========================

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
    kb.row(types.KeyboardButton("🔙 Назад к разделам"))
    kb.row(types.KeyboardButton("🏁 Выйти"))
    return kb


def test_nav_keyboard() -> types.ReplyKeyboardMarkup:
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(types.KeyboardButton("Ещё вопрос"), types.KeyboardButton("Закончить тест"))
    return kb


# =========================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# =========================

def normalize(text: str) -> str:
    return text.lower().replace("ё", "е").strip()


def get_or_reset_test_pool(user_id: int) -> List[str]:
    pool = user_test_pool.get(user_id)
    if not pool:
        pool = [p.id for p in PREPARATS]
        random.shuffle(pool)
        user_test_pool[user_id] = pool
    return pool


def get_random_preparat_from_errors(user_id: int) -> Optional[Preparat]:
    stats = get_user_stats(user_id)
    ids = list(stats["errors"])
    if not ids:
        return None
    ids = [pid for pid in ids if pid in PREP_BY_ID]
    if not ids:
        return None
    return PREP_BY_ID[random.choice(ids)]


def build_options(correct: Preparat, count: int = 4) -> List[Preparat]:
    others = [p for p in PREPARATS if p.id != correct.id]
    random.shuffle(others)
    options = [correct] + others[: count - 1]
    random.shuffle(options)
    return options


# ---------- ОБУЧЕНИЕ: ЛОГИКА ----------

def start_training_for_user(user_id: int, category_key: str) -> List[str]:
    """
    Подготавливаем список препаратов в случайном порядке.
    category_key:
      - одно из названий категорий
      - или RANDOM_CATEGORY_KEY для случайных из всех
    """
    if category_key == RANDOM_CATEGORY_KEY:
        ids = [p.id for p in PREPARATS]
    else:
        ids = [p.id for p in PREPARATS if p.category == category_key]

    random.shuffle(ids)

    st = user_state.setdefault(user_id, {})
    st["mode"] = "train"
    st["train_category"] = category_key
    st["train_order"] = ids
    st["train_index"] = 0

    return ids


def get_current_training_prep(user_id: int) -> Optional[Preparat]:
    st = user_state.get(user_id)
    if not st or st.get("mode") != "train":
        return None
    order = st.get("train_order", [])
    idx = st.get("train_index", 0)
    if idx >= len(order):
        return None
    return PREP_BY_ID[order[idx]]


def go_next_training_prep(user_id: int) -> Optional[Preparat]:
    st = user_state.get(user_id)
    if not st or st.get("mode") != "train":
        return None
    st["train_index"] = st.get("train_index", 0) + 1
    return get_current_training_prep(user_id)


def send_preparat_training(chat_id: int, prep: Preparat, with_keyboard: bool = False):
    """
    Сначала текст, потом все фотки (как ты просила).
    """
    kb = training_nav_keyboard() if with_keyboard else None

    # текст отдельным сообщением, без подписи к фото
    bot.send_message(chat_id, f"<b>{prep.name}</b>", reply_markup=kb)

    for filename in prep.files:
        path = os.path.join("preparats", filename)
        if not os.path.exists(path):
            bot.send_message(chat_id, f"Файл не найден: {path}")
            continue
        with open(path, "rb") as photo:
            bot.send_photo(chat_id, photo)


# ---------- ТЕСТЫ: ВОПРОСЫ ----------

def send_mcq_question(chat_id: int, user_id: int, only_errors: bool = False):
    if only_errors:
        prep = get_random_preparat_from_errors(user_id)
        if prep is None:
            bot.send_message(chat_id, "Ошибок пока нет — вообще красота 🤩", reply_markup=main_keyboard())
            return
        from_errors = True
    else:
        pool = get_or_reset_test_pool(user_id)
        if not pool:
            # все показали — перетасуем заново
            pool = [p.id for p in PREPARATS]
            random.shuffle(pool)
            user_test_pool[user_id] = pool
        prep_id = pool.pop()
        user_test_pool[user_id] = pool
        prep = PREP_BY_ID[prep_id]
        from_errors = False

    # сохраняем состояние
    st = user_state.setdefault(user_id, {})
    st["mode"] = "mcq"
    st["correct_id"] = prep.id
    st["from_errors"] = from_errors

    photo_path = os.path.join("preparats", prep.files[0])
    if not os.path.exists(photo_path):
        bot.send_message(chat_id, f"Файл не найден: {photo_path}")
        return

    options = build_options(prep)
    kb = types.InlineKeyboardMarkup()
    for p in options:
        kb.add(types.InlineKeyboardButton(text=p.name, callback_data=f"ans:{p.id}"))

    # сам вопрос
    with open(photo_path, "rb") as photo:
        bot.send_photo(
            chat_id,
            photo,
            caption="Что это за препарат?",
            reply_markup=kb,
        )


def send_typing_question(chat_id: int, user_id: int, only_errors: bool = False):
    if only_errors:
        prep = get_random_preparat_from_errors(user_id)
        if prep is None:
            bot.send_message(chat_id, "Ошибок пока нет — вообще красота 🤩", reply_markup=main_keyboard())
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

    st = user_state.setdefault(user_id, {})
    st["mode"] = "typing"
    st["correct_id"] = prep.id
    st["from_errors"] = from_errors

    photo_path = os.path.join("preparats", prep.files[0])
    if os.path.exists(photo_path):
        with open(photo_path, "rb") as photo:
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, f"Файл не найден: {photo_path}")

    bot.send_message(
        chat_id,
        "Напиши название препарата (можно не слово в слово, главное — смысл).",
    )


# =========================
# ХЕНДЛЕРЫ
# =========================

@bot.message_handler(commands=["start"])
def cmd_start(message: types.Message):
    bot.send_message(
        message.chat.id,
        "Ну что же, поучим препараты 🤓😜",
        reply_markup=main_keyboard(),
    )


# ---------- ОБУЧЕНИЕ: МЕНЮ ----------

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

    # отдельная кнопка для случайных препаратов (внутри обучения)
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

    ids = start_training_for_user(user_id, category_key)
    if not ids:
        bot.answer_callback_query(callback.id, "В этом разделе нет препаратов.")
        bot.send_message(chat_id, "В этом разделе нет препаратов.", reply_markup=main_keyboard())
        return

    cat_name = "Случайные препараты" if category_key == RANDOM_CATEGORY_KEY else category_key
    bot.answer_callback_query(callback.id, f"Раздел: {cat_name}")

    prep = get_current_training_prep(user_id)
    if prep:
        send_preparat_training(chat_id, prep, with_keyboard=True)
    else:
        bot.send_message(chat_id, "Что-то пошло не так с обучением 😅", reply_markup=main_keyboard())


@bot.message_handler(func=lambda m: m.text == "➡️ Следующий")
def handle_training_next(message: types.Message):
    user_id = message.from_user.id
    st = user_state.get(user_id)

    if not st or st.get("mode") != "train":
        bot.send_message(
            message.chat.id,
            "Сначала выбери раздел через «📚 Обучение».",
            reply_markup=main_keyboard(),
        )
        return

    prep = go_next_training_prep(user_id)
    if not prep:
        bot.send_message(
            message.chat.id,
            "Все препараты в этом разделе уже просмотрены 🎉",
            reply_markup=main_keyboard(),
        )
        # чистим режим
        st["mode"] = None
        st.pop("train_category", None)
        st.pop("train_order", None)
        st.pop("train_index", None)
        return

    send_preparat_training(message.chat.id, prep, with_keyboard=True)


@bot.message_handler(func=lambda m: m.text == "🔙 Назад к разделам")
def handle_training_back_to_categories(message: types.Message):
    user_id = message.from_user.id
    st = user_state.get(user_id)
    if st:
        st.pop("mode", None)
        st.pop("train_category", None)
        st.pop("train_order", None)
        st.pop("train_index", None)

    handle_training_menu(message)


@bot.message_handler(func=lambda m: m.text == "🏁 Выйти")
def handle_training_exit(message: types.Message):
    user_id = message.from_user.id
    st = user_state.get(user_id)
    if st:
        st.pop("mode", None)
        st.pop("train_category", None)
        st.pop("train_order", None)
        st.pop("train_index", None)

    bot.send_message(
        message.chat.id,
        "Ты вышел из режима обучения 👌",
        reply_markup=main_keyboard(),
    )


# ---------- ТЕСТЫ: ЗАПУСК ----------

@bot.message_handler(func=lambda m: m.text == "❓ Тест (варианты)")
def handle_test_mcq_start(message: types.Message):
    user_id = message.from_user.id
    st = user_state.setdefault(user_id, {})
    st["mode"] = "mcq"
    st["from_errors"] = False

    bot.send_message(
        message.chat.id,
        "Режим теста с вариантами.\nЖми «Ещё вопрос», чтобы получить задание.",
        reply_markup=test_nav_keyboard(),
    )
    # сразу первый вопрос
    send_mcq_question(message.chat.id, user_id, only_errors=False)


@bot.message_handler(func=lambda m: m.text == "⌨️ Тест (ввод)")
def handle_test_typing_start(message: types.Message):
    user_id = message.from_user.id
    st = user_state.setdefault(user_id, {})
    st["mode"] = "typing"
    st["from_errors"] = False

    bot.send_message(
        message.chat.id,
        "Режим теста с вводом ответа.\nЖми «Ещё вопрос», чтобы получать задания.",
        reply_markup=test_nav_keyboard(),
    )
    send_typing_question(message.chat.id, user_id, only_errors=False)


@bot.message_handler(func=lambda m: m.text == "🔁 Повторить ошибки")
def handle_test_errors_start(message: types.Message):
    user_id = message.from_user.id
    st = user_state.setdefault(user_id, {})
    st["mode"] = "mcq"
    st["from_errors"] = True

    bot.send_message(
        message.chat.id,
        "Режим: повторяем ошибки.\nЖми «Ещё вопрос».",
        reply_markup=test_nav_keyboard(),
    )
    send_mcq_question(message.chat.id, user_id, only_errors=True)


@bot.message_handler(func=lambda m: m.text == "Ещё вопрос")
def handle_test_next(message: types.Message):
    user_id = message.from_user.id
    st = user_state.get(user_id)

    if not st or st.get("mode") not in ("mcq", "typing"):
        bot.send_message(
            message.chat.id,
            "Сначала выбери режим теста.",
            reply_markup=main_keyboard(),
        )
        return

    mode = st["mode"]
    from_errors = st.get("from_errors", False)

    if mode == "mcq":
        send_mcq_question(message.chat.id, user_id, only_errors=from_errors)
    elif mode == "typing":
        send_typing_question(message.chat.id, user_id, only_errors=from_errors)


@bot.message_handler(func=lambda m: m.text == "Закончить тест")
def handle_test_finish(message: types.Message):
    user_id = message.from_user.id
    st = user_state.get(user_id)
    if st:
        st.pop("mode", None)
        st.pop("correct_id", None)
        st.pop("from_errors", None)

    bot.send_message(
        message.chat.id,
        "Тест закончен. Возвращаемся в меню 👌",
        reply_markup=main_keyboard(),
    )


# ---------- ТЕСТ (варианты): проверка ответа ----------

@bot.callback_query_handler(func=lambda c: c.data.startswith("ans:"))
def handle_answer(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    data = user_state.get(user_id)

    if not data or data.get("mode") != "mcq":
        bot.answer_callback_query(callback.id, "Этот вопрос уже не актуален. Нажми «Ещё вопрос».", show_alert=True)
        return

    chosen_id = callback.data.split(":", 1)[1]
    correct_id = data["correct_id"]
    from_errors = data.get("from_errors", False)
    correct_prep = PREP_BY_ID[correct_id]

    stats = get_user_stats(user_id)
    stats["total"] += 1

    if chosen_id == correct_id:
        stats["correct"] += 1
        stats["errors"].discard(correct_id)
        text = f"Молодец 🥳\nЭто <b>{correct_prep.name}</b>."
    else:
        stats["wrong"] += 1
        stats["errors"].add(correct_id)

        chosen_prep = PREP_BY_ID.get(chosen_id)
        chosen_name = chosen_prep.name if chosen_prep else "—"

        text = (
            "Всё фигня, переделывай 🤨🤡\n"
            f"Ты выбрал: <b>{chosen_name}</b>\n"
            f"Правильный ответ: <b>{correct_prep.name}</b>."
        )

    bot.send_message(callback.message.chat.id, text)
    bot.answer_callback_query(callback.id)

    # дальше пользователь сам жмет «Ещё вопрос»


# ---------- ТЕСТ (ввод): приём ответов ----------

@bot.message_handler(
    func=lambda m: m.text
    and m.text not in [
        "📚 Обучение",
        "❓ Тест (варианты)",
        "⌨️ Тест (ввод)",
        "📊 Статистика",
        "🔁 Повторить ошибки",
        "➡️ Следующий",
        "🔙 Назад к разделам",
        "🏁 Выйти",
        "Ещё вопрос",
        "Закончить тест",
    ]
)
def handle_typing_answer(message: types.Message):
    user_id = message.from_user.id
    data = user_state.get(user_id)

    # если не в режиме "ввод", просто игнорируем
    if not data or data.get("mode") != "typing":
        return

    correct_prep = PREP_BY_ID[data["correct_id"]]
    from_errors = data.get("from_errors", False)

    user_text = normalize(message.text)
    correct_name_norm = normalize(correct_prep.name)

    stats = get_user_stats(user_id)
    stats["total"] += 1

    words = [w for w in correct_name_norm.split() if len(w) > 3]

    if any(w in user_text for w in words):
        stats["correct"] += 1
        stats["errors"].discard(correct_prep.id)
        text = f"Молодец 🥳\nЭто <b>{correct_prep.name}</b>."
    else:
        stats["wrong"] += 1
        stats["errors"].add(correct_prep.id)
        text = (
            "Всё фигня, переделывай 🤨🤡\n"
            f"Правильный ответ: <b>{correct_prep.name}</b>."
        )

    bot.send_message(message.chat.id, text)
    # дальше пользователь жмет «Ещё вопрос», поэтому тут не вызываем следующий


# ---------- СТАТИСТИКА ----------

@bot.message_handler(func=lambda m: m.text == "📊 Статистика")
def handle_stats(message: types.Message):
    stats = get_user_stats(message.from_user.id)
    total = stats["total"]
    correct = stats["correct"]
    wrong = stats["wrong"]
    acc = round(correct * 100 / total, 1) if total > 0 else 0.0
    errors_count = len(stats["errors"])

    text = (
        "<b>Твоя статистика:</b>\n"
        f"• Всего вопросов: <b>{total}</b>\n"
        f"• Правильных ответов: <b>{correct}</b>\n"
        f"• Неправильных ответов: <b>{wrong}</b>\n"
        f"• Точность: <b>{acc}%</b>\n"
        f"• Препаратов в списке ошибок: <b>{errors_count}</b>\n"
        "\nСовет: режим «🔁 Повторить ошибки» как раз для этого 😉"
    )
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())


# =========================
# ЗАПУСК
# =========================

if __name__ == "__main__":
    print("Бот запущен (polling)...")
    bot.infinity_polling()
