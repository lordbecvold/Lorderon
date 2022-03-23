#Lorderon Client Dev by Lordbecvold
import app
import ui
import grp
import net
import guild
import messenger
import localeInfo
import constInfo
import uiToolTip
import uiGameOption
import chat
import uiCommon
import wndMgr
import ime
import uiGuild
import player
import time
import playerSettingModule
from _weakref import proxy

PROFILE_DICT = {}
PROFILE_STATE_LOAD = 1
PROFILE_STATE_EDIT_STATUS = 2
PROFILE_STATE_EDIT_LOCATION = 3
PROFILE_STATE_EDIT_BIRTHDAY_YEAR = 4
PROFILE_STATE_EDIT_BIRTHDAY_MONTH = 5
PROFILE_STATE_EDIT_BIRTHDAY_DAY = 6

DICTIONARY = {
	'EMOTICONS_NAME_LIST' : [
		"blushing", "crying", "devil", "angel", "smiley", "frowny", "gasp", "grinning", "kiss", "shark", "shocked", "glasses", "squint", "sunglasses", "tongue_out", "unsure", "upset", "winking", "heart"
	],
	'EMOTICONS_KEY_LIST' : [
		"^_^", ":'(", "3:)", "O:)", ":)", ":(", ":O", ":D", ":*", "(^^^)", "o.O", "8-)", "-_-", "8|", ":P", ":/", ">:O", ";)", "<3"
	],
	'BIRTHDAY_LIST' : [
		[1970, 2005],
		[1, 12],
		[1, 31]
	],
	'FACE_IMAGE_LIST' : {
		playerSettingModule.RACE_WARRIOR_M	: "icon/face/warrior_m.tga",
		playerSettingModule.RACE_WARRIOR_W	: "icon/face/warrior_w.tga",
		playerSettingModule.RACE_ASSASSIN_M	: "icon/face/assassin_m.tga",
		playerSettingModule.RACE_ASSASSIN_W	: "icon/face/assassin_w.tga",
		playerSettingModule.RACE_SURA_M		: "icon/face/sura_m.tga",
		playerSettingModule.RACE_SURA_W		: "icon/face/sura_w.tga",
		playerSettingModule.RACE_SHAMAN_M	: "icon/face/shaman_m.tga",
		playerSettingModule.RACE_SHAMAN_W	: "icon/face/shaman_w.tga",
	},
	'EMPIRE_IMAGE_LIST' : {
		net.EMPIRE_A : "d:/ymir work/ui/empire/empire_a_256.dds",
		net.EMPIRE_B : "d:/ymir work/ui/empire/empire_b_256.dds",
		net.EMPIRE_C : "d:/ymir work/ui/empire/empire_c_256.dds"
	},
	'LANGUAGE_IMAGE_STRING' : "d:/ymir work/ui/flag/%s.tga"
}

def swapcaseDictionary(dictionary, members):
	for i in xrange(len(dictionary)):
		if members == dictionary[i]:
			return FALSE
	return TRUE
	
def GetWhisperSendedTime():
	localtime = localtime = time.strftime("[%H:%M:%S]")
	return localtime

class Item(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad = 0
		self.text = fileName
		self.textLine = self.__CreateTextLine(fileName[:35])

	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)

	def GetText(self):
		return self.text

	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 6 * len(self.textLine.GetText()) + 4, height)

	def __CreateTextLine(self, fileName):
		textLine = ui.TextLine()
		textLine.SetParent(self)
		if localeInfo.IsARABIC():
			textLine.SetPosition(6 * len(fileName) + 6, 0)
		else:
			textLine.SetPosition(0, 0)
		textLine.SetText(fileName)
		textLine.Show()
		return textLine

class FileListDialog(ui.ScriptWindow):
	def __init__(self, wndProfileBoard):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = 0
		self.state = -1	
		if not wndProfileBoard:
			import exception
			exception.Abort("wndProfileBoard parameter must be set to FileListDialog")
			return
		self.wndProfileBoard = wndProfileBoard
		self.listBox = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		if self.isLoaded == 0:
			self.isLoaded = 1
			self.__Load()
		ui.ScriptWindow.Show(self)

	def Open(self):
		self.Show()
		self.SetTop()

	def Close(self):
		self.Hide()
		self.wndProfileBoard.ShowProfile()
		
	def GetState(self):
		return self.state
		
	def SetState(self, key):
		self.state = key

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def __CreateFileListBox(self, parent):
		listBox = ui.ListBoxEx()
		if localeInfo.IsARABIC():
			listBox.SetPosition(self.GetWidth() - listBox.GetWidth() - 10, 50)
		else:
			listBox.SetPosition(5, 0)
		listBox.SetParent(parent)
		listBox.Show()
		return listBox

	def __Load(self):
		self.__Load_LoadScript("uiscript/birthdatemistwindow.py")
		self.__Load_BindObject()
		self.UpdateRect()

	def __Load_LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("BirthDateListWindow.__Load")

	def __Load_BindObject(self):
		try:
			self.listBox = self.__CreateFileListBox(self.GetChild("board"))
			self.listBox.SetScrollBar(self.GetChild("ScrollBar"))
			self.listBox.SetSelectEvent(self.OnClick)	
			self.board = self.GetChild("board")
			self.scrollBar = self.GetChild("ScrollBar")
		except:
			import exception
			exception.Abort("BirthDateListWindow.__Bind")
		
	def OnClick(self, key):
		selectedItem = self.listBox.GetSelectedItem()
		if selectedItem:
			self.ReferenceTimeEvent()
			
	def LargeBoardType(self, flag):
		if flag:
			self.board.SetSize(175, self.board.GetHeight())
			self.scrollBar.SetPosition(160, 3)
		else:
			self.board.SetSize(60, self.board.GetHeight())
			self.scrollBar.SetPosition(45, 3)
		self.UpdateRect()

	def ReferenceTimeEvent(self):
		self.selectedItemWnd = WaitingDialog()
		self.selectedItemWnd.Open(0.2)
		self.selectedItemWnd.SAFE_SetTimeOverEvent(self.Close)
			
	def MovePosition(self, x, y):
		self.SetPosition(x, y)
		self.UpdateRect()

	def ClearFileList(self):
		self.listBox.RemoveAllItems()

	def AppendFile(self, fileName):
		self.listBox.AppendItem(Item(fileName))

class SelectKey(ui.ExpandedImageBox):
	def __init__(self, object, parent, x, y, event):
		ui.ExpandedImageBox.__init__(self)
		self.SetParent(parent)
		self.SetPosition(x, y)
		self.LoadImage(["d:/ymir work/ui/public/Parameter_Slot_01.sub", "d:/ymir work/ui/public/Parameter_Slot_06.sub"][object == PROFILE_STATE_EDIT_LOCATION])	
		if object == PROFILE_STATE_EDIT_LOCATION:
			self.SetScale(0.8, 1.0)
		self.mouse = uiGuild.MouseReflector(self)
		self.mouse.SetSize(self.GetWidth(), self.GetHeight())
		self.Enable = TRUE
		self.event = event
		self.state = 0
		self.Show()
		self.mouse.UpdateRect()

	def __del__(self):
		ui.ExpandedImageBox.__del__(self)
			
	def SetState(self, key):
		self.state = key
		
	def GetState(self):
		return self.state

	def OnMouseOverIn(self):
		self.mouse.Show()

	def OnMouseOverOut(self):
		self.mouse.Hide()

	def OnMouseLeftButtonDown(self):
		self.mouse.Down()

	def OnMouseLeftButtonUp(self):
		self.mouse.Up()
		self.event()

class SettingsProfileWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.wndObjects = {}
		self.textLine = {}
		self.STATE_LIST = [PROFILE_STATE_EDIT_BIRTHDAY_YEAR, PROFILE_STATE_EDIT_BIRTHDAY_MONTH, PROFILE_STATE_EDIT_BIRTHDAY_DAY, PROFILE_STATE_EDIT_LOCATION]
		self.listBox = FileListDialog(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def __LoadWindow(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/settingsprofilewindow.py")
		try:
			GetObject = self.GetChild
			self.board = GetObject("board")
			self.CharacterName =  GetObject("CharacterName")
			self.CharacterStatus = GetObject("CharacterStatus")
			self.CharacterIcon = GetObject("CharacterIcon")
		except:
			import exception
			exception.Abort("SettingsProfileWindow.__LoadWindow")
		for object in xrange(len(self.STATE_LIST)):
			if object == PROFILE_STATE_EDIT_LOCATION:
				self.wndObjects.update({object : [SelectKey(object, self, 55, 92, lambda arg = object: self.OnSelect(arg)), self.SetText(object)]})
			else:
				self.wndObjects.update({object : [SelectKey(object, self, 65 + (object * 60), 117, lambda arg = object: self.OnSelect(arg)), self.SetText(object)]})
		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		
	def SetText(self, state):
		self.textLine[state] = ui.TextLine()
		self.textLine[state].SetParent(self)	
		if state == PROFILE_STATE_EDIT_LOCATION:
			self.textLine[state].SetPosition(59, 93)
		else:
			self.textLine[state].SetPosition(75 + (state * 60), 119)
		self.textLine[state].Show()
		return self.textLine[state]
		
	def OnSelect(self, state):
		x, y = self.GetGlobalPosition()
		self.listBox.Open()
		self.listBox.SetState(self.STATE_LIST[state])
		if state == PROFILE_STATE_EDIT_LOCATION:
			self.listBox.LargeBoardType(True)
			self.listBox.MovePosition((x + 55), y + 92 + 20)
		else:
			self.listBox.LargeBoardType(False)
			self.listBox.MovePosition((x + 60) + (state * 60), y + 139)
		self.listBox.ClearFileList()
		self.listBox.AppendFile(localeInfo.PROFILE_SELECT_DEFAULT)			
		if state == PROFILE_STATE_EDIT_LOCATION:
			for c_pData in GetCountryList():
				self.listBox.AppendFile(c_pData['name'])
		else:
			for i in xrange(DICTIONARY['BIRTHDAY_LIST'][state][0], DICTIONARY['BIRTHDAY_LIST'][state][1] + 1):
				self.listBox.AppendFile(str(i))

	def ShowProfile(self):
		self.CharacterName.SetText(localeInfo.PROFILE_MAIN_NAME % player.GetMainCharacterName())
		self.CharacterStatus.SetText(PROFILE_DICT["status"])
		job = PROFILE_DICT["job"]
		if job in DICTIONARY['FACE_IMAGE_LIST']:
			self.CharacterIcon.LoadImage(DICTIONARY['FACE_IMAGE_LIST'][job])
		for k, v in enumerate([PROFILE_DICT["year"], PROFILE_DICT["month"], PROFILE_DICT["day"], PROFILE_DICT["location"]]):
			self.textLine[k].SetText(v)
		
	def Open(self):
		self.Show()
		self.SetCenterPosition()
		self.SetTop()
		self.ShowProfile()

	def Close(self):
		self.Hide()
		if self.listBox:
			self.listBox.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
		
class WaitingDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadDialog()
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "uiscript/warteschleife.py")
		except:
			import exception
			exception.Abort("WaitingDialog.LoadDialog.BindObject")

	def Open(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime

		self.Show()		

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)
		
	def OnUpdate(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			return
		
	def OnPressExitKey(self):
		self.Close()
		return TRUE
		
class EmoticonDialog(ui.ExpandedImageBox):
	def __init__(self, parent, x, y, event, emoticon):
		ui.ExpandedImageBox.__init__(self)
		self.SetParent(parent)
		self.SetPosition(x, y)
		self.LoadImage("d:/ymir work/ui/game/emoticons/%s.tga" % DICTIONARY['EMOTICONS_NAME_LIST'][emoticon])
		self.SetScale(0.1, 0.1)
		self.mouse = uiGuild.MouseReflector(self)
		self.mouse.SetSize(self.GetWidth(), self.GetHeight())
		image = ui.MakeImageBox(self, "d:/ymir work/ui/public/check_image.sub", 0, 0)
		image.AddFlag("not_pick")
		image.SetWindowHorizontalAlignCenter()
		image.SetWindowVerticalAlignCenter()
		image.Hide()
		self.Enable = TRUE
		self.image = image
		self.event = event
		self.Show()
		self.mouse.UpdateRect()

	def __del__(self):
		ui.ExpandedImageBox.__del__(self)

	def SetCheck(self, flag):
		if flag:
			self.image.Show()
		else:
			self.image.Hide()

	def Disable(self):
		self.Enable = FALSE

	def OnMouseOverIn(self):
		if not self.Enable:
			return
		self.mouse.Show()

	def OnMouseOverOut(self):
		if not self.Enable:
			return
		self.mouse.Hide()

	def OnMouseLeftButtonDown(self):
		if not self.Enable:
			return
		self.mouse.Down()

	def OnMouseLeftButtonUp(self):
		if not self.Enable:
			return
		self.mouse.Up()
		self.event()
		
def GetCountryList():
	return [{'code': 'CZ', 'name': 'Czech Republic'},]
	