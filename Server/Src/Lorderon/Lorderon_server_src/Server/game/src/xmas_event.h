//Lorderon Server Core Dev by Lordbecvold
#ifndef __INC_XMAS_EVENT_H
#define __INC_XMAS_EVENT_H
namespace xmas
{
	enum
	{
		MOB_SANTA_VNUM = 20031,	
		MOB_XMAS_TREE_VNUM = 20032,
	};
	void ProcessEventFlag(const std::string& name, int prev_value, int value);
	void SpawnSanta(long lMapIndex, int iTimeGapSec);
	void SpawnEventHelper(bool spawn);
}
#endif
