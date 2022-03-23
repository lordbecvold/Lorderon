#Lorderon Client Dev by Lordbecvold
import uiScriptLocale
window = {
	"name" : "SelectCharacterWindow",
	"x" : 0,
	"y" : 0,
	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,
	"children" :
	(
		{
			"name" : "Background",
			"type" : "expanded_image",
			"x" : 0,
			"y" : 0,
			"horizontal_align" : "center",
			"vertical_align" : "center",
			"image" : "twix_work/loginwindow/background.tga",
			"x_scale" : float(SCREEN_WIDTH) / 1366.0,
			"y_scale" : float(SCREEN_HEIGHT) / 768.0,
			"children" :
			(
				{
					"name" : "Ascalon",
					"type" : "expanded_image",
					"x" : -250,
					"y" : 0,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"image" : "twix_work/selectempirewindow/mildos_0.tga",
				},
				{
					"name" : "Mildos",
					"type" : "expanded_image",
					"x" : 250,
					"y" : 0,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"image" : "twix_work/selectempirewindow/ascalon_0.tga",
				},
			),
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
}
