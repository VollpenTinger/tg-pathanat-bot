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
    FSInputFile
)

# -------------------------------------
# TOKEN
# -------------------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN", "8245340349:AAF2sB8Gn5dXiqQQ1ldxAHqk_wpsdcLrH2c")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

PREP_DIR = "preparats"

# -------------------------------------
# КАТЕГОРИИ И ДИАГНОЗЫ
# -------------------------------------

CATEGORIES = {
    "Дистрофии": [
        "zernistaya_distrofiya_pochki",
        "zernistaya_distrofiya_pecheni",
        "gialinovo_kapelnaya_distrofiya_pochki",
        "vakuolnaya_distrofiya_pochki",
        "zhirovaia_distrofiya_pecheni",
        "kolloidnaya_distrofiya_shchitovidnoi"
    ],
    "Воспаления": [
        "ostryi_seroznyi_gastrit",
        "seroznoe_vosp_legkikh",
        "serozno_gemorragicheskaya_pnevmoniya",
        "gemorragicheskoe_vospalenie_kishechnika",
        "difteriticheskii_enterit",
        "gnoinyi_nefrit",
        "khronicheskii_kataralnyi_enterit_ge",
        "khronicheskii_kataralnyi_enterit_sudan"
    ],
    "Некрозы": [
        "nekroticheskii_nefroz",
        "tsenkerovskii_voskovidnyi_nekroz_myshc",
        "tvorozhistyi_nekroz_legkikh_tb",
        "tvorozhistyi_nekroz_lymph_tb"
    ],
    "Амилоидозы": [
        "amiloidoz_pecheni",
        "amiloidoz_pochki",
        "amiloidoz_selezenki_sagovaya",
        "amiloidoz_selezenki_salnaya"
    ],
    "Гемосидероз": [
        "hemosideroz_pecheni",
        "hemosideroz_pecheni_muskatnaya",
        "hemosideroz_selezenki_ge",
        "hemosideroz_selezenki_perls"
    ],
    "Гиперемия": [
        "ostraya_zastoynaya_giperemiya_otek_legkikh",
        "ostraya_zastoynaya_venoznaya_giperemiya_pecheni",
        "khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen"
    ],
    "Инфаркты": [
        "ishemicheskii_infarkt_pochki",
        "ishemicheskii_infarkt_selezenki",
        "gemorragicheskii_infarkt_pochki",
        "gemorragicheskii_infarkt_legkogo"
    ],
    "Индурации": [
        "buraya_induratsiya_legkogo",
        "buraya_induratsiya_pecheni"
    ],
    "Пневмонии": [
        "krupoznaya_pnevmoniya",
        "serozno_gemorragicheskaya_pnevmoniya"
    ],
    "Прочее": [
        "smeshannyi_tromb",
        "antrakoz_legkikh"
    ]
}

# -------------------------------------
# Русские названия
# -------------------------------------

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

    "nekroticheskii_nefroz": "Некротический нефроз",
    "tsenkerovskii_voskovidnyi_nekroz_myshc": "Ценкеровский восковидный некроз мышц",
    "tvorozhistyi_nekroz_legkikh_tb": "Творожистый некроз лёгких (туберкулёз)",
    "tvorozhistyi_nekroz_lymph_tb": "Творожистый (казеозный) некроз лимфоузла",

    "amiloidoz_pecheni": "Амилоидоз печени",
    "amiloidoz_pochki": "Амилоидоз почки",
    "amiloidoz_selezenki_sagovaya": "Амилоидоз селезёнки (саговая форма)",
    "amiloidoz_selezenki_salnaya": "Амилоидоз селезёнки (сальная форма)",

    "hemosideroz_pecheni": "Гемосидероз печени",
    "hemosideroz_pecheni_muskatnaya": "Гемосидероз печени (мускатная)",
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
    "antrакоz_legkikh": "Антракоз лёгких"
}

# -------------------------------------
# ЗАГРУЗКА ФАЙЛОВ
# -------------------------------------

SPECIMENS = {}  # base → [images]


def load_all_files():
    for fname in os.listdir(PREP_DIR):
        if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
            base = re.sub(r"[_\.\- ]?\d+$", "", fname.split(".")[0])
            SPECIMENS.setdefault(base, []).append(os.path.join(PREP_DIR, fname))

load_all_files()

# -------------------------------------
# КЛАВИАТУРЫ
# -------------------------------------

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Обучение")],
            [
                KeyboardButton(text="🟡 Лёгкий уровень"),
                KeyboardButton(text="🔴 Сложный уровень")
            ]
        ],
        resize_keyboard=True
    )

def categories_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=cat, callback_data=f"cat:{cat}")]
            for cat in CATEGORIES.keys()
        ]
    )

def diagnoses_kb(cat):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=RUS_NAMES.get(base, base),
                callback_data=f"diag:{base}"
            )]
            for base in CATEGORIES[cat]
        ]
    )

# -------------------------------------
# ОБУЧЕНИЕ
# -------------------------------------

@dp.message(F.text == "📚 Обучение")
async def learning(msg: Message):
    await msg.answer(
        "Выбери категорию:",
        reply_markup=categories_kb()
    )

@dp.callback_query(F.data.startswith("cat:"))
async def category_select(cb: CallbackQuery):
    cat = cb.data.split(":", 1)[1]
    await cb.message.answer(
        f"Выбери диагноз в категории <b>{cat}</b>:",
        reply_markup=diagnoses_kb(cat)
    )
    await cb.answer()

@dp.callback_query(F.data.startswith("diag:"))
async def diagnosis_show(cb: CallbackQuery):
    base = cb.data.split(":", 1)[1]
    name = RUS_NAMES.get(base, base)
    images = SPECIMENS.get(base, [])

    for img in images:
        await cb.message.answer_photo(FSInputFile(img))

    await cb.message.answer(f"<b>{name}</b>")
    await cb.answer()

# -------------------------------------
# ЛЁГКИЙ ТЕСТ
# -------------------------------------

@dp.message(F.text == "🟡 Лёгкий уровень")
async def easy_test(msg: Message):

    base = random.choice(list(SPECIMENS.keys()))
    correct = RUS_NAMES.get(base, base)

    # выбираем неправильные варианты
    others = [RUS_NAMES[b] for b in SPECIMENS.keys() if b != base]
    variants = random.sample(others, 3) + [correct]
    random.shuffle(variants)

    # любое фото препарата
    img = random.choice(SPECIMENS[base])

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=v, callback_data=f"ans:{v}|{correct}")]
            for v in variants
        ]
    )

    await msg.answer_photo(
        FSInputFile(img),
        caption="Выбери правильный вариант:",
        reply_markup=kb
    )

@dp.callback_query(F.data.startswith("ans:"))
async def easy_answer(cb: CallbackQuery):
    chosen, correct = cb.data.split(":", 1)[1].split("|")

    if chosen == correct:
        await cb.message.answer(f"✅ Верно! Это <b>{correct}</b>")
    else:
        await cb.message.answer(f"❌ Неверно.\nПравильный ответ: <b>{correct}</b>")

    await cb.answer()

# -------------------------------------
# СЛОЖНЫЙ ТЕСТ
# -------------------------------------

@dp.message(F.text == "🔴 Сложный уровень")
async def hard_test(msg: Message):
    base = random.choice(list(SPECIMENS.keys()))
    img = random.choice(SPECIMENS[base])
    rus = RUS_NAMES.get(base, base)

    dp.data[msg.from_user.id] = rus.lower()

    await msg.answer_photo(
        FSInputFile(img),
        caption="Напиши название препарата:"
    )

def fuzzy(a, b):
    return SequenceMatcher(None, a, b).ratio()

@dp.message()
async def check_hard(msg: Message):
    if msg.from_user.id not in dp.data:
        return

    correct = dp.data[msg.from_user.id]
    user = msg.text.lower().strip()

    if fuzzy(user, correct) > 0.7:
        txt = f"✅ Верно! Это <b>{correct}</b>"
    else:
        txt = f"❌ Неверно.\nПравильный ответ: <b>{correct}</b>"

    await msg.answer(txt)
    del dp.data[msg.from_user.id]

# -------------------------------------
# START
# -------------------------------------

@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer(
        "Привет! Я бот для тренировки микропрепаратов по патанатомии.",
        reply_markup=main_menu()
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


    
        