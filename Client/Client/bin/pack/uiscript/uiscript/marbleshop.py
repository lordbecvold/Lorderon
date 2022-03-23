#Lorderon Client Dev By Lordbecvold
import uiScriptLocale

SMALL_VALUE_SLOT = "d:/ymir work/ui/public/Parameter_Slot_01.sub"
XLARGE_VALUE_SLOT = "d:/ymir work/ui/public/Parameter_Slot_05.sub"
ICON_SLOT_FILE = "d:/ymir work/ui/public/Slot_Base.sub"
ROOT_PATH = "d:/ymir work/ui/game/windows/"
GLOBAL_HEIGHT = 200

window = {
	"name" : "MarbleShop",
	"x" : (SCREEN_WIDTH - 300) / 2,
	"y" : (SCREEN_HEIGHT - 200) / 2,
	"style" : ("movable", "float",),
	"width" : 300,
	"height" : GLOBAL_HEIGHT,
	"children" : 
	(
		{
			"name" : "board",
			"type" : "board",
			"x" : 0,
			"y" : 0,
			"width" : 300,
			"height" : GLOBAL_HEIGHT,
			"children" : 
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 8,
					"y" : 7,
					"width" : 290,
					"color" : "yellow",
					"children" :
					(
						{ 
							"name": "TitleName",
							"type":"text",
							"x":142,
							"y":3,
							"text": "Obchod promìn",
							"text_horizontal_align":"center"
						},
					),
				},
				{
					"name" : "InformationsBar",
					"type" : "horizontalbar",
					"x" : 17,
					"y" : 34,
					"width" : 120,
					"horizontal_align" : "left",
					"children" :
					(
						{
							"name" : "ChoosePolyMarbleText",
							"type" : "text",
							"x" : 23,
							"y" : 0,
							"text" : "Výbìr kulièky",
						},
					),
				},
				{
					"name" : "MarblesListBar",
					"type" : "slotbar",
					"x" : 17,
					"y" : 54,
					"width" : 119,
					"height" : GLOBAL_HEIGHT - 71,
					"children" :
					(
						{
							"name" : "MarblesListBox",
							"type" : "listboxex",
							"x" : 3,
							"y" : 1,
							"width" : 100,
							"height" : 179,
						},
					),
				},
				{
					"name" : "center_separator",
					"type" : "line",
					"x" : 142,
					"y" : 34,
					"width" : 0,
					"height" : GLOBAL_HEIGHT - 50,
					"color" : 0xffAAA6A1,
				},
				{
					"name" : "SettingsBar",
					"type" : "horizontalbar",
					"x" : 147,
					"y" : 34,
					"width" : 137,
					"horizontal_align" : "left",
					"children" :
					(
						{
							"name" : "SettingsBarText",
							"type" : "text",
							"x" : 45,
							"y" : 0,
							"text" : "Nastavení",
						},
					),
				},
				{
					"name" : "CountOfMarbles",
					"type" : "bar",
					"x" : 147,
					"y" : 54,
					"width" : 137,
					"height" : 50,
					"color" : 0x77000000,
					"children" :
					(
						{
							"name" : "CountText",
							"type":"text",
							"text":"Poèet",
							"x":38,
							"y":8,
							"r":1.0,
							"g":1.0,
							"b":1.0,
							"a":1.0,
						},
						{ 
							"name":"CNT_Minus", 
							"type" : "button", 
							"x":25, 
							"y":27, 
							"default_image" : ROOT_PATH+"btn_minus_up.sub", 
							"over_image" : ROOT_PATH+"btn_minus_over.sub", 
							"down_image" : ROOT_PATH+"btn_minus_down.sub", 
						},
						{
							"name" : "MarbleCountSlot",
							"type" : "image",
							"x" : 41,
							"y" : 24,
							"image" : SMALL_VALUE_SLOT,
							"all_align" : "center",
							"children" :
							(
								{
									"name" : "MarbleCount",
									"type":"text",
									"text":"1",
									"x":0,
									"y":0,
									"r":1.0,
									"g":1.0,
									"b":1.0,
									"a":1.0,
									"all_align" : "center",
								},
							),
						},
						{ 
							"name":"CNT_Plus", 
							"type" : "button", 
							"x":100, 
							"y":28, 
							"default_image" : ROOT_PATH+"btn_plus_up.sub", 
							"over_image" : ROOT_PATH+"btn_plus_over.sub", 
							"down_image" : ROOT_PATH+"btn_plus_down.sub", 
						},
					),
				},
				{
					"name" : "ResumeBarLab",
					"type" : "horizontalbar",
					"x" : 147,
					"y" : 108,
					"width" : 137,
					"horizontal_align" : "left",
					"children" :
					(
						{
							"name" : "ResumeBarLabText",
							"type" : "text",
							"x" : 40,
							"y" : 0,
							"text" : "Výsledek",
						},
					),
				},
				{
					"name" : "ResumeBar",
					"type" : "bar",
					"x" : 147,
					"y" : 124,
					"width" : 137,
					"height" : 30,
					"color" : 0x77000000,
					"children" :
					(
						{
							"name" : "ResumeMarbleValue",
							"type" : "image",
							"x" : 3,
							"y" : 5,
							"image" : XLARGE_VALUE_SLOT,
							"all_align" : "center",
							"children" :
							(
								{
									"name" : "ResumeMarbleName",
									"type":"text",
									"text":"Stray Dog",
									"x":4,
									"y":2,
									"r":1.0,
									"g":1.0,
									"b":1.0,
									"a":1.0,
								},
								{
									"name" : "ResumeMarbleCount",
									"type":"text",
									"text":"1 szt.",
									"x":58,
									"y":0,
									"r":1.0,
									"g":1.0,
									"b":1.0,
									"a":1.0,
									"all_align" : "center",
								},
							),
						},
						{
							"name" : "ResumeMarblePrice",
							"type" : "image",
							"x" : 3,
							"y" : 25,
							"image" : XLARGE_VALUE_SLOT,
							"all_align" : "center",
							"children" :
							(
								{
									"name" : "ResumeMarbleGold",
									"type":"text",
									"text":"1.000.000",
									"x":0,
									"y":1,
									"r":1.0,
									"g":1.0,
									"b":1.0,
									"a":1.0,
									"all_align" : "center",
								},	
							),
						},
					),
				},
				{
					"name" : "BuyButton",
					"type" : "button",
					"x" : 171,
					"y" : GLOBAL_HEIGHT - 28,
					"text" : "Koupit",
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
			),
		},
	),
}
