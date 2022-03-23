//Lorderon server core Dev by Lordbecvold
#include "../../common/service.h"
#ifdef ENABLE_WOLFMAN_CHARACTER	
int tableBonus[10][10]
#else
int tableBonus[10][8]		 
#endif
={
	{POINT_MOV_SPEED, 10}, // Biologist level 30
	
	{POINT_ATT_SPEED, 5}, // Biologist level 40
	
	{POINT_DEF_GRADE_BONUS, 60}, // Biologist level 50
	
	{POINT_ATT_GRADE_BONUS, 50}, // Biologist level 60
	
	{POINT_MOV_SPEED, 11, POINT_DEF_BONUS, 10}, // Biologist level 70
									
	{POINT_ATT_SPEED, 6, POINT_ATT_BONUS, 10}, // Biologist level 80

#ifdef ENABLE_WOLFMAN_CHARACTER										
	{POINT_ATTBONUS_WARRIOR, 8, POINT_ATTBONUS_ASSASSIN, 8, POINT_ATTBONUS_SURA, 8, POINT_ATTBONUS_SHAMAN, 8, POINT_ATTBONUS_WOLFMAN, 10}, // Biologist level 90
#else	
	{POINT_ATTBONUS_WARRIOR, 8, POINT_ATTBONUS_ASSASSIN, 8, POINT_ATTBONUS_SURA, 8, POINT_ATTBONUS_SHAMAN, 8}, // Biologist level 90
#endif	

	{POINT_MAX_HP, 1000, POINT_ATT_GRADE_BONUS, 50, POINT_DEF_GRADE_BONUS, 120}, // Biologist level 92
									
	{POINT_MAX_HP, 1100, POINT_ATT_GRADE_BONUS, 60, POINT_DEF_GRADE_BONUS, 140} // Biologist level 94								
};
							
/*********
* Table translation, here modify messages that are sent in chat client but also in the box when something is wrong or worked.
*/							
const char* pTable_Translate[] =
{
	"[Biolog] Pøedmìt byl úspìšnì odevzdán!",
	"[Biolog] Lituji tato popožka není správné kvality!", 
	"[Biolog] Kategorie výzkumu byla dokonèena!",
	"[Biolog] Je tøeba poèkat [%d dnù] [%d Hod] [%d Min] [%d Sec] pro odevzdání!",
	"[Biolog] Nemáš v inventáøi patøièný pøedmìt!",
	"[Biolog] Potøebuješ %u úrovìn pro tento výzkum!",
	"[Biolog] již máš dokonèené všechny biologické výzkumy!"
}; 								
									
/*********
* Here are the settings for sending in box when you finish a mission.
* You would need to be change only these texts for the country you belong, values are taken directly bonuses configuration table tableBonus[i][i].
*/		
const char* pPopUp[10][4] =
{  
	{
		"[Gratulujeme] Biologova odmìna úrovnì 30",
		"[1. Bonus] Rychlost pohybu (Permanentní)."
	},	
	{
		"[Gratulujeme] Biologova odmìna úrovnì 40",
		"[1. Bonus] Rychlost úroku (Permanentní)."
	},	
	{
		"[Gratulujeme] Biologova odmìna úrovnì 50",
		"[1. Bonus] obrana (Permanentní)."
	},	
	{
		"[Gratulujeme] Biologova odmìna úrovnì 60",
		"[1. Bonus] Hodnota útoku (Permanentní)."
	},	
	{
		"[Gratulujeme] Biologova odmìna úrovnì 70",
		"[1. Bonus] Rychlost pohybu (Permanentní).",
		"[2. Bonus] Odolnost proti poškození (Permanentní)."
	},	
	{
		"[Gratulujeme] Biologova odmìna úrovnì 80",
		"[1. Bonus] Rychlost úroku (Permanentní).",
		"[2. Bonus] Hodnota útoku (Permanentní)."
	},	
	{
		"[Gratulujeme] Biologova odmìna úrovnì 85",
		"[1. Bonus] Snížení poškození ostatních hráèù (Permanentní)."
	},	
	{
		"[Gratulujeme] Biologova odmìna úrovnì 90",
		"[1. Bonus] Zvýšení poškození proti ostatním hráèùm (Permanentní)."
	},	
	{
		"[Gratulujeme] Biologova odmìna úrovnì 92",
		"[1. Bonus] Max ZB",						// Bonus is selected from player
		"[2. Bonus] Hodnota útoku",		// Bonus is selected from player
		"[3. Bonus] Obrana"			// Bonus is selected from player
	},	
	{
		"[Gratulujeme] Biologova odmìna úrovnì 94",
		"[1. Bonus] Max ZB",						// Bonus is selected from player
		"[2. Bonus] Hodnota útoku",		// Bonus is selected from player
		"[3. Bonus] Obrana"			// Bonus is selected from player
	}											
};	

/*********
* You can change the items that you provide when you finish biologist. (default is like official)
*/		
int pTableRewardItem[10] =
{
	50109, // Biologist level 30
	50110, // Biologist level 40
	50111, // Biologist level 50
	50112, // Biologist level 60
	50113, // Biologist level 70
	50114, // Biologist level 80
	50115, // Biologist level 85
	50114, // Biologist level 90
	71107, // Biologist level 92
	85015 // Biologist level 94
};	
							
/*********
* From here you can change the probability chance to succeed when you send an object biologist. 
* If you do not own the object 71035 in inventory then the chance of probability will be random between 60 and 100, 
* and if you held your inventory item 71035 then the chance of probability will be increased to 90, which means that the chance will be between 90 and 100, which what a great success. (default is like official)
*/	
int pTablePercentage[3]	=
{
	71035, // Vnum item 
	60, // Actual chance, if you not have the item in inventory 71035
	95 // The chance probability automatically if you change the item in inventory 71035. (all like official)
};	
	
/*********
* From here you can change how many objects the maximum result for a mission. (default is like official)
*/											
int pTableCountMax[10] =
{
	10, // Biologist level 30
	15, // Biologist level 40
	15, // Biologist level 50
	20, // Biologist level 60
	25, // Biologist level 70
	30, // Biologist level 80
	40, // Biologist level 85
	50, // Biologist level 90
	10, // Biologist level 92
	20 // Biologist level 94
};

/*********
* From here you can change the levels missions at what level you want to start each mission. (default is like official)
*/										
int pTableLevel[10]	=
{
	30, // Biologist level 30
	40, // Biologist level 40
	50, // Biologist level 50
	60, // Biologist level 60
	70, // Biologist level 70
	80, // Biologist level 80
	85, // Biologist level 85
	90, // Biologist level 90
	92, // Biologist level 92
	94 // Biologist level 94
};

/*********
* From here you can change the volume of any items that are needed to achieve mission. (default is like official)
*/	
int pTableVnum[10] =
{
	30006, // Biologist level 30
	30047, // Biologist level 40
	30015, // Biologist level 50
	30050, // Biologist level 60
	30165, // Biologist level 70
	30166, // Biologist level 80
	30167, // Biologist level 85
	30168, // Biologist level 90
	30251, // Biologist level 92
	30252 // Biologist level 94
};

/*********
* From here change the timeout and how long until you can give another object biologist system. (default is like official)
*/
int pTableTime[10] =
{ 
	24*60, // Biologist level 30
	24*60, // Biologist level 40
	24*60, // Biologist level 50
	24*60, // Biologist level 60
	24*60*60, // Biologist level 70 
	24*60*60, // Biologist level 80  // 24*60*60 = 24 hours
	24*60*60, // Biologist level 85
	24*60*60, // Biologist level 90
	24*60*60, // Biologist level 92
	24*60*60 // Biologist level 94
};

/*********
* From here change the timeout for time durating all bonus of biolog
*/
int unlimited = 60*60*60*365;