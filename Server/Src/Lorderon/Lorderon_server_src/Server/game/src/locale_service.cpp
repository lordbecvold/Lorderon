//Lorderon server core Dev by Lordbecvold
#include "stdafx.h"
#include "locale_service.h"
#include "constants.h"
#include "banword.h"
#include "utils.h"
#include "mob_manager.h"
#include "empire_text_convert.h"
#include "config.h"
#include "skill_power.h"
#include "../../common/CommonDefines.h"
using namespace std;
extern string g_stQuestDir;
extern set<string> g_setQuestObjectDir;
string g_stServiceName;
string g_stServiceBasePath = ".";
string g_stServiceMapPath = "data/map";
string g_stLocale = "euckr";
string g_stLocaleFilename;
BYTE PK_PROTECT_LEVEL = 30;
string g_stLocal = "";
eLocalization g_eLocalType = LC_NOSET;
int (*check_name) (const char * str) = NULL;
int (*is_twobyte) (const char * str) = NULL;
bool LC_InitLocalization( const std::string& szLocal );

int is_twobyte_euckr(const char * str)
{
	return ishan(*str);
}

int is_twobyte_gb2312(const char * str)
{
	if (!str || !*str)
		return 0;
	BYTE b1 = str[0];
	BYTE b2 = str[1];
	if (!(b1 & 0x80))
		return 0;
	if (b1 < 0xb0 || b1 > 0xf7 || b2 < 0xa1 || b2 > 0xfe)
		return 0;
	return 1;
}

int is_twobyte_big5(const char * str)
{
	if (!str || !*str)
		return 0;
	BYTE b1 = str[0];
	BYTE b2 = str[1];
	BYTE b[2];
	b[0] = b2;
	b[1] = b1;
	WORD b12 = 0;
	memcpy(&b12, b, 2);
	if (!(b1 & 0x80))
		return 0;
	if ((b12 < 0xa440 || b12 > 0xc67e) && (b12 < 0xc940 || b12 > 0xf9d5))
	{
		if (test_server)
		{
			sys_log(0, "twobyte_big5 %x %x", b1, b2);
		}
		return 0;
	}
	return 1;
}

int check_name_independent(const char * str)
{
	if (CBanwordManager::instance().CheckString(str, strlen(str)))
		return 0;
	char szTmp[256];
	str_lower(str, szTmp, sizeof(szTmp));
	if (CMobManager::instance().Get(szTmp, false))
		return 0;
	return 1;
}

int check_name_gb2312(const char * str)
{
	static const BYTE exceptions[5][2] =
	{
		{ 0xd7, 0xfa },
		{ 0xd7, 0xfb },
		{ 0xd7, 0xfc },
		{ 0xd7, 0xfd },
		{ 0xd7, 0xfe }
	};
	int i, j;
	BYTE b1, b2;
	if (!str || !*str)
		return 0;
	i = 0;
	size_t len = 0;
	while (str[i])
	{
		if (str[i] & 0x80)
		{
			if (!str[i + 1])
				return 0;
			b1 = str[i++];
			b2 = str[i++];
			if (b1 < 0xb0 || b1 > 0xf7 || b2 < 0xa1 || b2 > 0xfe)
				return 0;
			for (j = 0; j < 5; j++)
				if (b1 == exceptions[j][0] && b2 == exceptions[j][1])
					return 0;
			len++;
		}
		else
		{
			if (!isdigit(str[i]) && !isalpha(str[i]))
				return 0;
			i++;
			len++;
		}
	}
	if ( len > 6 ) return 0;
	return check_name_independent(str);
}

int check_name_big5(const char * str )
{
	int i;
	BYTE b1, b2;
	if (!str || !*str)
		return 0;
	i = 0;
	while (str[i])
	{
		if (str[i] & 0x80)
		{
			if (!str[i + 1])
				return 0;
			b1 = str[i++];
			b2 = str[i++];
			BYTE b[2];
			b[0] = b2;
			b[1] = b1;
			WORD b12 = 0;
			memcpy(&b12, b, 2);
			if ((b12 < 0xa440 || b12 > 0xc67e) && (b12 < 0xc940 || b12 > 0xf9d5))
			{
				if (test_server)
					sys_log(0, "check_name_big5[%d][%s] %x %x %x", i - 2, str, b1, b2, b12);
				return 0;
			}
		}
		else
		{
			if (!isdigit(str[i]) && !isalpha(str[i]))
				return 0;

			i++;
		}
	}
	return check_name_independent(str);
}

int check_name_euckr(const char * str)
{
	int code;
	const char*	tmp;
	if (!str || !*str)
		return 0;
	if ( strlen(str) < 2 || strlen(str) > 12 )
		return 0;
	for (tmp = str; *tmp; ++tmp)
	{
		if (isnhspace(*tmp))
			return 0;
		if (isnhdigit(*tmp))
			continue;
		if (!ishan(*tmp) && isalpha(*tmp))
			continue;
		code = *tmp;
		code += 256;
		if (code < 176 || code > 200)
			return 0;
		++tmp;
		if (!*tmp)
			break;
	}
	return check_name_independent(str);
}

int check_name_latin1(const char * str)
{
	int code;
	const char*	tmp;
	if (!str || !*str)
		return 0;
	if (strlen(str) < 2)
		return 0;
	for (tmp = str; *tmp; ++tmp)
	{
		if (isnhspace(*tmp))
			return 0;
		if (isnhdigit(*tmp))
			continue;
		if (!ishan(*tmp) && isalpha(*tmp))
			continue;
		unsigned char uc_tmp = *tmp;
		if (uc_tmp == 145 || uc_tmp == 146 || uc_tmp == 196 || uc_tmp == 214 || uc_tmp == 220 || uc_tmp == 223 || uc_tmp == 228 || uc_tmp == 246 || uc_tmp == 252 )
			continue;
		code = *tmp;
		code += 256;
		if (code < 176 || code > 200)
			return 0;
		++tmp;
		if (!*tmp)
			break;
	}
	return check_name_independent(str);
}

int check_name_alphabet(const char * str)
{
	const char*	tmp;
	if (!str || !*str)
		return 0;
	if (strlen(str) < 2)
		return 0;
	for (tmp = str; *tmp; ++tmp)
	{
		if (isdigit(*tmp) || isalpha(*tmp))
			continue;
		else
			return 0;
	}
	return check_name_independent(str);
}

bool sjis_is_disable_name_char(const char* src)
{
	static const char* sjis_symbols = "?";
	if (strncmp(src, sjis_symbols, 2) == 0)
		return true;
	return false;
}

#define issjishead(c) ((0x81<=(c) && (c)<=0x9f) || \
		                               ((0xe0<=(c)) && (c)<=0xfc))
#define issjistail(c) ((0x40<=(c) && (c)<=0x7e) || \
		                               (0x80<=(c) && (c)<=0xfc))

static int is_char_sjis(const char *p, const char *e)
{
	return (issjishead((BYTE) *p) && (e-p)>1 && issjistail((BYTE)p[1]) ? true : false);
}

int is_twobyte_sjis(const char *str)
{
	if (str && str[0] && str[1])
		return issjishead((BYTE)str[0]) && issjistail((BYTE)str[1]);
	else
		return 0;
}

int check_name_sjis(const char *str)
{
	const char	*p = str;
	const char	*e = str + strlen(str);	
	if ( strlen(str) < 2 || strlen(str) > 16 )
		return 0;
	while (*p)
	{
		if (is_char_sjis(p, e))
		{
			if (sjis_is_disable_name_char(p))
				return false;
			if ((BYTE)p[0]==0x81 && (BYTE)p[1]==0x40) return false;
			p += 2;
			continue;
		}
		else
		{
			if (isalpha(*p) || isdigit(*p))
			{
				p += 1;
				continue;
			}
			else
			{
				return 0;
			}
		}
	}
	return check_name_independent(str);
}

void LocaleService_LoadLocaleStringFile()
{
	if (g_stLocaleFilename.empty())
		return;
	if (g_bAuthServer)
		return;
	fprintf(stderr, "LocaleService %s\n", g_stLocaleFilename.c_str());
	locale_init(g_stLocaleFilename.c_str());
}

void LocaleService_LoadEmpireTextConvertTables()
{
	char szFileName[256];
	for (int iEmpire = 1; iEmpire <= 3; ++iEmpire)
	{
		snprintf(szFileName, sizeof(szFileName), "%s/lang%d.cvt", LocaleService_GetBasePath().c_str(), iEmpire);
		sys_log(0, "Load %s", szFileName);
		LoadEmpireTextConvertTable(iEmpire, szFileName);
	}
}

static void __LocaleService_Init_DEFAULT()
{
	g_stLocaleFilename = "";
	g_stServiceBasePath = "locale/" + g_stServiceName;
	g_stServiceMapPath = g_stServiceBasePath + "/map";
	g_stQuestDir = g_stServiceBasePath + "/quest";
	g_setQuestObjectDir.clear();
	g_setQuestObjectDir.insert(g_stQuestDir + "/object");
}

static void __LocaleService_Init_YMIR()
{
	g_stLocaleFilename = "";
	g_stServiceBasePath = "locale/" + g_stServiceName;
	g_stServiceMapPath = g_stServiceBasePath + "/map";
	g_stQuestDir = g_stServiceBasePath + "/quest";
	g_setQuestObjectDir.clear();
	g_setQuestObjectDir.insert(g_stQuestDir + "/object");
	PK_PROTECT_LEVEL = 30;
}

static void __LocaleService_Init_Czech()
{
	g_stLocale="latin2";
	g_stServiceBasePath = "locale/czech";
	g_stQuestDir = "locale/czech/quest";
	g_stServiceMapPath = "locale/czech/map";
	g_setQuestObjectDir.clear();
	g_setQuestObjectDir.insert("locale/czech/quest/object");
	g_stLocaleFilename = "locale/czech/locale_string.txt";
	g_iUseLocale = TRUE;
	check_name = check_name_alphabet;
	PK_PROTECT_LEVEL = 15;
}

static void __CheckPlayerSlot(const std::string& service_name)
{
#ifndef ENABLE_PLAYER_PER_ACCOUNT5
	if (PLAYER_PER_ACCOUNT != 4)
	{
		printf("<ERROR> PLAYER_PER_ACCOUNT = %d\n", PLAYER_PER_ACCOUNT);
		exit(0);
	}
#endif
}

bool LocaleService_Init(const std::string& c_rstServiceName)
{
	if (!g_stServiceName.empty())
	{
		sys_err("ALREADY exist service");
		return false;
	}
	g_stServiceName = c_rstServiceName;
	if ( "ymir" == g_stServiceName)
	{
		__LocaleService_Init_YMIR();
	}
	else if ( "czech" == g_stServiceName)
	{
		__LocaleService_Init_Czech();
	}
	else
	{
		__LocaleService_Init_DEFAULT();
	}
	fprintf(stdout, "Setting Locale \"%s\" (Path: %s)\n", g_stServiceName.c_str(), g_stServiceBasePath.c_str());
	__CheckPlayerSlot(g_stServiceName);
	if (false == LC_InitLocalization(c_rstServiceName))
		return false;
	return true;
}

void LocaleService_TransferDefaultSetting()
{
	if (!check_name)
		check_name = check_name_euckr;
	if (!is_twobyte)
		is_twobyte = is_twobyte_euckr;
	if (!exp_table)
		exp_table = exp_table_common;
	if (!CTableBySkill::instance().Check())
		exit(1);
	if (!aiPercentByDeltaLevForBoss)
		aiPercentByDeltaLevForBoss = aiPercentByDeltaLevForBoss_euckr;
	if (!aiPercentByDeltaLev)
		aiPercentByDeltaLev = aiPercentByDeltaLev_euckr;
	if (!aiChainLightningCountBySkillLevel)
		aiChainLightningCountBySkillLevel = aiChainLightningCountBySkillLevel_euckr;
}

const std::string& LocaleService_GetBasePath()
{
	return g_stServiceBasePath;
}

const std::string& LocaleService_GetMapPath()
{
	return g_stServiceMapPath;
}

const std::string& LocaleService_GetQuestPath()
{
	return g_stQuestDir;
}

bool LC_InitLocalization( const std::string& szLocal )
{
	g_stLocal = szLocal;
	if ( !g_stLocal.compare("ymir") )
		g_eLocalType = LC_YMIR;
	else if ( !g_stLocal.compare("czech") )
		g_eLocalType = LC_CZECH;
	else
		return false;
	return true;
}

eLocalization LC_GetLocalType()
{
	return g_eLocalType;
}

bool LC_IsLocale( const eLocalization t )
{
	return LC_GetLocalType() == t ? true : false;
}

bool LC_IsYMIR() { return LC_GetLocalType() == LC_YMIR ? true : false; }

bool LC_IsEurope()
{
	eLocalization val = LC_GetLocalType();
	switch ((int) val)
	{
		case LC_GERMANY:
		case LC_FRANCE:
		case LC_ITALY:
		case LC_TURKEY:
		case LC_POLAND:
		case LC_UK:
		case LC_SPAIN:
		case LC_PORTUGAL:
		case LC_GREEK:
		case LC_RUSSIA:
		case LC_DENMARK:
		case LC_BULGARIA:
		case LC_CROATIA:
		case LC_MEXICO: 
		case LC_ARABIA: 
		case LC_CZECH:
		case LC_ROMANIA:
		case LC_HUNGARY:
		case LC_NETHERLANDS:
		case LC_USA:
		case LC_WE_KOREA:	
		case LC_TAIWAN:		
		case LC_JAPAN:		
		case LC_NEWCIBN:
		case LC_CANADA:	
			return true;
	}
	return false;
}
