//Lorderon Server Core
#ifndef __INC_METIN2_COMMON_DEFINES_H__ //Enable CommonDefines settings file
#define __INC_METIN2_COMMON_DEFINES_H__ //Enable CommonDefines settings file
#define ENABLE_D_NJGUILD //Enable d.new_jump_all_guild+cpp relative functions (untested)
#define ENABLE_FULL_NOTICE //Enable big nottice form ingame command /big_notice
#define ENABLE_NEWSTUFF //Enable new stuff (new lua funcs, new CONFIG options, ecc)
#define ENABLE_PORT_SECURITY //Enable Port injection security
#define ENABLE_BELT_INVENTORY_EX // move the belt items into the BELT_INVENTORY window and prevents unknown belt 
enum eCommonDefines { // eComonDefines settings
	MAP_ALLOW_LIMIT = 32, //Set max Map limit implemented on server
}; //End of eCommonDefines
#define OFFLINE_SHOP //Enable Offline shops system
#define GIFT_SYSTEM //Enable offline shop gift system 
#define FULL_YANG //Enable Increase max yang in offline shop
#define SHOP_TIME_REFRESH 1*60 //Set time for cycle checking older shops
#define SHOP_BLOCK_GAME99 //Blocking create shops on channel 99
//#define SHOP_DISTANCE //Enable Show shops in pos distance like WoM2
#define SHOP_AUTO_CLOSE //Enable auto closing shop after sell last item
//#define SHOP_ONLY_ALLOWED_INDEX //Enable limiting for other map index which is not defined in player.shop_limit
//#define SHOP_HIDE_NAME //Enable hidding shop npc names like "Player's shop"
#define SHOP_GM_PRIVILEGES GM_IMPLEMENTOR //Minimum GM privileges to using Shop GM Panel
#define ENABLE_PLAYER_PER_ACCOUNT5 //Enable 5 character slot 
#define ENABLE_DICE_SYSTEM //Enable drop dice system
#define ENABLE_EXTEND_INVEN_SYSTEM //Enable 4 inventory page
#define ENABLE_MOUNT_COSTUME_SYSTEM  //Enable Mount costume system
#define ENABLE_WEAPON_COSTUME_SYSTEM //Enable weapon costume system
#define ENABLE_INFINITE_HORSE_HEALTH_STAMINA //Enable full horse health and stamina all the times
#define ENABLE_IMMUNE_FIX //Enable fix immune bug where you need to equip shield at last (or refresh compute e.g. un/riding horse)
#define ENABLE_CHECK_GHOSTMODE //Enable check that blocks the movements if the character is dead
//#define DISABLE_SYSERR //Disable Server Syserr channels folder
//#define DISABLE_SYSLOG //Disable Server Syslog channels folder
#endif //End of CommonDefines

