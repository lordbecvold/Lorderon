//Lorderon Server core Dev by Lordbecvold
#include "stdafx.h"
#include "desc.h"
#include "utils.h"
#include "config.h"
#include "char.h"
#include "item.h"
#include "char_manager.h"
#include "affect.h"
#include "start_position.h"
#include "p2p.h"
#include "db.h"
#include "skill.h"
#include "dungeon.h"
#include "castle.h"
#include <string>
#include <boost/algorithm/string/replace.hpp>
#include "desc_manager.h"
#include "buffer_manager.h"
#include "dev_log.h"
#include <fstream>
#include <algorithm>
#include <iostream>
#include "constants.h"
#include "questmanager.h"
#include "desc_client.h"
#include "sectree_manager.h"
#include "regen.h"
#include <boost/format.hpp>
#include "item_manager.h"
#include "profile.h"
#include "target.h"

CProfileManager::CProfileManager()
{ }

CProfileManager::~CProfileManager()
{ }

bool CProfileManager::GetExistName(const char* c_pszName)
{
	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT name FROM player.player WHERE name = '%s'", c_pszName));
	return (pMsg->Get()->uiNumRows);
}

DWORD CProfileManager::GetEmpire(const char* c_pszName)
{
	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT `empire` FROM player.player_index INNER JOIN player.player ON player.player.account_id = player.player_index.id WHERE player.player.`name` = '%s'", c_pszName));
	if (!pMsg->Get()->uiNumRows)
		return -1;
	return atoi(mysql_fetch_row(pMsg->Get()->pSQLResult)[0]);
}

std::string CProfileManager::GetGuild(const char* c_pszName)
{
	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT `id` FROM player.player WHERE name = '%s'", c_pszName));	
	std::auto_ptr<SQLMsg> pMsg2(DBManager::instance().DirectQuery("SELECT `guild_id` FROM player.guild_member WHERE pid = '%d'", atoi(mysql_fetch_row(pMsg->Get()->pSQLResult)[0])));
	if (!pMsg2->Get()->uiNumRows)
		return EMPTY_GUILD;
	std::auto_ptr<SQLMsg> pMsg3(DBManager::instance().DirectQuery("SELECT `name` FROM player.guild WHERE id = '%d'", atoi(mysql_fetch_row(pMsg2->Get()->pSQLResult)[0])));
	if (!pMsg3->Get()->uiNumRows)
		return EMPTY_GUILD;
	return mysql_fetch_row(pMsg3->Get()->pSQLResult)[0];
}

void CProfileManager::LoadProfileByName(LPCHARACTER ch, const char * c_pszName)
{
	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery("SELECT job, level, status, location, year, month, day FROM player.player WHERE name = '%s'", c_pszName));
	if (!pMsg->Get()->uiNumRows)
		return;
	MYSQL_ROW row = mysql_fetch_row(pMsg->Get()->pSQLResult);
	TPacketGCContactProfileLoad pack;
	pack.header = HEADER_GC_CONTACT_PROFILE_LOAD;
	strlcpy(pack.name, c_pszName, sizeof(pack.name));
	pack.job = atoi(row[0]);
	pack.level = atoi(row[1]);
	pack.empire = CProfileManager::instance().GetEmpire(c_pszName);
	strlcpy(pack.guild, CProfileManager::instance().GetGuild(c_pszName).c_str(), sizeof(pack.guild));
	strlcpy(pack.language, LANGUAGE_DEFAULT, sizeof(pack.language));	
	strlcpy(pack.status, row[2], sizeof(pack.status));	
	strlcpy(pack.location, row[3], sizeof(pack.location));
	strlcpy(pack.location, row[3], sizeof(pack.location));
	strlcpy(pack.year, row[4], sizeof(pack.year));
	strlcpy(pack.month, row[5], sizeof(pack.month));
	strlcpy(pack.day, row[6], sizeof(pack.day));
	ch->GetDesc()->Packet(&pack, sizeof(pack));
}

bool GetStateBirthDay(BYTE state)
{
	return (state == PROFILE_STATE_EDIT_BIRTHDAY_YEAR || state == PROFILE_STATE_EDIT_BIRTHDAY_MONTH || state == PROFILE_STATE_EDIT_BIRTHDAY_DAY);
}

void CProfileManager::Manager(LPCHARACTER ch, const char* c_pData)
{
	if (!ch)
		return;
	TPacketCGContactProfileManager * p = (TPacketCGContactProfileManager *)c_pData;
	if (p->state > PROFILE_STATE_MAX_NUM)
		return;
	if (!CProfileManager::instance().GetExistName(p->szTargetName))
		return;
	char szEscapedTargetName[CHAT_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(szEscapedTargetName, sizeof(szEscapedTargetName), p->szTargetName, strlen(p->szTargetName));
	char szEscapedString[CHAT_MAX_LEN * 2 + 1];
	DBManager::instance().EscapeString(szEscapedString, sizeof(szEscapedString), p->szText, strlen(p->szText));
	switch (p->state)
	{
		case PROFILE_STATE_LOAD:
			CProfileManager::instance().LoadProfileByName(ch, szEscapedTargetName);
			break;
		case PROFILE_STATE_EDIT_STATUS:
		case PROFILE_STATE_EDIT_LOCATION:
		case PROFILE_STATE_EDIT_BIRTHDAY_YEAR:
		case PROFILE_STATE_EDIT_BIRTHDAY_MONTH:
		case PROFILE_STATE_EDIT_BIRTHDAY_DAY:
		{
			if (GetStateBirthDay(p->state) && !isdigit(*szEscapedString) && !!strcmp(szEscapedString, "--"))
				return;
			static const char * c_strColumnSQL[5] = {
				"status","location","year","month","day"
			};
			DBManager::instance().Query("UPDATE player.player SET %s = '%s' WHERE id = '%d'", c_strColumnSQL[p->state - 2], szEscapedString, ch->GetPlayerID());
		}
		break;
		default:
			break;
	}
}
