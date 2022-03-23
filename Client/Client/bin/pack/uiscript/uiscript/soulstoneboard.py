#Lorderon Client Dev By Lordbecvold
import uiScriptLocale

BOARD_WIDTH = 250
BOARD_HEIGHT = 35 + 32 + 10 + 32 + 10 + 25 + 15

window = {
	"name" : "SoulStoneBoard",

	"x" : SCREEN_WIDTH / 2 - BOARD_WIDTH / 2,
	"y" : SCREEN_HEIGHT / 2 - BOARD_HEIGHT / 2,

	"style" : ("movable", "float",),

	"width"  : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),
			
			"x" : 0,
			"y" : 0,
			
			"width"  : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
			"title" : uiScriptLocale.SOUL_STONE_TITLE,

			"children" :
			(
				{
					"name" : "stone_slot",
					"type" : "slot",

					"x" : 10,
					"y" : 35,

					"width" : 32,
					"height" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",

					"horizontal_align" : "center",

					"slot" : (
						{"index":0, "x":0, "y":0, "width":32, "height":32},
					),
				},
				{
					"name" : "skill_slot",
					"type" : "slot",

					"x" : 10,
					"y" : 40 + 32 + 10,

					"width" : 32 * 6 + 5 * (6 - 1),
					"height" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",

					"horizontal_align" : "center",

					"slot" : (
						{"index":0, "x":37*0, "y":0, "width":32, "height":32},
						{"index":1, "x":37*1, "y":0, "width":32, "height":32},
						{"index":2, "x":37*2, "y":0, "width":32, "height":32},
						{"index":3, "x":37*3, "y":0, "width":32, "height":32},
						{"index":4, "x":37*4, "y":0, "width":32, "height":32},
						{"index":5, "x":37*5, "y":0, "width":32, "height":32},
					),
				},
				{
					"name" : "button_single",
					"type" : "button",

					"x" : BOARD_WIDTH / 4 * 1 - 88 / 2,
					"y" : 35 + 32 + 10 + 32 + 10,

					"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",

					"text" : uiScriptLocale.SOUL_STONE_BUTTON_SINGLE,
				},
				{
					"name" : "button_all",
					"type" : "button",

					"x" : BOARD_WIDTH / 4 * 3 - 88 / 2,
					"y" : 35 + 32 + 10 + 32 + 10,

					"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",

					"text" : uiScriptLocale.SOUL_STONE_BUTTON_ALL,
				},
			),
		},
	),
}
