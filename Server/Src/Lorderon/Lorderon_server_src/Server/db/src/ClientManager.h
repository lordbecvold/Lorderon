//Lorderon Server Core Dev by Lordbecvold
#ifndef __INC_CLIENTMANAGER_H__
#define __INC_CLIENTMANAGER_H__
#include <boost/unordered_map.hpp>
#include <boost/unordered_set.hpp>
#include "../../common/stl.h"
#include "../../common/building.h"
#include "../../common/auction_table.h"
#include "Peer.h"
#include "DBManager.h"
#include "LoginData.h"

#define ENABLE_PROTO_FROM_DB

class CPlayerTableCache;
class CItemCache;
class CItemPriceListTableCache;

class CPacketInfo
{
    public:
	void Add(int header);
	void Reset();
	std::map<int, int> m_map_info;
};

size_t CreatePlayerSaveQuery(char * pszQuery, size_t querySize, TPlayerTable * pkTab);

class CClientManager : public CNetBase, public singleton<CClientManager>
{
    public:
	typedef std::list<CPeer *> TPeerList;
	typedef boost::unordered_map<DWORD, CPlayerTableCache *> TPlayerTableCacheMap;
	typedef boost::unordered_map<DWORD, CItemCache *> TItemCacheMap;
	typedef boost::unordered_set<CItemCache *, boost::hash<CItemCache*> > TItemCacheSet;
	typedef boost::unordered_map<DWORD, TItemCacheSet *> TItemCacheSetPtrMap;
	typedef boost::unordered_map<DWORD, CItemPriceListTableCache*> TItemPriceListCacheMap;
	typedef boost::unordered_map<short, BYTE> TChannelStatusMap;
	typedef std::pair< DWORD, DWORD > TItemPricelistReqInfo;

	class ClientHandleInfo
	{
	    public:
			DWORD dwHandle;
			DWORD account_id;
			DWORD player_id;
			BYTE account_index;
			char login[LOGIN_MAX_LEN + 1];
			char safebox_password[SAFEBOX_PASSWORD_MAX_LEN + 1];
			char ip[MAX_HOST_LENGTH + 1];
			TAccountTable * pAccountTable;
			TSafeboxTable * pSafebox;

		ClientHandleInfo(DWORD argHandle, DWORD dwPID = 0)
		{
		    dwHandle = argHandle;
		    pSafebox = NULL;
		    pAccountTable = NULL;
		    player_id = dwPID;
		};
		ClientHandleInfo(DWORD argHandle, DWORD dwPID, DWORD accountId)
		{
		    dwHandle = argHandle;
		    pSafebox = NULL;
		    pAccountTable = NULL;
		    player_id = dwPID;
			account_id = accountId;
		};

		~ClientHandleInfo()
		{
		    if (pSafebox)
			{
				delete pSafebox;
				pSafebox = NULL;
			}
		}
	};

	public:
		CClientManager();
		~CClientManager();
		bool Initialize();
		time_t GetCurrentTime();
		void MainLoop();
		void Quit();
#ifdef OFFLINE_SHOP
		void ShopName(CPeer * peer, TPacketShopName * p);
		void ShopClose(CPeer * peer, TPacketShopClose *p);
		void ShopUpdateItem(CPeer * peer, TPacketShopUpdateItem *p);
#endif
		void GetPeerP2PHostNames(std::string& peerHostNames);
		void SetTablePostfix(const char* c_pszTablePostfix);
		void SetPlayerIDStart(int iIDStart);
		int	GetPlayerIDStart() { return m_iPlayerIDStart; }
		int	GetPlayerDeleteLevelLimit() { return m_iPlayerDeleteLevelLimit; }
		void SetChinaEventServer(bool flag) { m_bChinaEventServer = flag; }
		bool IsChinaEventServer() { return m_bChinaEventServer; }
		DWORD GetUserCount();	
		void SendAllGuildSkillRechargePacket();
		void SendTime();
		CPlayerTableCache *	GetPlayerCache(DWORD id);
		void PutPlayerCache(TPlayerTable * pNew);
		void CreateItemCacheSet(DWORD dwID);
		TItemCacheSet * GetItemCacheSet(DWORD dwID);
		void FlushItemCacheSet(DWORD dwID);
		CItemCache * GetItemCache(DWORD id);
		void PutItemCache(TPlayerItem * pNew, bool bSkipQuery = false);
		bool DeleteItemCache(DWORD id);
		void UpdatePlayerCache();
		void UpdateItemCache();
		CItemPriceListTableCache* GetItemPriceListCache(DWORD dwID);
		void PutItemPriceListCache(const TItemPriceListTable* pItemPriceList);
		void UpdateItemPriceListCache(void);
		void SendGuildSkillUsable(DWORD guild_id, DWORD dwSkillVnum, bool bUsable);
		void SetCacheFlushCountLimit(int iLimit);
		template <class Func>
		Func for_each_peer(Func f);
		CPeer *	GetAnyPeer();
		void ForwardPacket(BYTE header, const void* data, int size, BYTE bChannel = 0, CPeer * except = NULL);
		void SendNotice(const char * c_pszFormat, ...);
		char* GetCommand(char* str, char* command);		
		void ItemAward(CPeer * peer, char* login);	

    protected:
		void Destroy();

    private:
		bool InitializeTables();
		bool InitializeShopTable();
		bool InitializeMobTable();
		bool InitializeItemTable();
		bool InitializeQuestItemTable();
		bool InitializeSkillTable();
		bool InitializeRefineTable();
		bool InitializeBanwordTable();
		bool InitializeItemAttrTable();
		bool InitializeItemRareTable();
		bool InitializeLandTable();
		bool InitializeObjectProto();
		bool InitializeObjectTable();
		bool InitializeMonarch();
		bool MirrorMobTableIntoDB();
		bool MirrorItemTableIntoDB();
		void AddPeer(socket_t fd);
		void RemovePeer(CPeer * pPeer);
		CPeer *	GetPeer(IDENT ident);
		int AnalyzeQueryResult(SQLMsg * msg);
		int AnalyzeErrorMsg(CPeer * peer, SQLMsg * msg);
		int Process();
	    void ProcessPackets(CPeer * peer);
		CLoginData * GetLoginData(DWORD dwKey);
		CLoginData * GetLoginDataByLogin(const char * c_pszLogin);
		CLoginData * GetLoginDataByAID(DWORD dwAID);
		void InsertLoginData(CLoginData * pkLD);
		void DeleteLoginData(CLoginData * pkLD);
		bool InsertLogonAccount(const char * c_pszLogin, DWORD dwHandle, const char * c_pszIP);
		bool DeleteLogonAccount(const char * c_pszLogin, DWORD dwHandle);
		bool FindLogonAccount(const char * c_pszLogin);
		void GuildCreate(CPeer * peer, DWORD dwGuildID);
		void GuildSkillUpdate(CPeer * peer, TPacketGuildSkillUpdate* p);
		void GuildExpUpdate(CPeer * peer, TPacketGuildExpUpdate* p);
		void GuildAddMember(CPeer * peer, TPacketGDGuildAddMember* p);
		void GuildChangeGrade(CPeer * peer, TPacketGuild* p);
		void GuildRemoveMember(CPeer * peer, TPacketGuild* p);
		void GuildChangeMemberData(CPeer * peer, TPacketGuildChangeMemberData* p);
		void GuildDisband(CPeer * peer, TPacketGuild * p);
		void GuildWar(CPeer * peer, TPacketGuildWar * p);
		void GuildWarScore(CPeer * peer, TPacketGuildWarScore * p);
		void GuildChangeLadderPoint(TPacketGuildLadderPoint* p);
		void GuildUseSkill(TPacketGuildUseSkill* p);
		void GuildDepositMoney(TPacketGDGuildMoney* p);
		void GuildWithdrawMoney(CPeer* peer, TPacketGDGuildMoney* p);
		void GuildWithdrawMoneyGiveReply(TPacketGDGuildMoneyWithdrawGiveReply* p);
		void GuildWarBet(TPacketGDGuildWarBet * p);
		void GuildChangeMaster(TPacketChangeGuildMaster* p);
		void SetGuildWarEndTime(DWORD guild_id1, DWORD guild_id2, time_t tEndTime);
		void QUERY_BOOT(CPeer * peer, TPacketGDBoot * p);
		void QUERY_LOGIN(CPeer * peer, DWORD dwHandle, SLoginPacket* data);
		void QUERY_LOGOUT(CPeer * peer, DWORD dwHandle, const char *);
		void RESULT_LOGIN(CPeer * peer, SQLMsg *msg);
		void QUERY_PLAYER_LOAD(CPeer * peer, DWORD dwHandle, TPlayerLoadPacket*);
		void RESULT_COMPOSITE_PLAYER(CPeer * peer, SQLMsg * pMsg, DWORD dwQID);
		void RESULT_PLAYER_LOAD(CPeer * peer, MYSQL_RES * pRes, ClientHandleInfo * pkInfo);
		void RESULT_ITEM_LOAD(CPeer * peer, MYSQL_RES * pRes, DWORD dwHandle, DWORD dwPID);
		void RESULT_QUEST_LOAD(CPeer * pkPeer, MYSQL_RES * pRes, DWORD dwHandle, DWORD dwPID);
		void RESULT_AFFECT_LOAD(CPeer * pkPeer, MYSQL_RES * pRes, DWORD dwHandle, DWORD dwRealPID);
		void RESULT_PLAYER_INDEX_CREATE(CPeer *pkPeer, SQLMsg *msg);
		void RESULT_PRICELIST_LOAD(CPeer* peer, SQLMsg* pMsg);
		void RESULT_PRICELIST_LOAD_FOR_UPDATE(SQLMsg* pMsg);
		void QUERY_PLAYER_SAVE(CPeer * peer, DWORD dwHandle, TPlayerTable*);
		void __QUERY_PLAYER_CREATE(CPeer * peer, DWORD dwHandle, TPlayerCreatePacket *);
		void __QUERY_PLAYER_DELETE(CPeer * peer, DWORD dwHandle, TPlayerDeletePacket *);
		void __RESULT_PLAYER_DELETE(CPeer * peer, SQLMsg* msg);
		void QUERY_PLAYER_COUNT(CPeer * pkPeer, TPlayerCountPacket *);
		void QUERY_ITEM_SAVE(CPeer * pkPeer, const char * c_pData);
		void QUERY_ITEM_DESTROY(CPeer * pkPeer, const char * c_pData);
		void QUERY_ITEM_FLUSH(CPeer * pkPeer, const char * c_pData);
		void QUERY_QUEST_SAVE(CPeer * pkPeer, TQuestTable *, DWORD dwLen);
		void QUERY_ADD_AFFECT(CPeer * pkPeer, TPacketGDAddAffect * p);
		void QUERY_REMOVE_AFFECT(CPeer * pkPeer, TPacketGDRemoveAffect * p);
		void QUERY_SAFEBOX_LOAD(CPeer * pkPeer, DWORD dwHandle, TSafeboxLoadPacket *, bool bMall);
		void QUERY_SAFEBOX_SAVE(CPeer * pkPeer, TSafeboxTable * pTable);
		void QUERY_SAFEBOX_CHANGE_SIZE(CPeer * pkPeer, DWORD dwHandle, TSafeboxChangeSizePacket * p);
		void QUERY_SAFEBOX_CHANGE_PASSWORD(CPeer * pkPeer, DWORD dwHandle, TSafeboxChangePasswordPacket * p);
		void RESULT_SAFEBOX_LOAD(CPeer * pkPeer, SQLMsg * msg);
		void RESULT_SAFEBOX_CHANGE_SIZE(CPeer * pkPeer, SQLMsg * msg);
		void RESULT_SAFEBOX_CHANGE_PASSWORD(CPeer * pkPeer, SQLMsg * msg);
		void RESULT_SAFEBOX_CHANGE_PASSWORD_SECOND(CPeer * pkPeer, SQLMsg * msg);
		void QUERY_EMPIRE_SELECT(CPeer * pkPeer, DWORD dwHandle, TEmpireSelectPacket * p);
		void QUERY_SETUP(CPeer * pkPeer, DWORD dwHandle, const char * c_pData);
		void SendPartyOnSetup(CPeer * peer);
		void QUERY_HIGHSCORE_REGISTER(CPeer * peer, TPacketGDHighscore* data);
		void RESULT_HIGHSCORE_REGISTER(CPeer * pkPeer, SQLMsg * msg);
		void QUERY_FLUSH_CACHE(CPeer * pkPeer, const char * c_pData);
		void QUERY_PARTY_CREATE(CPeer * peer, TPacketPartyCreate* p);
		void QUERY_PARTY_DELETE(CPeer * peer, TPacketPartyDelete* p);
		void QUERY_PARTY_ADD(CPeer * peer, TPacketPartyAdd* p);
		void QUERY_PARTY_REMOVE(CPeer * peer, TPacketPartyRemove* p);
		void QUERY_PARTY_STATE_CHANGE(CPeer * peer, TPacketPartyStateChange* p);
		void QUERY_PARTY_SET_MEMBER_LEVEL(CPeer * peer, TPacketPartySetMemberLevel* p);
		void QUERY_RELOAD_PROTO();
		void QUERY_CHANGE_NAME(CPeer * peer, DWORD dwHandle, TPacketGDChangeName * p);
		void GetPlayerFromRes(TPlayerTable * player_table, MYSQL_RES* res);
		void QUERY_SMS(CPeer * pkPeer, TPacketGDSMS * p);
		void QUERY_LOGIN_KEY(CPeer * pkPeer, TPacketGDLoginKey * p);
		void AddGuildPriv(TPacketGiveGuildPriv* p);
		void AddEmpirePriv(TPacketGiveEmpirePriv* p);
		void AddCharacterPriv(TPacketGiveCharacterPriv* p);
		void MoneyLog(TPacketMoneyLog* p);
		void QUERY_AUTH_LOGIN(CPeer * pkPeer, DWORD dwHandle, TPacketGDAuthLogin * p);
#if defined(WJ_COMBAT_ZONE)	
		void CombatZoneResetRanking(const TPacketGDCombatZoneResetRanking* p);
		void UpdateSkillsCache(const TPacketGDCombatZoneSkillsCache* p);
#endif
		void QUERY_LOGIN_BY_KEY(CPeer * pkPeer, DWORD dwHandle, TPacketGDLoginByKey * p);
		void RESULT_LOGIN_BY_KEY(CPeer * peer, SQLMsg * msg);
		void ChargeCash(const TRequestChargeCash * p);
		void LoadEventFlag();
		void SetEventFlag(TPacketSetEventFlag* p);
		void SendEventFlagsOnSetup(CPeer* peer);
		void BillingExpire(TPacketBillingExpire * p);
		void BillingCheck(const char * data);
		void SendAllLoginToBilling();
		void SendLoginToBilling(CLoginData * pkLD, bool bLogin);
		void MarriageAdd(TPacketMarriageAdd * p);
		void MarriageUpdate(TPacketMarriageUpdate * p);
		void MarriageRemove(TPacketMarriageRemove * p);
		void WeddingRequest(TPacketWeddingRequest * p);
		void WeddingReady(TPacketWeddingReady * p);
		void WeddingEnd(TPacketWeddingEnd * p);
		void MyshopPricelistUpdate(const TItemPriceListTable* pPacket); 
		void MyshopPricelistRequest(CPeer* peer, DWORD dwHandle, DWORD dwPlayerID);
		void CreateObject(TPacketGDCreateObject * p);
		void DeleteObject(DWORD dwID);
		void UpdateLand(DWORD * pdw);
		void VCard(TPacketGDVCard * p);
		void VCardProcess();
		void BlockChat(TPacketBlockChat * p);

    private:
		int m_looping;
		socket_t m_fdAccept;	
		TPeerList m_peerList;
		CPeer * m_pkAuthPeer;
		typedef boost::unordered_map<DWORD, CLoginData *> TLoginDataByLoginKey;
		TLoginDataByLoginKey m_map_pkLoginData;
		typedef boost::unordered_map<std::string, CLoginData *> TLoginDataByLogin;
		TLoginDataByLogin m_map_pkLoginDataByLogin;
		typedef boost::unordered_map<DWORD, CLoginData *> TLoginDataByAID;
		TLoginDataByAID m_map_pkLoginDataByAID;
		typedef boost::unordered_map<std::string, CLoginData *> TLogonAccountMap;
		TLogonAccountMap m_map_kLogonAccount;
		int m_iPlayerIDStart;
		int m_iPlayerDeleteLevelLimit;
		int m_iPlayerDeleteLevelLimitLower;
		bool m_bChinaEventServer;
		std::vector<TMobTable> m_vec_mobTable;
		std::vector<TItemTable> m_vec_itemTable;
		std::map<DWORD, TItemTable *> m_map_itemTableByVnum;
		int m_iShopTableSize;
		TShopTable * m_pShopTable;
		int m_iRefineTableSize;
		TRefineTable * m_pRefineTable;
		std::vector<TSkillTable> m_vec_skillTable;
		std::vector<TBanwordTable> m_vec_banwordTable;
		std::vector<TItemAttrTable> m_vec_itemAttrTable;
		std::vector<TItemAttrTable> m_vec_itemRareTable;
		std::vector<building::TLand> m_vec_kLandTable;
		std::vector<building::TObjectProto>	m_vec_kObjectProto;
		std::map<DWORD, building::TObject *> m_map_pkObjectTable;
		std::queue<TPacketGDVCard> m_queue_vcard;
		bool m_bShutdowned;
		TPlayerTableCacheMap m_map_playerCache;  
		TItemCacheMap m_map_itemCache;  
		TItemCacheSetPtrMap m_map_pkItemCacheSetPtr;  
		TItemPriceListCacheMap m_mapItemPriceListCache;  
		TChannelStatusMap m_mChannelStatus;

		struct TPartyInfo
		{
		    BYTE bRole;
		    BYTE bLevel;
			TPartyInfo() :bRole(0), bLevel(0)
			{ }
		};

		typedef std::map<DWORD, TPartyInfo>	TPartyMember;
		typedef std::map<DWORD, TPartyMember> TPartyMap;
		typedef std::map<BYTE, TPartyMap> TPartyChannelMap;
		TPartyChannelMap m_map_pkChannelParty;
		typedef std::map<std::string, long>	TEventFlagMap;
		TEventFlagMap m_map_lEventFlag;
		BYTE m_bLastHeader;
		int m_iCacheFlushCount;
		int m_iCacheFlushCountLimit;

    private :
		TItemIDRangeTable m_itemRange;

    public :
		bool InitializeNowItemID();
		DWORD GetItemID();
		DWORD GainItemID();
		TItemIDRangeTable GetItemRange() { return m_itemRange; }

    public:
		bool InitializeLocalization();

    private:
		std::vector<tLocale> m_vec_Locale;
		bool __GetAdminInfo(const char *szIP, std::vector<tAdminInfo> & rAdminVec);
		bool __GetHostInfo(std::vector<std::string> & rIPVec);
		void ReloadAdmin(CPeer * peer, TPacketReloadAdmin * p);
		void BreakMarriage(CPeer * peer, const char * data);

		struct TLogoutPlayer
		{
		    DWORD	pid;
		    time_t	time;
		    bool operator < (const TLogoutPlayer & r)
		    {
			return (pid < r.pid);
		    }
		};

		typedef boost::unordered_map<DWORD, TLogoutPlayer*> TLogoutPlayerMap;
		TLogoutPlayerMap m_map_logout;
		void InsertLogoutPlayer(DWORD pid);
		void DeleteLogoutPlayer(DWORD pid);
		void UpdateLogoutPlayer();
		void UpdateItemCacheSet(DWORD pid);
		void FlushPlayerCacheSet(DWORD pid);
		void Election(CPeer * peer, DWORD dwHandle, const char * p);
		void Candidacy(CPeer * peer, DWORD dwHandle, const char * p);
		void AddMonarchMoney(CPeer * peer, DWORD dwHandle, const char * p);
		void TakeMonarchMoney(CPeer * peer, DWORD dwHandle, const char * p);
		void ComeToVote(CPeer * peer, DWORD dwHandle, const char * p);
		void RMCandidacy(CPeer * peer, DWORD dwHandle, const char * p);
		void SetMonarch(CPeer * peer, DWORD dwHandle, const char * p);
		void RMMonarch(CPeer * peer, DWORD dwHandle, const char * p);
		void DecMonarchMoney(CPeer * peer, DWORD dwHandle, const char * p);
		void ChangeMonarchLord(CPeer* peer, DWORD dwHandle, TPacketChangeMonarchLord* info);
		void BlockException(TPacketBlockException *data);
		void SendSpareItemIDRange(CPeer* peer);
		void UpdateHorseName(TPacketUpdateHorseName* data, CPeer* peer);
		void AckHorseName(DWORD dwPID, CPeer* peer);
		void DeleteLoginKey(TPacketDC *data);
		void ResetLastPlayerID(const TPacketNeedLoginLogInfo* data);
		void DeleteAwardId(TPacketDeleteAwardID* data);
		void UpdateChannelStatus(TChannelStatus* pData);
		void RequestChannelStatus(CPeer* peer, DWORD dwHandle);
#ifdef __AUCTION__
		void EnrollInAuction (CPeer * peer, DWORD owner_id, AuctionEnrollProductInfo* data);
		void EnrollInSale (CPeer * peer, DWORD owner_id, AuctionEnrollSaleInfo* data);
		void EnrollInWish (CPeer * peer, DWORD wisher_id, AuctionEnrollWishInfo* data);
		void AuctionBid (CPeer * peer, DWORD bidder_id, AuctionBidInfo* data);
		void AuctionImpur (CPeer * peer, DWORD purchaser_id, AuctionImpurInfo* data);
		void AuctionGetAuctionedItem (CPeer * peer, DWORD actor_id, DWORD item_id);
		void AuctionBuySoldItem (CPeer * peer, DWORD actor_id, DWORD item_id);
		void AuctionCancelAuction (CPeer * peer, DWORD actor_id, DWORD item_id);
		void AuctionCancelWish (CPeer * peer, DWORD actor_id, DWORD item_num);
		void AuctionCancelSale (CPeer * peer, DWORD actor_id, DWORD item_id);
		void AuctionDeleteAuctionItem (CPeer * peer, DWORD actor_id, DWORD item_id);
		void AuctionDeleteSaleItem (CPeer * peer, DWORD actor_id, DWORD item_id);
		void AuctionReBid (CPeer * peer, DWORD bidder_id, AuctionBidInfo* data);
		void AuctionBidCancel (CPeer * peer, DWORD bidder_id, DWORD item_id);
#endif
#ifdef ENABLE_PROTO_FROM_DB
		public:
		bool InitializeMobTableFromDB();
		bool InitializeItemTableFromDB();
		protected:
		bool bIsProtoReadFromDB;
#endif
};

template<class Func>
Func CClientManager::for_each_peer(Func f)
{
    TPeerList::iterator it;
    for (it = m_peerList.begin(); it!=m_peerList.end();++it)
    {
	f(*it);
    }
    return f;
}
#endif
