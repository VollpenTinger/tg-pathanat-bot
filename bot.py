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
