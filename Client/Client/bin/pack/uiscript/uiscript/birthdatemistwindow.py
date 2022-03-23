#Lorderon Client Dev by Lordbecvold
import uiScriptLocale

window = {
	"name" : "SettingsProfileWindow",
	"x" : SCREEN_WIDTH - 170,
	"y" : SCREEN_HEIGHT - 180 - 50,
	"style" : ("float",),
	"width" : 170,
	"height" : 180,
	"children" :
	(
		{
			"name" : "board",
			"type" : "slotbar",
			"x" : 0,
			"y" : 0,
			"width" : 60,
			"height" : 185,
		},
		{
			"name" : "ScrollBar",
			"type" : "scrollbar",
			"x" : 125,
			"y" : 3,
			"size" : 180,
		},
	)
}
