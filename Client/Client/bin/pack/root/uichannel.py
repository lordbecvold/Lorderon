#Lorderon Client Dev by Lordbecvold
import ui
import net
import app
import chat
import math
import wndMgr
import serverInfo
import background
import ServerStateChecker

class ChannelChanger(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__MakeWindow()
		self.__MakeBoard()
		self.__Fill_Up_ChannelList()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.Hide()
		return TRUE

	def __MakeWindow(self):
		ServerStateChecker.Create(self)
		self.SetSize(150, 175)
		self.SetPosition(
			(wndMgr.GetScreenWidth() / 2) - int(math.floor(self.GetWidth() / 2.)),
			(wndMgr.GetScreenHeight() / 2) - int(math.floor(self.GetHeight() / 2.))
		)
		self.AddFlag("float")
		self.Show()

	def __MakeBoard(self):
		self.Board = ui.Board()
		self.Board.SetParent(self)
		self.Board.SetSize(self.GetWidth(), self.GetHeight())
		self.Board.SetPosition(0, 0)
		self.Board.AddFlag("float")
		self.Board.Show()
		self.TitleBar = ui.TitleBar()
		self.TitleBar.SetParent(self.Board)
		self.TitleBar.SetPosition(7, 7)
		self.TitleBar.MakeTitleBar(self.GetWidth() - 2 * 7, 'red')
		self.TitleBar.SetCloseEvent(self.Close)
		self.TitleBar.Show()
		self.RefreshButton = ui.Button()
		self.RefreshButton.SetParent(self.TitleBar)
		self.RefreshButton.SetPosition(3, 3)
		self.RefreshButton.SetUpVisual("d:/ymir work/ui/game/guild/refresh_button_01.sub")
		self.RefreshButton.SetOverVisual("d:/ymir work/ui/game/guild/refresh_button_02.sub")
		self.RefreshButton.SetDownVisual("d:/ymir work/ui/game/guild/refresh_button_03.sub")
		self.RefreshButton.SetToolTipText("Refresh", 0, - 23)
		self.RefreshButton.SetEvent(lambda : self.__Fill_Up_ChannelList())
		self.RefreshButton.Show()
		self.TitleText = ui.TextLine()
		self.TitleText.SetParent(self.TitleBar)
		self.TitleText.SetPosition(0, 4)
		self.TitleText.SetText("Zmìnit Channel")
		self.TitleText.SetWindowHorizontalAlignCenter()
		self.TitleText.SetHorizontalAlignCenter()
		self.TitleText.Show()
		self.ServerName = ui.TextLine()
		self.ServerName.SetParent(self.TitleBar)
		self.ServerName.SetPosition(0, self.TitleBar.GetHeight())
		self.ServerName.SetText(str(net.GetServerInfo()).split(",")[0])
		self.ServerName.SetWindowHorizontalAlignCenter()
		self.ServerName.SetHorizontalAlignCenter()
		self.ServerName.Show()
		self.ChannelListBase = ui.SlotBar()
		self.ChannelListBase.SetParent(self.Board)
		self.ChannelListBase.SetSize(self.Board.GetWidth() - 2 * 16, 5 * 18 - 4)
		self.ChannelListBase.SetPosition(16 , 7 + self.TitleBar.GetHeight() + 6 + 10)
		self.ChannelListBase.Show()
		self.ChannelList = ui.ListBox()
		self.ChannelList.SetParent(self.ChannelListBase)
		self.ChannelList.SetSize(self.ChannelListBase.GetWidth()- 20, self.ChannelListBase.GetHeight())
		self.ChannelList.SetPosition(0, 0)
		self.ChannelList.SetEvent(ui.__mem_func__(self.__OnSelectChannel))
		self.ChannelList.Show()
		self.ChangeButton = ui.Button()
		self.ChangeButton.SetParent(self.Board)
		self.ChangeButton.SetPosition(self.Board.GetWidth() / 2 - 44, self.Board.GetHeight() - 35)
		self.ChangeButton.SetUpVisual('d:/ymir work/ui/public/Large_button_01.sub')
		self.ChangeButton.SetOverVisual('d:/ymir work/ui/public/Large_button_02.sub')
		self.ChangeButton.SetDownVisual('d:/ymir work/ui/public/Large_button_03.sub')
		self.ChangeButton.SetEvent(lambda : self.__OnClickConnectButton())
		self.ChangeButton.SetText("Zvolit")
		self.ChangeButton.Show()
		self.DisableChangeButton()

	def DisableChangeButton(self):
		self.ChangeButton.Disable()
		self.ChangeButton.Down()
		self.ChangeButton.ButtonText.SetFontColor(0.4, 0.4, 0.4)

	def EnableChangeButton(self):
		self.ChangeButton.Enable()
		self.ChangeButton.SetUp()
		self.ChangeButton.ButtonText.SetFontColor(1, 1, 1)

	def __GetRegionID(self):
		return 0

	def __GetServerID(self):
		regionID = self.__GetRegionID()
		for i in serverInfo.REGION_DICT[regionID].keys():
			if serverInfo.REGION_DICT[regionID][i]["name"] == net.GetServerInfo().split(",")[0]:
				serverID = int(i)
				break
		return serverID

	def __Fill_Up_ChannelList(self):
		self.__RequestServerStateList()
		self.__RefreshServerStateList()

	def __RequestServerStateList(self):
		regionID = self.__GetRegionID()
		serverID = self.__GetServerID()
		try:
			channelDict = serverInfo.REGION_DICT[regionID][serverID]["channel"]
		except:
			return
		ServerStateChecker.Initialize(self)
		for id, channelDataDict in channelDict.items():
			key=channelDataDict["key"]
			ip=channelDataDict["ip"]
			udp_port=channelDataDict["udp_port"]
			ServerStateChecker.AddChannel(key, ip, udp_port)
		ServerStateChecker.Request()

	def __RefreshServerStateList(self):
		regionID = self.__GetRegionID()
		serverID = self.__GetServerID()
		bakChannelID = self.ChannelList.GetSelectedItem()
		self.ChannelList.ClearItem()
		try:
			channelDict = serverInfo.REGION_DICT[regionID][serverID]["channel"]
		except:
			return
		for channelID, channelDataDict in channelDict.items():
			channelName = channelDataDict["name"]
			channelState = channelDataDict["state"]
			self.ChannelList.InsertItem(channelID, "%s" % ("       " + channelName))
			#self.ChannelList.InsertItem(channelID, "%s %s" % (channelName, channelState))
		self.ChannelList.SelectItem(bakChannelID-1)

	def NotifyChannelState(self, addrKey, state):
		try:
			stateName = serverInfo.STATE_DICT[state]
		except:
			stateName = serverInfo.STATE_NONE
		regionID  = int(addrKey / 1000)
		serverID  = int(addrKey / 10) % 100
		channelID = addrKey % 10
		try:
			serverInfo.REGION_DICT[regionID][serverID]["channel"][channelID]["state"] = stateName
			self.__RefreshChannelStateList()
		except:
			pass

	def __IsSpecialMap(self):
		dis_maps = [
			"season1/metin2_map_oxevent",
			"season2/metin2_map_guild_inside01",
			"season2/metin2_map_empirewar01",
			"season2/metin2_map_empirewar02",
			"season2/metin2_map_empirewar03",
			"metin2_map_dragon_timeattack_01",
			"metin2_map_dragon_timeattack_02",
			"metin2_map_dragon_timeattack_03",
			"metin2_map_skipia_dungeon_boss",
			"metin2_map_skipia_dungeon_boss2",
			"metin2_map_devilsCatacomb",
			"metin2_map_deviltower1",
			"metin2_map_t1",
			"metin2_map_t2",
			"metin2_map_t3",
			"metin2_map_t4",
			"metin2_map_t5",
			"metin2_map_wedding_01",
			"metin2_map_duel",
			"metin2_map_orclabyrinth",
			"metin2_map_n_flame_dungeon_01",
			"metin2_map_n_snow_dungeon_01"
		]
		if str(background.GetCurrentMapName()) in dis_maps:
			return TRUE
		return FALSE

	def __OnSelectChannel(self):
		if self.ChangeButton.IsDown():
			self.EnableChangeButton()

	def __OnClickConnectButton(self):
		ServerStateChecker.Update()
		channelID = self.ChannelList.GetSelectedItem()
		if not channelID:
			return
		if net.GetServerInfo().strip().split(", ")[1] == self.ChannelList.textDict[self.ChannelList.selectedLine].strip().split(" ")[0]:
			chat.AppendChat(1, "Jste již na vybraném kanálu!")
			return
		elif self.__IsSpecialMap():
			chat.AppendChat(1, "Litujeme, ale na této mapì nemùžete zmìnit svùj kanál bez odhlášení!")
			return
		net.SetServerInfo(net.GetServerInfo()[:-1] + str(channelID))
		self.Close()
		net.SendChatPacket("/channel "+str(channelID))

	def DirectConnect(self, ChannelIP, ChannelPort, AuthServerIP, AuthServerPort):
		net.SetLoginInfo(decode_string(net.ACCOUNT_ID), decode_string(net.ACCOUNT_PW))
		net.ConnectToAccountServer(ChannelIP, ChannelPort, AuthServerIP, AuthServerPort)
		net.DirectEnter(0)
		net.SendSelectCharacterPacket(0)
		net.SendEnterGamePacket()

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		ServerStateChecker.Initialize(self)
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnUpdate(self):
		ServerStateChecker.Update()
		