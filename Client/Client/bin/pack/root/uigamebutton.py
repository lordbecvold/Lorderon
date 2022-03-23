#Lorderon Client Dev by Lordbecvold
import app
import ui
import player
import net
from switchbot import Bot
import game

class GameButtonWindow(ui.ScriptWindow):
	def __init__(self):
		self.switchbot = Bot()
		self.switchbot.Hide()
		ui.ScriptWindow.__init__(self)
		if app.ENABLE_PVP_ADVANCED:
			import uiduel
			self.wndBlockEquip = uiduel.WindowEquipmentBlock()
		self.__LoadWindow("UIScript/gamewindow.py")

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self, filename):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, filename)
		except Exception, msg:
			import dbg
			dbg.TraceError("GameButtonWindow.LoadScript - %s" % (msg))
			app.Abort()
			return False
		try:
			self.gameButtonDict={
				"STATUS" : self.GetChild("StatusPlusButton"),
				"SKILL" : self.GetChild("SkillPlusButton"),
				"QUEST" : self.GetChild("QuestButton"),
				"HELP" : self.GetChild("HelpButton"),
				"BUILD" : self.GetChild("BuildGuildBuilding"),
				"EXIT_OBSERVER" : self.GetChild("ExitObserver"),
				"GIFT" : self.GetChild("GiftIcon"),
			}
			self.gameButtonDict["EXIT_OBSERVER"].SetEvent(ui.__mem_func__(self.__OnClickExitObserver))
			self.GetChild("warp_open").SetEvent(ui.__mem_func__(self.__OnClicwarp))
			self.GetChild("eq_button").SetEvent(ui.__mem_func__(self.__OnClickeq))
			self.GetChild("special_stor").SetEvent(ui.__mem_func__(self.__OnClickspecials))
			if app.ENABLE_PVP_ADVANCED:
				self.GetChild("BlockEquipmentButton").SetEvent(ui.__mem_func__(self.__OnClickBlockEquipment))
		except Exception, msg:
			import dbg
			dbg.TraceError("GameButtonWindow.LoadScript - %s" % (msg))
			app.Abort()
			return False
		self.__HideAllGameButton()
		self.SetObserverMode(player.IsObserverMode())
		return True

	def Destroy(self):
		for key in self.gameButtonDict:
			self.gameButtonDict[key].SetEvent(0)
		self.gameButtonDict={}

	def SetButtonEvent(self, name, event):
		try:
			self.gameButtonDict[name].SetEvent(event)
		except Exception, msg:
			print "GameButtonWindow.LoadScript - %s" % (msg)
			app.Abort()
			return

	def ShowBuildButton(self):
		self.gameButtonDict["BUILD"].Show()

	def HideBuildButton(self):
		self.gameButtonDict["BUILD"].Hide()
		
	def ShowGiftButton(self):
		self.gameButtonDict["GIFT"].Show()

	def HideGiftButton(self):
		self.gameButtonDict["GIFT"].Hide()

	def CheckGameButton(self):
		if not self.IsShow():
			return
		statusPlusButton=self.gameButtonDict["STATUS"]
		skillPlusButton=self.gameButtonDict["SKILL"]
		helpButton=self.gameButtonDict["HELP"]
		if player.GetStatus(player.STAT) > 0:
			statusPlusButton.Show()
		else:
			statusPlusButton.Hide()
		if self.__IsSkillStat():
			skillPlusButton.Show()
		else:
			skillPlusButton.Hide()
		if 0 == player.GetPlayTime():
			helpButton.Show()
		else:
			helpButton.Hide()

	def __IsSkillStat(self):
		if player.GetStatus(player.SKILL_ACTIVE) > 0:
			return True
		return False

	def __OnClicwarp(self):
		net.SendChatPacket("/localization open")

	def __OnClickExitObserver(self):
		net.SendChatPacket("/observer_exit")

	def __OnClickeq(self):
		import uifastequip
		self.uuifastequipDlg = uifastequip.changeequip()
		self.uuifastequipDlg.Show()

	def __OnClickspecials(self):
		self.switchbot.Show()

	if app.ENABLE_PVP_ADVANCED:
		def __OnClickBlockEquipment(self):
			if self.wndBlockEquip.IsShow():
				self.wndBlockEquip.Hide()
			else:
				self.wndBlockEquip.Show()
				
	def __HideAllGameButton(self):
		for btn in self.gameButtonDict.values():
			btn.Hide()

	def SetObserverMode(self, isEnable):
		if isEnable:
			self.gameButtonDict["EXIT_OBSERVER"].Show()
		else:
			self.gameButtonDict["EXIT_OBSERVER"].Hide()
			