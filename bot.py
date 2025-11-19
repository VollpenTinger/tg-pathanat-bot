import asyncio
import random
from dataclasses import dataclass
from typing import List, Dict
from difflib import SequenceMatcher

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

# ============================================================
#   ТОКЕН
# ============================================================

BOT_TOKEN = "8245340349:AAF2sB8Gn5dXiqQQ1ldxAHqk_wpsdcLrH2c"

# ============================================================
#   ДАННЫЕ О ПРЕПАРАТАХ
# ============================================================

BASE_URL = "https://raw.githubusercontent.com/lapinaalina845-ux/tg-pathanat-bot/main/preparats/"

@dataclass
class Preparat:
    id: str
    name: str
    category: str
    files: List[str]

PREPARATS: List[Preparat] = [
    Preparat("amiloidoz_pecheni","Амилоидоз печени","Амилоидозы",
             ["amiloidoz_pecheni_1.jpeg","amiloidoz_pecheni_2.jpeg","amiloidoz_pecheni_3.jpeg"]),
    Preparat("amiloidoz_pochki","Амилоидоз почки","Амилоидозы",
             ["amiloidoz_pochki_1.jpeg","amiloidoz_pochki_2.jpeg"]),
    Preparat("amiloidoz_selezenki_sagovaya","Амилоидоз селезёнки («саговая» форма)","Амилоидозы",
             ["amiloidoz_selezenki_sagovaya_1.jpeg","amiloidoz_selezenki_sagovaya_2.jpeg"]),
    Preparat("amiloidoz_selezenki_salnaya","Амилоидоз селезёнки («сальная» форма)","Амилоидозы",
             ["amiloidoz_selezenki_salnaya_1.jpeg","amiloidoz_selezenki_salnaya_2.jpeg","amiloidoz_selezenki_salnaya_3.jpeg"]),

    # ----- воспаление -----
    Preparat("serozno_gemorragicheskaya_pnevmoniya","Серозно-геморрагическая пневмония","Воспаление",
             ["serozno_gemorragicheskaya_pnevmoniya_1.jpeg","serozno_gemorragicheskaya_pnevmoniya_2.jpeg","serozno_gemorragicheskaya_pnevmoniya_3.jpeg"]),

    Preparat("seroznoe_vosp_legkikh","Серозное воспаление лёгких","Воспаление",
             ["seroznoe_vosp_legkikh_1.jpeg","seroznoe_vosp_legkikh_2.jpeg","seroznoe_vosp_legkikh_3.jpeg"]),

    Preparat("ostryi_seroznyi_gastrit","Острый серозный гастрит","Воспаление",
             ["ostryi_seroznyi_gastrit_1.jpeg","ostryi_seroznyi_gastrit_2.jpeg","ostryi_seroznyi_gastrit_3.jpeg","ostryi_seroznyi_gastrit_4.jpeg"]),

    Preparat("krupoznaya_pnevmoniya","Крупозная пневмония","Воспаление",
             ["krupoznaya_pnevmoniya_1.jpeg","krupoznaya_pnevmoniya_2.jpeg"]),

    Preparat("fibrinoznyi_perikardit","Фибринозный перикардит","Воспаление",
             ["fibrinoznyi_perikardit_1.jpeg","fibrinoznyi_perikardit_2.jpeg","fibrinoznyi_perikardit_3.jpeg"]),

    Preparat("difteriticheskii_enterit","Дифтеритический энтерит","Воспаление",
             ["difteriticheskii_enterit_1.jpeg","difteriticheskii_enterit_2.jpeg"]),

    Preparat("gemorragicheskoe_vospalenie_kishechnika","Геморрагическое воспаление кишечника","Воспаление",
             ["gemorragicheskoe_vospalenie_kishechnika_1.jpeg",
              "gemorragicheskoe_vospalenie_kishechnika_2.jpeg",
              "gemorragicheskoe_vospalenie_kishechnika_3.jpeg"]),

    Preparat("gnoinyi_nefrit","Гнойный нефрит","Воспаление",
             ["gnoinyi_nefrit_1.jpeg","gnoinyi_nefrit_2.jpeg","gnoinyi_nefrit_3.jpeg","gnoinyi_nefrit_4.jpeg"]),

    Preparat("khronicheskii_abscess_pecheni","Хронический абсцесс печени","Воспаление",
             ["khronicheskii_abscess_pecheni_1.jpeg"]),

    Preparat("khronicheskii_kataralnyi_enterit_ge","Хронический катаральный энтерит (ГЭ)","Воспаление",
             ["khronicheskii_kataralnyi_enterit_ge_1.jpeg",
              "khronicheskii_kataralnyi_enterit_ge_2.jpeg",
              "khronicheskii_kataralnyi_enterit_ge_3.jpeg",
              "khronicheskii_kataralnyi_enterit_ge_4.jpeg"]),

    Preparat("khronicheskii_kataralnyi_enterit_sudan","Хронический катаральный энтерит (Судан III)","Воспаление",
             ["khronicheskii_kataralnyi_enterit_sudan_1.jpeg",
              "khronicheskii_kataralnyi_enterit_sudan_2.jpeg",
              "khronicheskii_kataralnyi_enterit_sudan_3.jpeg"]),

    # ---- дистрофии ----
    Preparat("zernistaya_distrofiya_pochki","Зернистая дистрофия почки","Дистрофии",
             ["zernistaya_distrofiya_pochki_1.jpeg","zernistaya_distrofiya_pochki_2.jpeg"]),
    Preparat("zernistaya_distrofiya_pecheni","Зернистая дистрофия печени","Дистрофии",
             ["zernistaya_distrofiya_pecheni_1.jpeg","zernistaya_distrofiya_pecheni_2.jpeg"]),

    Preparat("gialinovo_kapelnaya_distrofiya_pochki","Гиалиново-капельная дистрофия почки","Дистрофии",
             ["gialinovo_kapelnaya_distrofiya_pochki_1.jpeg",
              "gialinovo_kapelnaya_distrofiya_pochki_2.jpeg",
              "gialinovo_kapelnaya_distrofiya_pochki_3.jpeg"]),

    Preparat("vakuolnaya_distrofiya_pochki","Вакуольная дистрофия почки","Дистрофии",
             ["vakuolnaya_distrofiya_pochki_1.jpeg"]),

    Preparat("kolloidnaya_distrofiya_shchitovidnoi","Коллоидная дистрофия щитовидной железы","Дистрофии",
             ["kolloidnaya_distrofiya_shchitovidnoi_1.jpeg","kolloidnaya_distrofiya_shchitovidnoi_2.jpeg"]),

    Preparat("zhirovaia_distrofiya_pecheni","Жировая дистрофия печени","Дистрофии",
             ["zhirovaia_distrofiya_pecheni_1.jpeg","zhirovaia_distrofiya_pecheni_2.jpeg"]),

    # ---- гиалиноз ----
    Preparat("gialinoz_stenki_sosuda_matki","Гиалиноз стенки сосуда матки","Гиалинозы",
             ["gialinoz_stenki_sosuda_matki_1.jpeg",
              "gialinoz_stenki_sosuda_matki_2.jpeg",
              "gialinoz_stenki_sosuda_matki_3.jpeg"]),

    Preparat("gialinoz_selezenki","Гиалиноз селезёнки","Гиалинозы",
             ["gialinoz_selezenki_1.jpeg",
              "gialinoz_selezenki_2.jpeg",
              "gialinoz_selezenki_3.jpeg"]),

    # ---- пигменты ----
    Preparat("hemosideroz_pecheni","Гемосидероз печени","Пигменты",
             ["hemosideroz_pecheni_1.jpeg","hemosideroz_pecheni_2.jpeg"]),

    Preparat("hemosideroz_pecheni_muskatnaya","Гемосидероз печени («мускатная печень»)","Пигменты",
             ["hemosideroz_pecheni_muskatnaya_1.jpeg",
              "hemosideroz_pecheni_muskatnaya_2.jpeg",
              "hemosideroz_pecheni_muskatnaya_3.jpeg"]),

    Preparat("hemosideroz_selezenki_ge","Гемосидероз селезёнки (ГЭ)","Пигменты",
             ["hemosideroz_selezenki_ge_1.jpeg",
              "hemosideroz_selezenki_ge_2.jpeg",
              "hemosideroz_selezenki_ge_3.jpeg",
              "hemosideroz_selezenki_ge_4.jpeg"]),

    Preparat("hemosideroz_selezenki_perls","Гемосидероз селезёнки (Перлс)","Пигменты",
             ["hemosideroz_selezenki_perls_1.jpeg",
              "hemosideroz_selezenki_perls_2.jpeg",
              "hemosideroz_selezenki_perls_3.jpeg",
              "hemosideroz_selezenki_perls_4.jpeg"]),

    Preparat("melanoz_pecheni","Меланоз печени","Пигменты",
             ["melanoz_pecheni_1.jpeg","melanoz_pecheni_2.jpeg","melanoz_pecheni_3.jpeg"]),

    Preparat("antrakoz_legkikh","Антракоз лёгких","Пигменты",
             ["antrakoz_legkikh_1.jpeg","antrakoz_legkikh_2.jpeg","antrakoz_legkikh_3.jpeg"]),

    # ---- некроз ----
    Preparat("nekroticheskii_nefroz","Некротический нефроз","Некроз",
             ["nekroticheskii_nefroz_1.jpeg","nekroticheskii_nefroz_2.jpeg","nekroticheskii_nefroz_3.jpeg"]),

    Preparat("tvorozhistyi_nekroz_lymph_tb","Творожистый некроз лимфоузла (туберкулёз)","Некроз",
             ["tvorozhistyi_nekroz_lymph_tb_1.jpeg","tvorozhistyi_nekroz_lymph_tb_2.jpeg"]),

    Preparat("tsenkerovskii_voskovidnyi_nekroz_myshc","Ценкеровский некроз мышц","Некроз",
             ["tsenkerovskii_voskovidnyi_nekroz_myshc_1.jpeg","tsenkerovskii_voskovidnyi_nekroz_myshc_2.jpeg"]),

    Preparat("tvorozhistyi_nekroz_legkikh_tb","Творожистый некроз лёгких (туберкулёз)","Некроз",
             ["tvorozhistyi_nekroz_legkikh_tb_1.jpeg","tvorozhistyi_nekroz_legkikh_tb_2.jpeg"]),

    # ---- кровообращение ----
    Preparat("buraya_induratsiya_pecheni","Бурая индурация печени","Кровообращение",
             ["buraya_induratsiya_pecheni_1.jpeg","buraya_induratsiya_pecheni_2.jpeg"]),

    Preparat("ostraya_zastoynaya_venoznaya_giperemiya_pecheni","Острая застойная венозная гиперемия печени","Кровообращение",
             ["ostraya_zастойная_venoznaya_giperemiya_pecheni_1.jpeg",
              "ostraya_zастойная_venознaya_giperemiya_pecheni_2.jpeg"]),

    Preparat("khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen","Хроническое венозное полнокровие печени («мускатная печень»)","Кровообращение",
             ["khronicheskoe_venoznoe_polnokrovie_muskatnaya_pechen_1.jpeg",
              "khronicheskoe_venoznoe_polнокровие_muskatnaya_pechen_2.jpeg"]),

    Preparat("ostraya_zastoynaya_giperemiya_otek_legkikh","Острая застойная гиперемия и отёк лёгких","Кровообращение",
             ["ostraya_zастoynaya_giperemiya_otek_legkikh_1.jpeg",
              "ostraya_zастoynaya_giperemiya_otek_legkikh_2.jpeg"]),

    Preparat("buraya_induratsiya_legkogo","Бурая индурация лёгкого","Кровообращение",
             ["buraya_induratsiya_legkogo_1.jpeg","buraya_induratsiya_legkogo_2.jpeg"]),

    # ---- инфаркты ----
    Preparat("ishemicheskii_infarkt_pochki","Ишемический инфаркт почки","Инфаркты",
             ["ishemicheskii_infarkt_pochki_1.jpeg","ishemicheskii_infarkt_pochki_2.jpeg"]),

    Preparat("ishemicheskii_infarkt_selezenki","Ишемический инфаркт селезёнки","Инфаркты",
             ["ishemicheskii_infarkt_selezenki_1.jpeg","ishemicheskii_infarkt_selezenki_2.jpeg"]),

    Preparat("gemorragicheskii_infarkt_pochki","Геморрагический инфаркт почки","Инфаркты",
             ["gemorragicheskii_infarkt_pochki_1.jpeg",
              "gemorragicheskii_infarkt_pochki_2.jpeg",
              "gemorragicheskii_infarkt_pochki_3.jpeg"]),

    Preparat("gemorragicheskii_infarkt_legkogo","Геморрагический инфаркт лёгкого","Инфаркты",
             ["gemorragicheskii_infarkt_legkogo_1.jpeg","gemorragicheskii_infarkt_legkogo_2.jpeg"]),

    # ---- тромбоз ----
    Preparat("smeshannyi_tromb","Смешанный тромб","Тромбоз",
             ["smeshannyi_tromb_1.jpeg","smeshannyi_tromb_2.jpeg"]),
]

# ============================================================
# КАТЕГОРИИ
# ============================================================

SECTIONS: Dict[str, List[Preparat]] = {}
for p in PREPARATS:
    SECTIONS.setdefault(p.category, []).append(p)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ============================================================
#   МЕНЮ
# ============================================================

def home_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📚 Режим обучения", callback_data="learn")],
        [InlineKeyboardButton(text="🎲 Случайный препарат", callback_data="random")],
        [InlineKeyboardButton(text="🧪 Тест", callback_data="test_menu")],
    ])

def sections_kb():
    kb = []
    for name in SECTIONS:
        kb.append([InlineKeyboardButton(text=name, callback_data=f"sec_{name}")])
    kb.append([InlineKeyboardButton(text="🏠 Домой", callback_data="home")])
    return InlineKeyboardMarkup(inline_keyboard=kb)

def learn_nav_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➡️ Следующий", callback_data="next")],
        [InlineKeyboardButton(text="🔙 К разделам", callback_data="learn")],
        [InlineKeyboardButton(text="🏠 Домой", callback_data="home")],
    ])

def test_menu_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1️⃣ Варианты ответов", callback_data="test_var")],
        [InlineKeyboardButton(text="2️⃣ Ввод ответа", callback_data="test_write")],
        [InlineKeyboardButton(text="📊 Ошибки", callback_data="test_err")],
        [InlineKeyboardButton(text="🏠 Домой", callback_data="home")],
    ])

# ============================================================
# СОСТОЯНИЕ ПОЛЬЗОВАТЕЛЯ
# ============================================================

USER = {}

def get_user(uid):
    if uid not in USER:
        USER[uid] = {
            "mode": None,
            "section": None,
            "index": 0,
            "used_random": set(),
            "errors": []
        }
    return USER[uid]

# ============================================================
# ОБРАБОТКА /start
# ============================================================

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("👋 Привет! Выбери режим:", reply_markup=home_kb())
# ============================================================
#   РЕЖИМ ОБУЧЕНИЯ
# ============================================================

@dp.callback_query(lambda c: c.data == "learn")
async def learn(call: types.CallbackQuery):
    await call.message.edit_text("Выберите раздел:", reply_markup=sections_kb())
    await call.answer()

@dp.callback_query(lambda c: c.data.startswith("sec_"))
async def choose_section(call: types.CallbackQuery):
    uid = call.from_user.id
    section = call.data[4:]
    u = get_user(uid)

    u["mode"] = "learn"
    u["section"] = section
    u["index"] = 0

    await send_prep(call, section, 0)

async def send_prep(call, section, index):
    items = SECTIONS[section]

    if index >= len(items):
        await call.message.edit_text(
            f"🎉 Вы прошли раздел *{section}*!",
            parse_mode="Markdown",
            reply_markup=sections_kb()
        )
        return

    prep = items[index]
    url = BASE_URL + random.choice(prep.files)

    await call.message.edit_photo(
        photo=url,
        caption=f"**{prep.name}**\nРаздел: {section}",
        parse_mode="Markdown",
        reply_markup=learn_nav_kb()
    )

@dp.callback_query(lambda c: c.data == "next")
async def next_prep(call: types.CallbackQuery):
    uid = call.from_user.id
    u = get_user(uid)

    if u["mode"] != "learn":
        await call.answer("Выберите раздел!", show_alert=True)
        return

    u["index"] += 1
    await send_prep(call, u["section"], u["index"])
    await call.answer()

# ============================================================
#   СЛУЧАЙНЫЙ ПРЕПАРАТ (БЕЗ ПОВТОРОВ)
# ============================================================

@dp.callback_query(lambda c: c.data == "random")
async def random_prep(call: types.CallbackQuery):
    uid = call.from_user.id
    u = get_user(uid)

    all_items = PREPARATS
    used = u["used_random"]

    available = [p for p in all_items if p.id not in used]

    if not available:
        await call.message.edit_text("🎉 Все препараты просмотрены!", reply_markup=home_kb())
        return

    prep = random.choice(available)
    used.add(prep.id)

    url = BASE_URL + random.choice(prep.files)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎲 Ещё", callback_data="random")],
        [InlineKeyboardButton(text="🏠 Домой", callback_data="home")]
    ])

    await call.message.edit_photo(
        photo=url,
        caption=f"Случайный препарат:\n**{prep.name}**",
        parse_mode="Markdown",
        reply_markup=kb
    )
    await call.answer()

# ============================================================
#   ТЕСТ — МЕНЮ
# ============================================================

@dp.callback_query(lambda c: c.data == "test_menu")
async def test_menu(call: types.CallbackQuery):
    await call.message.edit_text("Выберите тип теста:", reply_markup=test_menu_kb())
    await call.answer()

# ============================================================
#   ТЕСТ — ВАРИАНТЫ
# ============================================================

@dp.callback_query(lambda c: c.data == "test_var")
async def test_var(call: types.CallbackQuery):
    uid = call.from_user.id
    u = get_user(uid)

    target = random.choice(PREPARATS)
    u["test_target"] = target.name

    # варианты не повторяются и перемешиваются
    variants = {target.name}
    while len(variants) < 4:
        variants.add(random.choice(PREPARATS).name)

    variants = list(variants)
    random.shuffle(variants)

    kb = []
    for v in variants:
        kb.append([InlineKeyboardButton(text=v, callback_data=f"ans_{v}")])

    kb.append([InlineKeyboardButton(text="🏠 Домой", callback_data="home")])

    url = BASE_URL + random.choice(target.files)

    await call.message.edit_photo(
        photo=url,
        caption="Выберите название препарата:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=kb)
    )
    await call.answer()

@dp.callback_query(lambda c: c.data.startswith("ans_"))
async def check_var(call: types.CallbackQuery):
    uid = call.from_user.id
    u = get_user(uid)

    answer = call.data[4:]
    correct = u.get("test_target")

    if answer == correct:
        text = "✅ Правильно!"
    else:
        text = f"❌ Неверно\nПравильный ответ: *{correct}*"
        u["errors"].append(correct)

    await call.message.edit_text(text, parse_mode="Markdown", reply_markup=test_menu_kb())
    await call.answer()
    # ============================================================
#   ТЕСТ — ВВОД ОТВЕТА
# ============================================================

@dp.callback_query(lambda c: c.data == "test_write")
async def test_write(call: types.CallbackQuery):
    uid = call.from_user.id
    u = get_user(uid)
    u["mode"] = "test_write"

    target = random.choice(PREPARATS)
    u["test_target"] = target.name

    url = BASE_URL + random.choice(target.files)

    await call.message.edit_photo(
        photo=url,
        caption="Введите название препарата:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🏠 Домой", callback_data="home")]
        ])
    )
    await call.answer()

@dp.message()
async def test_write_answer(message: Message):
    uid = message.from_user.id
    u = get_user(uid)

    if u.get("mode") != "test_write":
        return

    correct = u.get("test_target")
    user_text = message.text.strip().lower()

    ratio = SequenceMatcher(None, user_text, correct.lower()).ratio()

    if ratio > 0.7:
        await message.answer(
            f"✅ Верно!\nСовпадение: {ratio:.2f}",
            reply_markup=test_menu_kb()
        )
    else:
        u["errors"].append(correct)
        await message.answer(
            f"❌ Неверно!\nПравильный ответ: *{correct}*\nСовпадение: {ratio:.2f}",
            parse_mode="Markdown",
            reply_markup=test_menu_kb()
        )

# ============================================================
#   ОШИБКИ
# ============================================================

@dp.callback_query(lambda c: c.data == "test_err")
async def test_err(call: types.CallbackQuery):
    uid = call.from_user.id
    u = get_user(uid)

    if not u["errors"]:
        text = "Ошибок нет — отлично! 🎉"
    else:
        text = "Ваши ошибки:\n" + "\n".join(f"— {e}" for e in set(u["errors"]))

    await call.message.edit_text(text, reply_markup=test_menu_kb())
    await call.answer()

# ============================================================
#   КНОПКА ДОМОЙ
# ============================================================

@dp.callback_query(lambda c: c.data == "home")
async def home(call: types.CallbackQuery):
    await call.message.edit_text("Главное меню:", reply_markup=home_kb())
    await call.answer()

# ============================================================
#   ЗАПУСК БОТА
# ============================================================

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())