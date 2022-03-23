#Lorderon Client Dev by Lordbecvold
import uiScriptLocale

SMALL_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_00.sub"
MIDDLE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_01.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_03.sub"
ROOT_PATH = "d:/ymir work/ui/game/windows/"
LOCALE_PATH = uiScriptLocale.WINDOWS_PATH

window = {
	"name" : "BonusWindow",
	"style" : ("movable", "float",),
	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - 420) / 2,
	"width" : 335,
	"height" : 460,
	"children" :
	(
		{
			"name" : "Board",
			"type" : "board",
			"x" : 0,
			"y" : 0,
			"width" : 335,
			"height" : 460,
			"children" :
			(
				{
					"name" : "Bonus_Page",
					"type" : "window",
					"style" : ("attach",),
					"x" : 0,
					"y" : 0,
					"width" : 345,
					"height" : 460,
					"children" :
					(
						{
							"name" : "BonusPvP_Page",
							"type" : "window",
							"style" : ("attach",),
							"x" : 0,
							"y" : 0,
							"width" : 345,
							"height" : 430,
							"children" :
							(
								{
									"name" : "BonusPvP_TitleBar", "type" : "titlebar", "style" : ("attach",), "x" : 8, "y" : 7, "width" : 320, "color" : "red",
									"children" :
									(
										{ "name" : "TitleName", "type":"text", "x":0, "y":-1, "text": "PvP bonusy", "all_align":"center" },
									),
								},
								{
									"name" : "I_Page",
									"type" : "window",
									"style" : ("attach",),
									"x" : 0,
									"y" : 35,
									"width" : 335,
									"height" : 395,
									"children" :
									(
										{ "name":"BonusPvP_Bar_01", "type":"horizontalbar", "x":12, "y":0, "width":308, },
										{ "name":"BonusPvP_Bar_01_Text", "type" : "text", "x" : 15, "y" : 1, "text" : "Primární obrany:", },
										{ "name":"Odpornosc_Miecze", "type":"text", "x":20, "y":20, "text":"Obrana proti meèùm:" },
										{
											"name":"Odpornosc_Miecze", "type":"window", "x":20, "y":35, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_Miecze_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OM_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_bron_2reczna", "type":"text", "x":20, "y":55, "text":"Obrana proti obouruè. meèùm:" },
										{
											"name":"Odpornosc_bron_2reczna", "type":"window", "x":20, "y":70, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_Miecze_2reczne_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"ODM_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_sztylety", "type":"text", "x":20, "y":90, "text":"Obrana proti dýkám:" },
										{
											"name":"Odpornosc_sztylety", "type":"window", "x":20, "y":105, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_sztylety_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OS_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_dzwony", "type":"text", "x":20, "y":125, "text":"Obrana proti zvonùm:" },
										{
											"name":"Odpornosc_dzwony", "type":"window", "x":20, "y":140, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_dzwony_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OD_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_wachlarze", "type":"text", "x":20, "y":160, "text":"Obrana proti vìjíøùm:" },
										{
											"name":"Odpornosc_wachlarze", "type":"window", "x":20, "y":175, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_wachlarze_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OW_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_strzaly", "type":"text", "x":180, "y":20, "text":"Odolnost proti šípùm:" },
										{
											"name":"Odpornosc_strzaly", "type":"window", "x":180, "y":35, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_strzaly_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OST_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_magia", "type":"text", "x":180, "y":55, "text":"Odolnost proti magii:" },
										{
											"name":"Odpornosc_magia", "type":"window", "x":180, "y":70, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_magia_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OMG_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_ogien", "type":"text", "x":180, "y":90, "text":"Odolnost proti ohni:" },
										{
											"name":"Odpornosc_ogien", "type":"window", "x":180, "y":105, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_ogien_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OOG_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_blyskawice", "type":"text", "x":180, "y":125, "text":"Odolnost proti blesku:" },
										{
											"name":"Odpornosc_blyskawice", "type":"window", "x":180, "y":140, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_blyskawice_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OBL_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_wiatr", "type":"text", "x":180, "y":160, "text":"Odolnost proti vìtru:" },
										{
											"name":"Odpornosc_wiatr", "type":"window", "x":180, "y":175, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_wiatr_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OWI_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"BonusPvP_Bar_02", "type":"horizontalbar", "x":12, "y":200, "width":151, },
										{ "name":"BonusPvP_Bar_02_Text", "type" : "text", "x" : 15, "y" : 201, "text" : "Obecné obrany:", },
										{ "name":"BonusPvP_Bar_02", "type":"horizontalbar", "x":168, "y":200, "width":154, },
										{ "name":"BonusPvP_Bar_03_Text", "type" : "text", "x" : 174, "y" : 201, "text" : "Obrany vùèi lidem:", },
										{ "name":"Odpornosc_trucizna", "type":"text", "x":20, "y":220, "text":"Odolnost vùèi jedu:" },
										{
											"name":"Odpornosc_trucizna", "type":"window", "x":20, "y":235, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_trucizna_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OTR_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Blok_ciosu", "type":"text", "x":20, "y":255, "text":"Šance odvrátit tìlesný útok:" },
										{
											"name":"Blok_ciosu", "type":"window", "x":20, "y":270, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Blok_ciosu_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"BC_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odbicie_ciosu", "type":"text", "x":20, "y":290, "text":"Šance odrazit pøímý tìl. útok:" },
										{
											"name":"Odbicie_ciosu", "type":"window", "x":20, "y":305, "width":50, "height":20, 
											"children" :
											(
												{ "name":"odbicie_ciosow_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OC_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Szansa_na_unikniecie_strzaly", "type":"text", "x":20, "y":325, "text":"Šance vyhnout se šípùm:" },
										{
											"name":"Szansa_na_unikniecie_strzaly", "type":"window", "x":20, "y":340, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Szan_ustrzaly_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OUS_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_woj", "type":"text", "x":180, "y":220, "text":"Obrana proti váleèníkùm:" },
										{
											"name":"Odpornosc_woj", "type":"window", "x":180, "y":235, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_woj_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OWOJ_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_ninja", "type":"text", "x":180, "y":255, "text":"Obrana proti surùm:" },
										{
											"name":"Odpornosc_ninja", "type":"window", "x":180, "y":270, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_ninja_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"ONINJA_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_sura", "type":"text", "x":180, "y":290, "text":"Obrana proti ninjùm:" },
										{
											"name":"Odpornosc_sura", "type":"window", "x":180, "y":305, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_sura_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OSURA_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Odpornosc_szaman", "type":"text", "x":180, "y":325, "text":"Obrana proti šamanùm:" },
										{
											"name":"Odpornosc_szaman", "type":"window", "x":180, "y":340, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Odp_szaman_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OSZAMAN_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
									),
								},
								{
									"name" : "II_Page",
									"type" : "window",
									"style" : ("attach",),
									"x" : 0,
									"y" : 35,
									"width" : 335,
									"height" : 395,
									"children" :
									(
										{ "name":"BonusPvP_Bar_04", "type":"horizontalbar", "x":12, "y":0, "width":308, },
										{ "name":"BonusPvP_Bar_04_Text", "type" : "text", "x" : 15, "y" : 1, "text" : "Primární útoky:", },
										{ "name":"Silny_ludzie", "type":"text", "x":20, "y":20, "text":"Silný proti pololidem:" },
										{
											"name":"Silny_ludzie", "type":"window", "x":20, "y":35, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Silny_ludzie_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"LUD_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Krytyk", "type":"text", "x":20, "y":55, "text":"Šance na kritický zásah:" },
										{
											"name":"Krytyk", "type":"window", "x":20, "y":70, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Krytyk_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"KRYT_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Przeszywa", "type":"text", "x":20, "y":90, "text":"Šance na pronikavý zásah:" },
										{
											"name":"Przeszywa", "type":"window", "x":20, "y":105, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Przeszywa_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"PRZESZYWA_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Otrucie", "type":"text", "x":20, "y":125, "text":"Šance na otrávení:" },
										{
											"name":"Otrucie", "type":"window", "x":20, "y":140, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Otrucie_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OTRUCIE_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Omdlenie", "type":"text", "x":20, "y":160, "text":"Šance na bezvìdomí:" },
										{
											"name":"Omdlenie", "type":"window", "x":20, "y":175, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Omdlenie_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"OMDLENIE_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Spowolnienie", "type":"text", "x":180, "y":20, "text":"Šance na zpomalení:" },
										{
											"name":"Spowolnienie", "type":"window", "x":180, "y":35, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Spowolnienie_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"SPOWOLNIENIE_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Srednie", "type":"text", "x":180, "y":55, "text":"Prùmìrná škoda:" },
										{
											"name":"Srednie", "type":"window", "x":180, "y":70, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Srednie_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"SREDNIE_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Umki", "type":"text", "x":180, "y":90, "text":"Poškození schopností:" },
										{
											"name":"Umki", "type":"window", "x":180, "y":105, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Umki_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"UMKI_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Szybkosc_zaklecia", "type":"text", "x":180, "y":125,  "text":"Rychlost kouzel:" },
										{
											"name":"Szybkosc_zaklecia", "type":"window", "x":180, "y":140, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Szybkosc_zaklecia_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"SZAKLECIA_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Wartosc_ataku", "type":"text", "x":180, "y":160, "text":"Hodnota útoku:" },
										{
											"name":"Wartosc_ataku", "type":"window", "x":180, "y":175, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Wartosc_ataku_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"WA_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"BonusPvP_Bar_05", "type":"horizontalbar", "x":12, "y":200, "width":151, },
										{ "name":"BonusPvP_Bar_05_Text", "type" : "text", "x" : 15, "y" : 201, "text" : "Odolnosti vùèi:", },
										{ "name":"NNO", "type":"text", "x":20, "y":220, "text":"Omráèení:" },
										{
											"name":"NNO", "type":"window", "x":20, "y":235, "width":50, "height":20, 
											"children" :
											(
												{ "name":"NNO_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"NNO_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"NNS", "type":"text", "x":20, "y":255, "text":"Zpomalení:" },
										{
											"name":"NNS", "type":"window", "x":20, "y":270, "width":50, "height":20, 
											"children" :
											(
												{ "name":"NNS_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"NNS_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"BonusPvP_Bar_06", "type":"horizontalbar", "x":168, "y":200, "width":154, },
										{ "name":"BonusPvP_Bar_06_Text", "type" : "text", "x" : 174, "y" : 201, "text" : "Silný proti lidem:", },
										{ "name":"Silny_woj", "type":"text", "x":180, "y":220, "text":"Silný proti váleèníkùm:" },
										{
											"name":"Silny_woj", "type":"window", "x":180, "y":235, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Silny_woj_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"SWOJ_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Silny_ninja", "type":"text", "x":180, "y":255, "text":"Silný proti ninjùm:" },
										{
											"name":"Silny_ninja", "type":"window", "x":180, "y":270, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Silny_ninja_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"SNINJA_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Silny_sura", "type":"text", "x":180, "y":290, "text":"Silný proti surùm:" },
										{
											"name":"Silny_sura", "type":"window", "x":180, "y":305, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Silny_sura_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"SSURA_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
										{ "name":"Silny_szaman", "type":"text", "x":180, "y":325, "text":"Silný proti šamanùm:" },
										{
											"name":"Silny_szaman", "type":"window", "x":180, "y":340, "width":50, "height":20, 
											"children" :
											(
												{ "name":"Silny_szaman_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
												{ "name":"SSZAMAN_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
											)
										},
									),
								},
								{
									"name" : "I_Button",
									"type" : "radio_button",
									"x" : 75,
									"y" : 400,
									"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_01.sub",
									"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_02.sub",
									"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_03.sub",
									"children" :
									(
										{
											"name" : "I_Button_Print",
											"type" : "text",
											"x" : 0,
											"y" : 0,
											"all_align" : "center",
											"text" : "I.",
										},
									),
								},
								{
									"name" : "II_Button",
									"type" : "radio_button",
									"x" : 185,
									"y" : 400,
									"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_01.sub",
									"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_02.sub",
									"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_03.sub",
									"children" :
									(
										{
											"name" : "II_Button_Print",
											"type" : "text",
											"x" : 0,
											"y" : 0,
											"all_align" : "center",
											"text" : "II.",
										},
									),
								},
							),
						},
						{
							"name" : "BonusPvM_Page",
							"type" : "window",
							"style" : ("attach",),
							"x" : 0,
							"y" : 0,
							"width" : 335,
							"height" : 430,
							"children" :
							(
								{
									"name" : "BonusPvM_TitleBar",
									"type" : "titlebar",
									"style" : ("attach",),
									"x" : 8,
									"y" : 7,
									"width" : 320,
									"color" : "red",
									"children" :
									(
										{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":"PvM bonusy", "all_align":"center" },
									),
								},
								{ "name":"BonusPvM_Bar_01", "type":"horizontalbar", "x":12, "y":35, "width":308, },
								{ "name":"BonusPvM_Bar_01_Text", "type" : "text", "x" : 15, "y": 36, "text" : "Primární bonusy:", },
								{ "name":"Silny_potwory", "type":"text", "x":20, "y":55, "text":"Silný proti pøíšerám:" },
								{
									"name":"Silny_potwory", "type":"window", "x":20, "y":70, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Silny_potwory_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"POTWORY_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Diably", "type":"text", "x":20, "y":90, "text":"Silný proti ïáblu:" },
								{
									"name":"Diably", "type":"window", "x":20, "y":105, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Diably_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"DIABLY_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Nieumarli", "type":"text", "x":20, "y":125, "text":"Silný proti nemrtvým:" },
								{
									"name":"Nieumarli", "type":"window", "x":20, "y":140, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Nieumarli_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"NIEUMARLI_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Mistyki", "type":"text", "x":20, "y":160, "text":"Silný proti ezoterikùm:" },
								{
									"name":"Mistyki", "type":"window", "x":20, "y":175, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Mistyki_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MISTYKI_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Orki", "type":"text", "x":20, "y":195, "text":"Silný proti orkùm:" },
								{
									"name":"Orki", "type":"window", "x":20, "y":210, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Orki_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"ORKI_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"REGPZ", "type":"text", "x":180, "y":55, "text":"Obnovení ZB:" },
								{
									"name":"REGPZ", "type":"window", "x":180, "y":70, "width":50, "height":20, 
									"children" :
									(
										{ "name":"REGPZ_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"REGPZ_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"REGPE", "type":"text", "x":180, "y":90, "text":"Obnovení MB:" },
								{
									"name":"REGPE", "type":"window", "x":180, "y":105, "width":50, "height":20, 
									"children" :
									(
										{ "name":"REGPE_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"REGPE_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Szansa_Bonus_Dos", "type":"text", "x":180, "y":125, "text":"Šance na EXP bonus:" },
								{
									"name":"Szansa_Bonus_Dos", "type":"window", "x":180, "y":140, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Szansa_Bonus_Dos", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"SZBONUSDOS_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Szansa_podwojna_YANG", "type":"text", "x":180, "y":160, "text":"Šance na YANG bonus:" },
								{
									"name":"Szansa_podwojna_YANG", "type":"window", "x":180, "y":175, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Szansa_podwojna_YANG_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"SZPYANG_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									),
								},
								{ "name":"Szansa_podwojne_przedmioty", "type":"text", "x":180, "y":195, "text":"Šance na DROP bonus:" },
								{
									"name":"Szansa_podwojne_przedmioty", "type":"window", "x":180, "y":210, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Szansa_podwojne_przedmioty_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"SZPP_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"BonusPvM_Bar_02", "type":"horizontalbar", "x":12, "y":235, "width":151, },
								{ "name":"BonusPvM_Bar_02_Text", "type" : "text", "x" : 15, "y" : 236, "text" : "Obecné:", },
								{ "name":"Krytyk", "type":"text", "x":20, "y":255, "text":"Šance na kritický zásah:" },
								{
									"name":"Krytyk", "type":"window", "x":20, "y":270, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Krytyk_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"KRYT2_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Przeszywa", "type":"text", "x":20, "y":290, "text":"Šance na pronikavý zásah:" },
								{
									"name":"Przeszywa", "type":"window", "x":20, "y":305, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Przeszywa_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"PRZESZYWA2_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Zwierzeta", "type":"text", "x":20, "y":325, "text":"Silný proti zvíøatùm:" },
								{
									"name":"Zwierzeta", "type":"window", "x":20, "y":340, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Zwierzeta_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"ZWIERZETA_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"BonusPvM_Bar_03", "type":"horizontalbar", "x":168, "y":235, "width":154, },
								{ "name":"BonusPvM_Bar_03_Text", "type" : "text", "x" : 174, "y" : 236, "text" : "Obrany:", },
								{ "name":"Blok_ciosu", "type":"text", "x":180, "y":255, "text":"Šance odvrátit tìlesný útok:" },
								{
									"name":"Blok_ciosu", "type":"window", "x":180, "y":270, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Blok_ciosow", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"BC2_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Odbicie_ciosu", "type":"text", "x":180, "y":290, "text":"Šance odrazit pøímý tìl. útok:" },
								{
									"name":"Odbicie_ciosu", "type":"window", "x":180, "y":305, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Odbicie_ciosow_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"OC2_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Obrona", "type":"text", "x":180, "y":325, "text":"Obrana:" },
								{
									"name":"Obrona", "type":"window", "x":180, "y":340, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Obrona_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"OBRONA_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
							),
						},
						{
							"name" : "Inne_Page",
							"type" : "window",
							"style" : ("attach",),
							"x" : 0,
							"y" : 0,
							"width" : 335,
							"height" : 430,
							"children" :
							(
								{
									"name" : "Inne_TitleBar",
									"type" : "titlebar",
									"style" : ("attach",),
									"x" : 8,
									"y" : 7,
									"width" : 320,
									"color" : "red",
									"children" :
									(
										{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":"Poèítadlo bonusù - ostatní", "all_align":"center" },
										
									),
								},
								{ "name":"Inne_Bar_01", "type":"horizontalbar", "x":12, "y":35, "width":308, },
								{ "name":"Inne_Bar_01_Text", "type" : "text", "x" : 15, "y" : 36, "text" : "Inne bonusy:", },
								{ "name":"Wit", "type":"text", "x":40, "y":55, "text":"Vitalita:" },
								{
									"name":"Wit", "type":"window", "x":40, "y":70, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Wit", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"WIT_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Int", "type":"text", "x":40, "y":90, "text":"Inteligence:" },
								{
									"name":"Int", "type":"window", "x":40, "y":105, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Int_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"INT_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Sil", "type":"text", "x":40, "y":125, "text":"Síla:" },
								{
									"name":"Sil", "type":"window", "x":40, "y":140, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Sil_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"SILA_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Zre", "type":"text", "x":40, "y":160, "text":"Pohyblivost:" },
								{
									"name":"Zre", "type":"window", "x":40, "y":175, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Zre_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"ZRE_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"MINPZ", "type":"text", "x":140, "y":55, "text":"Aktuální ZB:" },
								{
									"name":"MINPZ", "type":"window", "x":140, "y":70, "width":50, "height":20, 
									"children" :
									(
										{ "name":"MINPZ_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MINPZ_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"MINPE", "type":"text", "x":140, "y":90, "text":"Aktuální MB:" },
								{
									"name":"MINPE", "type":"window", "x":140, "y":105, "width":50, "height":20, 
									"children" :
									(
										{ "name":"MINPE_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MINPE_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"MINATK", "type":"text", "x":140, "y":125, "text":"Útok min.:" },
								{
									"name":"MINATK", "type":"window", "x":140, "y":140, "width":50, "height":20, 
									"children" :
									(
										{ "name":"MINATK_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MINATK_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"BonusObrony", "type":"text", "x":140, "y":160, "text":"Obrana +:" },
								{
									"name":"BonusObrony", "type":"window", "x":140, "y":175, "width":50, "height":20, 
									"children" :
									(
										{ "name":"BonusObrony_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"BOBRONY_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"MAXPZ", "type":"text", "x":240, "y":55, "text":"Poèet ZB:" },
								{
									"name":"MAXPZ", "type":"window", "x":240, "y":70, "width":50, "height":20, 
									"children" :
									(
										{ "name":"MAXPZ_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MAXPZ_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"MAXPE", "type":"text", "x":240, "y":90, "text":"Poèet MB:" },
								{
									"name":"MAXPE", "type":"window", "x":240, "y":105, "width":50, "height":20, 
									"children" :
									(
										{ "name":"MAXPE_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MAXPE_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"MAXATK", "type":"text", "x":240, "y":125, "text":"Útok max.:" },
								{
									"name":"MAXATK", "type":"window", "x":240, "y":140, "width":50, "height":20, 
									"children" :
									(
										{ "name":"MAXATK_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"MAXATK_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
								{ "name":"Obrona", "type":"text", "x":240, "y":160, "text":"Obrana:" },
								{
									"name":"Obrona", "type":"window", "x":240, "y":175, "width":50, "height":20, 
									"children" :
									(
										{ "name":"Obrona_Miejsce", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										{ "name":"OBRONA2_Value", "type":"text", "x":26, "y":3, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									)
								},
							),
						},
						{
							"name" : "Tabb_Button_01",
							"type" : "radio_button",

							"x" : 20,
							"y" : 430,

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_03.sub",
							"children" :
							(
								{
									"name" : "Bonus_Tab_01_Print",
									"type" : "text",
									"x" : 0,
									"y" : 0,
									"all_align" : "center",
									"text" : "PvP",
								},
							),
						},
						{
							"name" : "Tabb_Button_02",
							"type" : "radio_button",
							"x" : 128,
							"y" : 430,
							"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_03.sub",
							"children" :
							(
								{
									"name" : "Bonus_Tab_02_Print",
									"type" : "text",
									"x" : 0,
									"y" : 0,
									"all_align" : "center",
									"text" : "PvM",
								},
							),
						},
						{
							"name" : "Tabb_Button_03",
							"type" : "radio_button",
							"x" : 235,
							"y" : 430,
							"width" : 76,
							"height" : 17,
							"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_03.sub",
							"children" :
							(
								{
									"name" : "Bonus_Tab_03_Print",
									"type" : "text",
									"x" : 0,
									"y" : 0,
									"all_align" : "center",
									"text" : "Ostatní",
								},
							),
						},
					{ "name":"Sanex_Copyright", "type":"text", "x":280, "y":36, "text":"", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
					),
				},
			),
		},
	),
}
