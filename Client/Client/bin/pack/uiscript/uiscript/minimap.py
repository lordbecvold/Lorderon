#Lorderon Client Dev By Lordbecvold
ROOT = "d:/ymir work/ui/minimap/"

window = {
	"name" : "MiniMap",
	"x" : SCREEN_WIDTH - 136,
	"y" : 0,
	"width" : 136,
	"height" : 137,
	"children" :
	(
		{
			"name" : "OpenWindow",
			"type" : "window",
			"x" : 0,
			"y" : 0,
			"width" : 136,
			"height" : 137,
			"children" :
			(
				{
					"name" : "OpenWindowBGI",
					"type" : "image",
					"x" : 0,
					"y" : 0,
					"image" : ROOT + "minimap.sub",
				},
				{
					"name" : "MiniMapWindow",
					"type" : "window",
					"x" : 4,
					"y" : 5,
					"width" : 128,
					"height" : 128,
				},
				{
					"name" : "ScaleUpButton",
					"type" : "button",
					"x" : 101,
					"y" : 116,
					"default_image" : ROOT + "minimap_scaleup_default.sub",
					"over_image" : ROOT + "minimap_scaleup_over.sub",
					"down_image" : ROOT + "minimap_scaleup_down.sub",
				},
				{
					"name" : "ScaleDownButton",
					"type" : "button",

					"x" : 115,
					"y" : 103,

					"default_image" : ROOT + "minimap_scaledown_default.sub",
					"over_image" : ROOT + "minimap_scaledown_over.sub",
					"down_image" : ROOT + "minimap_scaledown_down.sub",
				},
				{
					"name" : "MiniMapHideButton",
					"type" : "button",
					"x" : 111,
					"y" : 6,
					"default_image" : ROOT + "minimap_close_default.sub",
					"over_image" : ROOT + "minimap_close_over.sub",
					"down_image" : ROOT + "minimap_close_down.sub",
				},
				{
					"name" : "AtlasShowButton",
					"type" : "button",
					"x" : 12,
					"y" : 12,

					"default_image" : ROOT + "atlas_open_default.sub",
					"over_image" : ROOT + "atlas_open_over.sub",
					"down_image" : ROOT + "atlas_open_down.sub",
				},
				{
					"name" : "ServerInfo",
					"type" : "text",
					"text_horizontal_align" : "center",
					"outline" : 1,
					"x" : 70,
					"y" : 140,
					"text" : "",
				},
				{
					"name" : "PositionInfo",
					"type" : "text",
					"text_horizontal_align" : "center",
					"outline" : 1,
					"x" : 70,
					"y" : 160,
					"text" : "",
				},
				{
					"name" : "ObserverCount",
					"type" : "text",
					"text_horizontal_align" : "center",
					"outline" : 1,
					"x" : 70,
					"y" : 180,
					"text" : "",
				},
			),
		},
		{
			"name" : "CloseWindow",
			"type" : "window",
			"x" : 0,
			"y" : 0,
			"width" : 132,
			"height" : 48,
			"children" :
			(
				{
					"name" : "MiniMapShowButton",
					"type" : "button",
					"x" : 100,
					"y" : 4,
					"default_image" : ROOT + "minimap_open_default.sub",
					"over_image" : ROOT + "minimap_open_default.sub",
					"down_image" : ROOT + "minimap_open_default.sub",
				},
			),
		},
	),
}
