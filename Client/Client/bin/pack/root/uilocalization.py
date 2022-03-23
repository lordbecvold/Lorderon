#Lorderon Client Dev by Lordbecvold
import ui
import wndMgr
import os as _server
import player as p
import net as server
import uiCommon as message
import localeInfo as translate
import dbg
import snd
import mouseModule
import chr

Y_PASS_ELEMENTS = 65

GET_LOCALIZATION_IMG = {
	0	: "d:/ymir work/ui/public/parameter_slot_06.sub",
	1	: "d:/ymir work/ui/game/localization_btn/btn_edit_01.tga",
	2	: "d:/ymir work/ui/game/localization_btn/btn_edit_02.tga",
	3	: "d:/ymir work/ui/game/localization_btn/btn_edit_03.tga",
	4	: "d:/ymir work/ui/public/Large_Button_01.sub",
	5	: "d:/ymir work/ui/public/Large_Button_02.sub",
	6	: "d:/ymir work/ui/public/Large_Button_03.sub"
}

class Initializate(ui.ScriptWindow):
	def __init__(self):	
		ui.ScriptWindow.__init__(self)
		self.LoadWindowLocalization()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def EditLocalizationBtn(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		btn = ui.Button()
		if parent != None:
			btn.SetParent(parent)
		btn.SetPosition(x, y)
		btn.SetUpVisual(UpVisual)
		btn.SetOverVisual(OverVisual)
		btn.SetDownVisual(DownVisual)
		btn.SetText(buttonName)
		btn.SetToolTipText(tooltipText)
		btn.Show()
		btn.SetEvent(func)
		return btn

	def LoadWindowLocalization(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/script_localization.py")
		getObject = self.GetChild
		self.Board = getObject("board")
		self.Board.SetSize(450, 60 + (7 * 40))
		self.Board.SetTitleName(translate.LOCALIZATION_TITLE)
		self.Board.SetCloseEvent(self.Close)
		self.btnEdit = {}
		idx = 1
		posY = 1 + Y_PASS_ELEMENTS
		while idx <= 7:
			self.btnEdit[idx] = self.EditLocalizationBtn(self.Board, "", translate.LOCALIZATION_DESC_BTN_EDIT, 233, posY-3, (lambda arg1 = "%d" % (idx-1), boolSave = "%d" % (999): self.RenameLocation(int(arg1), int(boolSave))), GET_LOCALIZATION_IMG[1], GET_LOCALIZATION_IMG[2], GET_LOCALIZATION_IMG[3])
			idx = idx + 1
			posY = posY + 40
		self.tmpBtn = []
		self.tmpFieldLocation = []
		self.tmpFieldPosition = []
		for tmp in xrange(0, 7):
			btn = ui.Button()
			btn.SetParent(self.Board)
			btn.SetPosition(10, Y_PASS_ELEMENTS + (tmp * 40))
			btn.SetUpVisual(GET_LOCALIZATION_IMG[0])
			btn.SetOverVisual(GET_LOCALIZATION_IMG[0])
			btn.SetDownVisual(GET_LOCALIZATION_IMG[0])
			btn.Show()
			textLine_Location = ui.EditLine()
			textLine_Location.SetParent(btn)
			textLine_Location.SetPosition(1, 1)
			textLine_Location.SetText("")
			textLine_Location.Disable()
			textLine_Location.Show()
			textLine_Position = ui.EditLine()
			textLine_Position.SetParent(btn)
			textLine_Position.SetPosition(166, 1)
			textLine_Position.SetText("(x, y)")
			textLine_Position.Disable()
			textLine_Position.Show()
			self.tmpBtn.append(btn)
			self.tmpFieldLocation.append(textLine_Location)
			self.tmpFieldPosition.append(textLine_Position)
			btn = ui.Button()
			btn.SetParent(self.Board)
			btn.SetPosition(263, Y_PASS_ELEMENTS + (tmp * 40))
			btn.SetUpVisual(GET_LOCALIZATION_IMG[4])
			btn.SetOverVisual(GET_LOCALIZATION_IMG[5])
			btn.SetDownVisual(GET_LOCALIZATION_IMG[6])
			btn.SetEvent(lambda ch = "/localization teleport %d" % (tmp): server.SendChatPacket(ch))
			btn.SetText(translate.LOCALIZATION_TELEPORT)
			btn.Show()
			self.tmpBtn.append(btn)
			btn = ui.Button()
			btn.SetParent(self.Board)
			btn.SetPosition(353, Y_PASS_ELEMENTS + (tmp*40))
			btn.SetUpVisual(GET_LOCALIZATION_IMG[4])
			btn.SetOverVisual(GET_LOCALIZATION_IMG[5])
			btn.SetDownVisual(GET_LOCALIZATION_IMG[6])
			btn.SetEvent(lambda arg = "%d" % (tmp), boolSave = "%d" % (tmp): self.RenameLocation(int(arg), int(boolSave)))
			btn.SetText(translate.LOCALIZATION_SAVE)
			btn.Show()
			self.tmpBtn.append(btn)

	def Close(self):
		self.Hide()
		for rmf in xrange(1, 8):
			self.btnEdit[rmf].Hide()

	def Show(self):
		wndMgr.Show(self.hWnd)
		self.Board.Show()

	def Destroy(self):
		self.Hide()
		self.tmpFieldLocation = []
		self.tmpFieldPosition = []
		self.tmpBtn = []

	def OnPressEscapeKey(self):
		self.Close()

	def Append(self, arg):
		myPathFile = "lib//localization//save_localization__%s.txt" % str(p.GetName())
		myPathCreate = "lib//localization"
		if not _server.path.exists("lib"):
			_server.mkdir("lib")
		if not _server.path.exists(myPathCreate):
			_server.mkdir(myPathCreate)
		if not _server.path.exists(myPathFile):
			tmpCreateFile = open(myPathFile, 'w')
			tmpCreateFile.write('-\n-\n-\n-\n-\n-\n-\n')
			tmpCreateFile.close()
		for idx in xrange(0, 7):
			lines = open(myPathFile, "r").readlines()
			result = lines[idx]
			self.tmpFieldLocation[idx].SetText(result)	
		self.tmpFieldPosition[0].SetText("(%s, %s)" % (str(arg[1]), str(arg[2])))
		self.tmpFieldPosition[1].SetText("(%s, %s)" % (str(arg[3]), str(arg[4])))
		self.tmpFieldPosition[2].SetText("(%s, %s)" % (str(arg[5]), str(arg[6])))
		self.tmpFieldPosition[3].SetText("(%s, %s)" % (str(arg[7]), str(arg[8])))
		self.tmpFieldPosition[4].SetText("(%s, %s)" % (str(arg[9]), str(arg[10])))
		self.tmpFieldPosition[5].SetText("(%s, %s)" % (str(arg[11]), str(arg[12])))
		self.tmpFieldPosition[6].SetText("(%s, %s)" % (str(arg[13]), str(arg[14])))
		for i in xrange(1, 8):
			self.btnEdit[i].Show()
		if int(arg[0]) < 1:
			wndMgr.Show(self.hWnd)
			self.Board.Show()

	def CloseDialog(self):
		self.inputDialog.Hide()

	def RenameLocation(self, tmpIndex, boolSave):
		myPathFile = "lib//localization//save_localization__%s.txt" % str(p.GetName())
		for mex in range(tmpIndex + 1):
			lines = open(myPathFile, "r").readlines()
			result = lines[mex]
		self.inputDialog = message.EditLineLocalization()
		self.inputDialog.SetMaxLength(35)
		if int(boolSave) == 999:
			self.inputDialog.SetAcceptEvent(lambda arg = "%d" % (tmpIndex), boolSave = "%d" % (tmpIndex): self.Get(int(arg), int(999)))
		else:
			self.inputDialog.SetAcceptEvent(lambda arg = "%d" % (tmpIndex), boolSave = "%d" % (tmpIndex): self.Get(int(arg), int(boolSave)))
		self.inputDialog.SetCancelEvent(ui.__mem_func__(self.CloseDialog))
		self.inputDialog.SetAcceptText(translate.LOCALIZATION_EDIT)
		self.inputDialog.SetCancelText(translate.LOCALIZATION_CANCEL)
		self.inputDialog.SetTitle(translate.LOCALIZATION_CHANGE_NAME)
		self.inputDialog.SetDescription(translate.LOCALIZATION_CURRENT_LINE + " " + str(result))
		self.inputDialog.Open()

	def Get(self, tmpIndex, boolSave):
		myPathFile = "lib//localization//save_localization__%s.txt" % str(p.GetName())
		textLine = self.inputDialog.GetText()
		saveLocationArray = []
		if _server.path.exists(myPathFile):
			tmpFile = open(myPathFile, "r")
			for mLine in tmpFile:
				saveLocationArray.append(mLine)
			tmpFile.close()
		while len(saveLocationArray) < int(tmpIndex+1):
			saveLocationArray.append("")
		saveLocationArray[int(tmpIndex + 1)-1] = str(textLine)
		tmpFile = open(myPathFile, "w")
		for mLine in saveLocationArray:
			tmpFile.write(mLine)
			if (len(mLine) > 0 and mLine[-1:] != "\n") or len(mLine) == 0:
				tmpFile.write("\n")
		tmpFile.close()
		if int(boolSave) != 999:
			server.SendChatPacket("/localization save %d" % (int(boolSave)))
			server.SendChatPacket("/localization refresh")
		self.CloseDialog()
		self.RefreshCurrentLine()

	def RefreshCurrentLine(self):
		myPathFile = "lib//localization//save_localization__%s.txt" % str(p.GetName())

		for ret in xrange(0, 7):
			lines = open(myPathFile, "r").readlines()
			result = lines[ret]
			