//Lorderon Client Binary Dev by Lordbecvold
#pragma once
#include "Packet.h"
#if defined(WJ_COMBAT_ZONE)
enum
{
	COMBAT_ZONE_MAX_ROWS_RANKING = 11,
	COMBAT_ZONE_EMPTY_DATA = 999,
	COMBAT_ZONE_ACTION_OPEN_RANKING = 1,
	COMBAT_ZONE_ACTION_CHANGE_PAGE_RANKING = 2,
	COMBAT_ZONE_ACTION_PARTICIPATE = 3,
	COMBAT_ZONE_ACTION_LEAVE = 4,
	COMBAT_ZONE_ACTION_REQUEST_POTION = 5,
	COMBAT_ZONE_TYPE_RANKING_WEEKLY = 1,
	COMBAT_ZONE_TYPE_RANKING_ALL = 2,
};

class CPythonCombatZone
{
public:
	CPythonCombatZone(void);
	~CPythonCombatZone(void);
	void Initialize(TPacketGCCombatZoneRankingData p);
	void SendDataDays(DWORD m_vec_infoData[7][8], bool bIsOnline);
	TPacketGCCombatZoneRanking Request(int);
	static CPythonCombatZone* instance();
private:
	std::vector<TPacketGCCombatZoneRanking> m_vecRankingData;
	static CPythonCombatZone * curInstance;

};
#endif
