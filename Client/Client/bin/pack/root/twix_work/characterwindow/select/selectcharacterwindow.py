#Lorderon Client Dev by Lordbecvold
import uiScriptLocale
window = {
	"name" : "selectcharacterwindow",
	"x" : 0, 
	"y" : 0,
	"width" : SCREEN_WIDTH,	
	"height" : SCREEN_HEIGHT,	
	"children" : 
	(
		{
			"name" : "BackGround",
			"type" : "expanded_image",
			"x" : 0, 
			"y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1366.0,
			"y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"image" : "twix_work/characterwindow/background.tga",
			"children" : 
			(
				{
					"name" : "board_main",
					"type" : "window",
					"x" : 0, 
					"y" : 0,
					"width" : 352, 
					"height" : 457,
					"vertical_align" : "center",
					"horizontal_align" : "left",
					"children" :
					(
						{
							"name" : "board",
							"type" : "image",
							"x" : 100,
							"y" : 0,
							"vertical_align" : "center",
							"horizontal_align" : "left",
							"image" : "twix_work/characterwindow/select/board.tga",
							"children" : 
							(
								{
									"name" : "name_slotbar",
									"type" : "image",
									"x" : 0, 
									"y" : -97,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"image" : "twix_work/characterwindow/select/slotbar.tga",
									"children" : 
									(
										{
											"name" : "name",
											"type" : "text",
											"x" : 0, 
											"y" : 0,
											"color" : 0xffccb3ad,
											"all_align" : True,
										},
									),
								},
								{
									"name" : "guild_slotbar",
									"type" : "image",
									"x" : 0, 
									"y" : -47,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"image" : "twix_work/characterwindow/select/slotbar.tga",
									"children" : 
									(
										{
											"name" : "guild",
											"type" : "text",
											"x" : 0, 
											"y" : 0,
											"color" : 0xffccb3ad,
											"all_align" : True,
										},
									),
								},
								{
									"name" : "level_slotbar",
									"type" : "image",
									"x" : 0, 
									"y" : 2,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"image" : "twix_work/characterwindow/select/slotbar.tga",
									"children" : 
									(
										{
											"name" : "level",
											"type" : "text",
											"x" : 0, 
											"y" : 0,
											"color" : 0xffccb3ad,
											"all_align" : True,
										},
									),
								},
								{
									"name" : "playtime_slotbar",
									"type" : "image",
									"x" : 0, 
									"y" : 53,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"image" : "twix_work/characterwindow/select/slotbar.tga",
									"children" : 
									(
										{
											"name" : "playtime",
											"type" : "text",
											"x" : 0, 
											"y" : 0,
											"color" : 0xffccb3ad,
											"all_align" : True,
										},
									),
								},
								{
									"name" : "empire_slotbar",
									"type" : "image",
									"x" : 0, 
									"y" : 103,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"image" : "twix_work/characterwindow/select/slotbar.tga",
									"children" : 
									(
										{
											"name" : "empire",
											"type" : "text",
											"x" : 0, 
											"y" : 0,
											"color" : 0xffccb3ad,
											"all_align" : True,
										},
									),
								},
								{
									"name" : "delete_button",
									"type" : "button",
									"x" : 50, 
									"y" : 145,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"default_image" : "twix_work/characterwindow/select/button_0.tga",
									"over_image" : "twix_work/characterwindow/select/button_1.tga",
									"down_image" : "twix_work/characterwindow/select/button_2.tga",
									"children" : 
									(
										{
											"name" : "delete_text",
											"type" : "text",
											"x" : 27, 
											"y" : 7,
											"text" : uiScriptLocale.SELECT_DELETE,
											"color" : 0xffe8b478,
										},
									),
								},
								{
									"name" : "select_button",
									"type" : "button",
									"x" : -50, 
									"y" : 145,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"default_image" : "twix_work/characterwindow/select/button_0.tga",
									"over_image" : "twix_work/characterwindow/select/button_1.tga",
									"down_image" : "twix_work/characterwindow/select/button_2.tga",
									"children" : 
									(
										{
											"name" : "select_text",
											"type" : "text",
											"x" : 30, 
											"y" : 7,
											"text" : uiScriptLocale.SELECT_SELECT,
											"color" : 0xffe8b478,
										},
									),
								},
								{
									"name" : "create_button",
									"type" : "button",
									"x" : -50, 
									"y" : 145,
									"vertical_align" : "center",
									"horizontal_align" : "center",
									"default_image" : "twix_work/characterwindow/select/button_0.tga",
									"over_image" : "twix_work/characterwindow/select/button_1.tga",
									"down_image" : "twix_work/characterwindow/select/button_2.tga",
									"children" : 
									(
										{
											"name" : "create_text",
											"type" : "text",
											"x" : 27, 
											"y" : 7,
											"text" : uiScriptLocale.SELECT_CREATE,
											"color" : 0xffe8b478,
										},
									),
								},
							),
						},
					),
				},
				{
					"name" : "left_button",
					"type" : "button",
					"x" : -180, 
					"y" : 130,
					"vertical_align" : "center",
					"horizontal_align" : "center",
					"default_image" : "twix_work/characterwindow/select/left_0.tga",
					"over_image" : "twix_work/characterwindow/select/left_1.tga",
					"down_image" : "twix_work/characterwindow/select/left_2.tga",
				},
				{
					"name" : "right_button",
					"type" : "button",
					"x" : 240, 
					"y" : 130,
					"vertical_align" : "center",
					"horizontal_align" : "center",
					"default_image" : "twix_work/characterwindow/select/right_0.tga",
					"over_image" : "twix_work/characterwindow/select/right_1.tga",
					"down_image" : "twix_work/characterwindow/select/right_2.tga",
				},
				{
					"name" : "exit_button",
					"type" : "button",
					"x" : SCREEN_WIDTH - 110, 
					"y" : 10,
					"default_image" : "twix_work/loginwindow/button_0.tga",
					"over_image" :  "twix_work/loginwindow/button_1.tga",
					"down_image" : "twix_work/loginwindow/button_2.tga",
					"children" : 
					(
						{
							"name" : "exit_text",
							"type" : "text",
							"x" : 36, 
							"y" : 7,
							"text" : uiScriptLocale.LOGIN_EXIT,
							"color" : 0xffe8b478,
						},
					),
				},
			),
		},
	),
}
