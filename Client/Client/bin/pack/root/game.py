#Lorderon Client Dev by Lordbecvold
import os
import app
import dbg
import grp
import item
import background
import chr
import chrmgr
import player
import snd
import chat
import textTail
import snd
import net
import effect
import wndMgr
import fly
import systemSetting
import quest
import guild
import skill
import messenger
import uimarbleshop
import localeInfo
import constInfo
import exchange
import ime
import ui
import uiCommon
import uiPhaseCurtain
import uiMapNameShower
import uiAffectShower
import uiPlayerGauge
import uiCharacter
import uiTarget
import uiPrivateShopBuilder
import mouseModule
import consoleModule
import localeInfo
import playerSettingModule
import interfaceModule
import musicInfo
import debugInfo
import stringCommander
import uiinventory
import event
import uiNewShop
import exception
if app.ENABLE_RENEW_MESSENGER_WHISPER:
	import uicontact
if app.ENABLE_BIOLOG_SYSTEM:
	import uiprofessionalbiolog
if app.ENABLE_PVP_ADVANCED:
	import constInfo as pvp
	import uiCommon as message
	import uiduel
from switchbot import Bot
from _weakref import proxy

SCREENSHOT_CWDSAVE = False
SCREENSHOT_DIR = None
if localeInfo.IsEUROPE():
	SCREENSHOT_CWDSAVE = True

cameraDistance = 1550.0
cameraPitch = 27.0
cameraRotation = 0.0
cameraHeight = 100.0
testAlignment = 0
CHECK_ACTIVE_PICKUP = 0
BPisLoaded = 0

class GameWindow(ui.ScriptWindow):
	def __init__(self, stream):
		ui.ScriptWindow.__init__(self, "GAME")
		self.SetWindowName("game")
		net.SetPhaseWindow(net.PHASE_WINDOW_GAME, self)
		player.SetGameWindow(self)
		self.switchbot = Bot()
		self.switchbot.Hide()
		self.quickSlotPageIndex = 0
		self.lastPKModeSendedTime = 0
		constInfo.nacht = 0
		constInfo.tag = 0
		self.pressNumber = None
		if (app.WJ_COMBAT_ZONE):
			import uicombatzone
			self.wndCombatZone = uicombatzone.CombatZoneWindow()
		self.guildWarQuestionDialog = None
		self.interface = None
		self.targetBoard = None
		self.console = None
		self.mapNameShower = None
		self.affectShower = None
		self.playerGauge = None
		if app.ENABLE_MANAGER_BANK_SYSTEM:
			self.managerAccountBank = None
		self.uiNewShopCreate = None
		self.uiNewShop = None
		self.stream=stream
		self.interface = interfaceModule.Interface()
		self.interface.MakeInterface()
		self.interface.ShowDefaultWindows()
		self.curtain = uiPhaseCurtain.PhaseCurtain()
		self.curtain.speed = 0.03
		self.curtain.Hide()
		self.targetBoard = uiTarget.TargetBoard()
		self.targetBoard.SetWhisperEvent(ui.__mem_func__(self.interface.OpenWhisperDialog))
		self.targetBoard.Hide()
		self.console = consoleModule.ConsoleWindow()
		self.console.BindGameClass(self)
		self.console.SetConsoleSize(wndMgr.GetScreenWidth(), 200)
		self.console.Hide()
		self.mapNameShower = uiMapNameShower.MapNameShower()
		self.affectShower = uiAffectShower.AffectShower()
		if app.ENABLE_TITLE_SYSTEM:
			import title_system
			self.wndTitleSystem = title_system.Title_System()
		self.wndMarbleShop = uimarbleshop.MarbleShopWindow()
		import uimaintenance
		self.wndMaintenance = uimaintenance.MaintenanceClass()
		if app.ENABLE_PVP_ADVANCED:
			self.wndDuelGui = uiduel.Initializate()
			self.wndDuelLive = uiduel.WindowLiveInformations()
		self.playerGauge = uiPlayerGauge.PlayerGauge(self)
		self.playerGauge.Hide()
		if app.ENABLE_MANAGER_BANK_SYSTEM:
			import uibankamanger
			self.managerAccountBank = uibankamanger.BankGui()
			self.managerAccountBank.Hide()
		if app.ENABLE_LOCALIZATION_SYSTEM:
			import uiLocalization
			self.wndPlayerLocalization = uiLocalization.Initializate()
		self.itemDropQuestionDialog = None
		self.__SetQuickSlotMode()
		self.__ServerCommand_Build()
		self.__ProcessPreservedServerCommand()

	def __del__(self):
		player.SetGameWindow(0)
		net.ClearPhaseWindow(net.PHASE_WINDOW_GAME, self)
		ui.ScriptWindow.__del__(self)

	def Open(self):
		app.SetFrameSkip(1)
		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.quickSlotPageIndex = 0
		self.PickingCharacterIndex = -1
		self.PickingItemIndex = -1
		self.consoleEnable = False
		self.isShowDebugInfo = False
		self.ShowNameFlag = False
		self.enableXMasBoom = False
		self.startTimeXMasBoom = 0.0
		self.indexXMasBoom = 0
		global cameraDistance, cameraPitch, cameraRotation, cameraHeight
		app.SetCamera(cameraDistance, cameraPitch, cameraRotation, cameraHeight)
		constInfo.SET_DEFAULT_CAMERA_MAX_DISTANCE()
		constInfo.SET_DEFAULT_CHRNAME_COLOR()
		constInfo.SET_DEFAULT_CONVERT_EMPIRE_LANGUAGE_ENABLE()
		constInfo.SET_DEFAULT_USE_ITEM_WEAPON_TABLE_ATTACK_BONUS()
		constInfo.SET_DEFAULT_USE_SKILL_EFFECT_ENABLE()
		constInfo.SET_TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE()	
		event.SetLeftTimeString(localeInfo.UI_LEFT_TIME)
		self.uiNewShop = uiNewShop.ShopDialog()
		self.uiNewShop.Close()
		self.uiNewShopCreate = uiNewShop.ShopDialogCreate()
		self.uiNewShopCreate.Hide()
		textTail.EnablePKTitle(constInfo.PVPMODE_ENABLE)
		if constInfo.PVPMODE_TEST_ENABLE:
			self.testPKMode = ui.TextLine()
			self.testPKMode.SetFontName(localeInfo.UI_DEF_FONT)
			self.testPKMode.SetPosition(0, 15)
			self.testPKMode.SetWindowHorizontalAlignCenter()
			self.testPKMode.SetHorizontalAlignCenter()
			self.testPKMode.SetFeather()
			self.testPKMode.SetOutline()
			self.testPKMode.Show()
			self.testAlignment = ui.TextLine()
			self.testAlignment.SetFontName(localeInfo.UI_DEF_FONT)
			self.testAlignment.SetPosition(0, 35)
			self.testAlignment.SetWindowHorizontalAlignCenter()
			self.testAlignment.SetHorizontalAlignCenter()
			self.testAlignment.SetFeather()
			self.testAlignment.SetOutline()
			self.testAlignment.Show()
		self.__BuildKeyDict()
		self.__BuildDebugInfo()
		uiPrivateShopBuilder.Clear()
		exchange.InitTrading()
		snd.SetMusicVolume(systemSetting.GetMusicVolume()*net.GetFieldMusicVolume())
		snd.SetSoundVolume(systemSetting.GetSoundVolume())
		self.__SetQuickSlotMode()
		self.__SelectQuickPage(self.quickSlotPageIndex)
		self.SetFocus()
		self.Show()
		app.ShowCursor()
		net.SendEnterGamePacket()
		try:
			self.StartGame()
		except:
			exception.Abort("GameWindow.Open")
		self.cubeInformation = {}
		self.currentCubeNPC = 0
		if app.ENABLE_FOG_FIX:
			if systemSetting.IsFogMode():
				background.SetEnvironmentFog(True)
			else:
				background.SetEnvironmentFog(False)	
				
	def BindInterfaceClass(self, interface):
		self.interface = interface

	def Close(self):
		self.Hide()
		global cameraDistance, cameraPitch, cameraRotation, cameraHeight
		(cameraDistance, cameraPitch, cameraRotation, cameraHeight) = app.GetCamera()
		self.onPressKeyDict = None
		self.onClickKeyDict = None
		chat.Close()
		snd.StopAllSound()
		grp.InitScreenEffect()
		chr.Destroy()
		textTail.Clear()
		quest.Clear()
		background.Destroy()
		guild.Destroy()
		messenger.Destroy()
		skill.ClearSkillData()
		wndMgr.Unlock()
		self.uiNewShop.Hide()
		self.uiNewShopCreate.Hide()
		uiPrivateShopBuilder.Clear()	
		mouseModule.mouseController.DeattachObject()
		if self.guildWarQuestionDialog:
			self.guildWarQuestionDialog.Close()
		self.guildNameBoard = None
		self.partyRequestQuestionDialog = None
		self.partyInviteQuestionDialog = None
		self.guildInviteQuestionDialog = None
		self.guildWarQuestionDialog = None
		self.messengerAddFriendQuestion = None
		self.itemDropQuestionDialog = None
		self.confirmDialog = None
		self.PrintCoord = None
		self.FrameRate = None
		self.Pitch = None
		self.Splat = None
		self.TextureNum = None
		self.ObjectNum = None
		self.ViewDistance = None
		self.PrintMousePos = None
		self.ClearDictionary()
		self.playerGauge = None
		self.mapNameShower = None
		self.affectShower = None
		if self.console:
			self.console.BindGameClass(0)
			self.console.Close()
			self.console=None
		if self.wndMaintenance.IsShow():
			self.wndMaintenance.Hide()
		if app.ENABLE_PVP_ADVANCED:
			if self.wndDuelLive.IsShow():
				self.wndDuelLive.Hide()		
		if self.targetBoard:
			self.targetBoard.Destroy()
			self.targetBoard = None
		if app.ENABLE_TITLE_SYSTEM:			
			self.wndTitleSystem.Close()
		if (app.WJ_COMBAT_ZONE):
			if self.wndCombatZone:
				self.wndCombatZone.Close()
		if self.wndMarbleShop:
			self.wndMarbleShop.Hide()
		if app.ENABLE_MANAGER_BANK_SYSTEM:
			if self.managerAccountBank:
				self.managerAccountBank.Close()		
		if app.ENABLE_LOCALIZATION_SYSTEM:
			if self.wndPlayerLocalization:
				self.wndPlayerLocalization.Close()
		if self.interface:
			self.interface.HideAllWindows()
			self.interface.Close()
			self.interface=None
		player.ClearSkillDict()
		player.ResetCameraRotation()
		self.KillFocus()
		app.HideCursor()
		print "---------------------------------------------------------------------------- CLOSE GAME WINDOW"

	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_1] = lambda : self.__PressNumKey(1)
		onPressKeyDict[app.DIK_2] = lambda : self.__PressNumKey(2)
		onPressKeyDict[app.DIK_3] = lambda : self.__PressNumKey(3)
		onPressKeyDict[app.DIK_4] = lambda : self.__PressNumKey(4)
		onPressKeyDict[app.DIK_5] = lambda : self.__PressNumKey(5)
		onPressKeyDict[app.DIK_6] = lambda : self.__PressNumKey(6)
		onPressKeyDict[app.DIK_7] = lambda : self.__PressNumKey(7)
		onPressKeyDict[app.DIK_8] = lambda : self.__PressNumKey(8)
		onPressKeyDict[app.DIK_9] = lambda : self.__PressNumKey(9)
		onPressKeyDict[app.DIK_F1]	= lambda : self.__PressQuickSlot(4)
		onPressKeyDict[app.DIK_F2]	= lambda : self.__PressQuickSlot(5)
		onPressKeyDict[app.DIK_F3]	= lambda : self.__PressQuickSlot(6)
		onPressKeyDict[app.DIK_F4]	= lambda : self.__PressQuickSlot(7)
		if app.ENABLE_TITLE_SYSTEM:	
			onPressKeyDict[app.DIK_F5] = lambda : self.OpenTitleSystem()
		#onPressKeyDict[app.DIK_F7]	= lambda : self.__EnablePickUpItem()
		onPressKeyDict[app.DIK_LALT] = lambda : self.ShowName()
		onPressKeyDict[app.DIK_LCONTROL] = lambda : self.ShowMouseImage()
		onPressKeyDict[app.DIK_SYSRQ] = lambda : self.SaveScreen()
		onPressKeyDict[app.DIK_SPACE] = lambda : self.StartAttack()
		onPressKeyDict[app.DIK_F8] = lambda : self.OpenMarbleShop()
		onPressKeyDict[app.DIK_UP] = lambda : self.MoveUp()
		onPressKeyDict[app.DIK_DOWN] = lambda : self.MoveDown()
		onPressKeyDict[app.DIK_LEFT] = lambda : self.MoveLeft()
		onPressKeyDict[app.DIK_RIGHT] = lambda : self.MoveRight()
		onPressKeyDict[app.DIK_W] = lambda : self.MoveUp()
		onPressKeyDict[app.DIK_S] = lambda : self.MoveDown()
		onPressKeyDict[app.DIK_A] = lambda : self.MoveLeft()
		onPressKeyDict[app.DIK_D] = lambda : self.MoveRight()
		onPressKeyDict[app.DIK_E] = lambda: app.RotateCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_R] = lambda: app.ZoomCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_T] = lambda: app.PitchCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_G] = self.__PressGKey
		onPressKeyDict[app.DIK_Q] = self.__PressQKey
		onPressKeyDict[app.DIK_NUMPAD9] = lambda: app.MovieResetCamera()
		onPressKeyDict[app.DIK_NUMPAD4] = lambda: app.MovieRotateCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_NUMPAD6] = lambda: app.MovieRotateCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_PGUP] = lambda: app.MovieZoomCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_PGDN] = lambda: app.MovieZoomCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_NUMPAD8] = lambda: app.MoviePitchCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_NUMPAD2] = lambda: app.MoviePitchCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_GRAVE] = lambda : self.PickUpItem()
		onPressKeyDict[app.DIK_Z] = lambda : self.PickUpItem()
		onPressKeyDict[app.DIK_C] = lambda state = "STATUS": self.interface.ToggleCharacterWindow(state)
		onPressKeyDict[app.DIK_V] = lambda state = "SKILL": self.interface.ToggleCharacterWindow(state)
		onPressKeyDict[app.DIK_N] = lambda state = "QUEST": self.interface.ToggleCharacterWindow(state)
		onPressKeyDict[app.DIK_I] = lambda : self.interface.ToggleInventoryWindow()
		onPressKeyDict[app.DIK_O] = lambda : self.interface.ToggleDragonSoulWindowWithNoInfo()
		onPressKeyDict[app.DIK_M] = lambda : self.interface.PressMKey()
		onPressKeyDict[app.DIK_ADD] = lambda : self.interface.MiniMapScaleUp()
		onPressKeyDict[app.DIK_SUBTRACT] = lambda : self.interface.MiniMapScaleDown()
		onPressKeyDict[app.DIK_L] = lambda : self.interface.ToggleChatLogWindow()
		onPressKeyDict[app.DIK_LSHIFT] = lambda : self.__SetQuickPageMode()
		onPressKeyDict[app.DIK_U] = lambda : self.interface.ToggleSpecialStorageWindow()
		onPressKeyDict[app.DIK_J] = lambda : self.__PressJKey()
		onPressKeyDict[app.DIK_H] = lambda : self.__PressHKey()
		onPressKeyDict[app.DIK_B] = lambda : self.__PressBKey()
		onPressKeyDict[app.DIK_F] = lambda : self.__PressFKey()
		onPressKeyDict[app.DIK_K] = lambda : self.NewShop()
		onPressKeyDict[app.DIK_TAB]	= lambda : net.SendChatPacket("/localization open")
		self.onPressKeyDict = onPressKeyDict
		onClickKeyDict = {}
		onClickKeyDict[app.DIK_UP] = lambda : self.StopUp()
		onClickKeyDict[app.DIK_DOWN] = lambda : self.StopDown()
		onClickKeyDict[app.DIK_LEFT] = lambda : self.StopLeft()
		onClickKeyDict[app.DIK_RIGHT] = lambda : self.StopRight()
		onClickKeyDict[app.DIK_SPACE] = lambda : self.EndAttack()
		onClickKeyDict[app.DIK_W] = lambda : self.StopUp()
		onClickKeyDict[app.DIK_S] = lambda : self.StopDown()
		onClickKeyDict[app.DIK_A] = lambda : self.StopLeft()
		onClickKeyDict[app.DIK_D] = lambda : self.StopRight()
		onClickKeyDict[app.DIK_Q] = lambda: app.RotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_E] = lambda: app.RotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_R] = lambda: app.ZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_F] = lambda: app.ZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_T] = lambda: app.PitchCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_G] = lambda: self.__ReleaseGKey()
		onClickKeyDict[app.DIK_NUMPAD4] = lambda: app.MovieRotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_NUMPAD6] = lambda: app.MovieRotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_PGUP] = lambda: app.MovieZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_PGDN] = lambda: app.MovieZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_NUMPAD8] = lambda: app.MoviePitchCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_NUMPAD2] = lambda: app.MoviePitchCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_LALT] = lambda: self.HideName()
		onClickKeyDict[app.DIK_LCONTROL] = lambda: self.HideMouseImage()
		onClickKeyDict[app.DIK_LSHIFT] = lambda: self.__SetQuickSlotMode()
		self.onClickKeyDict=onClickKeyDict

	if app.ENABLE_LOCALIZATION_SYSTEM:
		def OpenLocalizationSystem(self):
			net.SendChatPacket("/binary_localization open")

	def __PressNumKey(self,num):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			if num >= 1 and num <= 9:
				if(chrmgr.IsPossibleEmoticon(-1)):
					chrmgr.SetEmoticon(-1,int(num)-1)
					net.SendEmoticon(int(num)-1)
		else:
			if num >= 1 and num <= 4:
				self.pressNumber(num-1)

	def __ClickBKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			return
		else:
			if constInfo.PVPMODE_ACCELKEY_ENABLE:
				self.ChangePKMode()

	def	__PressJKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			if player.IsMountingHorse():
				net.SendChatPacket("/unmount")
			else:
				if not uiPrivateShopBuilder.IsBuildingPrivateShop():
					for i in xrange(player.INVENTORY_PAGE_SIZE*player.INVENTORY_PAGE_COUNT):
						if player.GetItemIndex(i) in (71114, 71116, 71118, 71120):
							net.SendItemUsePacket(i)
							break

	def	__PressHKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			net.SendChatPacket("/user_horse_ride")
		else:
			self.interface.OpenHelpWindow()

	def __BonusPage(self):
		import uiBonusPage
		global BPisLoaded
		try:
			if BPisLoaded != 1:
				exec 'uiBonusPage.BonusBoardDialog().Show()'
			else:
				pass
		except ImportError:
			import dbg,app
			dbg.Trace('uiBonusPage.py Importing error')
			app.Abort()	

	def __quikeqchange(self):
		import uifastequip
		self.uuifastequipDlg = uifastequip.changeequip()
		self.uuifastequipDlg.Show()

	def	__EnablePickUpItem(self):
		global CHECK_ACTIVE_PICKUP
		if CHECK_ACTIVE_PICKUP == 0:
			CHECK_ACTIVE_PICKUP = 1
			constInfo.ENABLE_PICKUP = 1
		else:
			CHECK_ACTIVE_PICKUP = 0
			constInfo.ENABLE_PICKUP = 0

	def __toggleSwitchbot(self):
		self.switchbot.Show()

	def	__PressBKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			net.SendChatPacket("/user_horse_back")
		else:
			state = "EMOTICON"
			self.interface.ToggleCharacterWindow(state)

	def	__PressFKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			net.SendChatPacket("/user_horse_feed")
		else:
			app.ZoomCamera(app.CAMERA_TO_POSITIVE)

	def __PressGKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			net.SendChatPacket("/ride")
		else:
			if self.ShowNameFlag:
				self.interface.ToggleGuildWindow()
			else:
				app.PitchCamera(app.CAMERA_TO_POSITIVE)

	def	__ReleaseGKey(self):
		app.PitchCamera(app.CAMERA_STOP)

	if app.ENABLE_TITLE_SYSTEM:	
		def OpenTitleSystem(self):		
			self.wndTitleSystem.OpenWindow()

	def __PressQKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			if 0==interfaceModule.IsQBHide:
				interfaceModule.IsQBHide = 1
				self.interface.HideAllQuestButton()
			else:
				interfaceModule.IsQBHide = 0
				self.interface.ShowAllQuestButton()
		else:
			app.RotateCamera(app.CAMERA_TO_NEGATIVE)

	def __SetQuickSlotMode(self):
		self.pressNumber=ui.__mem_func__(self.__PressQuickSlot)

	def __SetQuickPageMode(self):
		self.pressNumber=ui.__mem_func__(self.__SelectQuickPage)

	def __PressQuickSlot(self, localSlotIndex):
		if localeInfo.IsARABIC():
			if 0 <= localSlotIndex and localSlotIndex < 4:
				player.RequestUseLocalQuickSlot(3-localSlotIndex)
			else:
				player.RequestUseLocalQuickSlot(11-localSlotIndex)
		else:
			player.RequestUseLocalQuickSlot(localSlotIndex)

	def __SelectQuickPage(self, pageIndex):
		self.quickSlotPageIndex = pageIndex
		player.SetQuickPage(pageIndex)

	def ToggleDebugInfo(self):
		self.isShowDebugInfo = not self.isShowDebugInfo
		if self.isShowDebugInfo:
			self.PrintCoord.Show()
			self.FrameRate.Show()
			self.Pitch.Show()
			self.Splat.Show()
			self.TextureNum.Show()
			self.ObjectNum.Show()
			self.ViewDistance.Show()
			self.PrintMousePos.Show()
		else:
			self.PrintCoord.Hide()
			self.FrameRate.Hide()
			self.Pitch.Hide()
			self.Splat.Hide()
			self.TextureNum.Hide()
			self.ObjectNum.Hide()
			self.ViewDistance.Hide()
			self.PrintMousePos.Hide()

	def __BuildDebugInfo(self):
		self.PrintCoord = ui.TextLine()
		self.PrintCoord.SetFontName(localeInfo.UI_DEF_FONT)
		self.PrintCoord.SetPosition(wndMgr.GetScreenWidth() - 270, 0)
		self.FrameRate = ui.TextLine()
		self.FrameRate.SetFontName(localeInfo.UI_DEF_FONT)
		self.FrameRate.SetPosition(wndMgr.GetScreenWidth() - 270, 20)
		self.Pitch = ui.TextLine()
		self.Pitch.SetFontName(localeInfo.UI_DEF_FONT)
		self.Pitch.SetPosition(wndMgr.GetScreenWidth() - 270, 40)
		self.Splat = ui.TextLine()
		self.Splat.SetFontName(localeInfo.UI_DEF_FONT)
		self.Splat.SetPosition(wndMgr.GetScreenWidth() - 270, 60)
		self.PrintMousePos = ui.TextLine()
		self.PrintMousePos.SetFontName(localeInfo.UI_DEF_FONT)
		self.PrintMousePos.SetPosition(wndMgr.GetScreenWidth() - 270, 80)
		self.TextureNum = ui.TextLine()
		self.TextureNum.SetFontName(localeInfo.UI_DEF_FONT)
		self.TextureNum.SetPosition(wndMgr.GetScreenWidth() - 270, 100)
		self.ObjectNum = ui.TextLine()
		self.ObjectNum.SetFontName(localeInfo.UI_DEF_FONT)
		self.ObjectNum.SetPosition(wndMgr.GetScreenWidth() - 270, 120)
		self.ViewDistance = ui.TextLine()
		self.ViewDistance.SetFontName(localeInfo.UI_DEF_FONT)
		self.ViewDistance.SetPosition(0, 0)

	def __NotifyError(self, msg):
		chat.AppendChat(chat.CHAT_TYPE_INFO, msg)

	def ChangePKMode(self):
		if not app.IsPressed(app.DIK_LCONTROL):
			return
		if player.GetStatus(player.LEVEL)<constInfo.PVPMODE_PROTECTED_LEVEL:
			self.__NotifyError(localeInfo.OPTION_PVPMODE_PROTECT % (constInfo.PVPMODE_PROTECTED_LEVEL))
			return
		curTime = app.GetTime()
		if curTime - self.lastPKModeSendedTime < constInfo.PVPMODE_ACCELKEY_DELAY:
			return
		self.lastPKModeSendedTime = curTime
		curPKMode = player.GetPKMode()
		nextPKMode = curPKMode + 1
		if nextPKMode == player.PK_MODE_PROTECT:
			if 0 == player.GetGuildID():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_CANNOT_SET_GUILD_MODE)
				nextPKMode = 0
			else:
				nextPKMode = player.PK_MODE_GUILD
		elif nextPKMode == player.PK_MODE_MAX_NUM:
			nextPKMode = 0
		net.SendChatPacket("/PKMode " + str(nextPKMode))
		print "/PKMode " + str(nextPKMode)

	def OnChangePKMode(self):
		self.interface.OnChangePKMode()
		try:
			self.__NotifyError(localeInfo.OPTION_PVPMODE_MESSAGE_DICT[player.GetPKMode()])
		except KeyError:
			print "UNKNOWN PVPMode[%d]" % (player.GetPKMode())
		if constInfo.PVPMODE_TEST_ENABLE:
			curPKMode = player.GetPKMode()
			alignment, grade = chr.testGetPKData()
			self.pkModeNameDict = { 0 : "PEACE", 1 : "REVENGE", 2 : "FREE", 3 : "PROTECT", }
			self.testPKMode.SetText("Current PK Mode : " + self.pkModeNameDict.get(curPKMode, "UNKNOWN"))
			self.testAlignment.SetText("Current Alignment : " + str(alignment) + " (" + localeInfo.TITLE_NAME_LIST[grade] + ")")

	def StartGame(self):
		self.RefreshInventory()
		self.RefreshEquipment()
		self.RefreshCharacter()
		self.RefreshSkill()

	def CheckGameButton(self):
		if self.interface:
			self.interface.CheckGameButton()

	def RefreshAlignment(self):
		self.interface.RefreshAlignment()

	def RefreshStatus(self):
		self.CheckGameButton()

		if self.interface:
			self.interface.RefreshStatus()
		if self.playerGauge:
			self.playerGauge.RefreshGauge()

	def RefreshStamina(self):
		self.interface.RefreshStamina()

	def RefreshSkill(self):
		self.CheckGameButton()
		if self.interface:
			self.interface.RefreshSkill()

	def RefreshQuest(self):
		self.interface.RefreshQuest()

	def RefreshMessenger(self):
		self.interface.RefreshMessenger()

	def RefreshGuildInfoPage(self):
		self.interface.RefreshGuildInfoPage()

	def RefreshGuildBoardPage(self):
		self.interface.RefreshGuildBoardPage()

	def RefreshGuildMemberPage(self):
		self.interface.RefreshGuildMemberPage()

	def RefreshGuildMemberPageGradeComboBox(self):
		self.interface.RefreshGuildMemberPageGradeComboBox()

	def RefreshGuildSkillPage(self):
		self.interface.RefreshGuildSkillPage()

	def RefreshGuildGradePage(self):
		self.interface.RefreshGuildGradePage()

	def RefreshMobile(self):
		if self.interface:
			self.interface.RefreshMobile()

	def OnMobileAuthority(self):
		self.interface.OnMobileAuthority()

	def OnBlockMode(self, mode):
		self.interface.OnBlockMode(mode)

	def OpenQuestWindow(self, skin, idx):
		self.interface.OpenQuestWindow(skin, idx)

	def AskGuildName(self):

		guildNameBoard = uiCommon.InputDialog()
		guildNameBoard.SetTitle(localeInfo.GUILD_NAME)
		guildNameBoard.SetAcceptEvent(ui.__mem_func__(self.ConfirmGuildName))
		guildNameBoard.SetCancelEvent(ui.__mem_func__(self.CancelGuildName))
		guildNameBoard.Open()
		self.guildNameBoard = guildNameBoard

	def ConfirmGuildName(self):
		guildName = self.guildNameBoard.GetText()
		if not guildName:
			return
		if net.IsInsultIn(guildName):
			self.PopupMessage(localeInfo.GUILD_CREATE_ERROR_INSULT_NAME)
			return

		net.SendAnswerMakeGuildPacket(guildName)
		self.guildNameBoard.Close()
		self.guildNameBoard = None
		return True

	def CancelGuildName(self):
		self.guildNameBoard.Close()
		self.guildNameBoard = None
		return True

	def PopupMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, 0, localeInfo.UI_OK)

	def OpenRefineDialog(self, targetItemPos, nextGradeItemVnum, cost, prob, type=0):
		self.interface.OpenRefineDialog(targetItemPos, nextGradeItemVnum, cost, prob, type)

	def AppendMaterialToRefineDialog(self, vnum, count):
		self.interface.AppendMaterialToRefineDialog(vnum, count)

	def RunUseSkillEvent(self, slotIndex, coolTime):
		self.interface.OnUseSkill(slotIndex, coolTime)

	def ClearAffects(self):
		self.affectShower.ClearAffects()

	def SetAffect(self, affect):
		self.affectShower.SetAffect(affect)

	def ResetAffect(self, affect):
		self.affectShower.ResetAffect(affect)

	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		self.affectShower.BINARY_NEW_AddAffect(type, pointIdx, value, duration)
		if chr.NEW_AFFECT_DRAGON_SOUL_DECK1 == type or chr.NEW_AFFECT_DRAGON_SOUL_DECK2 == type:
			self.interface.DragonSoulActivate(type - chr.NEW_AFFECT_DRAGON_SOUL_DECK1)
		elif chr.NEW_AFFECT_DRAGON_SOUL_QUALIFIED == type:
			self.BINARY_DragonSoulGiveQuilification()

	def BINARY_NEW_RemoveAffect(self, type, pointIdx):
		self.affectShower.BINARY_NEW_RemoveAffect(type, pointIdx)
		if chr.NEW_AFFECT_DRAGON_SOUL_DECK1 == type or chr.NEW_AFFECT_DRAGON_SOUL_DECK2 == type:
			self.interface.DragonSoulDeactivate()

	def ActivateSkillSlot(self, slotIndex):
		if self.interface:
			self.interface.OnActivateSkill(slotIndex)

	def DeactivateSkillSlot(self, slotIndex):
		if self.interface:
			self.interface.OnDeactivateSkill(slotIndex)

	def RefreshEquipment(self):
		if self.interface:
			self.interface.RefreshInventory()

	def RefreshInventory(self):
		if self.interface:
			self.interface.RefreshInventory()

	def RefreshCharacter(self):
		if self.interface:
			self.interface.RefreshCharacter()

	def OnGameOver(self):
		self.CloseTargetBoard()
		self.OpenRestartDialog()

	if app.RENEWAL_DEAD_PACKET:
		def OnGameOver(self, d_time):
			self.CloseTargetBoard()
			self.OpenRestartDialog(d_time)
	else:
		def OnGameOver(self):
			self.CloseTargetBoard()
			self.OpenRestartDialog()

	def OpenRestartDialog(self):
		self.interface.OpenRestartDialog()

	if app.RENEWAL_DEAD_PACKET:
		def OpenRestartDialog(self, d_time):
			self.interface.OpenRestartDialog(d_time)
	else:
		def OpenRestartDialog(self):
			self.interface.OpenRestartDialog()
		
	def ChangeCurrentSkill(self, skillSlotNumber):
		self.interface.OnChangeCurrentSkill(skillSlotNumber)

	def SetPCTargetBoard(self, vid, name):
		self.targetBoard.Open(vid, name)
		if app.IsPressed(app.DIK_LCONTROL):
			if not player.IsSameEmpire(vid):
				return
			if player.IsMainCharacterIndex(vid):
				return
			elif chr.INSTANCE_TYPE_BUILDING == chr.GetInstanceType(vid):
				return
			self.interface.OpenWhisperDialog(name)

	def RefreshTargetBoardByVID(self, vid):
		self.targetBoard.RefreshByVID(vid)

	def RefreshTargetBoardByName(self, name):
		self.targetBoard.RefreshByName(name)

	def __RefreshTargetBoard(self):
		self.targetBoard.Refresh()

	if app.ENABLE_VIEW_TARGET_DECIMAL_HP:
		def SetHPTargetBoard(self, vid, hpPercentage, iMinHP, iMaxHP):
			if vid != self.targetBoard.GetTargetVID():
				self.targetBoard.ResetTargetBoard()
				self.targetBoard.SetEnemyVID(vid)
			self.targetBoard.SetHP(hpPercentage, iMinHP, iMaxHP)
			self.targetBoard.Show()
	else:
		def SetHPTargetBoard(self, vid, hpPercentage):
			if vid != self.targetBoard.GetTargetVID():
				self.targetBoard.ResetTargetBoard()
				self.targetBoard.SetEnemyVID(vid)	
			self.targetBoard.SetHP(hpPercentage)
			self.targetBoard.Show()
			
	def CloseTargetBoardIfDifferent(self, vid):
		if vid != self.targetBoard.GetTargetVID():
			self.targetBoard.Close()

	def CloseTargetBoard(self):
		self.targetBoard.Close()

	def OpenEquipmentDialog(self, vid):
		self.interface.OpenEquipmentDialog(vid)

	def OpenEquipmentDialog(self, vid):
		if app.ENABLE_PVP_ADVANCED:
			pvp.DUEL_IS_SHOW_EQUIP = 0
			pvp.DUEL_SAVE_VID = (int(vid))
		self.interface.OpenEquipment

	def SetEquipmentDialogItem(self, vid, slotIndex, vnum, count):
		self.interface.SetEquipmentDialogItem(vid, slotIndex, vnum, count)

	def SetEquipmentDialogSocket(self, vid, slotIndex, socketIndex, value):
		self.interface.SetEquipmentDialogSocket(vid, slotIndex, socketIndex, value)

	def SetEquipmentDialogAttr(self, vid, slotIndex, attrIndex, type, value):
		self.interface.SetEquipmentDialogAttr(vid, slotIndex, attrIndex, type, value)

	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def BINARY_OpenWhisperBySearchName(self, name):
			self.interface.OpenWhisperDialog(name)

		def BINARY_Profile_OnRecvData(self, name, job, level, empire, guild, language, status, location, year, month, day):	
			self.interface.RecvWhisperProfile(name, job, level, empire, guild, language, status, location, year, month, day)
			if str(name) == str(player.GetMainCharacterName()):
				uicontact.PROFILE_DICT.update({"job":job,"status":status,"location":location,"year":year,"month":month,"day":day})

	def ShowMapName(self, mapName, x, y):
		if self.mapNameShower:
			self.mapNameShower.ShowMapName(mapName, x, y)
		if self.interface:
			self.interface.SetMapName(mapName)

	def BINARY_OpenAtlasWindow(self):
		self.interface.BINARY_OpenAtlasWindow()

	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def OnRecvWhisper(self, mode, name, line, job, level, empire, guild, language, status, location, year, month, day):
			if mode == chat.WHISPER_TYPE_GM:
				self.interface.RegisterGameMasterName(name)
			chat.AppendWhisper(mode, name, "%s %s" % (uicontact.GetWhisperSendedTime(), line))
			self.interface.RecvWhisper(name, job, level, empire, guild, language, status, location, year, month, day)
	else:
		def OnRecvWhisper(self, mode, name, line):
			if mode == chat.WHISPER_TYPE_GM:
				self.interface.RegisterGameMasterName(name)
			chat.AppendWhisper(mode, name, line)
			self.interface.RecvWhisper(name)

	def OnRecvWhisperSystemMessage(self, mode, name, line):
		chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, line)
		self.interface.RecvWhisper(name)

	def OnRecvWhisperError(self, mode, name, line):
		if localeInfo.WHISPER_ERROR.has_key(mode):
			chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, localeInfo.WHISPER_ERROR[mode](name))
		else:
			chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, "Whisper Unknown Error(mode=%d, name=%s)" % (mode, name))
		self.interface.RecvWhisper(name)

	def RecvWhisper(self, name):
		self.interface.RecvWhisper(name)

	def OnPickMoney(self, money):
		self.interface.OnPickMoneyNew(money)

	def OnShopError(self, type):
		try:
			self.PopupMessage(localeInfo.SHOP_ERROR_DICT[type])
		except KeyError:
			self.PopupMessage(localeInfo.SHOP_ERROR_UNKNOWN % (type))

	def OnSafeBoxError(self):
		self.PopupMessage(localeInfo.SAFEBOX_ERROR)

	def OnFishingSuccess(self, isFish, fishName):
		chat.AppendChatWithDelay(chat.CHAT_TYPE_INFO, localeInfo.FISHING_SUCCESS(isFish, fishName), 2000)

	def OnFishingNotifyUnknown(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.FISHING_UNKNOWN)

	def OnFishingWrongPlace(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.FISHING_WRONG_PLACE)

	def OnFishingNotify(self, isFish, fishName):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.FISHING_NOTIFY(isFish, fishName))

	def OnFishingFailure(self):
		chat.AppendChatWithDelay(chat.CHAT_TYPE_INFO, localeInfo.FISHING_FAILURE, 2000)

	def OnCannotPickItem(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GAME_CANNOT_PICK_ITEM)

	def OnCannotMining(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GAME_CANNOT_MINING)

	def OnCannotUseSkill(self, vid, type):
		if localeInfo.USE_SKILL_ERROR_TAIL_DICT.has_key(type):
			textTail.RegisterInfoTail(vid, localeInfo.USE_SKILL_ERROR_TAIL_DICT[type])
		if localeInfo.USE_SKILL_ERROR_CHAT_DICT.has_key(type):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_SKILL_ERROR_CHAT_DICT[type])

	def	OnCannotShotError(self, vid, type):
		textTail.RegisterInfoTail(vid, localeInfo.SHOT_ERROR_TAIL_DICT.get(type, localeInfo.SHOT_ERROR_UNKNOWN % (type)))

	def StartPointReset(self):
		self.interface.OpenPointResetDialog()

	if (app.WJ_COMBAT_ZONE):
		def StartShop(self, vid, points, curLimit, maxLimit):
			self.interface.OpenShopDialog(vid, points, curLimit, maxLimit)
	else:
		def StartShop(self, vid):
			self.interface.OpenShopDialog(vid)

	def EndShop(self):
		self.interface.CloseShopDialog()

	def RefreshShop(self):
		self.interface.RefreshShopDialog()

	def SetShopSellingPrice(self, Price):
		pass

	def StartExchange(self):
		self.interface.StartExchange()

	def EndExchange(self):
		self.interface.EndExchange()

	def RefreshExchange(self):
		self.interface.RefreshExchange()

	def RecvPartyInviteQuestion(self, leaderVID, leaderName):
		partyInviteQuestionDialog = uiCommon.QuestionDialog()
		partyInviteQuestionDialog.SetText(leaderName + localeInfo.PARTY_DO_YOU_JOIN)
		partyInviteQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerPartyInvite(arg))
		partyInviteQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerPartyInvite(arg))
		partyInviteQuestionDialog.Open()
		partyInviteQuestionDialog.partyLeaderVID = leaderVID
		self.partyInviteQuestionDialog = partyInviteQuestionDialog

	def AnswerPartyInvite(self, answer):
		if not self.partyInviteQuestionDialog:
			return
		partyLeaderVID = self.partyInviteQuestionDialog.partyLeaderVID
		distance = player.GetCharacterDistance(partyLeaderVID)
		if distance < 0.0 or distance > 5000:
			answer = False
		net.SendPartyInviteAnswerPacket(partyLeaderVID, answer)
		self.partyInviteQuestionDialog.Close()
		self.partyInviteQuestionDialog = None

	def AddPartyMember(self, pid, name):
		self.interface.AddPartyMember(pid, name)

	def UpdatePartyMemberInfo(self, pid):
		self.interface.UpdatePartyMemberInfo(pid)

	def RemovePartyMember(self, pid):
		self.interface.RemovePartyMember(pid)
		self.__RefreshTargetBoard()

	def LinkPartyMember(self, pid, vid):
		self.interface.LinkPartyMember(pid, vid)

	def UnlinkPartyMember(self, pid):
		self.interface.UnlinkPartyMember(pid)

	def UnlinkAllPartyMember(self):
		self.interface.UnlinkAllPartyMember()

	def ExitParty(self):
		self.interface.ExitParty()
		self.RefreshTargetBoardByVID(self.targetBoard.GetTargetVID())

	def ChangePartyParameter(self, distributionMode):
		self.interface.ChangePartyParameter(distributionMode)

	def OnMessengerAddFriendQuestion(self, name):
		messengerAddFriendQuestion = uiCommon.QuestionDialog2()
		messengerAddFriendQuestion.SetText1(localeInfo.MESSENGER_DO_YOU_ACCEPT_ADD_FRIEND_1 % (name))
		messengerAddFriendQuestion.SetText2(localeInfo.MESSENGER_DO_YOU_ACCEPT_ADD_FRIEND_2)
		messengerAddFriendQuestion.SetAcceptEvent(ui.__mem_func__(self.OnAcceptAddFriend))
		messengerAddFriendQuestion.SetCancelEvent(ui.__mem_func__(self.OnDenyAddFriend))
		messengerAddFriendQuestion.Open()
		messengerAddFriendQuestion.name = name
		self.messengerAddFriendQuestion = messengerAddFriendQuestion

	def OnAcceptAddFriend(self):
		name = self.messengerAddFriendQuestion.name
		net.SendChatPacket("/messenger_auth y " + name)
		self.OnCloseAddFriendQuestionDialog()
		return True

	def OnDenyAddFriend(self):
		name = self.messengerAddFriendQuestion.name
		net.SendChatPacket("/messenger_auth n " + name)
		self.OnCloseAddFriendQuestionDialog()
		return True

	def OnCloseAddFriendQuestionDialog(self):
		self.messengerAddFriendQuestion.Close()
		self.messengerAddFriendQuestion = None
		return True

	def OpenSafeboxWindow(self, size):
		self.interface.OpenSafeboxWindow(size)

	def RefreshSafebox(self):
		self.interface.RefreshSafebox()

	def RefreshSafeboxMoney(self):
		self.interface.RefreshSafeboxMoney()

	def OpenMallWindow(self, size):
		self.interface.OpenMallWindow(size)

	def RefreshMall(self):
		self.interface.RefreshMall()

	def RecvGuildInviteQuestion(self, guildID, guildName):
		guildInviteQuestionDialog = uiCommon.QuestionDialog()
		guildInviteQuestionDialog.SetText(guildName + localeInfo.GUILD_DO_YOU_JOIN)
		guildInviteQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerGuildInvite(arg))
		guildInviteQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerGuildInvite(arg))
		guildInviteQuestionDialog.Open()
		guildInviteQuestionDialog.guildID = guildID
		self.guildInviteQuestionDialog = guildInviteQuestionDialog

	def AnswerGuildInvite(self, answer):
		if not self.guildInviteQuestionDialog:
			return
		guildLeaderVID = self.guildInviteQuestionDialog.guildID
		net.SendGuildInviteAnswerPacket(guildLeaderVID, answer)
		self.guildInviteQuestionDialog.Close()
		self.guildInviteQuestionDialog = None

	def DeleteGuild(self):
		self.interface.DeleteGuild()

	def ShowClock(self, second):
		self.interface.ShowClock(second)

	def HideClock(self):
		self.interface.HideClock()

	def BINARY_ActEmotion(self, emotionIndex):
		if self.interface.wndCharacter:
			self.interface.wndCharacter.ActEmotion(emotionIndex)

	def CheckFocus(self):
		if False == self.IsFocus():
			if True == self.interface.IsOpenChat():
				self.interface.ToggleChat()
			self.SetFocus()

	def SaveScreen(self):
		print "save screen"
		if SCREENSHOT_CWDSAVE:
			if not os.path.exists(os.getcwd()+os.sep+"screenshot"):
				os.mkdir(os.getcwd()+os.sep+"screenshot")
			(succeeded, name) = grp.SaveScreenShotToPath(os.getcwd()+os.sep+"screenshot"+os.sep)
		elif SCREENSHOT_DIR:
			(succeeded, name) = grp.SaveScreenShot(SCREENSHOT_DIR)
		else:
			(succeeded, name) = grp.SaveScreenShot()
		if succeeded:
			pass
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SCREENSHOT_SAVE_FAILURE)

	def ShowConsole(self):
		if debugInfo.IsDebugMode() or True == self.consoleEnable:
			player.EndKeyWalkingImmediately()
			self.console.OpenWindow()

	def ShowName(self):
		self.ShowNameFlag = True
		self.playerGauge.EnableShowAlways()
		player.SetQuickPage(self.quickSlotPageIndex+1)

	def __IsShowName(self):
		if systemSetting.IsAlwaysShowName():
			return True
		if self.ShowNameFlag:
			return True
		return False

	def HideName(self):
		self.ShowNameFlag = False
		self.playerGauge.DisableShowAlways()
		player.SetQuickPage(self.quickSlotPageIndex)

	def ShowMouseImage(self):
		self.interface.ShowMouseImage()

	def HideMouseImage(self):
		self.interface.HideMouseImage()

	def StartAttack(self):
		player.SetAttackKeyState(True)

	def EndAttack(self):
		player.SetAttackKeyState(False)

	def BINARY_Update_Maintenance(self, iTime, iDuration, iReason):
		sTime = int(iTime)
		sDuration = int(iDuration)
		sReason = str(iReason)
		if sTime != 0 and sDuration != 0:
			self.wndMaintenance.OpenMaintenance(int(iTime), int(iDuration), str(iReason))

	def MoveUp(self):
		player.SetSingleDIKKeyState(app.DIK_UP, True)

	def MoveDown(self):
		player.SetSingleDIKKeyState(app.DIK_DOWN, True)

	def MoveLeft(self):
		player.SetSingleDIKKeyState(app.DIK_LEFT, True)

	def MoveRight(self):
		player.SetSingleDIKKeyState(app.DIK_RIGHT, True)

	def StopUp(self):
		player.SetSingleDIKKeyState(app.DIK_UP, False)

	def StopDown(self):
		player.SetSingleDIKKeyState(app.DIK_DOWN, False)

	def StopLeft(self):
		player.SetSingleDIKKeyState(app.DIK_LEFT, False)

	def StopRight(self):
		player.SetSingleDIKKeyState(app.DIK_RIGHT, False)

	def PickUpItem(self):
		player.PickCloseItemVector()

	def OnKeyDown(self, key):
		if self.interface.wndWeb and self.interface.wndWeb.IsShow():
			return
		if key == app.DIK_ESC:
			self.RequestDropItem(False)
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
		try:
			self.onPressKeyDict[key]()
		except KeyError:
			pass
		except:
			raise
		return True

	def OnKeyUp(self, key):
		try:
			self.onClickKeyDict[key]()
		except KeyError:
			pass
		except:
			raise
		return True

	def OnMouseLeftButtonDown(self):
		if self.interface.BUILD_OnMouseLeftButtonDown():
			return
		if mouseModule.mouseController.isAttached():
			self.CheckFocus()
		else:
			hyperlink = ui.GetHyperlink()
			if hyperlink:
				return
			else:
				self.CheckFocus()
				player.SetMouseState(player.MBT_LEFT, player.MBS_PRESS);
		return True

	def OnMouseLeftButtonUp(self):
		if self.interface.BUILD_OnMouseLeftButtonUp():
			return
		if mouseModule.mouseController.isAttached():
			attachedType = mouseModule.mouseController.GetAttachedType()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()
			attachedItemSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()
			if player.SLOT_TYPE_QUICK_SLOT == attachedType:
				player.RequestDeleteGlobalQuickSlot(attachedItemSlotPos)
			elif player.SLOT_TYPE_INVENTORY == attachedType:
				if player.ITEM_MONEY == attachedItemIndex:
					self.__PutMoney(attachedType, attachedItemCount, self.PickingCharacterIndex)
				else:
					self.__PutItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, self.PickingCharacterIndex)
			elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
				self.__PutItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, self.PickingCharacterIndex)
			if app.ENABLE_SPECIAL_STORAGE:
				if player.SLOT_TYPE_UPGRADE_INVENTORY == attachedType or\
					player.SLOT_TYPE_BOOK_INVENTORY == attachedType or\
					player.SLOT_TYPE_STONE_INVENTORY == attachedType:
					self.__PutItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, self.PickingCharacterIndex)
			mouseModule.mouseController.DeattachObject()
		else:
			hyperlink = ui.GetHyperlink()
			if hyperlink:
				if app.IsPressed(app.DIK_LALT):
					link = chat.GetLinkFromHyperlink(hyperlink)
					ime.PasteString(link)
				else:
					self.interface.MakeHyperlinkTooltip(hyperlink)
				return
			else:
				player.SetMouseState(player.MBT_LEFT, player.MBS_CLICK)
		return True

	def __PutItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, dstChrID):
		if app.ENABLE_SPECIAL_STORAGE:
			if player.SLOT_TYPE_INVENTORY == attachedType or\
				player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType or\
				player.SLOT_TYPE_UPGRADE_INVENTORY == attachedType or\
				player.SLOT_TYPE_BOOK_INVENTORY == attachedType or\
				player.SLOT_TYPE_STONE_INVENTORY == attachedType:
				attachedInvenType = player.SlotTypeToInvenType(attachedType)
				if True == chr.HasInstance(self.PickingCharacterIndex) and player.GetMainCharacterIndex() != dstChrID:
					if player.IsEquipmentSlot(attachedItemSlotPos) and\
						player.SLOT_TYPE_DRAGON_SOUL_INVENTORY != attachedType and\
						player.SLOT_TYPE_UPGRADE_INVENTORY != attachedType and\
						player.SLOT_TYPE_BOOK_INVENTORY != attachedType and\
						player.SLOT_TYPE_STONE_INVENTORY != attachedType:
						self.stream.popupWindow.Close()
						self.stream.popupWindow.Open(localeInfo.EXCHANGE_FAILURE_EQUIP_ITEM, 0, localeInfo.UI_OK)
					else:
						if chr.IsNPC(dstChrID):
							if app.ENABLE_REFINE_RENEWAL:
								constInfo.AUTO_REFINE_TYPE = 2
								constInfo.AUTO_REFINE_DATA["NPC"][0] = dstChrID
								constInfo.AUTO_REFINE_DATA["NPC"][1] = attachedInvenType
								constInfo.AUTO_REFINE_DATA["NPC"][2] = attachedItemSlotPos
								constInfo.AUTO_REFINE_DATA["NPC"][3] = attachedItemCount
							net.SendGiveItemPacket(dstChrID, attachedInvenType, attachedItemSlotPos, attachedItemCount)
						else:
							net.SendExchangeStartPacket(dstChrID)
							net.SendExchangeItemAddPacket(attachedInvenType, attachedItemSlotPos, 0)
				else:
					self.__DropItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount)
		else:
			if player.SLOT_TYPE_INVENTORY == attachedType or player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
				attachedInvenType = player.SlotTypeToInvenType(attachedType)
				if True == chr.HasInstance(self.PickingCharacterIndex) and player.GetMainCharacterIndex() != dstChrID:
					if player.IsEquipmentSlot(attachedItemSlotPos) and player.SLOT_TYPE_DRAGON_SOUL_INVENTORY != attachedType:
						self.stream.popupWindow.Close()
						self.stream.popupWindow.Open(localeInfo.EXCHANGE_FAILURE_EQUIP_ITEM, 0, localeInfo.UI_OK)
					else:
						if chr.IsNPC(dstChrID):
							if app.ENABLE_REFINE_RENEWAL:
								constInfo.AUTO_REFINE_TYPE = 2
								constInfo.AUTO_REFINE_DATA["NPC"][0] = dstChrID
								constInfo.AUTO_REFINE_DATA["NPC"][1] = attachedInvenType
								constInfo.AUTO_REFINE_DATA["NPC"][2] = attachedItemSlotPos
								constInfo.AUTO_REFINE_DATA["NPC"][3] = attachedItemCount
							net.SendGiveItemPacket(dstChrID, attachedInvenType, attachedItemSlotPos, attachedItemCount)
						else:
							net.SendExchangeStartPacket(dstChrID)
							net.SendExchangeItemAddPacket(attachedInvenType, attachedItemSlotPos, 0)
				else:
					self.__DropItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount)

	def __PutMoney(self, attachedType, attachedMoney, dstChrID):
		if True == chr.HasInstance(dstChrID) and player.GetMainCharacterIndex() != dstChrID:
			net.SendExchangeStartPacket(dstChrID)
			net.SendExchangeElkAddPacket(attachedMoney)
		else:
			self.__DropMoney(attachedType, attachedMoney)

	def __DropMoney(self, attachedType, attachedMoney):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
		if attachedMoney>=1000:
			self.stream.popupWindow.Close()
			self.stream.popupWindow.Open(localeInfo.DROP_MONEY_FAILURE_1000_OVER, 0, localeInfo.UI_OK)
			return
		itemDropQuestionDialog = uiCommon.QuestionDialog()
		itemDropQuestionDialog.SetText(localeInfo.DO_YOU_DROP_MONEY % (attachedMoney))
		itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
		itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
		itemDropQuestionDialog.Open()
		itemDropQuestionDialog.dropType = attachedType
		itemDropQuestionDialog.dropCount = attachedMoney
		itemDropQuestionDialog.dropNumber = player.ITEM_MONEY
		self.itemDropQuestionDialog = itemDropQuestionDialog

	def __DropItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
		if player.SLOT_TYPE_INVENTORY == attachedType and player.IsEquipmentSlot(attachedItemSlotPos):
			self.stream.popupWindow.Close()
			self.stream.popupWindow.Open(localeInfo.DROP_ITEM_FAILURE_EQUIP_ITEM, 0, localeInfo.UI_OK)
		else:
			if player.SLOT_TYPE_INVENTORY == attachedType:
				dropItemIndex = player.GetItemIndex(attachedItemSlotPos)
				item.SelectItem(dropItemIndex)
				dropItemName = item.GetItemName()
				questionText = localeInfo.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemCount)
				itemDropQuestionDialog = uiCommon.QuestionDialog()
				itemDropQuestionDialog.SetText(questionText)
				itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
				itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
				itemDropQuestionDialog.Open()
				itemDropQuestionDialog.dropType = attachedType
				itemDropQuestionDialog.dropNumber = attachedItemSlotPos
				itemDropQuestionDialog.dropCount = attachedItemCount
				self.itemDropQuestionDialog = itemDropQuestionDialog
				constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
			elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
				dropItemIndex = player.GetItemIndex(player.DRAGON_SOUL_INVENTORY, attachedItemSlotPos)
				item.SelectItem(dropItemIndex)
				dropItemName = item.GetItemName()
				questionText = localeInfo.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemCount)
				itemDropQuestionDialog = uiCommon.QuestionDialog()
				itemDropQuestionDialog.SetText(questionText)
				itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
				itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
				itemDropQuestionDialog.Open()
				itemDropQuestionDialog.dropType = attachedType
				itemDropQuestionDialog.dropNumber = attachedItemSlotPos
				itemDropQuestionDialog.dropCount = attachedItemCount
				self.itemDropQuestionDialog = itemDropQuestionDialog
				constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
			if app.ENABLE_SPECIAL_STORAGE:
				if player.SLOT_TYPE_UPGRADE_INVENTORY == attachedType or\
					player.SLOT_TYPE_BOOK_INVENTORY == attachedType or\
					player.SLOT_TYPE_STONE_INVENTORY == attachedType:
					dropItemIndex = player.GetItemIndex(player.SlotTypeToInvenType(attachedType), attachedItemSlotPos)
					item.SelectItem(dropItemIndex)
					dropItemName = item.GetItemName()
					questionText = localeInfo.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemCount)
					itemDropQuestionDialog = uiCommon.QuestionDialog()
					itemDropQuestionDialog.SetText(questionText)
					itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
					itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
					itemDropQuestionDialog.Open()
					itemDropQuestionDialog.dropType = attachedType
					itemDropQuestionDialog.dropNumber = attachedItemSlotPos
					itemDropQuestionDialog.dropCount = attachedItemCount
					self.itemDropQuestionDialog = itemDropQuestionDialog
					constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

	def RequestDropItem(self, answer):
		if not self.itemDropQuestionDialog:
			return
		if answer:
			dropType = self.itemDropQuestionDialog.dropType
			dropCount = self.itemDropQuestionDialog.dropCount
			dropNumber = self.itemDropQuestionDialog.dropNumber
			if player.SLOT_TYPE_INVENTORY == dropType:
				if dropNumber == player.ITEM_MONEY:
					net.SendGoldDropPacketNew(dropCount)
					snd.PlaySound("sound/ui/money.wav")
				else:
					self.__SendDropItemPacket(dropNumber, dropCount)
			elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == dropType:
					self.__SendDropItemPacket(dropNumber, dropCount, player.DRAGON_SOUL_INVENTORY)
			if app.ENABLE_SPECIAL_STORAGE:
				if player.SLOT_TYPE_UPGRADE_INVENTORY == dropType or\
					player.SLOT_TYPE_BOOK_INVENTORY == dropType or\
					player.SLOT_TYPE_STONE_INVENTORY == dropType:
					self.__SendDropItemPacket(dropNumber, dropCount, player.SlotTypeToInvenType(dropType))		
		self.itemDropQuestionDialog.Close()
		self.itemDropQuestionDialog = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

	def __SendDropItemPacket(self, itemVNum, itemCount, itemInvenType = player.INVENTORY):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
		net.SendItemDropPacketNew(itemInvenType, itemVNum, itemCount)

	def OnMouseRightButtonDown(self):
		self.CheckFocus()
		if True == mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()
		else:
			player.SetMouseState(player.MBT_RIGHT, player.MBS_PRESS)
		return True

	def OnMouseRightButtonUp(self):
		if True == mouseModule.mouseController.isAttached():
			return True
		player.SetMouseState(player.MBT_RIGHT, player.MBS_CLICK)
		return True

	def OnMouseMiddleButtonDown(self):
		player.SetMouseMiddleButtonState(player.MBS_PRESS)

	def OnMouseMiddleButtonUp(self):
		player.SetMouseMiddleButtonState(player.MBS_CLICK)
		if app.ENABLE_MANAGER_BANK_SYSTEM:
			self.managerAccountBank.OnUpdate()

	def OnUpdate(self):
		self.day_night()
		app.UpdateGame()
		if app.ENABLE_TITLE_SYSTEM:		
			self.wndTitleSystem.OnUpdate()		
		if 1 == constInfo.ENABLE_PICKUP:
			self.PickUpItem()
		if app.ENABLE_PVP_ADVANCED:
			if pvp.DUEL_IS_SHOW_EQUIP == int(1):
				self.interface.CloseEquipmentDialog(int(pvp.DUEL_SAVE_VID))
		if self.mapNameShower.IsShow():
			self.mapNameShower.Update()
		if self.isShowDebugInfo:
			self.UpdateDebugInfo()
		if self.enableXMasBoom:
			self.__XMasBoom_Update()
		self.interface.BUILD_OnUpdate()

	def day_night(self):
		import time	
		localtime = time.strftime("%H")
		night = {"01", "02", "03", "04", "05", "06", "07", "08", "00", "23", "22", "21", "20"}
		checky = ""
		for n in night:
			checky = checky + n + "xx"
		if constInfo.nacht == 0:
			if checky.find(localtime) !=-1:
				background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
				background.SetEnvironmentData(1)
				constInfo.tag = 0
				constInfo.nacht = 1
		if constInfo.tag == 0:
			if checky.find(localtime) ==-1:
				background.SetEnvironmentData(0)
				constInfo.tag = 1
				constInfo.nacht = 0

	def UpdateDebugInfo(self):
		(x, y, z) = player.GetMainCharacterPosition()
		nUpdateTime = app.GetUpdateTime()
		nUpdateFPS = app.GetUpdateFPS()
		nRenderFPS = app.GetRenderFPS()
		nFaceCount = app.GetFaceCount()
		fFaceSpeed = app.GetFaceSpeed()
		nST=background.GetRenderShadowTime()
		(fAveRT, nCurRT) =  app.GetRenderTime()
		(iNum, fFarCilp) = background.GetDistanceSetInfo()
		(iPatch, iSplat, fSplatRatio, sTextureNum) = background.GetRenderedSplatNum()
		if iPatch == 0:
			iPatch = 1
		self.PrintCoord.SetText("Coordinate: %.2f %.2f %.2f ATM: %d" % (x, y, z, app.GetAvailableTextureMemory()/(1024*1024)))
		xMouse, yMouse = wndMgr.GetMousePosition()
		self.PrintMousePos.SetText("MousePosition: %d %d" % (xMouse, yMouse))
		self.FrameRate.SetText("UFPS: %3d UT: %3d FS %.2f" % (nUpdateFPS, nUpdateTime, fFaceSpeed))
		if fAveRT>1.0:
			self.Pitch.SetText("RFPS: %3d RT:%.2f(%3d) FC: %d(%.2f) " % (nRenderFPS, fAveRT, nCurRT, nFaceCount, nFaceCount/fAveRT))
		self.Splat.SetText("PATCH: %d SPLAT: %d BAD(%.2f)" % (iPatch, iSplat, fSplatRatio))
		self.ViewDistance.SetText("Num : %d, FS : %f, FE : %f, FC : %f" % (iNum, fFarCilp))

	def OnRender(self):
		app.RenderGame()
		if systemSetting.IsShowSalesText():
			uiPrivateShopBuilder.UpdateADBoard()
		if self.console.Console.collision:
			background.RenderCollision()
			chr.RenderCollision()
		(x, y) = app.GetCursorPosition()
		textTail.UpdateAllTextTail()
		if True == wndMgr.IsPickedWindow(self.hWnd):
			self.PickingCharacterIndex = chr.Pick()
			if -1 != self.PickingCharacterIndex:
				textTail.ShowCharacterTextTail(self.PickingCharacterIndex)
			if 0 != self.targetBoard.GetTargetVID():
				textTail.ShowCharacterTextTail(self.targetBoard.GetTargetVID())
			if not self.__IsShowName():
				self.PickingItemIndex = item.Pick()
				if -1 != self.PickingItemIndex:
					textTail.ShowItemTextTail(self.PickingItemIndex)
		if self.__IsShowName():
			textTail.ShowAllTextTail()
			self.PickingItemIndex = textTail.Pick(x, y)
		textTail.UpdateShowingTextTail()
		textTail.ArrangeTextTail()
		if -1 != self.PickingItemIndex:
			textTail.SelectItemName(self.PickingItemIndex)
		grp.PopState()
		grp.SetInterfaceRenderState()
		textTail.Render()
		textTail.HideAllTextTail()

	def OnPressEscapeKey(self):
		if app.TARGET == app.GetCursor():
			app.SetCursor(app.NORMAL)
		elif True == mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()
		else:
			self.interface.OpenSystemDialog()
		return True

	def OnIMEReturn(self):
		if app.IsPressed(app.DIK_LSHIFT):
			self.interface.OpenWhisperDialogWithoutTarget()
		else:
			self.interface.ToggleChat()
		return True

	def OnPressExitKey(self):
		self.interface.ToggleSystemDialog()
		return True

	def BINARY_LoverInfo(self, name, lovePoint):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnAddLover(name, lovePoint)
		if self.affectShower:
			self.affectShower.SetLoverInfo(name, lovePoint)

	def BINARY_UpdateLovePoint(self, lovePoint):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnUpdateLovePoint(lovePoint)
		if self.affectShower:
			self.affectShower.OnUpdateLovePoint(lovePoint)

	if app.ENABLE_SEND_TARGET_INFO:
		def BINARY_AddTargetMonsterDropInfo(self, raceNum, itemVnum, itemCount):
			if not raceNum in constInfo.MONSTER_INFO_DATA:
				constInfo.MONSTER_INFO_DATA.update({raceNum : {}})
				constInfo.MONSTER_INFO_DATA[raceNum].update({"items" : []})
			curList = constInfo.MONSTER_INFO_DATA[raceNum]["items"]
			isUpgradeable = False
			isMetin = False
			item.SelectItem(itemVnum)
			if item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR:
				isUpgradeable = True
			elif item.GetItemType() == item.ITEM_TYPE_METIN:
				isMetin = True
			for curItem in curList:
				if isUpgradeable:
					if curItem.has_key("vnum_list") and curItem["vnum_list"][0] / 10 * 10 == itemVnum / 10 * 10:
						if not (itemVnum in curItem["vnum_list"]):
							curItem["vnum_list"].append(itemVnum)
						return
				elif isMetin:
					if curItem.has_key("vnum_list"):
						baseVnum = curItem["vnum_list"][0]
					if curItem.has_key("vnum_list") and (baseVnum - baseVnum%1000) == (itemVnum - itemVnum%1000):
						if not (itemVnum in curItem["vnum_list"]):
							curItem["vnum_list"].append(itemVnum)
						return
				else:
					if curItem.has_key("vnum") and curItem["vnum"] == itemVnum and curItem["count"] == itemCount:
						return
			if isUpgradeable or isMetin:
				curList.append({"vnum_list":[itemVnum], "count":itemCount})
			else:
				curList.append({"vnum":itemVnum, "count":itemCount})

		def BINARY_RefreshTargetMonsterDropInfo(self, raceNum):
			self.targetBoard.RefreshMonsterInfoBoard()

	def BINARY_OnQuestConfirm(self, msg, timeout, pid):
		confirmDialog = uiCommon.QuestionDialogWithTimeLimit()
		confirmDialog.Open(msg, timeout)
		confirmDialog.SetAcceptEvent(lambda answer=True, pid=pid: net.SendQuestConfirmPacket(answer, pid) or self.confirmDialog.Hide())
		confirmDialog.SetCancelEvent(lambda answer=False, pid=pid: net.SendQuestConfirmPacket(answer, pid) or self.confirmDialog.Hide())
		self.confirmDialog = confirmDialog

	def Gift_Show(self):
		self.interface.ShowGift()

	def BINARY_Cube_Open(self, npcVNUM):
		self.currentCubeNPC = npcVNUM
		self.interface.OpenCubeWindow()
		if npcVNUM not in self.cubeInformation:
			net.SendChatPacket("/cube r_info")
		else:
			cubeInfoList = self.cubeInformation[npcVNUM]
			i = 0
			for cubeInfo in cubeInfoList:
				self.interface.wndCube.AddCubeResultItem(cubeInfo["vnum"], cubeInfo["count"])
				j = 0
				for materialList in cubeInfo["materialList"]:
					for materialInfo in materialList:
						itemVnum, itemCount = materialInfo
						self.interface.wndCube.AddMaterialInfo(i, j, itemVnum, itemCount)
					j = j + 1
				i = i + 1
			self.interface.wndCube.Refresh()

	def BINARY_Cube_Close(self):
		self.interface.CloseCubeWindow()

	def BINARY_Cube_UpdateInfo(self, gold, itemVnum, count):
		self.interface.UpdateCubeInfo(gold, itemVnum, count)

	def BINARY_Cube_Succeed(self, itemVnum, count):
		print "Å¥ºê Á¦ÀÛ ¼º°ø"
		self.interface.SucceedCubeWork(itemVnum, count)
		pass

	def BINARY_Cube_Failed(self):
		print "Å¥ºê Á¦ÀÛ ½ÇÆÐ"
		self.interface.FailedCubeWork()
		pass

	def BINARY_Cube_ResultList(self, npcVNUM, listText):
		if npcVNUM == 0:
			npcVNUM = self.currentCubeNPC
		self.cubeInformation[npcVNUM] = []
		try:
			for eachInfoText in listText.split("/"):
				eachInfo = eachInfoText.split(",")
				itemVnum	= int(eachInfo[0])
				itemCount	= int(eachInfo[1])
				self.cubeInformation[npcVNUM].append({"vnum": itemVnum, "count": itemCount})
				self.interface.wndCube.AddCubeResultItem(itemVnum, itemCount)
			resultCount = len(self.cubeInformation[npcVNUM])
			requestCount = 7
			modCount = resultCount % requestCount
			splitCount = resultCount / requestCount
			for i in xrange(splitCount):
				net.SendChatPacket("/cube r_info %d %d" % (i * requestCount, requestCount))
			if 0 < modCount:
				net.SendChatPacket("/cube r_info %d %d" % (splitCount * requestCount, modCount))
		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0
		pass

	def BINARY_Cube_MaterialInfo(self, startIndex, listCount, listText):
		try:
			if 3 > len(listText):
				dbg.TraceError("Wrong Cube Material Infomation")
				return 0
			eachResultList = listText.split("@")
			cubeInfo = self.cubeInformation[self.currentCubeNPC]
			itemIndex = 0
			for eachResultText in eachResultList:
				cubeInfo[startIndex + itemIndex]["materialList"] = [[], [], [], [], []]
				materialList = cubeInfo[startIndex + itemIndex]["materialList"]
				gold = 0
				splitResult = eachResultText.split("/")
				if 1 < len(splitResult):
					gold = int(splitResult[1])
				eachMaterialList = splitResult[0].split("&")
				i = 0
				for eachMaterialText in eachMaterialList:
					complicatedList = eachMaterialText.split("|")
					if 0 < len(complicatedList):
						for complicatedText in complicatedList:
							(itemVnum, itemCount) = complicatedText.split(",")
							itemVnum = int(itemVnum)
							itemCount = int(itemCount)
							self.interface.wndCube.AddMaterialInfo(itemIndex + startIndex, i, itemVnum, itemCount)
							materialList[i].append((itemVnum, itemCount))
					else:
						itemVnum, itemCount = eachMaterialText.split(",")
						itemVnum = int(itemVnum)
						itemCount = int(itemCount)
						self.interface.wndCube.AddMaterialInfo(itemIndex + startIndex, i, itemVnum, itemCount)
						materialList[i].append((itemVnum, itemCount))
					i = i + 1
				itemIndex = itemIndex + 1
			self.interface.wndCube.Refresh()
		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0
		pass

	def BINARY_Highlight_Item(self, inven_type, inven_pos):
		if self.interface:
			self.interface.Highligt_Item(inven_type, inven_pos)

	def BINARY_DragonSoulGiveQuilification(self):
		self.interface.DragonSoulGiveQuilification()

	def BINARY_DragonSoulRefineWindow_Open(self):
		self.interface.OpenDragonSoulRefineWindow()

	def BINARY_DragonSoulRefineWindow_RefineFail(self, reason, inven_type, inven_pos):
		self.interface.FailDragonSoulRefine(reason, inven_type, inven_pos)

	def BINARY_DragonSoulRefineWindow_RefineSucceed(self, inven_type, inven_pos):
		self.interface.SucceedDragonSoulRefine(inven_type, inven_pos)

	def BINARY_SetBigMessage(self, message):
		self.interface.bigBoard.SetTip(message)

	def BINARY_SetTipMessage(self, message):
		self.interface.tipBoard.SetTip(message)

	def BINARY_AppendNotifyMessage(self, type):
		if not type in localeInfo.NOTIFY_MESSAGE:
			return
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.NOTIFY_MESSAGE[type])

	def BINARY_Guild_EnterGuildArea(self, areaID):
		self.interface.BULID_EnterGuildArea(areaID)

	def BINARY_Guild_ExitGuildArea(self, areaID):
		self.interface.BULID_ExitGuildArea(areaID)

	def BINARY_GuildWar_OnSendDeclare(self, guildID):
		pass

	def BINARY_GuildWar_OnRecvDeclare(self, guildID, warType):
		mainCharacterName = player.GetMainCharacterName()
		masterName = guild.GetGuildMasterName()
		if mainCharacterName == masterName:
			self.__GuildWar_OpenAskDialog(guildID, warType)

	def BINARY_GuildWar_OnRecvPoint(self, gainGuildID, opponentGuildID, point):
		self.interface.OnRecvGuildWarPoint(gainGuildID, opponentGuildID, point)

	def BINARY_GuildWar_OnStart(self, guildSelf, guildOpp):
		self.interface.OnStartGuildWar(guildSelf, guildOpp)

	def BINARY_GuildWar_OnEnd(self, guildSelf, guildOpp):
		self.interface.OnEndGuildWar(guildSelf, guildOpp)

	def BINARY_BettingGuildWar_SetObserverMode(self, isEnable):
		self.interface.BINARY_SetObserverMode(isEnable)

	def BINARY_BettingGuildWar_UpdateObserverCount(self, observerCount):
		self.interface.wndMiniMap.UpdateObserverCount(observerCount)

	if app.ENABLE_BIOLOG_SYSTEM:
		def BINARY_Biolog_Update(self, pLeftTime, pCountActual, pCountNeed, pVnum):
			uiprofessionalbiolog.BIOLOG_BINARY_LOADED["time"][0] = int(pLeftTime) + app.GetGlobalTimeStamp()
			uiprofessionalbiolog.BIOLOG_BINARY_LOADED["countActual"][0] = str(pCountActual)	
			uiprofessionalbiolog.BIOLOG_BINARY_LOADED["countNeed"][0] = str(pCountNeed)
			uiprofessionalbiolog.BIOLOG_BINARY_LOADED["vnum"][0] = int(pVnum)

		def BINARY_Biolog_SendMessage(self, pMessage):
			if str(pMessage) != "":
				self.wndBiologMessage = uiCommon.PopupDialog()
				self.wndBiologMessage.SetWidth(350)
				self.wndBiologMessage.SetText((str(pMessage).replace("$"," ")))
				self.wndBiologMessage.Show()
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Error, i could not initialize message from server!")

		def BINARY_Biolog_PopUp(self, iRewardType, iRewardItem, iBonusName_1, iBonusValue_1, iBonusName_2, iBonusValue_2):
			self.wndBiologSlider = uiprofessionalbiolog.Biolog_FinishSlider()
			self.wndBiologSlider.BINARY_BiologPopUp_Load([str(iRewardType), int(iRewardItem), str(iBonusName_1), int(iBonusValue_1), str(iBonusName_2), int(iBonusValue_2)])
			self.wndBiologSlider.Show()

		def BINARY_Biolog_SelectReward(self, iTypeWindow, iRewardType, iBonusName_1, iBonusValue_1, iBonusName_2, iBonusValue_2, iBonusName_3, iBonusValue_3):
			self.wndBiologSelectReward = uiprofessionalbiolog.Biolog_SelectReward()
			self.wndBiologSelectReward.Open_SelectRewardType([int(iTypeWindow), str(iRewardType), str(iBonusName_1), int(iBonusValue_1), str(iBonusName_2), int(iBonusValue_2), str(iBonusName_3), int(iBonusValue_3)])
			self.wndBiologSelectReward.SetTitle((str(iRewardType).replace("$"," ")))
			self.wndBiologSelectReward.SetCenterPosition()
			self.wndBiologSelectReward.SetTop()
			self.wndBiologSelectReward.Show()

	def __GuildWar_UpdateMemberCount(self, guildID1, memberCount1, guildID2, memberCount2, observerCount):
		guildID1 = int(guildID1)
		guildID2 = int(guildID2)
		memberCount1 = int(memberCount1)
		memberCount2 = int(memberCount2)
		observerCount = int(observerCount)
		self.interface.UpdateMemberCount(guildID1, memberCount1, guildID2, memberCount2)
		self.interface.wndMiniMap.UpdateObserverCount(observerCount)

	def __GuildWar_OpenAskDialog(self, guildID, warType):
		guildName = guild.GetGuildName(guildID)
		if "Noname" == guildName:
			return
		import uiGuild
		questionDialog = uiGuild.AcceptGuildWarDialog()
		questionDialog.SAFE_SetAcceptEvent(self.__GuildWar_OnAccept)
		questionDialog.SAFE_SetCancelEvent(self.__GuildWar_OnDecline)
		questionDialog.Open(guildName, warType)
		self.guildWarQuestionDialog = questionDialog

	def __GuildWar_CloseAskDialog(self):
		self.guildWarQuestionDialog.Close()
		self.guildWarQuestionDialog = None

	def __GuildWar_OnAccept(self):
		guildName = self.guildWarQuestionDialog.GetGuildName()
		net.SendChatPacket("/war " + guildName)
		self.__GuildWar_CloseAskDialog()
		return 1

	def __GuildWar_OnDecline(self):
		guildName = self.guildWarQuestionDialog.GetGuildName()
		net.SendChatPacket("/nowar " + guildName)
		self.__GuildWar_CloseAskDialog()
		return 1

	def __ServerCommand_Build(self):
		serverCommandList={
			"ConsoleEnable" : self.__Console_Enable,
			"PRESERVE_DayMode" : self.__PRESERVE_DayMode_Update,
			"CloseRestartWindow" : self.__RestartDialog_Close,
			"OpenPrivateShop" : self.__PrivateShop_Open,
			"PartyHealReady" : self.PartyHealReady,
			"ShowMeSafeboxPassword"	: self.AskSafeboxPassword,
			"CloseSafebox" : self.CommandCloseSafebox,
            "Teamler_on" : self.__Team_On,
            "Teamler_off" : self.__Team_Off, 
			"CloseMall" : self.CommandCloseMall,
			"ShowMeMallPassword" : self.AskMallPassword,
			"item_mall" : self.__ItemMall_Open,
			"RefineSuceeded" : self.RefineSuceededMessage,
			"RefineFailed" : self.RefineFailedMessage,
			"xmas_snow" : self.__XMasSnow_Enable,
			"xmas_tree" : self.__XMasTree_Enable,
			"PartyRequest" : self.__PartyRequestQuestion,
			"PartyRequestDenied" : self.__PartyRequestDenied,
			"horse_state" : self.__Horse_UpdateState,
			"hide_horse_state" : self.__Horse_HideState,
			"WarUC" : self.__GuildWar_UpdateMemberCount,
			"test_server" : self.__EnableTestServerFlag,
			"mall" : self.__InGameShop_Show,
			"ITEMSHOP" : self.ManagerItemshop,
			"BINARY_Update_Maintenance"	: self.BINARY_Update_Maintenance,
			"BINARY_Biolog_Update" : self.BINARY_Biolog_Update,
			"BINARY_Biolog_SendMessage"	: self.BINARY_Biolog_SendMessage,	
			"BINARY_Biolog_PopUp" : self.BINARY_Biolog_PopUp,
			"BINARY_Biolog_SelectReward" : self.BINARY_Biolog_SelectReward,
			"lover_login" : self.__LoginLover,
			"lover_logout" : self.__LogoutLover,
			"lover_near" : self.__LoverNear,
			"lover_far" : self.__LoverFar,
			"BINARY_Duel_GetInfo" : self.BINARY_Duel_GetInfo,
			"BINARY_Duel_Request" : self.BINARY_Duel_Request,
			"BINARY_Duel_LiveInterface" : self.BINARY_Duel_LiveInterface,
			"BINARY_Duel_Delete" : self.BINARY_Duel_Delete,
			"BINARY_Duel_SendMessage" : self.BINARY_Duel_SendMessage,
			"lover_divorce" : self.__LoverDivorce,
			"MyShopPriceList" : self.__PrivateShop_PriceList,
			"shop" :self.NewShop,
			"shop_clear" :self.ShopClear,
			"shop_add" :self.ShopAdd,
			"shop_item" :self.ShopItem,
			"shop_cost" :self.ShopCost,
			"shop_cost_clear" :self.ShopCostClear,
			"shop_item_clear" :self.ShopItemClear,
			"gift_clear" :self.gift_clear,
			"gift_item" :self.gift_item,
			"gift_info" :self.gift_show,
			"gift_load" :self.gift_load,
			"BINARY_Localization_Append" : self.BINARY_Localization_Append,			
		}
		if app.ENABLE_MANAGER_BANK_SYSTEM:
			serverCommandList["BINARY_Account_Bank"] = self.managerAccountBank.Loading
		self.serverCommander=stringCommander.Analyzer()
		for serverCommandItem in serverCommandList.items():
			self.serverCommander.SAFE_RegisterCallBack(serverCommandItem[0], serverCommandItem[1])

	def __Team_On(self, name):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLogin(2, name)

	def __Team_Off(self, name):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLogout(2, name) 

	def BINARY_ServerCommand_Run(self, line):
		try:
			return self.serverCommander.Run(line)
		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0

	def __ProcessPreservedServerCommand(self):
		try:
			command = net.GetPreservedServerCommand()
			while command:
				print " __ProcessPreservedServerCommand", command
				self.serverCommander.Run(command)
				command = net.GetPreservedServerCommand()
		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0

	def NewShop(self):
		if self.uiNewShop:
			self.uiNewShop.Show()
	
	def ShopClear(self):
		if self.uiNewShop:
			self.uiNewShop.HideAll()
		constInfo.MyShops=[]
	def ShopCostClear(self):
		constInfo.shop_cost=[]
	def ShopCost(self,id,time,time_val,price):
		constInfo.shop_cost.append({"id":int(id),"time":int(time),"time_val":int(time_val),"price":int(price)})
	def ShopAdd(self,shop_id,shop_vid,szSign,gold,count,sold,days,date_close):
		if self.uiNewShop:
			shop={"id":shop_id, "vid":shop_vid, "name":szSign.replace("\\"," ").replace("_","#"), "gold":gold, "sold":sold, "items":int(count)-int(sold), "days":days, "time":date_close}
			self.uiNewShop.Load(shop)
			constInfo.MyShops.append(shop)

	def ShopItemClear(self):
		if self.uiNewShop:
			self.uiNewShop.ClearItems()

	def ShopItem(self,data):
		d=data.split("#")
		id=d[0]
		vnum=d[1]
		count=d[2]
		slot=d[3]
		price=d[4]
		s=d[5]
		a=d[6]
		sockets=[]
		for key in s.split("|"):
			sockets.append(int(key))
		attrs=[]
		for key in a.split("|"):
			a=key.split(",")
			attrs.append([int(a[0]),int(a[1])])
		if self.uiNewShop:
			self.uiNewShop.AddItem(slot,{"id":id,"vnum":vnum,"count":count,"price":price,"sockets":sockets,"attrs":attrs})
		
	def gift_clear(self):
		constInfo.gift_items={}
		self.interface.ClearGift()

	def gift_item(self, id, vnum, count, pos, date_add, give, reason, szSockets, szAttrs):
		sockets=[]
		for key in szSockets.split("|"):
			sockets.append(int(key))
		attrs=[]
		for key in szAttrs.split("|"):
			a=key.split(",")
			attrs.append([int(a[0]),int(a[1])])
		constInfo.gift_items[int(pos)]={"id":int(id),"vnum":int(vnum),"count":int(count),"pos":int(pos),"date_add":int(date_add),"reason":reason.replace("_"," "),"give":give.replace("_"," "),"sockets":sockets,"attrs":attrs}

	def gift_load(self):
		self.interface.wndGiftBox.Refresh()
	
	def gift_show(self,pages):
		self.interface.wndGiftBox.pageNum=int(pages)
		self.interface.OpenGift()	
	
	def PartyHealReady(self):
		self.interface.PartyHealReady()

	def AskSafeboxPassword(self):
		self.interface.AskSafeboxPassword()

	def AskMallPassword(self):
		self.interface.AskMallPassword()

	def __ItemMall_Open(self):
		self.interface.OpenItemMall();

	def CommandCloseMall(self):
		self.interface.CommandCloseMall()

	def RefineSuceededMessage(self):
		self.PopupMessage(localeInfo.REFINE_SUCCESS)
		if app.ENABLE_REFINE_RENEWAL:
			self.interface.CheckRefineDialog(False)

	def RefineFailedMessage(self):
		self.PopupMessage(localeInfo.REFINE_FAILURE)
		if app.ENABLE_REFINE_RENEWAL:
			self.interface.CheckRefineDialog(True)

	def CommandCloseSafebox(self):
		self.interface.CommandCloseSafebox()

	def __PrivateShop_PriceList(self, itemVNum, itemPrice):
		uiPrivateShopBuilder.SetPrivateShopItemPrice(itemVNum, itemPrice)

	def __Horse_HideState(self):
		self.affectShower.SetHorseState(0, 0, 0)

	if app.ENABLE_PVP_ADVANCED:
		def BINARY_Duel_GetInfo(self, a, b, c, d, e, f, g, h):
			self.wndDuelGui.OpenDialog(a, b, c, d, e, f, g, h)

		def BINARY_Duel_Request(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q):
			self.wndDuelGui.OpenDialog(a, b, c, d, e, f, g, h)
			self.wndDuelGui.Selected([int(i), int(j), int(k), int(l), int(m), int(n), int(o), int(p), int(q)])

		def BINARY_Duel_Delete(self):
			self.wndDuelGui.Remove()
			if self.wndDuelLive.IsShow():
				self.wndDuelLive.Hide()

		def BINARY_Duel_LiveInterface(self, a, b, c, d, e, f, g, h, i, j, k, l):
			self.wndDuelLive.ShowInformations([str(a), int(b), int(c), int(d), int(e), int(f), int(g), int(h), int(i), int(j), int(k), int(l)])

		def BINARY_Duel_SendMessage(self, textLine):
			if str(textLine) != "":
				self.wndMsg = message.PopupDialog()
				self.wndMsg.SetWidth(550)
				self.wndMsg.SetText((str(textLine).replace("$"," ")))
				self.wndMsg.Show()
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Error, i could not initialize message from server!")

	def __Horse_UpdateState(self, level, health, battery):
		self.affectShower.SetHorseState(int(level), int(health), int(battery))

	def __IsXMasMap(self):
		mapDict = ("metin2_map_n_flame_01", "metin2_map_n_desert_01", "metin2_map_spiderdungeon", "metin2_map_deviltower1", )
		if background.GetCurrentMapName() in mapDict:
			return False
		return True

	def __XMasSnow_Enable(self, mode):
		self.__XMasSong_Enable(mode)
		if "1"==mode:
			if not self.__IsXMasMap():
				return
			print "XMAS_SNOW ON"
			background.EnableSnow(1)
		else:
			print "XMAS_SNOW OFF"
			background.EnableSnow(0)

	def __XMasTree_Enable(self, grade):
		print "XMAS_TREE ", grade
		background.SetXMasTree(int(grade))

	def __RestartDialog_Close(self):
		self.interface.CloseRestartDialog()

	def __Console_Enable(self):
		constInfo.CONSOLE_ENABLE = True
		self.consoleEnable = True
		app.EnableSpecialCameraMode()
		ui.EnablePaste(True)

	def __PrivateShop_Open(self):
		self.uiNewShop.Show()

	def BINARY_PrivateShop_Appear(self, vid, text):
		self.interface.AppearPrivateShop(vid, text)

	def BINARY_PrivateShop_Disappear(self, vid):
		self.interface.DisappearPrivateShop(vid)

	def __PRESERVE_DayMode_Update(self, mode):
		if "light"==mode:
			background.SetEnvironmentData(0)
		elif "dark"==mode:
			if not self.__IsXMasMap():
				return
			background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
			background.SetEnvironmentData(1)

	def __DayMode_OnCompleteChangeToLight(self):
		background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
		background.SetEnvironmentData(0)
		self.curtain.FadeIn()

	def __DayMode_OnCompleteChangeToDark(self):
		background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
		background.SetEnvironmentData(1)
		self.curtain.FadeIn()

	def __XMasBoom_Update(self):
		self.BOOM_DATA_LIST = ( (2, 5), (5, 2), (7, 3), (10, 3), (20, 5) )
		if self.indexXMasBoom >= len(self.BOOM_DATA_LIST):
			return
		boomTime = self.BOOM_DATA_LIST[self.indexXMasBoom][0]
		boomCount = self.BOOM_DATA_LIST[self.indexXMasBoom][1]
		if app.GetTime() - self.startTimeXMasBoom > boomTime:
			self.indexXMasBoom += 1
			for i in xrange(boomCount):
				self.__XMasBoom_Boom()

	def __XMasBoom_Boom(self):
		x, y, z = player.GetMainCharacterPosition()
		randX = app.GetRandom(-150, 150)
		randY = app.GetRandom(-150, 150)
		snd.PlaySound3D(x+randX, -y+randY, z, "sound/common/etc/salute.mp3")

	def __PartyRequestQuestion(self, vid):
		vid = int(vid)
		partyRequestQuestionDialog = uiCommon.QuestionDialog()
		partyRequestQuestionDialog.SetText(chr.GetNameByVID(vid) + localeInfo.PARTY_DO_YOU_ACCEPT)
		partyRequestQuestionDialog.SetAcceptText(localeInfo.UI_ACCEPT)
		partyRequestQuestionDialog.SetCancelText(localeInfo.UI_DENY)
		partyRequestQuestionDialog.SetAcceptEvent(lambda arg=True: self.__AnswerPartyRequest(arg))
		partyRequestQuestionDialog.SetCancelEvent(lambda arg=False: self.__AnswerPartyRequest(arg))
		partyRequestQuestionDialog.Open()
		partyRequestQuestionDialog.vid = vid
		self.partyRequestQuestionDialog = partyRequestQuestionDialog

	def __AnswerPartyRequest(self, answer):
		if not self.partyRequestQuestionDialog:
			return
		vid = self.partyRequestQuestionDialog.vid
		if answer:
			net.SendChatPacket("/party_request_accept " + str(vid))
		else:
			net.SendChatPacket("/party_request_deny " + str(vid))
		self.partyRequestQuestionDialog.Close()
		self.partyRequestQuestionDialog = None

	def __PartyRequestDenied(self):
		self.PopupMessage(localeInfo.PARTY_REQUEST_DENIED)

	if (app.WJ_COMBAT_ZONE):
		def BINARY_CombatZone_Manager(self, tokens, arg1 = 0, arg2 = 0, arg3 = 0, arg4 = 0):
			if tokens == "OpenWindow":
				self.wndCombatZone.Open(arg1, arg2, arg3, arg4)
			elif tokens == "RegisterRank":
				self.wndCombatZone.RegisterRanking()
			elif tokens == "StartFlashing":
				if self.interface:
					self.interface.wndMiniMap.btnCombatZone.FlashEx()		
			elif tokens == "RefreshShop":
				if self.interface:
					self.interface.dlgShop.SetCombatZonePoints(arg1)
					self.interface.dlgShop.SetLimitCombatZonePoints(arg2, arg3)
					
	def __EnableTestServerFlag(self):
		app.EnableTestServerFlag()

	def __InGameShop_Show(self, url):
		if constInfo.IN_GAME_SHOP_ENABLE:
			self.interface.OpenWebWindow(url)

	def ManagerItemshop(self, cmd):
		cmd = cmd.split('#')
		if cmd[0] == 'QID':
			constInfo.ItemShop['QID'] = int(cmd[1])
		elif cmd[0] == 'INPUT':
			constInfo.INPUT_IGNORE = int(cmd[1])
		elif cmd[0] == 'SEND':
			net.SendQuestInputStringPacket(str(constInfo.ItemShop['QCMD']))
			constInfo.ItemShop['QCMD'] = ''
		elif cmd[0] == 'CREATE_CATEGORY':
			constInfo.ItemShop['ITEMS'][cmd[1]][int(cmd[2])] = []
		elif cmd[0] == 'SET_ITEM':
			constInfo.ItemShop['ITEMS'][cmd[1]][int(cmd[2])].append([int(cmd[3]), int(cmd[4]), int(cmd[5]), [(int(cmd[6]), int(cmd[7])), (int(cmd[8]), int(cmd[9])), (int(cmd[10]), int(cmd[11])), (int(cmd[12]), int(cmd[13])), (int(cmd[14]), int(cmd[15])), (int(cmd[16]), int(cmd[17])), (int(cmd[18]), int(cmd[19]))], [int(cmd[20]), int(cmd[21]), int(cmd[22])], int(cmd[23]), int(cmd[24]), int(cmd[25])])
		elif cmd[0] == 'CLEAR_CONTENT':
			constInfo.ItemShop['ITEMS']['mostBought'] = []
			constInfo.ItemShop['ITEMS']['hotOffers'] = []
		elif cmd[0] == 'SET_ITEM_MOSTBOUGHT':
			constInfo.ItemShop['ITEMS']['mostBought'].append([int(cmd[1]), int(cmd[2]), int(cmd[3]), [(int(cmd[4]), int(cmd[5])), (int(cmd[6]), int(cmd[7])), (int(cmd[8]), int(cmd[9])), (int(cmd[10]), int(cmd[11])), (int(cmd[12]), int(cmd[13])), (int(cmd[14]), int(cmd[15])), (int(cmd[16]), int(cmd[17]))], [int(cmd[17]), int(cmd[19]), int(cmd[20])], int(cmd[21]), int(cmd[22]), int(cmd[23])])
		elif cmd[0] == 'SET_ITEM_HOTOFFERS':
			constInfo.ItemShop['ITEMS']['hotOffers'].append([int(cmd[1]), int(cmd[2]), int(cmd[3]), [(int(cmd[4]), int(cmd[5])), (int(cmd[6]), int(cmd[7])), (int(cmd[8]), int(cmd[9])), (int(cmd[10]), int(cmd[11])), (int(cmd[12]), int(cmd[13])), (int(cmd[14]), int(cmd[15])), (int(cmd[16]), int(cmd[17]))], [int(cmd[17]), int(cmd[19]), int(cmd[20])], int(cmd[21]), int(cmd[22]), int(cmd[23])])
		elif cmd[0] == 'SET_LOG':
			constInfo.ItemShop['LOGS'].append([int(cmd[1]), int(cmd[2]), int(cmd[3]), cmd[4], [(int(cmd[5]), int(cmd[6])), (int(cmd[7]), int(cmd[8])), (int(cmd[9]), int(cmd[10])), (int(cmd[11]), int(cmd[12])), (int(cmd[13]), int(cmd[14])), (int(cmd[15]), int(cmd[16])), (int(cmd[17]), int(cmd[18]))], [int(cmd[19]), int(cmd[20]), int(cmd[21])]])
		elif cmd[0] == 'SEND_COINS':
			constInfo.COINS_DRS = [int(cmd[1]), int(cmd[2])]
		elif cmd[0] == 'SEND_3RD_SHOP_COIN':
			self.interface.wndItemShop.Set3rdCoins(int(cmd[1]))
		elif cmd[0] == 'ALLOW_SPIN_WHEEL':
			self.interface.wndItemShop.SpinWheel()
		elif cmd[0] == 'CLEAR_WHEEL_CONTENT':
			constInfo.ItemShop['WOD'] = [[], []]
		elif cmd[0] == 'SET_WHEEL_PRIZE':
			prize = cmd[2].split(',')
			if cmd[1] == 'G':
				for i in xrange(len(prize)-1):
					constInfo.ItemShop['WOD'][1].append(int(prize[i]))
			elif cmd[1] == 'B':
				for i in xrange(len(prize)-1):
					constInfo.ItemShop['WOD'][0].append(int(prize[i]))
		elif cmd[0] == 'OPEN':
			self.interface.wndItemShop.Open(int(cmd[1]))
		elif cmd[0] == 'REFRESH_CONTENT':
			self.interface.wndItemShop.RefreshWindow()
			
	def __LoginLover(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLoginLover()

	def __LogoutLover(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLogoutLover()
		if self.affectShower:
			self.affectShower.HideLoverState()

	def __LoverNear(self):
		if self.affectShower:
			self.affectShower.ShowLoverState()

	if app.ENABLE_LOCALIZATION_SYSTEM:
		def BINARY_Localization_Append(self, register_callback, idx1, idx2, idx3, idx4, idx5, idx6, idx7, idx8, idx9, idx10, idx11, idx12, idx13, idx14):
			self.wndPlayerLocalization.Append([int(register_callback), int(idx1), int(idx2), int(idx3), int(idx4), int(idx5), int(idx6), int(idx7), int(idx8), int(idx9), int(idx10), int(idx11), int(idx12), int(idx13), int(idx14)])

	if app.ENABLE_MANAGER_BANK_SYSTEM:
		def BINARY_Account_Bank_Logs(self):
			self.managerAccountBank.BINARY_Account_Bank_Logs()

	def __LoverFar(self):
		if self.affectShower:
			self.affectShower.HideLoverState()

	def __LoverDivorce(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.ClearLoverInfo()
		if self.affectShower:
			self.affectShower.ClearLoverState()

	if app.ENABLE_ACCE_SYSTEM:
		def ActAcce(self, iAct, bWindow):
			if self.interface:
				self.interface.ActAcce(iAct, bWindow)

		def AlertAcce(self, bWindow):
			snd.PlaySound("sound/ui/make_soket.wav")
			if bWindow:
				self.PopupMessage(localeInfo.ACCE_DEL_SERVEITEM)
			else:
				self.PopupMessage(localeInfo.ACCE_DEL_ABSORDITEM)

	if app.ENABLE_SHOW_CHEST_DROP:
		def BINARY_AddChestDropInfo(self, chestVnum, pageIndex, slotIndex, itemVnum, itemCount):
			if self.interface:
				self.interface.AddChestDropInfo(chestVnum, pageIndex, slotIndex, itemVnum, itemCount)
						
		def BINARY_RefreshChestDropInfo(self, chestVnum):
			if self.interface:
				self.interface.RefreshChestDropInfo(chestVnum)

	def __switch_channel(self):
		import uichannel
		a = uichannel.ChannelChanger()
		a.Show()

	def	OpenMarbleShop(self):
		if self.wndMarbleShop.IsShow():
			self.wndMarbleShop.Hide()
		else:
			self.wndMarbleShop.Show()
																