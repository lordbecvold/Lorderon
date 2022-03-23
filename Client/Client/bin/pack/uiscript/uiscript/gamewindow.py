#Lorderon Client Dev By Lordbecvold
import uiScriptLocale
import localeInfo

window = {
	"name" : "GameWindow",
	"style" : ("not_pick",),
	"x" : 0,
	"y" : 0,
	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,
	"children" :
	(
		{ 
			"name":"HelpButton", 
			"type":"button", 
			"x" : 80,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",
			"children" : 
			(
				{ 
					"name":"HelpButtonLabel", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text":uiScriptLocale.GAME_HELP, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},
			),
		},
		{ 
			"name":"QuestButton", 
			"type":"button", 
			"x" : SCREEN_WIDTH-50-32,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",
			"children" : 
			(
				{ 
					"name":"QuestButtonLabel", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text":uiScriptLocale.GAME_QUEST, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},
			),
		},
		{ 
			"name":"warp_open", "type" : "button",  "x" : SCREEN_WIDTH-32, "y" : SCREEN_HEIGHT-160, "default_image" : "d:/ymir work/ui/game/windows/inel_teleport_1.tga", "over_image" : "d:/ymir work/ui/game/windows/inel_teleport_2.tga", "down_image" : "d:/ymir work/ui/game/windows/inel_teleport_2.tga",
		},
		{ 
			"name":"eq_button", "type" : "button",  "x" : SCREEN_WIDTH-32, "y" : SCREEN_HEIGHT-130, "default_image" : "d:/ymir work/ui/game/windows/pagina_bonusuri_1.tga", "over_image" : "d:/ymir work/ui/game/windows/pagina_bonusuri_2.tga", "down_image" : "d:/ymir work/ui/game/windows/pagina_bonusuri_2.tga",
		},
		{ 
			"name":"special_stor", "type" : "button",  "x" : SCREEN_WIDTH-32, "y" : SCREEN_HEIGHT-100, "default_image" : "d:/ymir work/ui/game/windows/switchbot_1.tga", "over_image" : "d:/ymir work/ui/game/windows/switchbot_2.tga", "down_image" : "d:/ymir work/ui/game/windows/switchbot_2.tga",
		},
		{ 
			"name":"BlockEquipmentButton", "type" : "button",  "x" : SCREEN_WIDTH-32, "y" : SCREEN_HEIGHT-69, "default_image" : "d:/ymir work/ui/game/windows/Party_Exit_01.sub", "over_image" : "d:/ymir work/ui/game/windows/Party_Exit_02.sub", "down_image" : "d:/ymir work/ui/game/windows/Party_Exit_03.sub",
		},
		{
			"name" : "GiftIcon",
			"type" : "button",
			"x" : 5, 
			"y" : SCREEN_HEIGHT-135, 
			"default_image" : "D:/Ymir Work/UI/Pattern/GiftBox/present_for_fruends_icon.tga",
			"over_image" : "D:/Ymir Work/UI/Pattern/GiftBox/present_for_fruends_icon.tga",
			"down_image" : "D:/Ymir Work/UI/Pattern/GiftBox/present_for_fruends_icon.tga",
		},
		{ 
			"name":"StatusPlusButton", 
			"type" : "button", 
			"x" : 80, 
			"y" : SCREEN_HEIGHT-100, 
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",
			"children" :
			(
				{ 
					"name":"StatusPlusLabel", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text":uiScriptLocale.GAME_STAT_UP, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},		
			),
		},	
		{ 
			"name":"SkillPlusButton", 
			"type" : "button", 
			"x" : SCREEN_WIDTH-9999999999999-32,
			"y" : SCREEN_HEIGHT-9999999999999,
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",
			"children" : 
			(
				{ 
					"name":"SkillPlusLabel", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text":uiScriptLocale.GAME_SKILL_UP, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},	
			),
		},		
		{ 
			"name":"ExitObserver", 
			"type" : "button", 
			"x" : SCREEN_WIDTH-50-32,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",
			"children" : 
			(
				{ 
					"name":"ExitObserverButtonName", 
					"type":"text", 
					"x": 16, 
					"y": 40, 
					"text": uiScriptLocale.GAME_EXIT_OBSERVER, 
					"r":1.0, "g":1.0, "b":1.0, "a":1.0, 
					"text_horizontal_align":"center" 
				},	
			),
		},
		{ 
			"name":"BuildGuildBuilding",
			"type" : "button",
			"x" : SCREEN_WIDTH-50-32,
			"y" : SCREEN_HEIGHT-170,
			"default_image" : "d:/ymir work/ui/game/windows/btn_bigplus_up.sub",
			"over_image" : "d:/ymir work/ui/game/windows/btn_bigplus_over.sub",
			"down_image" : "d:/ymir work/ui/game/windows/btn_bigplus_down.sub",
			"children" : 
			(
				{ 
					"name":"BuildGuildBuildingButtonName",
					"type":"text",
					"x": 16,
					"y": 40,
					"text": uiScriptLocale.GUILD_BUILDING_TITLE,
					"r":1.0, "g":1.0, "b":1.0, "a":1.0,
					"text_horizontal_align":"center"
				},	
			),
		},
	),
}
