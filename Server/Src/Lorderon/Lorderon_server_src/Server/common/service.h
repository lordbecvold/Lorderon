///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//-----------------------------------------LORDERON SERVER SYSTEM DEFINES----------------------------------------//
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifndef __INC_SERVICE_H__ //Enable service.h config file
#define __INC_SERVICE_H__ //Enable service.h config file
#define ENABLE_AGGREGATE_MONSTER_EFFECT //Enable * in agresive mob name
#define _IMPROVED_PACKET_ENCRYPTION_ //Enable packet security system
#define __PET_SYSTEM__ //Enable normal pet system form lua
#define __UDP_BLOCK__ //Enable blocks the udp packets More.
#define __SEND_TARGET_INFO__ //Enable Mob target info
#define ENABLE_IP_SECURITY //Enable ip security system settings in mysql (account.ip_security table)
#define ENABLE_IGNORE_LOWER_BUFFS //Enable blocking low % buf 
#define ENABLE_LOCALIZATION_SYSTEM //Enable save location system
#define ENABLE_BIOLOG_SYSTEM //Enable Biolog system in inventory
#define ENABLE_SPECIAL_STORAGE //Enable external inv system
#define __ACCE_SYSTEM__ //Enable Sash system
#define ENABLE_ACCE_COSTUME_SYSTEM //Enable Sash Absorbation system
#define ENABLE_SHOW_CHEST_DROP //Enable chest open system
#define ENABLE_FEATURES_REFINE_SYSTEM //Enable New refine system
#ifndef ENABLE_ANNOUNCEMENT_REFINE_SUCCES //Enable item refine notification in global chat
	#define ENABLE_ANNOUNCEMENT_REFINE_SUCCES //Enable item refine notification in global chat
	#define ENABLE_ANNOUNCEMENT_REFINE_SUCCES_MIN_LEVEL 9 //Set minimal + item for chat notification
#endif //End of ANNOUNCEMENT_REFINE_SUCCES
#define __VIEW_TARGET_PLAYER_HP__ //Enable view hp from other players
#define __VIEW_TARGET_DECIMAL_HP__ //Enable view mobs hp in target
#define ENABLE_MAINTENANCE_SYSTEM //Enable Maintenance system
#define ENABLE_PVP_ADVANCED //Enable Advanced pvp
#ifdef ENABLE_PVP_ADVANCED //Enable Advanced pvp
	#define BLOCK_CHANGEITEM "pvp.BlockChangeItem" //Advanced pvp option
	#define BLOCK_BUFF "pvp.BlockBuff" //Advanced pvp option
	#define BLOCK_POTION "pvp.BlockPotion" //Advanced pvp option
	#define BLOCK_RIDE "pvp.BlockRide" //Advanced pvp option
	#define BLOCK_PET "pvp.BlockPet" //Advanced pvp option
	#define BLOCK_POLY "pvp.BlockPoly" //Advanced pvp option
	#define BLOCK_PARTY "pvp.BlockParty" //Advanced pvp option
	#define BLOCK_EXCHANGE_	"pvp.BlockExchange" //Advanced pvp option
	#define BLOCK_EQUIPMENT_ "pvp.BLOCK_VIEW_EQUIPMENT" //Advanced pvp option
	#define BET_WINNER "pvp.BetMoney" //Advanced pvp option
	#define CHECK_IS_FIGHT "pvp.IsFight" //Advanced pvp option
#endif //End of ADVANCED_PVP
#define ENABLE_POLY_SHOP //Enable ingame polymorph shop
#define RENEWAL_DEAD_PACKET //Enable restart dialog counter
#define ENABLE_ANNOUNCEMENT_LEVELUP //Enable Level up ANNOUNCEMENT
#define __NEW_EXCHANGE_WINDOW__ //Enable new Trade system
#define ENABLE_TITLE_SYSTEM //Enable Title system
//#define WJ_COMBAT_ZONE //Enable official combat zone system
//#define WJ_COMBAT_ZONE_HIDE_INFO_USER //Enable Hide info from player stats in Combat zone
#endif //End of __INC_SERVICE_H__  
