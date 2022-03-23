//Lorderon server core Dev by Lordbecvold
const static int nBATTLE_ARENA_MAP[] = { 0, 190, 191, 192 };
const static std::string strRegen[] =
{
	"",
	"/battlearena01/regen00.txt",
	"/battlearena02/regen00.txt",
	"/battlearena03/regen00.txt",
};

enum BATTLEARENA_STATUS
{
	STATUS_CLOSE = 0,
	STATUS_BATTLE,
	STATUS_END,
};

class CBattleArena : public singleton<CBattleArena>
{
	private :
		LPEVENT m_pEvent;
		BATTLEARENA_STATUS m_status;
		int m_nMapIndex;
		int m_nEmpire;
		bool m_bForceEnd;

	public :
		CBattleArena();
		static bool IsBattleArenaMap(int nMapIndex);
		bool IsRunning();
		void SetStatus(BATTLEARENA_STATUS status);
		bool Start(int nEmpire);
		void ForceEnd();
		void End();
		void SpawnLastBoss();
		void SpawnRandomStone();
};
