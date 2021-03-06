//Lorderon Client Binary Dev by Lordbecvold
#include "stdafx.h"
#include "../eterPack/EterPackManager.h"
#include "pythonnonplayer.h"
#include "InstanceBase.h"
#include "PythonCharacterManager.h"

bool CPythonNonPlayer::LoadNonPlayerData(const char * c_szFileName)
{
	static DWORD s_adwMobProtoKey[4] = {4813894, 18955, 552631, 6822045};
	CMappedFile file;
	LPCVOID pvData;
	Tracef("CPythonNonPlayer::LoadNonPlayerData: %s, sizeof(TMobTable)=%u\n", c_szFileName, sizeof(TMobTable));
	if (!CEterPackManager::Instance().Get(file, c_szFileName, &pvData))
		return false;
	DWORD dwFourCC, dwElements, dwDataSize;
	file.Read(&dwFourCC, sizeof(DWORD));
	if (dwFourCC != MAKEFOURCC('M', 'M', 'P', 'T'))
	{
#ifdef ENABLE_DEV_MODE
		TraceError("CPythonNonPlayer::LoadNonPlayerData: invalid Mob proto type %s", c_szFileName);
#endif
		return false;
	}
	file.Read(&dwElements, sizeof(DWORD));
	file.Read(&dwDataSize, sizeof(DWORD));
	BYTE * pbData = new BYTE[dwDataSize];
	file.Read(pbData, dwDataSize);
	CLZObject zObj;
	if (!CLZO::Instance().Decompress(zObj, pbData, s_adwMobProtoKey))
	{
		delete [] pbData;
		return false;
	}
	DWORD structSize = zObj.GetSize() / dwElements;
	DWORD structDiff = zObj.GetSize() % dwElements;
#ifdef ENABLE_PROTOSTRUCT_AUTODETECT
	if (structDiff!=0 && !CPythonNonPlayer::TMobTableAll::IsValidStruct(structSize))
#else
	if ((zObj.GetSize() % sizeof(TMobTable)) != 0)
#endif
	{
#ifdef ENABLE_DEV_MODE
		TraceError("CPythonNonPlayer::LoadNonPlayerData: invalid size %u check data format. structSize %u, structDiff %u", zObj.GetSize(), structSize, structDiff);
#endif
		return false;
	}
    for (DWORD i = 0; i < dwElements; ++i)
	{
#ifdef ENABLE_PROTOSTRUCT_AUTODETECT
		CPythonNonPlayer::TMobTable t = {0};
		CPythonNonPlayer::TMobTableAll::Process(zObj.GetBuffer(), structSize, i, t);
#else
		CPythonNonPlayer::TMobTable & t = *((CPythonNonPlayer::TMobTable *) zObj.GetBuffer() + i);
#endif
		TMobTable * pTable = &t;
		TMobTable * pNonPlayerData = new TMobTable;
		memcpy(pNonPlayerData, pTable, sizeof(TMobTable));
		m_NonPlayerDataMap.insert(TNonPlayerDataMap::value_type(pNonPlayerData->dwVnum, pNonPlayerData));
	}
	delete [] pbData;
	return true;
}

bool CPythonNonPlayer::GetName(DWORD dwVnum, const char ** c_pszName)
{
	const TMobTable * p = GetTable(dwVnum);
	if (!p)
		return false;
	*c_pszName = p->szLocaleName;
	return true;
}

bool CPythonNonPlayer::GetInstanceType(DWORD dwVnum, BYTE* pbType)
{
	const TMobTable * p = GetTable(dwVnum);
	if (!p)
		return false;
	*pbType=p->bType;
	return true;
}

const CPythonNonPlayer::TMobTable * CPythonNonPlayer::GetTable(DWORD dwVnum)
{
	TNonPlayerDataMap::iterator itor = m_NonPlayerDataMap.find(dwVnum);
	if (itor == m_NonPlayerDataMap.end())
		return NULL;
	return itor->second;
}

BYTE CPythonNonPlayer::GetEventType(DWORD dwVnum)
{
	const TMobTable * p = GetTable(dwVnum);
	if (!p)
	{
		return ON_CLICK_EVENT_NONE;
	}
	return p->bOnClickType;
}

#if defined(WJ_SHOW_MOB_INFO) && defined(ENABLE_SHOW_MOBLEVEL)
DWORD CPythonNonPlayer::GetMonsterLevel(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
		return 0;
	return c_pTable->bLevel;
}
#endif

#if defined(WJ_SHOW_MOB_INFO) && defined(ENABLE_SHOW_MOBAIFLAG)
bool CPythonNonPlayer::IsAggressive(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
		return 0;
	return (IS_SET(c_pTable->dwAIFlag, AIFLAG_AGGRESSIVE));
}
#endif

BYTE CPythonNonPlayer::GetEventTypeByVID(DWORD dwVID)
{
	CInstanceBase * pInstance = CPythonCharacterManager::Instance().GetInstancePtr(dwVID);
	if (NULL == pInstance)
	{
		return ON_CLICK_EVENT_NONE;
	}
	WORD dwVnum = pInstance->GetVirtualNumber();
	return GetEventType(dwVnum);
}

const char*	CPythonNonPlayer::GetMonsterName(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
	{
		static const char* sc_szEmpty="";
		return sc_szEmpty;
	}
	return c_pTable->szLocaleName;
}

bool CPythonNonPlayer::MonsterHasRaceFlag(DWORD dwVnum, const char * szSearchString)
{
	string raceFlagList[] = {"ANIMAL", "UNDEAD", "DEVIL", "HUMAN", "ORC", "MILGYO", "INSECT", "FIRE", "ICE", "DESERT", "TREE", "ATT_ELEC", "ATT_FIRE", "ATT_ICE", "ATT_WIND", "ATT_EARTH", "ATT_DARK"};
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
		return false;
	DWORD dwRaceFlag = c_pTable->dwRaceFlag;
	if (dwRaceFlag == 0)
		return false;
	string toSearchString("");
	string searchString(szSearchString);
	int tmpFlag;
	for (int i = 0; i < sizeof(raceFlagList) / sizeof(raceFlagList[0]); i++)
	{
		tmpFlag = static_cast<int>(pow(2.0, static_cast<double>(i)));
		if (dwRaceFlag & tmpFlag)
		{
			if (!!toSearchString.compare(""))
				toSearchString += ",";
			toSearchString += raceFlagList[i];
		}
	}
	size_t found = toSearchString.find(searchString);
	if (found != string::npos){
		return true;
	}
	return false;
}

DWORD CPythonNonPlayer::GetMonsterColor(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
		return 0;
	return c_pTable->dwMonsterColor;
}

DWORD CPythonNonPlayer::GetMonsterType(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable* c_pTable = GetTable(dwVnum);
	if (!c_pTable)
		return 0;
	return c_pTable->bType;
}

DWORD CPythonNonPlayer::GetMonsterRank(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable* c_pTable = GetTable(dwVnum);
	if (!c_pTable)
		return 0;
	return c_pTable->bRank;
}
	
void CPythonNonPlayer::GetMatchableMobList(int iLevel, int iInterval, TMobTableList * pMobTableList)
{
}

#ifdef ENABLE_SEND_TARGET_INFO
DWORD CPythonNonPlayer::GetMonsterMaxHP(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
	{
		DWORD dwMaxHP = 0;
		return dwMaxHP;
	}
	return c_pTable->dwMaxHP;
}

DWORD CPythonNonPlayer::GetMonsterRaceFlag(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
	{
		DWORD dwRaceFlag = 0;
		return dwRaceFlag;
	}
	return c_pTable->dwRaceFlag;
}

DWORD CPythonNonPlayer::GetMonsterDamage1(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
	{
		DWORD range = 0;
		return range;
	}
	return c_pTable->dwDamageRange[0];
}

DWORD CPythonNonPlayer::GetMonsterDamage2(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
	{
		DWORD range = 0;
		return range;
	}
	return c_pTable->dwDamageRange[1];
}

DWORD CPythonNonPlayer::GetMonsterExp(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
	{
		DWORD dwExp = 0;
		return dwExp;
	}
	return c_pTable->dwExp;
}

float CPythonNonPlayer::GetMonsterDamageMultiply(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
	{
		DWORD fDamMultiply = 0;
		return fDamMultiply;
	}
	return c_pTable->fDamMultiply;
}

DWORD CPythonNonPlayer::GetMonsterST(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
	{
		DWORD bStr = 0;
		return bStr;
	}
	return c_pTable->bStr;
}

DWORD CPythonNonPlayer::GetMonsterDX(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
	{
		DWORD bDex = 0;
		return bDex;
	}
	return c_pTable->bDex;
}

bool CPythonNonPlayer::IsMonsterStone(DWORD dwVnum)
{
	const CPythonNonPlayer::TMobTable * c_pTable = GetTable(dwVnum);
	if (!c_pTable)
	{
		DWORD bType = 0;
		return bType;
	}
	return c_pTable->bType == 2;
}
#endif

void CPythonNonPlayer::Clear()
{
}

void CPythonNonPlayer::Destroy()
{
	for (TNonPlayerDataMap::iterator itor=m_NonPlayerDataMap.begin(); itor!=m_NonPlayerDataMap.end(); ++itor)
	{
		delete itor->second;
	}
	m_NonPlayerDataMap.clear();
}

CPythonNonPlayer::CPythonNonPlayer()
{
	Clear();
}

CPythonNonPlayer::~CPythonNonPlayer(void)
{
	Destroy();
}
