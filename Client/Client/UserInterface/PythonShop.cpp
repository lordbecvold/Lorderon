//Lorderon Client Binary Dev by Lordbecvold
#include "stdafx.h"
#include "PythonShop.h"
#include "PythonNetworkStream.h"

void CPythonShop::SetTabCoinType(BYTE tabIdx, BYTE coinType)
{
	if (tabIdx >= m_bTabCount)
	{
#ifdef ENABLE_DEV_MODE
		TraceError("Out of Index. tabIdx(%d) must be less than %d.", tabIdx, SHOP_TAB_COUNT_MAX);
#endif		
		return;
	}
	m_aShoptabs[tabIdx].coinType = coinType;
}

BYTE CPythonShop::GetTabCoinType(BYTE tabIdx)
{
	if (tabIdx >= m_bTabCount)
	{
#ifdef ENABLE_DEV_MODE
		TraceError("Out of Index. tabIdx(%d) must be less than %d.", tabIdx, SHOP_TAB_COUNT_MAX);
#endif		
		return 0xff;
	}
	return m_aShoptabs[tabIdx].coinType;
}

void CPythonShop::SetTabName(BYTE tabIdx, const char* name)
{
	if (tabIdx >= m_bTabCount)
	{
#ifdef ENABLE_DEV_MODE
		TraceError("Out of Index. tabIdx(%d) must be less than %d.", tabIdx, SHOP_TAB_COUNT_MAX);
#endif
		return;
	}
	m_aShoptabs[tabIdx].name = name;
}

const char* CPythonShop::GetTabName(BYTE tabIdx)
{
	if (tabIdx >= m_bTabCount)
	{
#ifdef ENABLE_DEV_MODE
		TraceError("Out of Index. tabIdx(%d) must be less than %d.", tabIdx, SHOP_TAB_COUNT_MAX);
#endif
		return NULL;
	}
	return m_aShoptabs[tabIdx].name.c_str();
}

void CPythonShop::SetItemData(DWORD dwIndex, const TShopItemData & c_rShopItemData)
{
	BYTE tabIdx = dwIndex / SHOP_HOST_ITEM_MAX_NUM;
	DWORD dwSlotPos = dwIndex % SHOP_HOST_ITEM_MAX_NUM;
	SetItemData(tabIdx, dwSlotPos, c_rShopItemData);
}

BOOL CPythonShop::GetItemData(DWORD dwIndex, const TShopItemData ** c_ppItemData)
{
	BYTE tabIdx = dwIndex / SHOP_HOST_ITEM_MAX_NUM;
	DWORD dwSlotPos = dwIndex % SHOP_HOST_ITEM_MAX_NUM;
	return GetItemData(tabIdx, dwSlotPos, c_ppItemData);
}

void CPythonShop::SetItemData(BYTE tabIdx, DWORD dwSlotPos, const TShopItemData & c_rShopItemData)
{
	if (tabIdx >= SHOP_TAB_COUNT_MAX || dwSlotPos >= SHOP_HOST_ITEM_MAX_NUM)
	{
#ifdef ENABLE_DEV_MODE
		TraceError("Out of Index. tabIdx(%d) must be less than %d. dwSlotPos(%d) must be less than %d", tabIdx, SHOP_TAB_COUNT_MAX, dwSlotPos, SHOP_HOST_ITEM_MAX_NUM);
#endif	
		return;
	}
	m_aShoptabs[tabIdx].items[dwSlotPos] = c_rShopItemData;
}

BOOL CPythonShop::GetItemData(BYTE tabIdx, DWORD dwSlotPos, const TShopItemData ** c_ppItemData)
{
	if (tabIdx >= SHOP_TAB_COUNT_MAX || dwSlotPos >= SHOP_HOST_ITEM_MAX_NUM)
	{
#ifdef ENABLE_DEV_MODE
		TraceError("Out of Index. tabIdx(%d) must be less than %d. dwSlotPos(%d) must be less than %d", tabIdx, SHOP_TAB_COUNT_MAX, dwSlotPos, SHOP_HOST_ITEM_MAX_NUM);
#endif
		return FALSE;
	}
	*c_ppItemData = &m_aShoptabs[tabIdx].items[dwSlotPos];
	return TRUE;
}

void CPythonShop::ClearPrivateShopStock()
{
	m_PrivateShopItemStock.clear();
}
#ifdef ENABLE_FULL_YANG
void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice)
#else
void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice)
#endif
{
	DelPrivateShopItemStock(ItemPos);
	TShopItemTable SellingItem;
	SellingItem.vnum = 0;
	SellingItem.count = 0;
	SellingItem.pos = ItemPos;
	SellingItem.price = dwPrice;
	SellingItem.display_pos = dwDisplayPos;
	m_PrivateShopItemStock.insert(make_pair(ItemPos, SellingItem));
}
void CPythonShop::DelPrivateShopItemStock(TItemPos ItemPos)
{
	if (m_PrivateShopItemStock.end() == m_PrivateShopItemStock.find(ItemPos))
		return;
	m_PrivateShopItemStock.erase(ItemPos);
}
#ifdef ENABLE_FULL_YANG
long long CPythonShop::GetPrivateShopItemPrice(TItemPos ItemPos)
#else
int CPythonShop::GetPrivateShopItemPrice(TItemPos ItemPos)
#endif
{
	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.find(ItemPos);
	if (m_PrivateShopItemStock.end() == itor)
		return 0;
	TShopItemTable & rShopItemTable = itor->second;
	return rShopItemTable.price;
}
struct ItemStockSortFunc
{
	bool operator() (TShopItemTable & rkLeft, TShopItemTable & rkRight)
	{
		return rkLeft.display_pos < rkRight.display_pos;
	}
};
#ifdef ENABLE_OFFLINE_SHOP
void CPythonShop::BuildPrivateShop(const char * c_szName, DWORD days)
#else
void CPythonShop::BuildPrivateShop(const char * c_szName)
#endif
{
	std::vector<TShopItemTable> ItemStock;
	ItemStock.reserve(m_PrivateShopItemStock.size());
	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.begin();
	for (; itor != m_PrivateShopItemStock.end(); ++itor)
	{
		ItemStock.push_back(itor->second);
	}
	std::sort(ItemStock.begin(), ItemStock.end(), ItemStockSortFunc());
#ifdef ENABLE_OFFLINE_SHOP
	CPythonNetworkStream::Instance().SendBuildPrivateShopPacket(c_szName, ItemStock, days);
#else
	CPythonNetworkStream::Instance().SendBuildPrivateShopPacket(c_szName, ItemStock);
#endif
}

void CPythonShop::Open(BOOL isPrivateShop, BOOL isMainPrivateShop)
{
	m_isShoping = TRUE;
	m_isPrivateShop = isPrivateShop;
	m_isMainPlayerPrivateShop = isMainPrivateShop;
}

void CPythonShop::Close()
{
	m_isShoping = FALSE;
	m_isPrivateShop = FALSE;
	m_isMainPlayerPrivateShop = FALSE;
}

BOOL CPythonShop::IsOpen()
{
	return m_isShoping;
}

BOOL CPythonShop::IsPrivateShop()
{
	return m_isPrivateShop;
}

BOOL CPythonShop::IsMainPlayerPrivateShop()
{
	return m_isMainPlayerPrivateShop;
}

void CPythonShop::Clear()
{
	m_isShoping = FALSE;
	m_isPrivateShop = FALSE;
	m_isMainPlayerPrivateShop = FALSE;
	ClearPrivateShopStock();
	m_bTabCount = 1;
	for (int i = 0; i < SHOP_TAB_COUNT_MAX; i++)
		memset (m_aShoptabs[i].items, 0, sizeof(TShopItemData) * SHOP_HOST_ITEM_MAX_NUM);
}

CPythonShop::CPythonShop(void)
{
	Clear();
}

CPythonShop::~CPythonShop(void)
{
}

PyObject * shopOpen(PyObject * poSelf, PyObject * poArgs)
{
	int isPrivateShop = false;
	PyTuple_GetInteger(poArgs, 0, &isPrivateShop);
	int isMainPrivateShop = false;
	PyTuple_GetInteger(poArgs, 1, &isMainPrivateShop);
	CPythonShop& rkShop=CPythonShop::Instance();
	rkShop.Open(isPrivateShop, isMainPrivateShop);
	return Py_BuildNone();
}

PyObject * shopClose(PyObject * poSelf, PyObject * poArgs)
{
	CPythonShop& rkShop=CPythonShop::Instance();
	rkShop.Close();
	return Py_BuildNone();
}

PyObject * shopIsOpen(PyObject * poSelf, PyObject * poArgs)
{
	CPythonShop& rkShop=CPythonShop::Instance();
	return Py_BuildValue("i", rkShop.IsOpen());
}

PyObject * shopIsPrviateShop(PyObject * poSelf, PyObject * poArgs)
{
	CPythonShop& rkShop=CPythonShop::Instance();
	return Py_BuildValue("i", rkShop.IsPrivateShop());
}

PyObject * shopIsMainPlayerPrivateShop(PyObject * poSelf, PyObject * poArgs)
{
	CPythonShop& rkShop=CPythonShop::Instance();
	return Py_BuildValue("i", rkShop.IsMainPlayerPrivateShop());
}

PyObject * shopGetItemID(PyObject * poSelf, PyObject * poArgs)
{
	int nPos;
	if (!PyTuple_GetInteger(poArgs, 0, &nPos))
		return Py_BuildException();
	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(nPos, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->vnum);
	return Py_BuildValue("i", 0);
}

PyObject * shopGetItemCount(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();
	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->count);
	return Py_BuildValue("i", 0);
}

PyObject * shopGetItemPrice(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();
	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
#ifdef ENABLE_FULL_YANG
		return Py_BuildValue("L", c_pItemData->price);
#else
		return Py_BuildValue("i", c_pItemData->price);
#endif
	return Py_BuildValue("i", 0);
}

PyObject * shopGetItemMetinSocket(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();
	int iMetinSocketIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iMetinSocketIndex))
		return Py_BuildException();
	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->alSockets[iMetinSocketIndex]);
	return Py_BuildValue("i", 0);
}

PyObject * shopGetItemAttribute(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();
	int iAttrSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iAttrSlotIndex))
		return Py_BuildException();
	if (iAttrSlotIndex >= 0 && iAttrSlotIndex < ITEM_ATTRIBUTE_SLOT_MAX_NUM)
	{
		const TShopItemData * c_pItemData;
		if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
			return Py_BuildValue("ii", c_pItemData->aAttr[iAttrSlotIndex].bType, c_pItemData->aAttr[iAttrSlotIndex].sValue);
	}
	return Py_BuildValue("ii", 0, 0);
}

PyObject * shopClearPrivateShopStock(PyObject * poSelf, PyObject * poArgs)
{
	CPythonShop::Instance().ClearPrivateShopStock();
	return Py_BuildNone();
}
PyObject * shopAddPrivateShopItemStock(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();
	int iDisplaySlotIndex;
	if (!PyTuple_GetInteger(poArgs, 2, &iDisplaySlotIndex))
		return Py_BuildException();
#ifdef ENABLE_FULL_YANG
	PyObject* val;
	if (!PyTuple_GetObject(poArgs, 3, &val))
		return Py_BuildException();
	long long iPrice = PyLong_AsLongLong(val);
#else
	int iPrice;
	if (!PyTuple_GetInteger(poArgs, 3, &iPrice))
		return Py_BuildException();
#endif
	CPythonShop::Instance().AddPrivateShopItemStock(TItemPos(bItemWindowType, wItemSlotIndex), iDisplaySlotIndex, iPrice);
	return Py_BuildNone();
}
PyObject * shopDelPrivateShopItemStock(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();
	CPythonShop::Instance().DelPrivateShopItemStock(TItemPos(bItemWindowType, wItemSlotIndex));
	return Py_BuildNone();
}
PyObject * shopGetPrivateShopItemPrice(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();
#ifdef ENABLE_FULL_YANG
	return Py_BuildValue("L", CPythonShop::Instance().GetPrivateShopItemPrice(TItemPos(bItemWindowType, wItemSlotIndex)));
#else
	return Py_BuildValue("i", CPythonShop::Instance().GetPrivateShopItemPrice(TItemPos(bItemWindowType, wItemSlotIndex)));
#endif
	return Py_BuildValue("i", 0);
}
PyObject * shopBuildPrivateShop(PyObject * poSelf, PyObject * poArgs)
{
	char * szName;
	if (!PyTuple_GetString(poArgs, 0, &szName))
		return Py_BuildException();
#ifdef ENABLE_OFFLINE_SHOP
	int days;
	if (!PyTuple_GetInteger(poArgs, 1, &days))
		return Py_BuildException();
	CPythonShop::Instance().BuildPrivateShop(szName, days);
#else
	CPythonShop::Instance().BuildPrivateShop(szName);
#endif
	return Py_BuildNone();
}

PyObject * shopGetTabCount(PyObject * poSelf, PyObject * poArgs)
{
	return Py_BuildValue("i", CPythonShop::instance().GetTabCount());
}

PyObject * shopGetTabName(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bTabIdx;
	if (!PyTuple_GetInteger(poArgs, 0, &bTabIdx))
		return Py_BuildException();
	return Py_BuildValue("s", CPythonShop::instance().GetTabName(bTabIdx));
}

PyObject * shopGetTabCoinType(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bTabIdx;
	if (!PyTuple_GetInteger(poArgs, 0, &bTabIdx))
		return Py_BuildException();
	return Py_BuildValue("i", CPythonShop::instance().GetTabCoinType(bTabIdx));
}

void initshop()
{
	static PyMethodDef s_methods[] =
	{
		{ "Open", shopOpen, METH_VARARGS },
		{ "Close", shopClose, METH_VARARGS },
		{ "IsOpen", shopIsOpen, METH_VARARGS },
		{ "IsPrivateShop", shopIsPrviateShop, METH_VARARGS },
		{ "IsMainPlayerPrivateShop", shopIsMainPlayerPrivateShop, METH_VARARGS },
		{ "GetItemID", shopGetItemID, METH_VARARGS },
		{ "GetItemCount", shopGetItemCount, METH_VARARGS },
		{ "GetItemPrice", shopGetItemPrice, METH_VARARGS },
		{ "GetItemMetinSocket", shopGetItemMetinSocket, METH_VARARGS },
		{ "GetItemAttribute", shopGetItemAttribute, METH_VARARGS },
		{ "GetTabCount", shopGetTabCount, METH_VARARGS },
		{ "GetTabName", shopGetTabName, METH_VARARGS },
		{ "GetTabCoinType", shopGetTabCoinType, METH_VARARGS },
		{ "ClearPrivateShopStock", shopClearPrivateShopStock, METH_VARARGS },
		{ "AddPrivateShopItemStock", shopAddPrivateShopItemStock, METH_VARARGS },
		{ "DelPrivateShopItemStock", shopDelPrivateShopItemStock, METH_VARARGS },
		{ "GetPrivateShopItemPrice", shopGetPrivateShopItemPrice, METH_VARARGS },
		{ "BuildPrivateShop", shopBuildPrivateShop, METH_VARARGS },
		{ NULL, NULL, NULL },
	};
	PyObject * poModule = Py_InitModule("shop", s_methods);
	PyModule_AddIntConstant(poModule, "SHOP_SLOT_COUNT", SHOP_HOST_ITEM_MAX_NUM);
	PyModule_AddIntConstant(poModule, "SHOP_COIN_TYPE_GOLD", SHOP_COIN_TYPE_GOLD);
	PyModule_AddIntConstant(poModule, "SHOP_COIN_TYPE_SECONDARY_COIN", SHOP_COIN_TYPE_SECONDARY_COIN);
#if defined(WJ_COMBAT_ZONE)
	PyModule_AddIntConstant(poModule, "SHOP_COIN_TYPE_COMBAT_ZONE", SHOP_COIN_TYPE_COMBAT_ZONE);
#endif
}
