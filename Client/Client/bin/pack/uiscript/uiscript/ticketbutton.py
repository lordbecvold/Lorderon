#Lorderon Client Dev By Lordbecvold
import uiScriptLocale, localeInfo

PATH = "d:/ymir work/ui/public/ticketsystem/"
window = {
	"name" : "TicketWindow",
	"x" : SCREEN_WIDTH - 136 - 100,
	"y" : 15,
	"width" : 100,
	"height" : 58,
	"children" :
	(
		{
			"name" : "ticket_window",
			"type" : "window",
			"x" : 0,
			"y" : 0,
			"width" : 100,
			"height" : 58,
			
			"children" :
			(
				{
					"name" : "ticket_button",
					"type" : "button",
					"x" : 0,
					"y" : 0,
					"tooltip_text" : "|cff29f6d2" + localeInfo.TICKET_BUTTON_DESC,
					"tooltip_x" : -6,
					"tooltip_y" : 40,
					
					"default_image" : PATH + "ticket_button_1.tga",
					"over_image" : PATH + "ticket_button_2.tga",
					"down_image" : PATH + "ticket_button_3.tga",
				},
			),
		},		
	),	
}
