import uiScriptLocale
CREATE_BOARD_X = 255
CREATE_BOARD_Y = 150
COLOR_LINE = 0xff5b5e5e
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_03.sub"
XLARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_04.sub"

window = {
	"name" : "SettingsProfileWindow",
	"x" : SCREEN_WIDTH - SCREEN_WIDTH + 400,
	"y" : SCREEN_HEIGHT - CREATE_BOARD_Y,
	"style" : ("float",),
	"width" : CREATE_BOARD_X,
	"height" : CREATE_BOARD_Y,
	"children" :
	(

		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"x" : 0,
			"y" : 0,
			"width" : CREATE_BOARD_X,
			"height" : CREATE_BOARD_Y,
			"title" : "Profile Settings",
		},
		
		{ "name" : "LINE_BGCREATE_LEFT", "type" : "line", "x" : 8, "y" : 30, "width" : 0, "height" : CREATE_BOARD_Y-40, "color" : COLOR_LINE, },
		{ "name" : "LINE_BGCREATE_RIGHT", "type" : "line", "x" : CREATE_BOARD_X-10, "y" : 30, "width" : 0, "height" : CREATE_BOARD_Y-40, "color" : COLOR_LINE, },
		{ "name" : "LINE_BGCREATE_DOWN", "type" : "line", "x" : 8, "y" : CREATE_BOARD_Y-10, "width" : CREATE_BOARD_X-17, "height" : 0, "color" : COLOR_LINE, },
		{ "name" : "LINE_BGCREATE_UP", "type" : "line", "x" : 8, "y" : 30, "width" : CREATE_BOARD_X-17, "height" : 0, "color" : COLOR_LINE, },
		{ "name" : "LINE_UNDERCOVER_A", "type":"image", "x" : 60, "y" : 37, "image" : "d:/ymir work/ui/game/profile/bar.tga", },
		{ "name" : "LINE_UNDERCOVER_B", "type":"image", "x" : 60, "y" : 64, "image" : "d:/ymir work/ui/game/profile/bar.tga", },
		
		{
			"name" : "CharacterIcon_Bar",
			"type" : "slotbar",
			"x" : 12,
			"y" : 35,
			"width" : 50,
			"height" : 48,
			"children" :
			(
				{
					"name" : "CharacterIcon",
					"type" : "expanded_image",
					"style" : ("attach",),
					"x" : 0,
					"y" : 3,
					"horizontal_align" : "center",
					"image" : "icon/face/warrior_m.tga",
				},	
			),
		},
						
		{
			"name" : "CharacterStatus_Title", "type" : "text", "x" : 67, "y" : 67, "text" : uiScriptLocale.PROFILE_STATUS,
			"children" :
			(
				{
					"name" : "CharacterStatus_Bar",
					"type" : "image",
					"x" : 60,
					"y" : -2,
					"image" : XLARGE_VALUE_FILE,
					"children" :
					(
					),
				},
			),
		},

		{
			"name" : "ChangeStatusButton",
			"type" : "button",
			"x" : 221,
			"y" : 63,
			"tooltip_text" : uiScriptLocale.PROFILE_CHANGE_STATUS,
			"tooltip_x" : 55,
			"tooltip_y" : 0,
			"default_image" : "d:/ymir work/ui/game/profile/btn_edit_01.tga",
			"over_image" : "d:/ymir work/ui/game/profile/btn_edit_02.tga",
			"down_image" : "d:/ymir work/ui/game/profile/btn_edit_03.tga",
		},
		
		{"name" : "CharacterStatus", "type" : "editline", "x" : 131, "y" : 66, "width" : 100, "height" : 20, "input_limit" : 20, "text" : ""},
		{ "name" : "CharacterName", "type" : "text", "x" : 67, "y" : 40, "text" : ""},
	)
}
