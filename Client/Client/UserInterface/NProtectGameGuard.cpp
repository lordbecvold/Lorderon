//Lorderon Client Binary Dev by Lordbecvold
#include "StdAfx.h"
#include "NProtectGameGuard.h"
#ifdef USE_NPROTECT_GAMEGUARD

static struct GameGuard
{
	bool	 isInitError;
	bool	 isProcError;
	unsigned msg;
	unsigned arg;
} gs_gameGuard = {
	false, 0, 0,
};

#ifdef LOCALE_SERVICE_EUROPE
#include "NProtect/NPGameLibEU.h"
#pragma comment(lib, "NPGameLibEU_MT.lib")
CNPGameLib npgl("Metin2EU");
#endif
BOOL CALLBACK NPGameMonCallback(DWORD msg, DWORD arg)
{
	switch (msg)
    {
	case NPGAMEMON_COMM_ERROR:
	case NPGAMEMON_COMM_CLOSE:
	case NPGAMEMON_INIT_ERROR:
	case NPGAMEMON_SPEEDHACK:
	case NPGAMEMON_GAMEHACK_KILLED:
	case NPGAMEMON_GAMEHACK_DETECT:
	case NPGAMEMON_GAMEHACK_DOUBT:
		gs_gameGuard.msg = msg;
		gs_gameGuard.arg = arg;
		gs_gameGuard.isProcError = true;
		return false;
		break;
	}
	return true;
}

bool LocaleService_IsGameGuardError()
{
	return gs_gameGuard.isProcError;
}

bool LocaleService_InitGameGuard()
{
	unsigned result = npgl.Init();
	if (NPGAMEMON_SUCCESS != result)
	{
		gs_gameGuard.isInitError = true;
		gs_gameGuard.msg = result;
		return false;
	}
	return true;
}

bool LocaleService_RunGameGuard(HWND hWnd)
{
	npgl.SetHwnd(hWnd);
	return true;
}

void LocaleService_NoticeGameGuardInitError_HongKong()
{
	char msg[256];
	switch (gs_gameGuard.msg)
	{
		case NPGAMEMON_ERROR_EXIST:
			sprintf(msg, "ERROR 1 ");
			break;
		case NPGAMEMON_ERROR_GAME_EXIST:
			sprintf(msg, "ERROR  ");
			break;
		case NPGAMEMON_ERROR_INIT:
			sprintf(msg, "ERROR 3 ");
			break;
		case NPGAMEMON_ERROR_AUTH_GAMEGUARD:
		case NPGAMEMON_ERROR_NFOUND_GG:
		case NPGAMEMON_ERROR_AUTH_INI:
		case NPGAMEMON_ERROR_NFOUND_INI:
			sprintf(msg, "ERROR 4 ");
			break;
		case NPGAMEMON_ERROR_CRYPTOAPI:
			sprintf(msg, "ERROR 5 ");
			break;
		case NPGAMEMON_ERROR_EXECUTE:
			sprintf(msg, "ERROR 6 ");
			break;
		case NPGAMEMON_ERROR_ILLEGAL_PRG:
			sprintf(msg, "ERROR 7 ");
			break;
		case NPGMUP_ERROR_ABORT:
			sprintf(msg, "ERROR 8 ");
			break;
		case NPGMUP_ERROR_CONNECT:
		case NPGMUP_ERROR_DOWNCFG:
			sprintf(msg, "ERROR 9 ");
			break;
		case NPGMUP_ERROR_AUTH:
			sprintf(msg, "ERROR 10 ");
			break;
		case NPGAMEMON_ERROR_NPSCAN:
			sprintf(msg, "ERROR 11 ");
			break;
		default:
			sprintf(msg, "ERROR 12 ");
			break;
	}
	MessageBox(NULL, msg, "GAME ERROR", MB_OK);
}

void LocaleService_NoticeGameGuardInitError_International()
{
	char msg[256];
	switch (gs_gameGuard.msg)
	{
	case NPGAMEMON_ERROR_EXIST:
		sprintf(msg, "Game is already running.\nPlease reboot and restart the game.");
		break;
	case NPGAMEMON_ERROR_GAME_EXIST:
		sprintf(msg, "Game is already running.\nPlease restart the game.");
		break;
	case NPGAMEMON_ERROR_INIT:
		sprintf(msg, "Game has initial error.\nPlease kill other conflict programs and restart game.");
		break;
	case NPGAMEMON_ERROR_AUTH_GAMEGUARD:
	case NPGAMEMON_ERROR_NFOUND_GG:
	case NPGAMEMON_ERROR_AUTH_INI:
	case NPGAMEMON_ERROR_NFOUND_INI:
		sprintf(msg, "Game files are modified or deleted.\nPlease reinstall Game.");
		break;
	case NPGAMEMON_ERROR_CRYPTOAPI:
		sprintf(msg, "Game detects Windows system file error.\nPlease reinstall Internet Explorer(IE)");
		break;
	case NPGAMEMON_ERROR_EXECUTE:
		sprintf(msg, "Game running is failed.\nPlease reinstall Game.");
		break;
	case NPGAMEMON_ERROR_ILLEGAL_PRG:
		sprintf(msg, "Game detects Illegal Program.\nPlease kill other programs not needs and restart game");
		break;
	case NPGMUP_ERROR_ABORT:
		sprintf(msg, "Game update was canceled.\nWhen not connect, change the internal or private firewall settings");
		break;
	case NPGMUP_ERROR_CONNECT:
		sprintf(msg, "Game hooking is failed.\nPlease download newer anti-virus and check all system.");
		break;
	case NPGAMEMON_ERROR_GAMEGUARD:
		sprintf(msg, "Game has initial error or old game guard.\nPlease reinstall Game");
		break;
	case NPGMUP_ERROR_PARAM:
		sprintf(msg, "Game detects .ini file is modified.\nPlease reinstall Game");
		break;
	case NPGMUP_ERROR_INIT:
		sprintf(msg, "Game detects npgmup.des initial error.\nPlease delete Game Folder and reinstall Game");
		break;
	case NPGMUP_ERROR_DOWNCFG:
		sprintf(msg, "Game update server connection is failed.\nPlease restart or check private firewall settings.");
		break;
	case NPGMUP_ERROR_AUTH:
		sprintf(msg, "Game update is not completed.\nPlease pause anti-virus and restart game.");
		break;
	case NPGAMEMON_ERROR_NPSCAN:
		sprintf(msg, "Game virus-hacking checker loading is failed\nPlease check memory lack or virus.");
		break;
	default:
		sprintf(msg, "UnknownErrorCode: %d\nPlease send a letter that has *.erl in game folder to Game1@inca.co.kr", gs_gameGuard.msg);
		break;
	}
	MessageBox(NULL, msg, "Game Initiail Error", MB_OK);
}

void LocaleService_NoticeGameGuardProcError_HongKong()
{
	char msg[256];
	switch (gs_gameGuard.msg)
	{
		case NPGAMEMON_COMM_ERROR:
		case NPGAMEMON_COMM_CLOSE:
			return;
		case NPGAMEMON_INIT_ERROR:
			sprintf(msg, "GAME ERROR 1 : %lu", gs_gameGuard.arg);
			break;
		case NPGAMEMON_SPEEDHACK:
			sprintf(msg,  "GAME ERROR 2 ");
			break;
		case NPGAMEMON_GAMEHACK_KILLED:
			sprintf(msg,  "GAME ERROR 3 ");
			break;
		case NPGAMEMON_GAMEHACK_DETECT:
			sprintf(msg,  "GAME ERROR 4 ");
			break;
		case NPGAMEMON_GAMEHACK_DOUBT:
			sprintf(msg,  "GAME ERROR 5 ");
			break;
	}
	MessageBox(NULL, msg, "GAME Error MB", MB_OK);
}

void LocaleService_NoticeGameGuardProcError_International()
{
	char msg[256];
	switch (gs_gameGuard.msg)
	{
	case NPGAMEMON_COMM_ERROR:
	case NPGAMEMON_COMM_CLOSE:
		break;
	case NPGAMEMON_INIT_ERROR:
		wsprintf(msg, "GAME has initial error : %lu", gs_gameGuard.arg);
		break;
	case NPGAMEMON_SPEEDHACK:
		wsprintf(msg, "GAME detects SpeedHack");
		break;
	case NPGAMEMON_GAMEHACK_KILLED:
		wsprintf(msg, "GAME detects GameHack\r\n%s", npgl.GetInfo());
		break;
	case NPGAMEMON_GAMEHACK_DETECT:
		wsprintf(msg, "GAME detects GameHack\r\n%s", npgl.GetInfo());
		break;
	case NPGAMEMON_GAMEHACK_DOUBT:
		wsprintf(msg, "Game or Gamguard was modified.");
		break;
	}
	MessageBox(NULL, msg, "GAME Error", MB_OK);
}

void LocaleService_NoticeGameGuardMessasge()
{
	if (gs_gameGuard.isInitError)
	{
		if (LocaleService_IsHONGKONG())
			LocaleService_NoticeGameGuardInitError_HongKong();
		else
			LocaleService_NoticeGameGuardInitError_International();
	}
	else if (gs_gameGuard.isProcError)
	{
		if (LocaleService_IsHONGKONG())
			LocaleService_NoticeGameGuardProcError_HongKong();
		else
			LocaleService_NoticeGameGuardProcError_International();
	}
}
#endif 
