#Lorderon Client Dev By Lordbecvold
import uiScriptLocale
import localeInfo

LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_05.sub"

window = {
	"name" : "Board",
	"style" : ("movable", "float",),
	"x" : 0,
	"y" : 0,
	"width" : 450,
	"height" : 340,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : 0,
			"height" : 0,
			"children" :
			(
				{
					"name":"HorizontalBar1", "type":"horizontalbar", "x": 10, "y": 35, "width": 220,
					"children" :
					(
						{ "name":"TextLine1", "type":"text", "x": 8, "y":2, "text": localeInfo.LOCALIZATION_HORIZONTALBAR_1, },
					),
				},
				
				{
					"name":"HorizontalBar2", "type":"horizontalbar", "x": 235, "y": 35, "width": 206,
					"children" :
					(
						{ "name":"TextLine2", "type":"text", "x": 8, "y": 2, "text": localeInfo.LOCALIZATION_HORIZONTALBAR_2, },
					),
				},
			),
		},
	),
}
