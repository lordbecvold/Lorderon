#Lorderon Client Dev By Lordbecvold
import uiScriptLocale
 
ROOT = "d:/ymir work/ui/game/"
window = {
        "name" : "ExchangeDialog",
        "x" : 0,
        "y" : 0,
        "style" : ("movable", "float",),
        "width" : 450,
        "height" : 200,
        "children" :
        (
                {
                        "name" : "board",
                        "type" : "board",
                        "style" : ("attach",),
                        "x" : 0,
                        "y" : 0,
                        "width" : 450,
                        "height" : 200,
                        "children" :
                        (
                                {
                                        "name" : "TitleBar",
                                        "type" : "titlebar",
                                        "style" : ("attach",),
                                        "x" : 8,
                                        "y" : 8,
                                        "width" : 434,
                                        "color" : "gray",
                                        "children" :
                                        (
                                                { "name":"TitleName", "type":"text", "x":192, "y":3, "text":uiScriptLocale.EXCHANGE_TITLE, "text_horizontal_align":"center" },
                                        ),
                                },
                                {
                                        "name" : "Middle_Bar",
                                        "type" : "image",
                                        "x" : 200,
                                        "y" : 31,
                                        "image" : ROOT + "windows/middlebar.sub",
                                },
                                {
                                        "name" : "Owner",
                                        "type" : "window",
                                        "x" : 250,
                                        "y" : 33,
                                        "width" : 200,
                                        "height" : 150,
                                        "children" :
                                        (
                                            {
                                                "name" : "Owner_Slot",
                                                "type" : "grid_table",
                                                "start_index" : 0,
                                                "x" : 0,
                                                "y" : 0,
                                                "x_count" : 6,
                                                "y_count" : 4,
                                                "x_step" : 32,
                                                "y_step" : 32,
                                                "x_blank" : 0,
                                                "y_blank" : 0,
                                                "image" : "d:/ymir work/ui/public/slot_base.sub",
                                            },
                                            {
                                                "name" : "Owner_Money",
                                                "type" : "button",
                                                "x" : 0,
                                                "y" : 136, 
                                                "default_image" : "d:/ymir work/ui/public/parameter_slot_02.sub",
                                                "over_image" : "d:/ymir work/ui/public/parameter_slot_02.sub",
                                                "down_image" : "d:/ymir work/ui/public/parameter_slot_02.sub",
                                                    "children" :
                                                        (
                                                            {
                                                                "name" : "Owner_Money_Value",
                                                                "type" : "text",
                                                                "x" : 59,
                                                                "y" : 2,
                                                                "text" : "1234567",
                                                                "text_horizontal_align" : "right",
                                                            },
                                                        ),
                                                },
                                                {
                                                   "name" : "Owner_Accept_Light",
                                                   "type" : "button",
                                                   "x" : 140,
                                                   "y" : 135,
                                                   "default_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub",
                                                   "over_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub",
                                                   "down_image" : "d:/ymir work/ui/game/windows/accept_button_on.sub",
                                                },
                                                {
                                                   "name" : "Owner_Accept_Button",
                                                   "type" : "toggle_button",
                                                   "x" : 140,
                                                   "y" : 135,
                                                   "text" : uiScriptLocale.EXCHANGE_ACCEPT,
                                                   "default_image" : "d:/ymir work/ui/public/small_button_01.sub",
                                                   "over_image" : "d:/ymir work/ui/public/small_button_02.sub",
                                                   "down_image" : "d:/ymir work/ui/public/small_button_03.sub",
                                                },
                                        ),
                                },
                                 {
                                    "name" : "Target",
                                    "type" : "window",
                                    "x" : 10,
                                    "y" : 33,
                                    "width" : 200,
                                    "height" : 150,
                                    "children" :
                                        (
                                            {
                                                "name" : "Target_Slot",
                                                "type" : "grid_table",
                                                "start_index" : 0,
                                                "x" : 0,
                                                "y" : 0,
                                                "x_count" : 6,
                                                "y_count" : 4,
                                                "x_step" : 32,
                                                "y_step" : 32,
                                                "x_blank" : 0,
                                                "y_blank" : 0,
                                                "image" : "d:/ymir work/ui/public/slot_base.sub",
                                                },
                                                {
                                                "name" : "Target_Money",
                                                "type" : "image",
                                                "x" : 0,
                                                "y" : 135,
                                                "image" : "d:/ymir work/ui/public/parameter_slot_02.sub",
                                                    "children" :
                                                        (
                                                            {
                                                                "name" : "Target_Money_Value",
                                                                "type" : "text",
                                                                "x" : 59,
                                                                "y" : 2,
                                                                "text" : "1234567",
                                                                "text_horizontal_align" : "right",
                                                                },
                                                            ),
                                                        },
                                                    {
                                                        "name" : "Target_Accept_Light",
                                                        "type" : "button",
                                                        "x" : 62,
                                                        "y" : 135,
                                                        "default_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub",
                                                        "over_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub",
                                                        "down_image" : "d:/ymir work/ui/game/windows/accept_button_on.sub",
                                                },
                                        ),
                                },
                        ),
                },
        ),
}
