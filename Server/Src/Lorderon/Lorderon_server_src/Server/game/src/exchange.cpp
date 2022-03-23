//Lorderon server core Dev by Lordbecvold
#include "stdafx.h"
#include "../../libgame/include/grid.h"
#include "utils.h"
#include "desc.h"
#include "desc_client.h"
#include "char.h"
#include "item.h"
#include "item_manager.h"
#include "packet.h"
#include "log.h"
#include "db.h"
#include "locale_service.h"
#include "../../common/length.h"
#include "exchange.h"
#if defined(WJ_COMBAT_ZONE)	
	#include "combat_zone.h"
#endif
#include "DragonSoul.h"
#include "questmanager.h" 

void exchange_packet(LPCHARACTER ch, BYTE sub_header, bool is_me, long long arg1, TItemPos arg2, DWORD arg3, void * pvData = NULL);
void exchange_packet(LPCHARACTER ch, BYTE sub_header, bool is_me, long long arg1, TItemPos arg2, DWORD arg3, void * pvData)
{
	if (!ch->GetDesc())
		return;
	struct packet_exchange pack_exchg;
	pack_exchg.header = HEADER_GC_EXCHANGE;
	pack_exchg.sub_header = sub_header;
	pack_exchg.is_me = is_me;
	pack_exchg.arg1 = arg1;
	pack_exchg.arg2 = arg2;
	pack_exchg.arg3 = arg3;
	if (sub_header == EXCHANGE_SUBHEADER_GC_ITEM_ADD && pvData)
	{
		thecore_memcpy(&pack_exchg.alSockets, ((LPITEM) pvData)->GetSockets(), sizeof(pack_exchg.alSockets));
		thecore_memcpy(&pack_exchg.aAttr, ((LPITEM) pvData)->GetAttributes(), sizeof(pack_exchg.aAttr));
	}
	else
	{
		memset(&pack_exchg.alSockets, 0, sizeof(pack_exchg.alSockets));
		memset(&pack_exchg.aAttr, 0, sizeof(pack_exchg.aAttr));
	}
	ch->GetDesc()->Packet(&pack_exchg, sizeof(pack_exchg));
}

bool CHARACTER::ExchangeStart(LPCHARACTER victim)
{
	if (this == victim)	
		return false;
	if (IsObserverMode())
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("you_cant_attack_if_you_war_fun"));
		return false;
	}
	if (victim->IsNPC())
		return false;
#if defined(WJ_COMBAT_ZONE)	
	if (CCombatZoneManager::Instance().IsCombatZoneMap(GetMapIndex()) || CCombatZoneManager::Instance().IsCombatZoneMap(victim->GetMapIndex()))
		return false;
#endif
#ifdef ENABLE_PVP_ADVANCED
	if ((GetDuel("BlockExchange")))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("duel_block_function"));
		return false;
	}
	if ((victim->GetDuel("BlockExchange")))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("duel_block_victim"), victim->GetName());
		return false;
	}
#endif
	if ( IsOpenSafebox() || GetShopOwner() || GetMyShop() || IsCubeOpen())
	{
		ChatPacket( CHAT_TYPE_INFO, LC_TEXT("exchange_window_is_open" ) );
		return false;
	}
	if ( victim->IsOpenSafebox() || victim->GetShopOwner() || victim->GetMyShop() || victim->IsCubeOpen() )
	{
		ChatPacket( CHAT_TYPE_INFO, LC_TEXT("this_player_is_trading" ) );
		return false;
	}
	int iDist = DISTANCE_APPROX(GetX() - victim->GetX(), GetY() - victim->GetY());
	if (iDist >= EXCHANGE_MAX_DISTANCE)
		return false;
	if (GetExchange())
		return false;
	if (victim->GetExchange())
	{
		exchange_packet(this, EXCHANGE_SUBHEADER_GC_ALREADY, 0, 0, NPOS, 0);
		return false;
	}
	if (victim->IsBlockMode(BLOCK_EXCHANGE))
	{
		ChatPacket(CHAT_TYPE_INFO, LC_TEXT("player_has_blocked_exchange"));
		return false;
	}
	SetExchange(M2_NEW CExchange(this));
	victim->SetExchange(M2_NEW CExchange(victim));
	victim->GetExchange()->SetCompany(GetExchange());
	GetExchange()->SetCompany(victim->GetExchange());
	SetExchangeTime();
	victim->SetExchangeTime();
	exchange_packet(victim, EXCHANGE_SUBHEADER_GC_START, 0, GetVID(), NPOS, 0);
	exchange_packet(this, EXCHANGE_SUBHEADER_GC_START, 0, victim->GetVID(), NPOS, 0);
	return true;
}

CExchange::CExchange(LPCHARACTER pOwner)
{
	m_pCompany = NULL;
	m_bAccept = false;
	for (int i = 0; i < EXCHANGE_ITEM_MAX_NUM; ++i)
	{
		m_apItems[i] = NULL;
		m_aItemPos[i] = NPOS;
		m_abItemDisplayPos[i] = 0;
	}
	m_lGold = 0;
	m_pOwner = pOwner;
	pOwner->SetExchange(this);
#ifdef __NEW_EXCHANGE_WINDOW__
	m_pGrid = M2_NEW CGrid(6, 4);
#else
	m_pGrid = M2_NEW CGrid(4, 3);
#endif
}

CExchange::~CExchange()
{
	M2_DELETE(m_pGrid);
}

bool CExchange::AddItem(TItemPos item_pos, BYTE display_pos)
{
	assert(m_pOwner != NULL && GetCompany());
	if (!item_pos.IsValidItemPosition())
		return false;
	if (item_pos.IsEquipPosition())
		return false;
	LPITEM item;
	if (!(item = m_pOwner->GetItem(item_pos)))
		return false;
	if (IS_SET(item->GetAntiFlag(), ITEM_ANTIFLAG_GIVE))
	{
		m_pOwner->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("this_item_is_not_tradeble_exchange"));
		return false;
	}
	if (true == item->isLocked())
	{
		return false;
	}
	if (item->IsExchanging())
	{
		sys_log(0, "EXCHANGE under exchanging");
		return false;
	}
	if (!m_pGrid->IsEmpty(display_pos, 1, item->GetSize()))
	{
		sys_log(0, "EXCHANGE not empty item_pos %d %d %d", display_pos, 1, item->GetSize());
		return false;
	}
	Accept(false);
	GetCompany()->Accept(false);
	for (int i = 0; i < EXCHANGE_ITEM_MAX_NUM; ++i)
	{
		if (m_apItems[i])
			continue;
		m_apItems[i] = item;
		m_aItemPos[i] = item_pos;
		m_abItemDisplayPos[i] = display_pos;
		m_pGrid->Put(display_pos, 1, item->GetSize());
		item->SetExchanging(true);
		exchange_packet(m_pOwner,EXCHANGE_SUBHEADER_GC_ITEM_ADD,true,item->GetVnum(),TItemPos(RESERVED_WINDOW, display_pos),item->GetCount(),item);
		exchange_packet(GetCompany()->GetOwner(),EXCHANGE_SUBHEADER_GC_ITEM_ADD,false,item->GetVnum(),TItemPos(RESERVED_WINDOW, display_pos),item->GetCount(),item);
		sys_log(0, "EXCHANGE AddItem success %s pos(%d, %d) %d", item->GetName(), item_pos.window_type, item_pos.cell, display_pos);
		return true;
	}
	return false;
}

bool CExchange::RemoveItem(BYTE pos)
{
	if (pos >= EXCHANGE_ITEM_MAX_NUM)
		return false;
	if (!m_apItems[pos])
		return false;
	TItemPos PosOfInventory = m_aItemPos[pos];
	m_apItems[pos]->SetExchanging(false);
	m_pGrid->Get(m_abItemDisplayPos[pos], 1, m_apItems[pos]->GetSize());
	exchange_packet(GetOwner(),	EXCHANGE_SUBHEADER_GC_ITEM_DEL, true, pos, NPOS, 0);
	exchange_packet(GetCompany()->GetOwner(), EXCHANGE_SUBHEADER_GC_ITEM_DEL, false, pos, PosOfInventory, 0);
	Accept(false);
	GetCompany()->Accept(false);
	m_apItems[pos] = NULL;
	m_aItemPos[pos] = NPOS;
	m_abItemDisplayPos[pos] = 0;
	return true;
}

bool CExchange::AddGold(long long gold)
{
	if (gold <= 0)
		return false;
	if (GetOwner()->GetGold() < gold)
	{
		exchange_packet(GetOwner(), EXCHANGE_SUBHEADER_GC_LESS_GOLD, 0, 0, NPOS, 0);
		return false;
	}
	if (m_lGold > 0)
		return false;
	Accept(false);
	GetCompany()->Accept(false);
	m_lGold = gold;
	exchange_packet(GetOwner(), EXCHANGE_SUBHEADER_GC_GOLD_ADD, true, m_lGold, NPOS, 0);
	exchange_packet(GetCompany()->GetOwner(), EXCHANGE_SUBHEADER_GC_GOLD_ADD, false, m_lGold, NPOS, 0);
	return true;
}

bool CExchange::Check(int * piItemCount)
{
	if (GetOwner()->GetGold() < m_lGold)
		return false;
	int item_count = 0;
	for (int i = 0; i < EXCHANGE_ITEM_MAX_NUM; ++i)
	{
		if (!m_apItems[i])
			continue;
		if (!m_aItemPos[i].IsValidItemPosition())
			return false;
		if (m_apItems[i] != GetOwner()->GetItem(m_aItemPos[i]))
			return false;
		++item_count;
	}
	*piItemCount = item_count;
	return true;
}

bool CExchange::CheckSpace()
{
	static CGrid s_grid1(INVENTORY_PAGE_COLUMN, INVENTORY_PAGE_ROW); 
	static CGrid s_grid2(INVENTORY_PAGE_COLUMN, INVENTORY_PAGE_ROW); 
#ifdef ENABLE_EXTEND_INVEN_SYSTEM
	static CGrid s_grid3(INVENTORY_PAGE_COLUMN, INVENTORY_PAGE_ROW); 
	static CGrid s_grid4(INVENTORY_PAGE_COLUMN, INVENTORY_PAGE_ROW); 
#endif
	s_grid1.Clear();
	s_grid2.Clear();
#ifdef ENABLE_EXTEND_INVEN_SYSTEM
	s_grid3.Clear();
	s_grid4.Clear();
#endif
	LPCHARACTER	victim = GetCompany()->GetOwner();
	LPITEM item;
	int i;
	for (i = 0; i < INVENTORY_PAGE_SIZE*1; ++i)
	{
		if (!(item = victim->GetInventoryItem(i)))
			continue;
		s_grid1.Put(i, 1, item->GetSize());
	}
#ifdef ENABLE_SPECIAL_STORAGE
	LPITEM item2,item3;
	static CGrid s_upp_grid1(5, SPECIAL_INVENTORY_MAX_NUM / 5 / 2);
	static CGrid s_upp_grid2(5, SPECIAL_INVENTORY_MAX_NUM / 5 / 2);
	static CGrid s_book_grid1(5, SPECIAL_INVENTORY_MAX_NUM / 5 / 2);
	static CGrid s_book_grid2(5, SPECIAL_INVENTORY_MAX_NUM / 5 / 2);
	static CGrid s_stone_grid1(5, SPECIAL_INVENTORY_MAX_NUM / 5 / 2);
	static CGrid s_stone_grid2(5, SPECIAL_INVENTORY_MAX_NUM / 5 / 2);
	s_upp_grid1.Clear();
	s_upp_grid2.Clear();
	s_book_grid1.Clear();
	s_book_grid2.Clear();
	s_stone_grid1.Clear();
	s_stone_grid2.Clear();
	int upgde_cnt = 0;
	for (int i = 0; i < SPECIAL_INVENTORY_MAX_NUM; ++i)
	{
		if (!(item = victim->GetUpgradeInventoryItem(i)))
			continue;
		if (i < SPECIAL_INVENTORY_MAX_NUM / 2)
		{
			s_upp_grid1.Put(i, 1, item->GetSize());
			upgde_cnt++;
		}
		else
		{
			s_upp_grid2.Put(i, 1, item->GetSize());
			upgde_cnt++;
		}
	}
	int book_cnt = 0;
	for (int i = 0; i < SPECIAL_INVENTORY_MAX_NUM; ++i)
	{
		if (!(item = victim->GetBookInventoryItem(i)))
			continue;
		if (i < SPECIAL_INVENTORY_MAX_NUM / 2)
		{
			s_book_grid1.Put(i, 1, item->GetSize());
			book_cnt++;
		}
		else
		{
			s_book_grid2.Put(i, 1, item->GetSize());
			book_cnt++;
		}
	}
	int stne_cnt = 0;
	for (int i = 0; i < SPECIAL_INVENTORY_MAX_NUM; ++i)
	{
		if (!(item = victim->GetStoneInventoryItem(i)))
			continue;
		if (i < SPECIAL_INVENTORY_MAX_NUM / 2)
		{
			s_stone_grid1.Put(i, 1, item->GetSize());
			stne_cnt++;
		}
		else
		{
			s_stone_grid2.Put(i, 1, item->GetSize());
			stne_cnt++;
		}
	}
#endif
	for (i = INVENTORY_PAGE_SIZE*1; i < INVENTORY_PAGE_SIZE*2; ++i)
	{
		if (!(item = victim->GetInventoryItem(i)))
			continue;

		s_grid2.Put(i - INVENTORY_PAGE_SIZE*1, 1, item->GetSize());
	}
#ifdef ENABLE_EXTEND_INVEN_SYSTEM
	for (i = INVENTORY_PAGE_SIZE*2; i < INVENTORY_PAGE_SIZE*3; ++i)
	{
		if (!(item = victim->GetInventoryItem(i)))
			continue;

		s_grid3.Put(i - INVENTORY_PAGE_SIZE*2, 1, item->GetSize());
	}
	for (i = INVENTORY_PAGE_SIZE*3; i < INVENTORY_PAGE_SIZE*4; ++i)
	{
		if (!(item = victim->GetInventoryItem(i)))
			continue;

		s_grid4.Put(i - INVENTORY_PAGE_SIZE*3, 1, item->GetSize());
	}
#endif
	static std::vector <WORD> s_vDSGrid(DRAGON_SOUL_INVENTORY_MAX_NUM);
	bool bDSInitialized = false;
	for (i = 0; i < EXCHANGE_ITEM_MAX_NUM; ++i)
	{
		if (!(item = m_apItems[i]))
			continue;
		if (item->IsDragonSoul())
		{
			if (!victim->DragonSoul_IsQualified())
			{
				return false;
			}
			if (!bDSInitialized)
			{
				bDSInitialized = true;
				victim->CopyDragonSoulItemGrid(s_vDSGrid);
			}
			bool bExistEmptySpace = false;
			WORD wBasePos = DSManager::instance().GetBasePosition(item);
			if (wBasePos >= DRAGON_SOUL_INVENTORY_MAX_NUM)
				return false;
			for (int i = 0; i < DRAGON_SOUL_BOX_SIZE; i++)
			{
				WORD wPos = wBasePos + i;
				if (0 == s_vDSGrid[wPos]) 
				{
					bool bEmpty = true;
					for (int j = 1; j < item->GetSize(); j++)
					{
						if (s_vDSGrid[wPos + j * DRAGON_SOUL_BOX_COLUMN_NUM])
						{
							bEmpty = false;
							break;
						}
					}
					if (bEmpty)
					{
						for (int j = 0; j < item->GetSize(); j++)
						{
							s_vDSGrid[wPos + j * DRAGON_SOUL_BOX_COLUMN_NUM] =  wPos + 1;
						}
						bExistEmptySpace = true;
						break;
					}
				}
				if (bExistEmptySpace)
					break;
			}
			if (!bExistEmptySpace)
				return false;
#ifdef ENABLE_SPECIAL_STORAGE
		else if(item->IsUpgradeItem())
		{
			if (upgde_cnt == 90)
				return false;
			int iPos = s_upp_grid1.FindBlank(1, item->GetSize());
			if (iPos >= 0)
			{
				s_upp_grid1.Put(iPos, 1, item->GetSize());
				continue;
			}
			iPos = s_upp_grid2.FindBlank(1, item->GetSize());
			if (iPos >= 0)
			{
				s_upp_grid2.Put(iPos, 1, item->GetSize());
				continue;
			}
			return false;
		}
		else if(item->IsBook())
		{
			if (book_cnt == 90)
				return false;
			int iPos = s_book_grid1.FindBlank(1, item->GetSize());
			if (iPos >= 0)
			{
				s_book_grid1.Put(iPos, 1, item->GetSize());
				continue;
			}
			iPos = s_book_grid2.FindBlank(1, item->GetSize());
			if (iPos >= 0)
			{
				s_book_grid2.Put(iPos, 1, item->GetSize());
				continue;
			}
			return false;
		}
		else if(item->IsStone())
		{
			if (stne_cnt == 90)
				return false;
			int iPos = s_stone_grid1.FindBlank(1, item->GetSize());
			if (iPos >= 0)
			{
				s_stone_grid1.Put(iPos, 1, item->GetSize());
				continue;
			}
			iPos = s_stone_grid2.FindBlank(1, item->GetSize());
			if (iPos >= 0)
			{
				s_stone_grid2.Put(iPos, 1, item->GetSize());
				continue;
			}
			return false;
		}
#endif
		}
		else
		{
			int iPos;
			if ((iPos = s_grid1.FindBlank(1, item->GetSize())) >= 0)
			{
				s_grid1.Put(iPos, 1, item->GetSize());
			}
			else if ((iPos = s_grid2.FindBlank(1, item->GetSize())) >= 0)
			{
				s_grid2.Put(iPos, 1, item->GetSize());
			}
#ifdef ENABLE_EXTEND_INVEN_SYSTEM
			else if ((iPos = s_grid3.FindBlank(1, item->GetSize())) >= 0)
			{
				s_grid3.Put(iPos, 1, item->GetSize());
			}
			else if ((iPos = s_grid4.FindBlank(1, item->GetSize())) >= 0)
			{
				s_grid4.Put(iPos, 1, item->GetSize());
			}
#endif
			else
				return false;
		}
	}
	return true;
}

bool CExchange::Done()
{
	int empty_pos, i;
	LPITEM item;
	LPCHARACTER	victim = GetCompany()->GetOwner();
	for (i = 0; i < EXCHANGE_ITEM_MAX_NUM; ++i)
	{
		if (!(item = m_apItems[i]))
			continue;
		if (item->IsDragonSoul())
			empty_pos = victim->GetEmptyDragonSoulInventory(item);
#ifdef ENABLE_SPECIAL_STORAGE
		else if(item->IsUpgradeItem())
			empty_pos = victim->GetEmptyUpgradeInventory(item);
		else if(item->IsBook())
			empty_pos = victim->GetEmptyBookInventory(item);
		else if(item->IsStone())
			empty_pos = victim->GetEmptyStoneInventory(item);
#endif
		else
			empty_pos = victim->GetEmptyInventory(item->GetSize());
		if (empty_pos < 0)
		{
			sys_err("Exchange::Done : Cannot find blank position in inventory %s <-> %s item %s", m_pOwner->GetName(), victim->GetName(), item->GetName());
			continue;
		}
		assert(empty_pos >= 0);
		if (item->GetVnum() == 90008 || item->GetVnum() == 90009) // VCARD
		{
			VCardUse(m_pOwner, victim, item);
			continue;
		}
		m_pOwner->SyncQuickslot(QUICKSLOT_TYPE_ITEM, item->GetCell(), 255);
		item->RemoveFromCharacter();
		if (item->IsDragonSoul())
			item->AddToCharacter(victim, TItemPos(DRAGON_SOUL_INVENTORY, empty_pos));
#ifdef ENABLE_SPECIAL_STORAGE
		else if(item->IsUpgradeItem())
			item->AddToCharacter(victim, TItemPos(UPGRADE_INVENTORY, empty_pos));
		else if(item->IsBook())
			item->AddToCharacter(victim, TItemPos(BOOK_INVENTORY, empty_pos));
		else if(item->IsStone())
			item->AddToCharacter(victim, TItemPos(STONE_INVENTORY, empty_pos));
#endif
		else
			item->AddToCharacter(victim, TItemPos(INVENTORY, empty_pos));
		ITEM_MANAGER::instance().FlushDelayedSave(item);
		item->SetExchanging(false);
		{
			char exchange_buf[51];
			snprintf(exchange_buf, sizeof(exchange_buf), "%s %u %u", item->GetName(), GetOwner()->GetPlayerID(), item->GetCount());
			LogManager::instance().ItemLog(victim, item, "EXCHANGE_TAKE", exchange_buf);
			snprintf(exchange_buf, sizeof(exchange_buf), "%s %u %u", item->GetName(), victim->GetPlayerID(), item->GetCount());
			LogManager::instance().ItemLog(GetOwner(), item, "EXCHANGE_GIVE", exchange_buf);
			if (item->GetVnum() >= 80003 && item->GetVnum() <= 80007)
			{
				LogManager::instance().GoldBarLog(victim->GetPlayerID(), item->GetID(), EXCHANGE_TAKE, "");
				LogManager::instance().GoldBarLog(GetOwner()->GetPlayerID(), item->GetID(), EXCHANGE_GIVE, "");
			}
			m_pOwner->CreateFly(FLY_SP_MEDIUM, victim);
			for (int i = 0; i < 3; i++){
			m_pOwner->CreateFly(FLY_SP_SMALL, victim);
			}
		}
		m_apItems[i] = NULL;
	}
	if (m_lGold)
	{
		GetOwner()->PointChange(POINT_GOLD, -m_lGold, true);
		victim->PointChange(POINT_GOLD, m_lGold, true);
		if (m_lGold > 1000)
		{
			char exchange_buf[51];
			snprintf(exchange_buf, sizeof(exchange_buf), "%u %s", GetOwner()->GetPlayerID(), GetOwner()->GetName());
			LogManager::instance().CharLog(victim, m_lGold, "EXCHANGE_GOLD_TAKE", exchange_buf);
			snprintf(exchange_buf, sizeof(exchange_buf), "%u %s", victim->GetPlayerID(), victim->GetName());
			LogManager::instance().CharLog(GetOwner(), m_lGold, "EXCHANGE_GOLD_GIVE", exchange_buf);
		}
	}
	m_pGrid->Clear();
	return true;
}

bool CExchange::Accept(bool bAccept)
{
	if (m_bAccept == bAccept)
		return true;
	m_bAccept = bAccept;
	if (m_bAccept && GetCompany()->m_bAccept)
	{
		int	iItemCount;
		LPCHARACTER victim = GetCompany()->GetOwner();
		GetOwner()->SetExchangeTime();
		victim->SetExchangeTime();
		if (quest::CQuestManager::instance().GetPCForce(GetOwner()->GetPlayerID())->IsRunning() == true)
		{
			GetOwner()->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("you_cant_trade_if_using_quest"));
			victim->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("you_cant_trade_if_using_quest"));
			goto EXCHANGE_END;
		}
		else if (quest::CQuestManager::instance().GetPCForce(victim->GetPlayerID())->IsRunning() == true)
		{
			victim->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("you_cant_trade_if_using_quest"));
			GetOwner()->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("you_cant_trade_if_using_quest"));
			goto EXCHANGE_END;
		}
		if (!Check(&iItemCount))
		{
			GetOwner()->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("you_dont_have_yang_of_full_inventory"));
			victim->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("player_have_full_inventory_or_0_gold"));
			goto EXCHANGE_END;
		}
		if (!CheckSpace())
		{
			GetOwner()->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("you_inventory_is_full"));
			victim->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("you_inventory_is_full_dont_pick"));
			goto EXCHANGE_END;
		}
		if (!GetCompany()->Check(&iItemCount))
		{
			victim->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("you_dont_have_yang_of_full_inventory"));
			GetOwner()->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("player_have_full_inventory_or_0_gold"));
			goto EXCHANGE_END;
		}
		if (!GetCompany()->CheckSpace())
		{
			victim->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("you_inventory_is_full"));
			GetOwner()->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("you_inventory_is_full_dont_pick"));
			goto EXCHANGE_END;
		}
		if (db_clientdesc->GetSocket() == INVALID_SOCKET)
		{
			sys_err("Cannot use exchange feature while DB cache connection is dead.");
			victim->ChatPacket(CHAT_TYPE_INFO, "unknown_error");
			GetOwner()->ChatPacket(CHAT_TYPE_INFO, "unknown_error");
			goto EXCHANGE_END;
		}
		if (Done())
		{
			if (m_lGold) 
				GetOwner()->Save();
			if (GetCompany()->Done())
			{
				if (GetCompany()->m_lGold) 
					victim->Save();
				GetOwner()->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%s exchange_success"), victim->GetName());
				victim->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("%s exchange_success"), GetOwner()->GetName());
			}
		}
EXCHANGE_END:
		Cancel();
		return false;
	}
	else
	{
		exchange_packet(GetOwner(), EXCHANGE_SUBHEADER_GC_ACCEPT, true, m_bAccept, NPOS, 0);
		exchange_packet(GetCompany()->GetOwner(), EXCHANGE_SUBHEADER_GC_ACCEPT, false, m_bAccept, NPOS, 0);
		return true;
	}
}

void CExchange::Cancel()
{
	exchange_packet(GetOwner(), EXCHANGE_SUBHEADER_GC_END, 0, 0, NPOS, 0);
	GetOwner()->SetExchange(NULL);
	for (int i = 0; i < EXCHANGE_ITEM_MAX_NUM; ++i)
	{
		if (m_apItems[i])
			m_apItems[i]->SetExchanging(false);
	}
	if (GetCompany())
	{
		GetCompany()->SetCompany(NULL);
		GetCompany()->Cancel();
	}
	M2_DELETE(this);
}
