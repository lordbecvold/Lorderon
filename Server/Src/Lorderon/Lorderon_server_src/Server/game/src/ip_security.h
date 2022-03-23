//Lorderon server core Dev by Lordbecvold
//ADD INTO GAME SOURCE
#ifdef ENABLE_IP_SECURITY
class CIPSecurity : public singleton<CIPSecurity>
{
	public :
		CIPSecurity();
		bool isMatchIP(const char* pLogin, const char* pIP);
};
#endif