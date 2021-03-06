#Lorderon Client Dev By Lordbecvold
import uiScriptLocale

TEXT_Y = 8
TEXT_GAP = 30
WIDTH_GAP = 6
THINBOARD_X = WIDTH_GAP*3 + 32
THINBOARD_Y = 50
THINBOARD_WIDTH = 192
THINBOARD_HEIGHT = (5*TEXT_GAP) + (2*TEXT_Y)
SIZE_X = 334
SIZE_Y = 255

window = {
	"name" : "SelectAttrWindow",
	"style" : ("movable", "float",),
	"x" : (SCREEN_WIDTH/2) - (SIZE_X/2),
	"y" : (SCREEN_HEIGHT/2) - (SIZE_Y/2),	
	"width" : SIZE_X,
	"height" : SIZE_Y,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : SIZE_X,
			"height" : SIZE_Y,
			"children" :
			(
				{
					"name" : "SelectAttr_TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 6,
					"y" : 7,
					"width" : SIZE_X - 13,
					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"text": uiScriptLocale.SELECT_SECOND_ATTR_TITLE,
							"all_align":"center"
						},
					),
				},
				{
					"name" : "toolTipItem_Slot_Area",
					"type" : "window",
					"style" : ("attach",),
					"x" : WIDTH_GAP*2,
					"y" : THINBOARD_Y,
					"width" : 32,
					"height" : 96,
					"children" :
					(
						{
							"name" : "toolTipItemSlot",
							"type" : "grid_table",
							"x" : 0,
							"y" : 0,
							"start_index" : 0,
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,
							"image" : "d:/ymir work/ui/public/Slot_Base.sub"
						},
					),
				},
				{
					"name" : "left_black_board",
					"type" : "thinboard",
					"x" : THINBOARD_X,
					"y" : THINBOARD_Y,
					"width" : THINBOARD_WIDTH,
					"height" : THINBOARD_HEIGHT,
					"children" :
					(
						{
							"name" : "lTitle",
							"type" : "text",
							"x" : THINBOARD_WIDTH/2,
							"y" : -17,
							"text" : uiScriptLocale.SELECT_SECOND_ATTR_CURRENT,
							"text_horizontal_align" : "center",
						},
						{
							"name" : "lText0",
							"type" : "text",
							"x" : THINBOARD_WIDTH/2,
							"y" : TEXT_Y,
							"text" : "Hello",
							"text_horizontal_align" : "center",
							"color" : 0xFF777777,
						},
						{
							"name" : "lText1",
							"type" : "text",
							"x" : THINBOARD_WIDTH/2,
							"y" : TEXT_Y + TEXT_GAP,
							"text" : "Hello",
							"text_horizontal_align" : "center",
							"color" : 0xFF777777,
						},
						{
							"name" : "lText2",
							"type" : "text",
							"x" : THINBOARD_WIDTH/2,
							"y" : TEXT_Y + TEXT_GAP * 2,
							"text" : "Hello",
							"text_horizontal_align" : "center",
							"color" : 0xFF777777,
						},
						{
							"name" : "lText3",
							"type" : "text",
							"x" : THINBOARD_WIDTH/2,
							"y" : TEXT_Y + TEXT_GAP * 3,
							"text" : "Hello",
							"text_horizontal_align" : "center",
							"color" : 0xFF777777,
						},
						{
							"name" : "lText4",
							"type" : "text",
							"x" : THINBOARD_WIDTH/2,
							"y" : TEXT_Y + TEXT_GAP * 4,
							"text" : "Hello",
							"text_horizontal_align" : "center",
							"color" : 0xFF777777,
						},
					),
				},
				{
					"name" : "BlockBtn1",
					"type" : "radio_button",
					"x" : THINBOARD_WIDTH + 5 + THINBOARD_X,
					"y" : TEXT_Y + TEXT_GAP + TEXT_Y + 10,
					"text" : uiScriptLocale.SELECT_SECOND_ATTR_BLOCK,
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "BlockBtn2",
					"type" : "radio_button",
					"x" : THINBOARD_WIDTH + 5 + THINBOARD_X,
					"y" : TEXT_Y + TEXT_GAP * 2 + TEXT_Y + 10,
					"text" : uiScriptLocale.SELECT_SECOND_ATTR_BLOCK,
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "BlockBtn3",
					"type" : "radio_button",
					"x" : THINBOARD_WIDTH + 5 + THINBOARD_X,
					"y" : TEXT_Y + TEXT_GAP * 3 + TEXT_Y + 10,
					"text" : uiScriptLocale.SELECT_SECOND_ATTR_BLOCK,
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "BlockBtn4",
					"type" : "radio_button",
					"x" : THINBOARD_WIDTH + 5 + THINBOARD_X,
					"y" : TEXT_Y + TEXT_GAP * 4 + TEXT_Y + 10,
					"text" : uiScriptLocale.SELECT_SECOND_ATTR_BLOCK,
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "BlockBtn5",
					"type" : "radio_button",
					"x" : THINBOARD_WIDTH + 5 + THINBOARD_X,
					"y" : TEXT_Y + TEXT_GAP * 5 + TEXT_Y + 10,
					"text" : uiScriptLocale.SELECT_SECOND_ATTR_BLOCK,
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "accept_button",
					"type" : "button",
					"x" : SIZE_X - 100,
					"y" : SIZE_Y - 31,
					"text" : uiScriptLocale.OK,
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
			),				
		},
	),
}
