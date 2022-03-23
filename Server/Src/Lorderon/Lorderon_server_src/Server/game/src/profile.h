//Lorderon Server core Dev by Lordbecvold
#define LANGUAGE_DEFAULT "en"
#define EMPTY_GUILD ""

enum EProfileSetter
{
	PROFILE_STATE_LOAD = 1,
	PROFILE_STATE_EDIT_STATUS = 2,
	PROFILE_STATE_EDIT_LOCATION = 3,
	PROFILE_STATE_EDIT_BIRTHDAY_YEAR = 4,
	PROFILE_STATE_EDIT_BIRTHDAY_MONTH = 5,
	PROFILE_STATE_EDIT_BIRTHDAY_DAY = 6,
	PROFILE_STATE_MAX_NUM = 6,
};

class CProfileManager : public singleton<CProfileManager>
{
	public:
		CProfileManager();
		~CProfileManager();
		void Manager(LPCHARACTER ch, const char* c_pData);
		void LoadProfileByName(LPCHARACTER ch, const char * c_pszName);
		bool GetExistName(const char* c_pszName);
		DWORD GetEmpire(const char* c_pszName);
		std::string GetGuild(const char* c_pszName);
};