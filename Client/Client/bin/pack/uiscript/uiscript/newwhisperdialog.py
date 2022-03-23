import uiScriptLocale

ROOT = "d:/ymir work/ui/public/"
SMALL_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_01.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_03.sub"
XLARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_04.sub"
CREATE_BOARD_X = 392
CREATE_BOARD_Y = 212
COLOR_LINE = 0xff5b5e5e
CREATE_BOARD_X2 = 190
CREATE_BOARD_Y2 = 205

window = {
	"name" : "WhisperDialog",
	"style" : ("movable", "float",),
	"x" : SCREEN_WIDTH + 447,
	"y" : 0,
	"width" : 447,
	"height" : 200,
	"children" :
	(
		{
			"name" : "Board_Whisper_Profile",
			"type" : "board",
			"style" : ("attach",),
			"x" : - 167,
			"y" : 15,
			"width" : 190,
			"height" : 205,
			"children" :
			(
				{
					"name" : "Background",
					"type" : "bar",
					"x" : 7,
					"y" : 10,
					"width" : CREATE_BOARD_X2,
					"height" : CREATE_BOARD_Y2-20,
					"color" : 0x000000,
				},
				{ "name" : "LINE_BGCREATE_LEFT", "type" : "line", "x" : 8, "y" : 10, "width" : 0, "height" : CREATE_BOARD_Y2-20, "color" : COLOR_LINE, },
				{ "name" : "LINE_BGCREATE_DOWN", "type" : "line", "x" : 8, "y" : CREATE_BOARD_Y2-10, "width" : CREATE_BOARD_X2-17, "height" : 0, "color" : COLOR_LINE, },
				{ "name" : "LINE_BGCREATE_UP", "type" : "line", "x" : 8, "y" : 10, "width" : CREATE_BOARD_X2-17, "height" : 0, "color" : COLOR_LINE, },
				{
					"name" : "Whisper_Profile",
					"type" : "window",
					"x" : 9,
					"y" : 10,
					"width" : 0,
					"height" : 0,
					"children" :
					(
						{
							"name" : "Whisper_Profile_Photo",
							"type" : "slotbar",
							"x" : 3,
							"y" : 5,
							"width" : 50,
							"height" : 48,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Photo_Icon",
									"type" : "expanded_image",
									"style" : ("attach",),
									"x" : 0,
									"y" : 3,
									"horizontal_align" : "center",
									"image" : "icon/face/warrior_m.tga",
								},	
							),
						},
						{ "name" : "LINE_UNDERCOVER_A", "type":"image", "x" : 52, "y" : 5, "image" : "d:/ymir work/ui/game/profile/bar.tga", },
						{ "name" : "LINE_UNDERCOVER_B", "type":"image", "x" : 52, "y" : 5 + 27, "image" : "d:/ymir work/ui/game/profile/bar.tga", },
						{"name": "Whisper_Profile_Empire_Title", "type" : "text", "x" : 60, "y" : 7, "text" : "Zem"},
						{
							"name" : "Whisper_Profile_Empire",
							"type" : "slotbar",
							"x" : 125,
							"y" : 7,
							"width" : 19,
							"height" : 16,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Empire_Icon",
									"type" : "expanded_image",
									"style" : ("attach",),
									"x" : 2,
									"y" : 2,
									"image" : "d:/ymir work/ui/game/profile/empire_a_256.dds",
								},	
							),
						},
						{"name": "Whisper_Profile_Language_Title", "type" : "text", "x" : 60, "y" : 35, "text" : uiScriptLocale.PROFILE_LANGUAGE},
						{
							"name" : "Whisper_Profile_Language",
							"type" : "slotbar",
							"x" : 125,
							"y" : 35,
							"width" : 19,
							"height" : 16,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Language_Icon",
									"type" : "expanded_image",
									"style" : ("attach",),
									"x" : 1,
									"y" : 2,
									"image" : "d:/ymir work/ui/flag/en.tga",
								},	
							),
						},
						{
							"name" : "Whisper_Profile_Name", "type" : "text", "x" : 5, "y" : 65, "text" : uiScriptLocale.PROFILE_NAME,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Name_Slot",
									"type" : "image",
									"x" : 60,
									"y" : -2,
									"image" : LARGE_VALUE_FILE,
									"children" :
									(
										{"name" : "Whisper_Profile_Name_Value", "type": "text", "text": "", "x": 0, "y": 0, "all_align": "center"},
									),
								},
							),
						},
						{
							"name" : "Whisper_Profile_Level", "type" : "text", "x" : 5, "y" : 85, "text" : uiScriptLocale.PROFILE_LEVEL,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Level_Slot",
									"type" : "image",
									"x" : 60,
									"y" : -2,
									"image" : LARGE_VALUE_FILE,
									"children" :
									(
										{"name" : "Whisper_Profile_Level_Value", "type": "text", "text": "", "x": 0, "y": 0, "all_align": "center"},
									),
								},
							),
						},
						{
							"name" : "Whisper_Profile_Guild", "type" : "text", "x" : 5, "y" : 105, "text" : uiScriptLocale.PROFILE_GUILD,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Guild_Slot",
									"type" : "image",
									"x" : 60,
									"y" : -2,
									"image" : LARGE_VALUE_FILE,
									"children" :
									(
										{"name" : "Whisper_Profile_Guild_Value", "type":"text", "text": "", "x":0, "y":0, "all_align": "center"},
									),
								},
							),
						},
						{
							"name" : "Whisper_Profile_Status", "type" : "text", "x" : 5, "y" : 125, "text" : uiScriptLocale.PROFILE_STATUS,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Status_Slot",
									"type" : "image",
									"x" : 60,
									"y" : -2,
									"image" : LARGE_VALUE_FILE,
									"children" :
									(
										{"name" : "Whisper_Profile_Status_Value", "type": "text", "text": "", "x": 2, "y": 1, "text_horizontal_align" : "left"},
									),
								},
							),
						},
						{
							"name" : "Whisper_Profile_Birthday", "type" : "text", "x" : 5, "y" : 145, "text" : uiScriptLocale.PROFILE_BIRTHDAY,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Birthday_Slot",
									"type" : "image",
									"x" : 60,
									"y" : -2,
									"image" : LARGE_VALUE_FILE,
									"children" :
									(
										{"name" : "Whisper_Profile_Birthday_Value", "type":"text", "text": "", "x":0, "y":0, "all_align": "center"},
									),
								},
							),
						},
						{
							"name" : "Whisper_Profile_Location", "type" : "text", "x" : 5, "y" : 165, "text" : uiScriptLocale.PROFILE_LOCATION,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Location_Slot",
									"type" : "image",
									"x" : 60,
									"y" : -2,
									"image" : LARGE_VALUE_FILE,
									"children" :
									(
										{"name" : "Whisper_Profile_Location_Value", "type":"text", "text": "", "x":2, "y":0, "all_align": "center"},
									),
								},
							),
						},
					),
				},
			)
		},
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : 280,
			"height" : 200,
			"title" : uiScriptLocale.MESSENGER_WHISPER,
			"children" :
			(	
				{
					"name" : "gamemastermark",
					"type" : "expanded_image",
					"style" : ("attach",),
					"x" : 330,
					"y" : 37,
					"x_scale" : 0.2,
					"y_scale" : 0.2,
					"image" : LOCALE_PATH + "/effect/ymirred.tga",
				},
				{
					"name" : "minimizebutton",
					"type" : "button",
					"x" : 280 - 47,
					"y" : 8,
					"tooltip_text" : uiScriptLocale.MINIMIZE,
					"default_image" : "d:/ymir work/ui/public/minimize_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/minimize_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/minimize_button_03.sub",
				},
				{
					"name" : "scrollbar",
					"type" : "scrollbar",
					"x" : 280 - 25,
					"y" : 35,
					"size" : 280 - 160,
				},
				{
					"name" : "editbar",
					"type" : "bar",
					"x" : 10,
					"y" : 200 - 60,
					"width" : 280 - 18,
					"height" : 50,
					"color" : 0x77000000,
					"children" :
					(
						{
							"name" : "chatline",
							"type" : "editline",
							"x" : 5,
							"y" : 5,
							"width" : 280 - 70,
							"height" : 40,
							"with_codepage" : 1,
							"input_limit" : 40,
							"limit_width" : 280 - 90,
							"multi_line" : 1,
						},
						{
							"name" : "sendbutton",
							"type" : "button",
							"x" : 280 - 80,
							"y" : 10,
							"text" : uiScriptLocale.WHISPER_SEND,
							"default_image" : "d:/ymir work/ui/public/xlarge_thin_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/xlarge_thin_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/xlarge_thin_button_03.sub",
						},
					),
				},
			),
		},
		{ "name" : "LINE_BGCREATE_LEFT", "type" : "line", "x" : 8, "y" : 30, "width" : 0, "height" : CREATE_BOARD_Y-40, "color" : COLOR_LINE, },
		{ "name" : "LINE_BGCREATE_RIGHT", "type" : "line", "x" : CREATE_BOARD_X-10, "y" : 30, "width" : 0, "height" : CREATE_BOARD_Y-40, "color" : COLOR_LINE, },
		{ "name" : "LINE_BGCREATE_DOWN", "type" : "line", "x" : 8, "y" : CREATE_BOARD_Y-10, "width" : CREATE_BOARD_X-17, "height" : 0, "color" : COLOR_LINE, },
		{ "name" : "LINE_BGCREATE_UP", "type" : "line", "x" : 8, "y" : 30, "width" : CREATE_BOARD_X-17, "height" : 0, "color" : COLOR_LINE, },
		{ "name" : "LINE_BGCREATE_LEFT", "type" : "line", "x" : 12, "y" : 34, "width" : 0, "height" : CREATE_BOARD_Y-48, "color" : COLOR_LINE, },
		{ "name" : "LINE_BGCREATE_RIGHT", "type" : "line", "x" : CREATE_BOARD_X-14, "y" : 34, "width" : 0, "height" : CREATE_BOARD_Y-48, "color" : COLOR_LINE, },
		{ "name" : "LINE_BGCREATE_DOWN", "type" : "line", "x" : 12, "y" : CREATE_BOARD_Y-14, "width" : CREATE_BOARD_X-25, "height" : 0, "color" : COLOR_LINE, },
		{ "name" : "LINE_BGCREATE_UP", "type" : "line", "x" : 12, "y" : 34, "width" : CREATE_BOARD_X-25, "height" : 0, "color" : COLOR_LINE, },
		{
			"name" : "Background",
			"type" : "bar",
			"x" : 7,
			"y" : 31,
			"width" : CREATE_BOARD_X-15,
			"height" : CREATE_BOARD_Y-39,
			"color" : 0x000000,
		},
				{
					"name" : "titlename_editBar",
					"type" : "image",
					"style" : ("attach",),
					"x" : 14,
					"y" : 40,
					"image":"d:/ymir work/ui/public/Parameter_Slot_05.sub",
					"children" :
					(
						{
							"name" : "titlename_edit",
							"type" : "editline",
							"x" : 3,
							"y" : 3,
							"width" : 120,
							"height" : 17,
							"input_limit" : PLAYER_NAME_MAX_LEN,
							"text" : uiScriptLocale.WHISPER_NAME,
						},
					),
				},
				{
					"name" : "acceptbutton",
					"type" : "button",

					"x" : 14 + 135,
					"y" : 40,

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/small_thin_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_thin_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_thin_button_03.sub",
				},
	),
}
