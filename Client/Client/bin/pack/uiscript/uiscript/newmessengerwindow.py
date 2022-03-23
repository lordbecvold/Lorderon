import uiScriptLocale

BUTTON_START_X_POS = -60
BUTTON_X_STEP = 30
BUTTON_ROOT = "d:/ymir work/ui/public/"
ROOT_PATH = "d:/ymir work/ui/game/windows/"

window = {
	"name" : "MessengerWindow",
	"x" : SCREEN_WIDTH - 360,
	"y" : SCREEN_HEIGHT - 400 - 50,
	"style" : ("movable", "float",),
	"width" : 360,
	"height" : 800,
	"children" :
	(
		{
			"name" : "Messenger_Profile_Board",
			"type" : "board",
			"style" : ("attach",),
			"x" : 161,
			"y" : 30,
			"width" : 190,
			"height" : 130,	
			"children" :
			(
				{
					"name":"Messenger_Profile_Member", "type":"horizontalbar", "x": 3, "y": 37, "width": 180,
					"children" :
					(
						{ "name":"Messenger_Profile_Member_Title", "type":"text", "x":8, "y":3, "text": uiScriptLocale.PROFILE_SEARCH_CONTACT_TITLE, },
					),
				},
				{
					"name" : "Messenger_Profile_Settings_Button",
					"type" : "button",
					"x" : 5,
					"y" : 8,
					"text" : uiScriptLocale.PROFILE_CHANGE_SETTINGS,
					"default_image" : "d:/ymir work/ui/public/XLarge_Button_01.sub",
					"over_image" : "d:/ymir work/ui/public/XLarge_Button_02.sub",
					"down_image" : "d:/ymir work/ui/public/XLarge_Button_03.sub",
				},
				{
					"name" : "Messenger_Profile_Contacts_Online_Icon",
					"type" : "ani_image",
					"x" : 15,
					"y" : 60,
					"width"  : 40,
					"height" : 40,
					"delay" : 25,
					"images" :
					(
						"d:/ymir work/ui/game/profile/messenger_list_online_1.tga",
						"d:/ymir work/ui/game/profile/messenger_list_online_2.tga",
						"d:/ymir work/ui/game/profile/messenger_list_online_3.tga",
						"d:/ymir work/ui/game/profile/messenger_list_online_4.tga",
						"d:/ymir work/ui/game/profile/messenger_list_online_5.tga",
					),
					"children" :
					(
						{"name": "Messenger_Profile_Contacts_Online_Value", "type": "text", "x": 20, "y": 0, "text": ""},
					),
				},
				{
					"name" : "Messenger_Profile_Contacts_Offline_Icon",
					"type" : "image",
					"x" : 15,
					"y" : 80,
					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
					"children" :
					(
						{"name": "Messenger_Profile_Contacts_Offline_Value", "type": "text", "x": 20, "y": 0, "text": ""},
					),
				},
				{
					"name" : "Messenger_Profile_Input_Search_Bar",
					"type" : "slotbar",
					"x" : 48,
					"y" : 100,
					"width" : 130,
					"height" : 20,
					"children" :
					(
						{"name": "Messenger_Profile_Input_Search_Info", "type": "text", "x": - 37, "y": 3, "text": uiScriptLocale.PROFILE_SEARCH_CONTACT_NAME},
						{"name" : "Messenger_Profile_Input_Search_Value", "type" : "editline", "x" : 5, "y" : 3, "width" : 197, "height" : 17, "input_limit" : 12, "text" : ""},
					),
				},
				{
					"name" : "Messenger_Profile_Input_Search_Result_Bar",
					"type" : "slotbar",
					"x" : 48,
					"y" : 120,
					"width" : 130,
					"height" : 70,
					"children" :
					(
						{
							"name" : "Messenger_Profile_Input_Search_Result_ListBox",
							"type" : "listbox2",
							"x" : 0,
							"y" : 0,
							"row_count" : 8,
							"width" : 130,
							"height" : 200,
						},
					),
				},
			)
		},
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"x" : 0,
			"y" : 0,
			"width" : 0,
			"height" : 800,
			"title" : uiScriptLocale.MESSENGER_TITLE,
		},
		{
			"name" : "ScrollBar",
			"type" : "scrollbar",
			"x" : 27,
			"y" : 40,
			"size" : 100,
			"horizontal_align" : "right",
		},
		{
			"name" : "AddFriendButton",
			"type" : "button",
			"x" : BUTTON_START_X_POS + BUTTON_X_STEP*0,
			"y" : 30,
			"horizontal_align" : "center",
			"vertical_align" : "bottom",
			"tooltip_text" : uiScriptLocale.MESSENGER_ADD_FRIEND,
			"tooltip_x" : 0,
			"tooltip_y" : 35,
			"default_image" : "d:/ymir work/ui/game/windows/messenger_add_friend_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/messenger_add_friend_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/messenger_add_friend_03.sub",
			"disable_image" : "d:/ymir work/ui/game/windows/messenger_add_friend_04.sub",
		},
		{
			"name" : "WhisperButton",
			"type" : "button",
			"x" : BUTTON_START_X_POS + BUTTON_X_STEP*1,
			"y" : 30,
			"horizontal_align" : "center",
			"vertical_align" : "bottom",
			"tooltip_text" : uiScriptLocale.MESSENGER_WHISPER,
			"tooltip_x" : 0,
			"tooltip_y" : 35,
			"default_image" : "d:/ymir work/ui/game/windows/messenger_whisper_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/messenger_whisper_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/messenger_whisper_03.sub",
			"disable_image" : "d:/ymir work/ui/game/windows/messenger_whisper_04.sub",
		},
		{
			"name" : "MobileButton",
			"type" : "button",
			"x" : BUTTON_START_X_POS + BUTTON_X_STEP*2,
			"y" : 30,
			"horizontal_align" : "center",
			"vertical_align" : "bottom",
			"tooltip_text" : uiScriptLocale.MESSENGER_MOBILE,
			"tooltip_x" : 0,
			"tooltip_y" : 35,
			"default_image" : "d:/ymir work/ui/game/windows/messenger_mobile_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/messenger_mobile_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/messenger_mobile_03.sub",
			"disable_image" : "d:/ymir work/ui/game/windows/messenger_mobile_04.sub",
		},
		{
			"name" : "RemoveButton",
			"type" : "button",
			"x" : BUTTON_START_X_POS + BUTTON_X_STEP*3,
			"y" : 30,
			"horizontal_align" : "center",
			"vertical_align" : "bottom",
			"tooltip_text" : uiScriptLocale.MESSENGER_DELETE_FRIEND,
			"tooltip_x" : 0,
			"tooltip_y" : 35,
			"default_image" : "d:/ymir work/ui/game/windows/messenger_delete_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/messenger_delete_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/messenger_delete_03.sub",
			"disable_image" : "d:/ymir work/ui/game/windows/messenger_delete_04.sub",
		},
		{
			"name" : "GuildButton",
			"type" : "button",
			"x" : BUTTON_START_X_POS + BUTTON_X_STEP*4,
			"y" : 30,
			"horizontal_align" : "center",
			"vertical_align" : "bottom",
			"tooltip_text" : uiScriptLocale.MESSENGER_OPEN_GUILD,
			"tooltip_x" : 0,
			"tooltip_y" : 35,
			"default_image" : "d:/ymir work/ui/game/windows/messenger_guild_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/messenger_guild_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/messenger_guild_03.sub",
			"disable_image" : "d:/ymir work/ui/game/windows/messenger_guild_04.sub",
		},
	), 
}
