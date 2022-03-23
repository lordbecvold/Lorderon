//Lorderon Client Binary Dev by Lordbecvold
#pragma once

#include "../eterLib/GrpSubImage.h"
#include "../eterGrnLib/Thing.h"
#include "../UserInterface/Locale_inc.h"
#include "GameLibDefines.h"


class CItemData
{
	public:
		enum
		{
			ITEM_NAME_MAX_LEN = 24,
			ITEM_LIMIT_MAX_NUM = 2,
			ITEM_VALUES_MAX_NUM = 6,
			ITEM_SMALL_DESCR_MAX_LEN = 256,
			ITEM_APPLY_MAX_NUM = 3,
			ITEM_SOCKET_MAX_NUM = 3,
#ifdef __UNIMPLEMENTED__
			ITEM_PICK_MAX_LEVEL = 9,
			ITEM_ROD_MAX_LEVEL = 20,
#endif
		};

#ifdef ENABLE_SOULBIND_SYSTEM
		enum ESealBind
		{
			SEAL_BIND_FLAG_DROP,
			SEAL_BIND_FLAG_UPGRADE,
			SEAL_BIND_FLAG_SELL,
			SEAL_BIND_FLAG_ENCHANT,
			SEAL_BIND_FLAG_TRADE,
			SEAL_BIND_FLAG_UNSEAL,
			SEAL_BIND_FLAG_MAX,
		};
		enum ESealDate
		{
			SEAL_DATE_DEFAULT_TIMESTAMP = 0, 
			SEAL_DATE_UNLIMITED_TIMESTAMP = -1, 
		};
		enum ESealItem
		{
			SEAL_ITEM_BINDING_VNUM = 50263,
			SEAL_ITEM_UNBINDING_VNUM = 50264,
		};
#endif
#ifdef __UNIMPLEMENTED__
		enum EPetData
		{
			EGG_USE_SUCCESS = 0,
			EGG_USE_FAILED_TIMEOVER = 2,
			EGG_USE_FAILED_BECAUSE_NAME = 1,
			GROWTH_PET_ITEM_USE_COOL_TIME = 1,
			PET_EGG_USE_TRUE = 0,
			PET_EGG_USE_FAILED_BECAUSE_TRADING = 1,
			PET_EGG_USE_FAILED_BECAUSE_SHOP_OPEN = 2,
			PET_EGG_USE_FAILED_BECAUSE_MALL_OPEN = 3,
			PET_EGG_USE_FAILED_BECAUSE_SAFEBOX_OPEN = 4,
			PET_HATCHING_MONEY = 100000,
			PET_NAME_MAX_SIZE = 20,
			PET_NAME_MIN_SIZE = 4,
		};
#endif
		enum EItemType
		{
			ITEM_TYPE_NONE,					
			ITEM_TYPE_WEAPON,				
			ITEM_TYPE_ARMOR,				
			ITEM_TYPE_USE,					
			ITEM_TYPE_AUTOUSE,				
			ITEM_TYPE_MATERIAL,				
			ITEM_TYPE_SPECIAL,				
			ITEM_TYPE_TOOL,					
			ITEM_TYPE_LOTTERY,			
			ITEM_TYPE_ELK,				
			ITEM_TYPE_METIN,			
			ITEM_TYPE_CONTAINER,		
			ITEM_TYPE_FISH,				
			ITEM_TYPE_ROD,				
			ITEM_TYPE_RESOURCE,			
			ITEM_TYPE_CAMPFIRE,				
			ITEM_TYPE_UNIQUE,				
			ITEM_TYPE_SKILLBOOK,			
			ITEM_TYPE_QUEST,				
			ITEM_TYPE_POLYMORPH,			
			ITEM_TYPE_TREASURE_BOX,			
			ITEM_TYPE_TREASURE_KEY,			
			ITEM_TYPE_SKILLFORGET,		
			ITEM_TYPE_GIFTBOX,			
			ITEM_TYPE_PICK,				
			ITEM_TYPE_HAIR,				
			ITEM_TYPE_TOTEM,			
			ITEM_TYPE_BLEND,				
			ITEM_TYPE_COSTUME,				
			ITEM_TYPE_DS,					
			ITEM_TYPE_SPECIAL_DS,			
			ITEM_TYPE_EXTRACT,					
			ITEM_TYPE_SECONDARY_COIN,			
			ITEM_TYPE_RING,					
			ITEM_TYPE_BELT,				
#ifdef ENABLE_PET_SLOT
			ITEM_TYPE_PET,
#endif
#ifdef __UNIMPLEMENTED__
			ITEM_TYPE_PET,				
			ITEM_TYPE_MEDIUM,			
#endif
			ITEM_TYPE_MAX_NUM,
		};
#ifdef __UNIMPLEMENTED__
		enum EResourceSubTypes
		{
			RESOURCE_FISHBONE = 0,
			RESOURCE_WATERSTONEPIECE = 1,
			RESOURCE_WATERSTONE = 2,
			RESOURCE_BLOOD_PEARL = 3,
			RESOURCE_BLUE_PEARL = 4,
			RESOURCE_WHITE_PEARL = 5,
			RESOURCE_BUCKET = 6,
			RESOURCE_CRYSTAL = 7,
			RESOURCE_GEM = 8,
			RESOURCE_STONE = 9,
			RESOURCE_METIN = 10,
			RESOURCE_ORE = 11,
		};
		enum EPetSubTypes
		{
			PET_EGG = 0,
			PET_UPBRINGING = 1,
			PET_BAG = 2,
			PET_FEEDSTUFF = 3,
			PET_SKILL = 4,
			PET_SKILL_DEL_BOOK = 5,
		};
		enum EMediumSubTypes
		{
			MEDIUM_MOVE_COSTUME_ATTR = 0,
		};
#endif
		enum EWeaponSubTypes
		{
			WEAPON_SWORD, 
			WEAPON_DAGGER, 
			WEAPON_BOW, 
			WEAPON_TWO_HANDED, 
			WEAPON_BELL, 
			WEAPON_FAN, 
			WEAPON_ARROW,
			WEAPON_MOUNT_SPEAR, 
#ifdef ENABLE_WOLFMAN_CHARACTER
			WEAPON_CLAW = 8, 
#endif
#ifdef ENABLE_QUIVER_SYSTEM
			WEAPON_QUIVER = 9, 
#endif
#ifdef __UNIMPLEMENTED__
			WEAPON_BOUQUET = 10, 
#endif
			WEAPON_NUM_TYPES, 

			WEAPON_NONE = WEAPON_NUM_TYPES+1,
		};
		enum EMaterialSubTypes
		{
			MATERIAL_LEATHER,
			MATERIAL_BLOOD,
			MATERIAL_ROOT,
			MATERIAL_NEEDLE,
			MATERIAL_JEWEL,
			MATERIAL_DS_REFINE_NORMAL,
			MATERIAL_DS_REFINE_BLESSED,
			MATERIAL_DS_REFINE_HOLLY,
		};
		enum EArmorSubTypes
		{
			ARMOR_BODY,
			ARMOR_HEAD,
			ARMOR_SHIELD,
			ARMOR_WRIST,
			ARMOR_FOOTS,
		    ARMOR_NECK,
			ARMOR_EAR,
			ARMOR_NUM_TYPES
		};
		enum ECostumeSubTypes
		{
			COSTUME_BODY,				
			COSTUME_HAIR,
#ifdef ENABLE_MOUNT_COSTUME_SYSTEM
			COSTUME_MOUNT	= 2,		
#endif
#ifdef ENABLE_ACCE_COSTUME_SYSTEM
			COSTUME_ACCE	= 3,		
#endif
#ifdef ENABLE_WEAPON_COSTUME_SYSTEM
			COSTUME_WEAPON	= 4,		
#endif
			COSTUME_NUM_TYPES,
		};
		enum EUseSubTypes
		{
			USE_POTION,					
			USE_TALISMAN,
			USE_TUNING,
			USE_MOVE,
			USE_TREASURE_BOX,
			USE_MONEYBAG,
			USE_BAIT,
			USE_ABILITY_UP,
			USE_AFFECT,
			USE_CREATE_STONE,
			USE_SPECIAL,				
			USE_POTION_NODELAY,
			USE_CLEAR,
			USE_INVISIBILITY,
			USE_DETACHMENT,
			USE_BUCKET,
			USE_POTION_CONTINUE,
			USE_CLEAN_SOCKET,
			USE_CHANGE_ATTRIBUTE,
			USE_ADD_ATTRIBUTE,
			USE_ADD_ACCESSORY_SOCKET,	
			USE_PUT_INTO_ACCESSORY_SOCKET,
			USE_ADD_ATTRIBUTE2,
			USE_RECIPE,
			USE_CHANGE_ATTRIBUTE2,
			USE_BIND,
			USE_UNBIND,
			USE_TIME_CHARGE_PER,
			USE_TIME_CHARGE_FIX,				
			USE_PUT_INTO_BELT_SOCKET,			
			USE_PUT_INTO_RING_SOCKET,
#ifdef ENABLE_NEW_ENCHANT_ATTR
			USE_CHANGE_ATTRIBUTE3,
#endif			
#ifdef ENABLE_USE_COSTUME_ATTR
			USE_CHANGE_COSTUME_ATTR,			
			USE_RESET_COSTUME_ATTR,				
#endif
		};
		enum EDragonSoulSubType
		{
			DS_SLOT1,
			DS_SLOT2,
			DS_SLOT3,
			DS_SLOT4,
			DS_SLOT5,
			DS_SLOT6,
			DS_SLOT_NUM_TYPES = 6,
		};
		enum EMetinSubTypes
		{
			METIN_NORMAL,
			METIN_GOLD,
		};
		enum ELimitTypes
		{
			LIMIT_NONE,
			LIMIT_LEVEL,
			LIMIT_STR,
			LIMIT_DEX,
			LIMIT_INT,
			LIMIT_CON,
			LIMIT_PCBANG,
			LIMIT_REAL_TIME,
			LIMIT_REAL_TIME_START_FIRST_USE,
			LIMIT_TIMER_BASED_ON_WEAR,
			LIMIT_MAX_NUM
		};
		enum EItemAntiFlag
		{
			ITEM_ANTIFLAG_FEMALE        = (1 << 0),		
			ITEM_ANTIFLAG_MALE          = (1 << 1),		
			ITEM_ANTIFLAG_WARRIOR       = (1 << 2),		
			ITEM_ANTIFLAG_ASSASSIN      = (1 << 3),		
			ITEM_ANTIFLAG_SURA          = (1 << 4),		
			ITEM_ANTIFLAG_SHAMAN        = (1 << 5),		
			ITEM_ANTIFLAG_GET           = (1 << 6),	
			ITEM_ANTIFLAG_DROP          = (1 << 7),		
			ITEM_ANTIFLAG_SELL          = (1 << 8),		
			ITEM_ANTIFLAG_EMPIRE_A      = (1 << 9),		
			ITEM_ANTIFLAG_EMPIRE_B      = (1 << 10),	
			ITEM_ANTIFLAG_EMPIRE_R      = (1 << 11),	
			ITEM_ANTIFLAG_SAVE          = (1 << 12),	
			ITEM_ANTIFLAG_GIVE          = (1 << 13),	
			ITEM_ANTIFLAG_PKDROP        = (1 << 14),	
			ITEM_ANTIFLAG_STACK         = (1 << 15),	
			ITEM_ANTIFLAG_MYSHOP        = (1 << 16),	
			ITEM_ANTIFLAG_SAFEBOX		= (1 << 17),
#ifdef ENABLE_WOLFMAN_CHARACTER
			ITEM_ANTIFLAG_WOLFMAN		= (1 << 18),
#endif
		};
		enum EItemFlag
		{
			ITEM_FLAG_REFINEABLE        = (1 << 0),		
			ITEM_FLAG_SAVE              = (1 << 1),
			ITEM_FLAG_STACKABLE         = (1 << 2),     
			ITEM_FLAG_COUNT_PER_1GOLD   = (1 << 3),		
			ITEM_FLAG_SLOW_QUERY        = (1 << 4),		
			ITEM_FLAG_RARE              = (1 << 5),
			ITEM_FLAG_UNIQUE            = (1 << 6),
			ITEM_FLAG_MAKECOUNT			= (1 << 7),
			ITEM_FLAG_IRREMOVABLE		= (1 << 8),
			ITEM_FLAG_CONFIRM_WHEN_USE	= (1 << 9),
			ITEM_FLAG_QUEST_USE         = (1 << 10),    
			ITEM_FLAG_QUEST_USE_MULTIPLE= (1 << 11),    
			ITEM_FLAG_UNUSED03          = (1 << 12),   
			ITEM_FLAG_LOG               = (1 << 13),   
			ITEM_FLAG_APPLICABLE		= (1 << 14),
		};
		enum EWearPositions
		{
			WEAR_BODY,          
			WEAR_HEAD,         
			WEAR_FOOTS,       
			WEAR_WRIST,      
			WEAR_WEAPON,      
			WEAR_NECK,        
			WEAR_EAR,         
			WEAR_UNIQUE1,     
			WEAR_UNIQUE2,      
			WEAR_ARROW,         
			WEAR_SHIELD,     
			WEAR_ABILITY1, 
			WEAR_ABILITY2,  
			WEAR_ABILITY3,  
			WEAR_ABILITY4,  
			WEAR_ABILITY5, 
			WEAR_ABILITY6,
			WEAR_ABILITY7,  
			WEAR_ABILITY8,  
			WEAR_COSTUME_BODY,	
			WEAR_COSTUME_HAIR,
#ifdef ENABLE_ACCE_SYSTEM
			WEAR_COSTUME_ACCE,
#endif
			WEAR_RING1,			
#ifdef ENABLE_MOUNT_COSTUME_SYSTEM
			WEAR_COSTUME_MOUNT = WEAR_RING1, 
#endif
			WEAR_BELT,			
#ifdef ENABLE_WEAPON_COSTUME_SYSTEM
			WEAR_COSTUME_WEAPON,
#endif
			WEAR_MAX_NUM = 32,
		};
		enum EItemWearableFlag
		{
			WEARABLE_BODY       = (1 << 0),
			WEARABLE_HEAD       = (1 << 1),
			WEARABLE_FOOTS      = (1 << 2),
			WEARABLE_WRIST      = (1 << 3),
			WEARABLE_WEAPON     = (1 << 4),
			WEARABLE_NECK       = (1 << 5),
			WEARABLE_EAR        = (1 << 6),
			WEARABLE_UNIQUE     = (1 << 7),
			WEARABLE_SHIELD     = (1 << 8),
			WEARABLE_ARROW      = (1 << 9),
		};
		enum EApplyTypes
		{
			APPLY_NONE,                 
			APPLY_MAX_HP,             
			APPLY_MAX_SP,              
			APPLY_CON,                 
			APPLY_INT,                  
			APPLY_STR,                 
			APPLY_DEX,                 
			APPLY_ATT_SPEED,           
			APPLY_MOV_SPEED,           
			APPLY_CAST_SPEED,           
			APPLY_HP_REGEN,           
			APPLY_SP_REGEN,            
			APPLY_POISON_PCT,           
			APPLY_STUN_PCT,            
			APPLY_SLOW_PCT,            
			APPLY_CRITICAL_PCT,        
			APPLY_PENETRATE_PCT,        
			APPLY_ATTBONUS_HUMAN,     
			APPLY_ATTBONUS_ANIMAL,     
			APPLY_ATTBONUS_ORC,       
			APPLY_ATTBONUS_MILGYO,     
			APPLY_ATTBONUS_UNDEAD,     
			APPLY_ATTBONUS_DEVIL,      
			APPLY_STEAL_HP,           
			APPLY_STEAL_SP,           
			APPLY_MANA_BURN_PCT,       
			APPLY_DAMAGE_SP_RECOVER,    
			APPLY_BLOCK,               
			APPLY_DODGE,                
			APPLY_RESIST_SWORD,        
			APPLY_RESIST_TWOHAND,     
			APPLY_RESIST_DAGGER,       
			APPLY_RESIST_BELL,       
			APPLY_RESIST_FAN,        
			APPLY_RESIST_BOW,       
			APPLY_RESIST_FIRE,       
			APPLY_RESIST_ELEC,          
			APPLY_RESIST_MAGIC,        
			APPLY_RESIST_WIND,        
			APPLY_REFLECT_MELEE,       
			APPLY_REFLECT_CURSE,      
			APPLY_POISON_REDUCE,     
			APPLY_KILL_SP_RECOVER,     
			APPLY_EXP_DOUBLE_BONUS,     
			APPLY_GOLD_DOUBLE_BONUS,   
			APPLY_ITEM_DROP_BONUS,     
			APPLY_POTION_BONUS,        
			APPLY_KILL_HP_RECOVER,    
			APPLY_IMMUNE_STUN,         
			APPLY_IMMUNE_SLOW,          
			APPLY_IMMUNE_FALL,          
			APPLY_SKILL,                
			APPLY_BOW_DISTANCE,        
			APPLY_ATT_GRADE_BONUS,            
			APPLY_DEF_GRADE_BONUS,          
			APPLY_MAGIC_ATT_GRADE,      
			APPLY_MAGIC_DEF_GRADE,    
			APPLY_CURSE_PCT,         
			APPLY_MAX_STAMINA,			
			APPLY_ATT_BONUS_TO_WARRIOR, 
			APPLY_ATT_BONUS_TO_ASSASSIN,
			APPLY_ATT_BONUS_TO_SURA,    
			APPLY_ATT_BONUS_TO_SHAMAN,  
			APPLY_ATT_BONUS_TO_MONSTER, 
			APPLY_MALL_ATTBONUS,        
			APPLY_MALL_DEFBONUS,        
			APPLY_MALL_EXPBONUS,        
			APPLY_MALL_ITEMBONUS,       
			APPLY_MALL_GOLDBONUS,       
			APPLY_MAX_HP_PCT,         
			APPLY_MAX_SP_PCT,          
			APPLY_SKILL_DAMAGE_BONUS, 
			APPLY_NORMAL_HIT_DAMAGE_BONUS,    
			APPLY_SKILL_DEFEND_BONUS,   
			APPLY_NORMAL_HIT_DEFEND_BONUS,      
			APPLY_EXTRACT_HP_PCT,		
			APPLY_PC_BANG_EXP_BONUS,	
			APPLY_PC_BANG_DROP_BONUS,	
			APPLY_RESIST_WARRIOR,		
			APPLY_RESIST_ASSASSIN ,		
			APPLY_RESIST_SURA,			
			APPLY_RESIST_SHAMAN,		
			APPLY_ENERGY,			
			APPLY_DEF_GRADE,				
			APPLY_COSTUME_ATTR_BONUS,		
			APPLY_MAGIC_ATTBONUS_PER,		
			APPLY_MELEE_MAGIC_ATTBONUS_PER,			
			APPLY_RESIST_ICE,		
			APPLY_RESIST_EARTH,		
			APPLY_RESIST_DARK,		
			APPLY_ANTI_CRITICAL_PCT,	
			APPLY_ANTI_PENETRATE_PCT,	
#ifdef ENABLE_WOLFMAN_CHARACTER
			APPLY_BLEEDING_REDUCE			= 92,	
			APPLY_BLEEDING_PCT				= 93,	
			APPLY_ATT_BONUS_TO_WOLFMAN		= 94,	
			APPLY_RESIST_WOLFMAN			= 95,	
			APPLY_RESIST_CLAW				= 96,	
#endif
#ifdef ENABLE_ACCE_COSTUME_SYSTEM
			APPLY_ACCEDRAIN_RATE			= 97,	
#endif
#ifdef ENABLE_MAGIC_REDUCTION_SYSTEM
			APPLY_RESIST_MAGIC_REDUCTION	= 98,	
#endif
			MAX_APPLY_NUM					= 99,
		};
		enum EImmuneFlags
		{
			IMMUNE_PARA         = (1 << 0),
			IMMUNE_CURSE        = (1 << 1),
			IMMUNE_STUN         = (1 << 2),
			IMMUNE_SLEEP        = (1 << 3),
			IMMUNE_SLOW         = (1 << 4),
			IMMUNE_POISON       = (1 << 5),
			IMMUNE_TERROR       = (1 << 6),
		};
#pragma pack(push)
#pragma pack(1)
		typedef struct SItemLimit
		{
			BYTE        bType;
			long        lValue;
		} TItemLimit;
		typedef struct SItemApply
		{
			BYTE        bType;
			long        lValue;
		} TItemApply;
		typedef struct SItemTable_r152
		{
			DWORD       dwVnum;
			char        szName[ITEM_NAME_MAX_LEN + 1];
			char        szLocaleName[ITEM_NAME_MAX_LEN + 1];
			BYTE        bType;
			BYTE        bSubType;
			BYTE        bWeight;
			BYTE        bSize;
			DWORD       dwAntiFlags;
			DWORD       dwFlags;
			DWORD       dwWearFlags;
			DWORD       dwImmuneFlag;
			DWORD       dwIBuyItemPrice;
			DWORD		dwISellItemPrice;
			TItemLimit  aLimits[ITEM_LIMIT_MAX_NUM];
			TItemApply  aApplies[ITEM_APPLY_MAX_NUM];
			long        alValues[ITEM_VALUES_MAX_NUM];
			long        alSockets[ITEM_SOCKET_MAX_NUM];
			DWORD       dwRefinedVnum;
			WORD		wRefineSet;
			BYTE        bAlterToMagicItemPct;
			BYTE		bSpecular;
			BYTE        bGainSocketPct;
		} TItemTable_r152;
		typedef struct SItemTable_r156
		{
			DWORD       dwVnum;
			DWORD       dwVnumRange;
			char        szName[ITEM_NAME_MAX_LEN + 1];
			char        szLocaleName[ITEM_NAME_MAX_LEN + 1];
			BYTE        bType;
			BYTE        bSubType;
			BYTE        bWeight;
			BYTE        bSize;
			DWORD       dwAntiFlags;
			DWORD       dwFlags;
			DWORD       dwWearFlags;
			DWORD       dwImmuneFlag;
			DWORD       dwIBuyItemPrice;
			DWORD		dwISellItemPrice;
			TItemLimit  aLimits[ITEM_LIMIT_MAX_NUM];
			TItemApply  aApplies[ITEM_APPLY_MAX_NUM];
			long        alValues[ITEM_VALUES_MAX_NUM];
			long        alSockets[ITEM_SOCKET_MAX_NUM];
			DWORD       dwRefinedVnum;
			WORD		wRefineSet;
			BYTE        bAlterToMagicItemPct;
			BYTE		bSpecular;
			BYTE        bGainSocketPct;
		} TItemTable_r156;

		typedef struct SItemTable_r158
		{
			DWORD       dwVnum;
			DWORD       dwVnumRange;
			char        szName[ITEM_NAME_MAX_LEN + 1];
			char        szLocaleName[ITEM_NAME_MAX_LEN + 1];
			BYTE        bType;
			BYTE        bSubType;
			BYTE        bWeight;
			BYTE        bSize;
			DWORD       dwAntiFlags;
			DWORD       dwFlags;
			DWORD       dwWearFlags;
			DWORD       dwImmuneFlag;
			DWORD       dwIBuyItemPrice;
			DWORD		dwISellItemPrice;
			TItemLimit  aLimits[ITEM_LIMIT_MAX_NUM];
			TItemApply  aApplies[ITEM_APPLY_MAX_NUM];
			long        alValues[ITEM_VALUES_MAX_NUM];
			long        alSockets[ITEM_SOCKET_MAX_NUM];
			DWORD       dwRefinedVnum;
			WORD		wRefineSet;
			BYTE        bAlterToMagicItemPct;
			BYTE		bSpecular;
			BYTE        bGainSocketPct;
			WORD		wWearableFlag;
		} TItemTable_r158;
		typedef SItemTable_r156 SItemTable, TItemTable;
#ifdef ENABLE_ACCE_SYSTEM
		struct SScaleInfo
		{
			float	fScaleX, fScaleY, fScaleZ;
			float	fPositionX, fPositionY, fPositionZ;
		};
		typedef struct SScaleTable
		{
			SScaleInfo	tInfo[10];
		} TScaleTable;
#endif

#ifdef ENABLE_PROTOSTRUCT_AUTODETECT
		typedef struct SItemTableAll
		{
			static bool IsValidStruct(DWORD structSize)
			{
				switch (structSize)
				{
					case sizeof(TItemTable_r152):
					case sizeof(TItemTable_r156):
					case sizeof(TItemTable_r158):
						return true;
						break;
				}
				return false;
			}
			static void Process(void* obj, DWORD structSize, DWORD i, CItemData::TItemTable& t)
			{
				#define ITABLE_COPY_STR(x) strncpy_s(t.##x##, sizeof(t.##x##), r.##x##, _TRUNCATE)
				#define ITABLE_COPY_INT(x) t.##x## = r.##x
				#define ITABLE_ZERO_STR(x) memset(t.##x##, 0, sizeof(t.##x##));
				#define ITABLE_ZERO_INT(x) t.##x## = 0
				#define ITABLE_COUNT(x) _countof(t.##x##)
				#define ITABLE_PROCESS(len)\
					CItemData::TItemTable_r##len## & r = *((CItemData::TItemTable_r##len## *) obj + i);\
					ITABLE_COPY_INT(dwVnum);\
					ITABLE_COPY_STR(szName);\
					ITABLE_COPY_STR(szLocaleName);\
					ITABLE_COPY_INT(bType);\
					ITABLE_COPY_INT(bSubType);\
					ITABLE_COPY_INT(bWeight);\
					ITABLE_COPY_INT(bSize);\
					ITABLE_COPY_INT(dwAntiFlags);\
					ITABLE_COPY_INT(dwFlags);\
					ITABLE_COPY_INT(dwWearFlags);\
					ITABLE_COPY_INT(dwImmuneFlag);\
					ITABLE_COPY_INT(dwIBuyItemPrice);\
					ITABLE_COPY_INT(dwISellItemPrice);\
					for (size_t i=0; i<ITABLE_COUNT(aLimits); ++i)\
					{\
						ITABLE_COPY_INT(aLimits[i].bType);\
						ITABLE_COPY_INT(aLimits[i].lValue);\
					}\
					for (size_t i=0; i<CItemData::ITEM_APPLY_MAX_NUM; ++i)\
					{\
						ITABLE_COPY_INT(aApplies[i].bType);\
						ITABLE_COPY_INT(aApplies[i].lValue);\
					}\
					for (size_t i=0; i<CItemData::ITEM_VALUES_MAX_NUM; ++i)\
					{\
						ITABLE_COPY_INT(alValues[i]);\
					}\
					for (size_t i=0; i<CItemData::ITEM_SOCKET_MAX_NUM; ++i)\
					{\
						ITABLE_COPY_INT(alSockets[i]);\
					}\
					ITABLE_COPY_INT(dwRefinedVnum);\
					ITABLE_COPY_INT(wRefineSet);\
					ITABLE_COPY_INT(bAlterToMagicItemPct);\
					ITABLE_COPY_INT(bSpecular);\
					ITABLE_COPY_INT(bGainSocketPct);
				switch (structSize)
				{
					case sizeof(TItemTable_r152):
						{
							ITABLE_PROCESS(152);
							ITABLE_ZERO_INT(dwVnumRange);
						}
						break;
					case sizeof(TItemTable_r156):
						{
							ITABLE_PROCESS(156);
							ITABLE_COPY_INT(dwVnumRange);
						}
						break;
					case sizeof(TItemTable_r158):
						{
							ITABLE_PROCESS(158);
							ITABLE_COPY_INT(dwVnumRange);
						}
						break;
				}
			}
		} TItemTableAll;
#endif

#pragma pack(pop)

	public:
		CItemData();
		virtual ~CItemData();
		void Clear();
		void SetSummary(const std::string& c_rstSumm);
		void SetDescription(const std::string& c_rstDesc);
		CGraphicThing * GetModelThing();
		CGraphicThing * GetSubModelThing();
		CGraphicThing * GetDropModelThing();
		CGraphicSubImage * GetIconImage();
		DWORD GetLODModelThingCount();
		BOOL GetLODModelThingPointer(DWORD dwIndex, CGraphicThing ** ppModelThing);
		DWORD GetAttachingDataCount();
		BOOL GetCollisionDataPointer(DWORD dwIndex, const NRaceData::TAttachingData ** c_ppAttachingData);
		BOOL GetAttachingDataPointer(DWORD dwIndex, const NRaceData::TAttachingData ** c_ppAttachingData);
		const TItemTable*	GetTable() const;
		DWORD GetIndex() const;
		const char * GetName() const;
		const char * GetDescription() const;
		const char * GetSummary() const;
		BYTE GetType() const;
		BYTE GetSubType() const;
		UINT GetRefine() const;
		const char* GetUseTypeString() const;
		DWORD GetWeaponType() const;
		BYTE GetSize() const;
		BOOL IsAntiFlag(DWORD dwFlag) const;
		BOOL IsFlag(DWORD dwFlag) const;
		BOOL IsWearableFlag(DWORD dwFlag) const;
		BOOL HasNextGrade() const;
		DWORD GetWearFlags() const;
		DWORD GetIBuyItemPrice() const;
		DWORD GetISellItemPrice() const;
		BOOL GetLimit(BYTE byIndex, TItemLimit * pItemLimit) const;
		BOOL GetApply(BYTE byIndex, TItemApply * pItemApply) const;
		long GetValue(BYTE byIndex) const;
		long GetSocket(BYTE byIndex) const;
		long SetSocket(BYTE byIndex,DWORD value);
		int GetSocketCount() const;
		DWORD GetIconNumber() const;
		UINT	GetSpecularPoweru() const;
		float	GetSpecularPowerf() const;
		BOOL IsEquipment() const;
		void SetDefaultItemData(const char * c_szIconFileName, const char * c_szModelFileName  = NULL);
		void SetItemTableData(TItemTable * pItemTable);
#ifdef ENABLE_ACCE_SYSTEM
		void	SetItemScale(const std::string strJob, const std::string strSex, const std::string strScaleX, const std::string strScaleY, const std::string strScaleZ, const std::string strPositionX, const std::string strPositionY, const std::string strPositionZ);
		bool	GetItemScale(DWORD dwPos, float & fScaleX, float & fScaleY, float & fScaleZ, float & fPositionX, float & fPositionY, float & fPositionZ);
#endif

	protected:
		void __LoadFiles();
		void __SetIconImage(const char * c_szFileName);

	protected:
		std::string m_strModelFileName;
		std::string m_strSubModelFileName;
		std::string m_strDropModelFileName;
		std::string m_strIconFileName;
		std::string m_strDescription;
		std::string m_strSummary;
		std::vector<std::string> m_strLODModelFileNameVector;
		CGraphicThing * m_pModelThing;
		CGraphicThing * m_pSubModelThing;
		CGraphicThing * m_pDropModelThing;
		CGraphicSubImage * m_pIconImage;
		std::vector<CGraphicThing *> m_pLODModelThingVector;
		NRaceData::TAttachingDataVector m_AttachingDataVector;
		DWORD		m_dwVnum;
		TItemTable m_ItemTable;
#ifdef ENABLE_ACCE_SYSTEM
		TScaleTable	m_ScaleTable;
#endif

	public:
		static void DestroySystem();
		static CItemData* New();
		static void Delete(CItemData* pkItemData);
		static CDynamicPool<CItemData>		ms_kPool;
};
