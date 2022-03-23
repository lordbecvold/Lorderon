#Lorderon Client Dev by Lordbecvold
import ui
import net
import chat
import player
import app
import localeInfo
import ime
import chr

if app.ENABLE_RENEW_MESSENGER_WHISPER:
	import uiContact

class WhisperButton(ui.Button):
	def __init__(self):
		ui.Button.__init__(self, "TOP_MOST")

	def __del__(self):
		ui.Button.__del__(self)

	def SetToolTipText(self, text, x=0, y = 32):
		ui.Button.SetToolTipText(self, text, x, y)
		self.ToolTipText.Show()

	def SetToolTipTextWithColor(self, text, color, x=0, y = 32):
		ui.Button.SetToolTipText(self, text, x, y)
		self.ToolTipText.SetPackedFontColor(color)
		self.ToolTipText.Show()

	def ShowToolTip(self):
		if 0 != self.ToolTipText:
			self.ToolTipText.Show()

	def HideToolTip(self):
		if 0 != self.ToolTipText:
			self.ToolTipText.Show()

class WhisperDialog(ui.ScriptWindow):

	class TextRenderer(ui.Window):
		def SetTargetName(self, targetName):
			self.targetName = targetName

		def OnRender(self):
			(x, y) = self.GetGlobalPosition()
			chat.RenderWhisper(self.targetName, x, y)

	class ResizeButton(ui.DragButton):

		def __init__(self):
			ui.DragButton.__init__(self)

		def __del__(self):
			ui.DragButton.__del__(self)

		def OnMouseOverIn(self):
			app.SetCursor(app.HVSIZE)

		def OnMouseOverOut(self):
			app.SetCursor(app.NORMAL)

	def __init__(self, eventMinimize, eventClose):
		print "NEW WHISPER DIALOG  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		self.targetName = ""
		self.eventMinimize = eventMinimize
		self.eventClose = eventClose
		self.eventAcceptTarget = None
		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.InitializeProfileData()
		
	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE WHISPER DIALOG"
		ui.ScriptWindow.__del__(self)		

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			if app.ENABLE_RENEW_MESSENGER_WHISPER:
				pyScrLoader.LoadScriptFile(self, "UIScript/NewWhisperDialog.py")
			else:
				pyScrLoader.LoadScriptFile(self, "UIScript/WhisperDialog.py")			
		except:
			import exception
			exception.Abort("WhisperDialog.LoadDialog.LoadScript")
		try:
			GetObject = self.GetChild
			self.scrollBar = GetObject("scrollbar")
			self.titleNameEdit = GetObject("titlename_edit")
			if not app.ENABLE_RENEW_MESSENGER_WHISPER:
				self.titleName = GetObject("titlename")
				self.ignoreButton = GetObject("ignorebutton")
				self.reportViolentWhisperButton = GetObject("reportviolentwhisperbutton")
				self.closeButton = GetObject("closebutton")
			if app.ENABLE_RENEW_MESSENGER_WHISPER:
				self.titleNameEditBar = GetObject("titlename_editBar")
			self.chatLine = GetObject("chatline")
			self.minimizeButton = GetObject("minimizebutton")
			self.sendButton = GetObject("sendbutton")
			self.board = GetObject("board")
			self.editBar = GetObject("editbar")
			self.gamemasterMark = GetObject("gamemastermark")
			self.acceptButton = GetObject("acceptbutton")
			if app.ENABLE_RENEW_MESSENGER_WHISPER:
				self.Whisper_Profile_Photo_Icon = GetObject("Whisper_Profile_Photo_Icon")
				self.Whisper_Profile_Empire_Icon = GetObject("Whisper_Profile_Empire_Icon")
				self.Whisper_Profile_Language_Icon = GetObject("Whisper_Profile_Language_Icon")
				self.Whisper_Profile_Name_Value = GetObject("Whisper_Profile_Name_Value")
				self.Whisper_Profile_Level_Value = GetObject("Whisper_Profile_Level_Value")
				self.Whisper_Profile_Status_Value = GetObject("Whisper_Profile_Status_Value")
				self.Whisper_Profile_Guild_Value = GetObject("Whisper_Profile_Guild_Value")
				self.Whisper_Profile_Birthday_Value = GetObject("Whisper_Profile_Birthday_Value")
				self.Whisper_Profile_Location_Value = GetObject("Whisper_Profile_Location_Value")			
		except:
			import exception
			exception.Abort("DialogWindow.LoadDialog.BindObject")
		self.titleNameEdit.SetText("")
		self.gamemasterMark.Hide()
		self.minimizeButton.SetEvent(ui.__mem_func__(self.Minimize))
		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		self.scrollBar.SetPos(1.0)
		self.scrollBar.SetScrollEvent(ui.__mem_func__(self.OnScroll))
		self.chatLine.SetReturnEvent(ui.__mem_func__(self.SendWhisper))
		self.chatLine.SetEscapeEvent(ui.__mem_func__(self.Minimize))
		self.chatLine.SetMultiLine()
		self.chatLine.OnIMEKeyDown = ui.__mem_func__(self.OnIMEKeyDown)
		self.sendButton.SetEvent(ui.__mem_func__(self.SendWhisper))
		self.titleNameEdit.SetReturnEvent(ui.__mem_func__(self.AcceptTarget))
		self.titleNameEdit.SetEscapeEvent(ui.__mem_func__(self.Close))
		self.acceptButton.SetEvent(ui.__mem_func__(self.AcceptTarget))
		self.textRenderer = self.TextRenderer()
		self.textRenderer.SetParent(self)
		self.textRenderer.SetPosition(20, 28)
		self.textRenderer.SetTargetName("")
		self.textRenderer.Show()
		if not app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.titleName.SetText("")
			self.closeButton.SetEvent(ui.__mem_func__(self.Close))
			self.ignoreButton.SetToggleDownEvent(ui.__mem_func__(self.IgnoreTarget))
			self.ignoreButton.SetToggleUpEvent(ui.__mem_func__(self.IgnoreTarget))
			self.reportViolentWhisperButton.SetEvent(ui.__mem_func__(self.ReportViolentWhisper))
			self.resizeButton = self.ResizeButton()
			self.resizeButton.SetParent(self)
			self.resizeButton.SetSize(20, 20)
			self.resizeButton.SetPosition(280, 180)
			self.resizeButton.SetMoveEvent(ui.__mem_func__(self.ResizeWhisperDialog))
			self.resizeButton.Show()
			self.ResizeWhisperDialog()
		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.SetWhisperDialogSize(410, 280)
			self.emoticonsDict = {}
			for objectEmoticons in xrange(len(uiContact.DICTIONARY['EMOTICONS_NAME_LIST'])):
				self.emoticonsDict.update({objectEmoticons : [uiContact.EmoticonDialog(self.board, 10 + (objectEmoticons * 20), 205, lambda argument = objectEmoticons: self.OnSelectEmoticon(argument), objectEmoticons)]})

	def Destroy(self):
		self.eventMinimize = None
		self.eventClose = None
		self.eventAcceptTarget = None
		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.InitializeProfileData()
		self.ClearDictionary()
		self.scrollBar.Destroy()
		self.titleNameEdit = None
		self.titleNameEditBar = None
		self.acceptButton = None
		self.scrollBar = None
		self.chatLine = None
		self.sendButton = None
		self.minimizeButton = None
		self.textRenderer = None
		self.board = None
		self.editBar = None
		if not app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.ignoreButton = None
			self.reportViolentWhisperButton = None
			self.acceptButton = None
			self.resizeButton = None
			self.closeButton = None
			self.titleName = None

	if not app.ENABLE_RENEW_MESSENGER_WHISPER:
		def ResizeWhisperDialog(self):
			(xPos, yPos) = self.resizeButton.GetLocalPosition()
			if xPos < 280:
				self.resizeButton.SetPosition(280, yPos)
				return
			if yPos < 150:
				self.resizeButton.SetPosition(xPos, 150)
				return
			self.SetWhisperDialogSize(xPos + 20, yPos + 20)

	def SetWhisperDialogSize(self, width, height):
		try:
			max = int((width - 90) / 6) * 3 - 6
			self.board.SetSize(width, height)
			self.scrollBar.SetPosition(width - 25, 35)
			self.scrollBar.SetScrollBarSize(height - 100)
			self.scrollBar.SetPos(1.0)
			self.editBar.SetSize(width - 18, 50)
			self.chatLine.SetSize(width - 90, 40)
			self.chatLine.SetLimitWidth(width-90)
			self.SetSize(width, height)
			if 0 != self.targetName:
				chat.SetWhisperBoxSize(self.targetName, width - 50, height - 90)			
			if localeInfo.IsARABIC():
				self.textRenderer.SetPosition(width - 20, 28)
				self.scrollBar.SetPosition(width - 25 + self.scrollBar.GetWidth(), 35)
				self.editBar.SetPosition(10 + self.editBar.GetWidth(), height - 60)
				self.sendButton.SetPosition(width - 80 + self.sendButton.GetWidth(), 10)
				self.minimizeButton.SetPosition(width - 42 + self.minimizeButton.GetWidth(), 12)	
				if not app.ENABLE_RENEW_MESSENGER_WHISPER:
					self.closeButton.SetPosition(width - 24 + self.closeButton.GetWidth(), 12)
				self.chatLine.SetPosition(5 + self.chatLine.GetWidth(), 5)
				self.board.SetPosition(self.board.GetWidth(), 0)
			else:
				self.textRenderer.SetPosition(20, 28)
				self.scrollBar.SetPosition(width - 25, 35)
				self.editBar.SetPosition(10, height - 60)
				self.sendButton.SetPosition(width - 80, 10)
				if app.ENABLE_RENEW_MESSENGER_WHISPER:
					self.minimizeButton.SetPosition(width - 44, 10)
				else:
					self.minimizeButton.SetPosition(width - 42, 12)
				if not app.ENABLE_RENEW_MESSENGER_WHISPER:
					self.closeButton.SetPosition(width - 24, 12)
			self.SetChatLineMax(max)
		except:
			import exception
			exception.Abort("WhisperDialog.SetWhisperDialogSize.BindObject")

	def SetChatLineMax(self, max):
		self.chatLine.SetMax(max)
		from grpText import GetSplitingTextLine
		text = self.chatLine.GetText()
		if text:
			self.chatLine.SetText(GetSplitingTextLine(text, max, 0))

	def OpenWithTarget(self, targetName):
		chat.CreateWhisper(targetName)
		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			chat.SetWhisperBoxSize(targetName, self.GetWidth() - 60, self.GetHeight() - 110)
			self.titleNameEditBar.Hide()
			self.SetPosition(170, 0)
		else:
			chat.SetWhisperBoxSize(targetName, self.GetWidth() - 60, self.GetHeight() - 90)	
		if not app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.titleName.SetText(targetName)
			self.ignoreButton.Hide()
			if app.IsDevStage():
				self.reportViolentWhisperButton.Show()
			else:
				self.reportViolentWhisperButton.Hide()
		self.chatLine.SetFocus()
		self.targetName = targetName
		self.textRenderer.SetTargetName(targetName)
		self.gamemasterMark.Hide()
		self.minimizeButton.Show()
		self.titleNameEdit.Hide()
		self.acceptButton.Hide()

	def OpenWithoutTarget(self, event):
		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.titleNameEditBar.Show()
			self.SetPosition(250, 0)
		self.eventAcceptTarget = event
		self.minimizeButton.Hide()
		self.gamemasterMark.Hide()
		self.titleNameEdit.SetText("")
		self.titleNameEdit.SetFocus()
		self.targetName = 0
		self.titleNameEdit.Show()
		self.acceptButton.Show()
		if not app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.titleName.SetText("")
			self.minimizeButton.Hide()
			self.gamemasterMark.Hide()
			self.ignoreButton.Hide()
			self.reportViolentWhisperButton.Hide()

	def SetGameMasterLook(self):
		self.gamemasterMark.Show()

	def Minimize(self):
		self.titleNameEdit.KillFocus()
		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.titleNameEditBar.Hide()
			self.acceptButton.Hide()
		self.chatLine.KillFocus()
		self.Hide()
		if None != self.eventMinimize:
			if app.ENABLE_RENEW_MESSENGER_WHISPER:
				self.eventMinimize(self.targetName, self.job, self.level, self.empire, self.guild, self.language, self.status, self.location, self.year, self.month, self.day)
			else:
				self.eventMinimize(self.targetName)

	def Close(self):
		chat.ClearWhisper(self.targetName)
		self.titleNameEdit.KillFocus()
		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.titleNameEditBar.Hide()
			self.acceptButton.Hide()
		self.chatLine.KillFocus()
		self.Hide()
		if None != self.eventClose:
			self.eventClose(self.targetName)

	def ReportViolentWhisper(self):
		net.SendChatPacket("/reportviolentwhisper " + self.targetName)

	def IgnoreTarget(self):
		net.SendChatPacket("/ignore " + self.targetName)

	def AcceptTarget(self):
		name = self.titleNameEdit.GetText()
		if len(name) <= 0:
			self.Close()
			return
		if None != self.eventAcceptTarget:
			self.titleNameEdit.KillFocus()
			self.eventAcceptTarget(name)

	def OnScroll(self):
		chat.SetWhisperPosition(self.targetName, self.scrollBar.GetPos())
		
	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def InitializeProfileData(self):
			self.job = -1
			self.level = -1
			self.empire = -1
			self.guild = ""
			self.language = ""
			self.status = ""
			self.location = ""
			self.year = ""
			self.month = ""
			self.day = ""
			self.lastSentenceStack = []
			self.lastSentencePos = 0

		def OnIMEKeyDown(self, key):
			if app.VK_UP == key:
				self.__PrevLastSentenceStack()
				return TRUE
			if app.VK_DOWN == key:
				self.__NextLastSentenceStack()				
				return TRUE
			return FALSE
			
		def __PrevLastSentenceStack(self):
			if self.lastSentenceStack and self.lastSentencePos < len(self.lastSentenceStack):
				self.lastSentencePos += 1
				lastSentence = self.lastSentenceStack[- self.lastSentencePos]
				self.chatLine.SetText(lastSentence)				
				self.chatLine.SetEndPosition()

		def __NextLastSentenceStack(self):
			if self.lastSentenceStack and self.lastSentencePos > 1:
				self.lastSentencePos -= 1
				lastSentence = self.lastSentenceStack[- self.lastSentencePos]
				self.chatLine.SetText(lastSentence)				
				self.chatLine.SetEndPosition()

		def __PushLastSentenceStack(self, text):		
			if len(text) <= 0:
				return
			LAST_SENTENCE_STACK_SIZE = 32
			if len(self.lastSentenceStack) > LAST_SENTENCE_STACK_SIZE:
				self.lastSentenceStack.pop(0)
			self.lastSentenceStack.append(text)
			
		def OnSelectEmoticon(self, key):
			self.chatLine.SetText("%s %s" % (self.chatLine.GetText(), uiContact.DICTIONARY['EMOTICONS_KEY_LIST'][key]))
			self.chatLine.OnSetFocus()

		def RecvWhisperProfile(self, job, level, empire, guild, language, status, location, year, month, day):
			def get(text):
				if not text:
					return localeInfo.PROFILE_SELECT_DEFAULT
				return text
			self.job = job
			self.level = level
			self.empire = empire
			self.guild = guild
			self.language = language
			self.status = status
			self.location = location
			self.year = year
			self.month = month
			self.day = day
			if empire in uiContact.DICTIONARY['EMPIRE_IMAGE_LIST']:
				self.Whisper_Profile_Empire_Icon.LoadImage(uiContact.DICTIONARY['EMPIRE_IMAGE_LIST'][empire])
			if job in uiContact.DICTIONARY['FACE_IMAGE_LIST']:
				self.Whisper_Profile_Photo_Icon.LoadImage(uiContact.DICTIONARY['FACE_IMAGE_LIST'][job])
			if language:
				self.Whisper_Profile_Language_Icon.LoadImage(uiContact.DICTIONARY['LANGUAGE_IMAGE_STRING'] % (language))
			self.Whisper_Profile_Name_Value.SetText("--")
			self.Whisper_Profile_Level_Value.SetText("--")
			self.Whisper_Profile_Guild_Value.SetText("--")
			self.Whisper_Profile_Birthday_Value.SetText("--")	
			if len(location) > 19:
				location = location[:16] + "..."
			if len(status) > 19:
				status = status[:16] + "..."			
			self.Whisper_Profile_Location_Value.SetText("--")
			self.Whisper_Profile_Status_Value.SetText("--")

	def SendWhisper(self):
		text = self.chatLine.GetText()
		textLength = len(text)
		if textLength > 0:
			if net.IsInsultIn(text):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHAT_INSULT_STRING)
				return
			net.SendWhisperPacket(self.targetName, text)
			self.chatLine.SetText("")
			if app.ENABLE_RENEW_MESSENGER_WHISPER:
				self.__PushLastSentenceStack(text)
				chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, "%s %s : %s" % (uiContact.GetWhisperSendedTime(), player.GetName(), text))
			else:
				chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, self.targetName, player.GetName() + " : " + text)

	def OnTop(self):
		if self.chatLine:
			self.chatLine.SetFocus()
		
	def BindInterface(self, interface):
		self.interface = interface
		
	def OnMouseLeftButtonDown(self):
		hyperlink = ui.GetHyperlink()
		if hyperlink:
			if app.IsPressed(app.DIK_LALT):
				link = chat.GetLinkFromHyperlink(hyperlink)
				ime.PasteString(link)
			else:
				self.interface.MakeHyperlinkTooltip(hyperlink)

if "__main__" == __name__:
	import uiTest

	class TestApp(uiTest.App):
		def OnInit(self):
			wnd = WhisperDialog(self.OnMax, self.OnMin)
			wnd.LoadDialog()
			wnd.OpenWithoutTarget(self.OnNew)
			wnd.SetPosition(0, 0)
			wnd.Show()
			self.wnd = wnd

		def OnMax(self):
			pass

		def OnMin(self):
			pass

		def OnNew(self):
			pass

	TestApp().MainLoop()
