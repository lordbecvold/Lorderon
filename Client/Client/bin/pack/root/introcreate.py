#Lorderon Client Dev by Lordbecvold
import chr
import grp
import app
import net
import snd
import wndMgr
import systemSetting
import localeInfo
import ui
import musicInfo
import playerSettingModule
MAN			= 0
WOMAN		= 1
SHAPE0		= 0
SHAPE1		= 1
PAGE_COUNT	= 2
SLOT_COUNT	= 4
BASE_CHR_ID	= 3

class CreateCharacterWindow(ui.Window):
	class CharacterRenderer(ui.Window):
		def OnRender(self):
			grp.ClearDepthBuffer()
			grp.SetGameRenderState()
			grp.PushState()
			grp.SetOmniLight()
			screenWidth = wndMgr.GetScreenWidth()
			screenHeight = wndMgr.GetScreenHeight()
			newScreenWidth = float(screenWidth+30)
			newScreenHeight = float(screenHeight+30)
			grp.SetViewport(270.0/screenWidth, 0.0, newScreenWidth/screenWidth, newScreenHeight/screenHeight)
			app.SetCenterPosition(5.0, 350.0, 20.0)
			app.SetCamera(800.0, 15.0, 180.0, 205.0)
			grp.SetPerspective(16.0, newScreenWidth/newScreenHeight, 1000.0, 4000.0)
			(x, y) = app.GetCursorPosition()
			grp.SetCursorPosition(x, y)
			chr.Deform()
			chr.Render()
			grp.RestoreViewport()
			grp.PopState()
			grp.SetInterfaceRenderState()

	def __init__(self, stream):
		ui.Window.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_CREATE, self)
		self.stream = stream

	def __del__(self):
		net.SetPhaseWindow(net.PHASE_WINDOW_CREATE, 0)
		ui.Window.__del__(self)

	def Open(self):
		playerSettingModule.LoadGameData("INIT")
		self.reservingRaceIndex = -1
		self.reservingShapeIndex = -1
		self.reservingStartTime = 0
		self.gender = 0
		self.slot = -1
		self.shape = 0
		try:
			dlgBoard = ui.ScriptWindow()
			pythonScriptLoader = ui.PythonScriptLoader()
			pythonScriptLoader.LoadScriptFile(dlgBoard, "twix_work/characterwindow/create/createcharacterwindow.py")
		except:
			import exception
			exception.Abort("CreateCharacterWindow.Open.LoadObject")
		try:
			getChild = dlgBoard.GetChild
			self.NameList = []
			self.NameList.append(getChild("name_warrior"))
			self.NameList.append(getChild("name_assassin"))
			self.NameList.append(getChild("name_sura"))
			self.NameList.append(getChild("name_shaman"))			
			self.btnCreate = getChild("create_button")
			self.btnExit = getChild("exit_button")		
			self.editCharacterName = getChild("name")		
			self.genderButton = []
			self.genderButton.append(getChild("gender_man"))
			self.genderButton.append(getChild("gender_woman"))		
			self.shapeButton = []
			self.shapeButton.append(getChild("shape1"))
			self.shapeButton.append(getChild("shape2"))			
			self.btnLeft = getChild("left_button")
			self.btnRight = getChild("right_button")
			self.backGround = getChild("BackGround")
		except:
			import exception
			exception.Abort("CreateCharacterWindow.Open.BindObject")	
		self.btnCreate.SetEvent(ui.__mem_func__(self.CreateCharacter))
		self.btnExit.SetEvent(ui.__mem_func__(self.CancelCreate))	
		self.btnLeft.SetEvent(ui.__mem_func__(self.__DecreaseSlotIndex))
		self.btnRight.SetEvent(ui.__mem_func__(self.__IncreaseSlotIndex))	
		self.genderButton[0].SetEvent(ui.__mem_func__(self.__SelectGender), MAN)
		self.genderButton[1].SetEvent(ui.__mem_func__(self.__SelectGender), WOMAN)
		self.editCharacterName.SetText("")
		self.editCharacterName.SetReturnEvent(ui.__mem_func__(self.CreateCharacter))
		self.editCharacterName.SetEscapeEvent(ui.__mem_func__(self.CancelCreate))
		self.chrRenderer = self.CharacterRenderer()
		self.chrRenderer.SetParent(self.backGround)
		self.chrRenderer.Show()		
		self.dlgBoard = dlgBoard	
		self.curNameAlpha	= [0.0, 0.0, 0.0, 0.0, 0.0]
		self.destNameAlpha	= [0.0, 0.0, 0.0, 0.0, 0.0]	
		self.characters = {0 : [playerSettingModule.RACE_WARRIOR_M, playerSettingModule.RACE_ASSASSIN_M, playerSettingModule.RACE_SURA_M, playerSettingModule.RACE_SHAMAN_M],1 : [playerSettingModule.RACE_WARRIOR_W, playerSettingModule.RACE_ASSASSIN_W, playerSettingModule.RACE_SURA_W, playerSettingModule.RACE_SHAMAN_W]}
		self.shapeButton[0].SetEvent(ui.__mem_func__(self.__SelectShape), 0)
		self.shapeButton[1].SetEvent(ui.__mem_func__(self.__SelectShape), 1)
		self.EnableWindow()
		self.__SelectSlot(app.GetRandom(0,3))
		app.SetCamera(800.0, 15.0, 180.0, 205.0)
		self.__SelectGender(0)
		self.__SelectShape(0)
		self.Show()
		self.dlgBoard.Show()
		app.ShowCursor()
		
	def Close(self):
		self.btnLeft = 0
		self.btnRight = 0
		for id in xrange(BASE_CHR_ID + SLOT_COUNT * PAGE_COUNT):
			chr.DeleteInstance(id)
		self.dlgBoard.Hide()
		self.Hide()
		app.HideCursor()

	def EnableWindow(self):
		self.reservingRaceIndex = -1
		self.reservingShapeIndex = -1
		self.reservingHairstyleIndex = -1
		self.btnCreate.Enable()
		self.btnExit.Enable()
		self.editCharacterName.SetFocus()
		self.editCharacterName.Enable()	
		self.genderButton[0].Enable()
		self.genderButton[1].Enable()	
		self.shapeButton[0].Enable()
		self.shapeButton[1].Enable()
		for page in xrange(PAGE_COUNT):
			for slot in xrange(SLOT_COUNT):
				chr_id = self.__GetSlotChrID(page, slot)
				chr.SelectInstance(chr_id)
				chr.BlendLoopMotion(chr.MOTION_INTRO_WAIT, 0.1)

	def DisableWindow(self):
		self.btnCreate.Disable()
		self.btnExit.Disable()	
		self.genderButton[0].Disable()
		self.genderButton[1].Disable()		
		self.shapeButton[0].Disable()
		self.shapeButton[1].Disable()	
		self.editCharacterName.Disable()

	def __GetSlotChrID(self, page, slot):
		return BASE_CHR_ID + page * SLOT_COUNT + slot

	def __MakeCharacter(self,chr_id,race):
		chr.CreateInstance(chr_id)
		chr.SelectInstance(chr_id)
		chr.SetVirtualID(chr_id)
		chr.SetRace(race)
		chr.SetArmor(0)
		chr.SetHair(0)
		chr.Refresh()
		chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
		chr.SetLoopMotion(chr.MOTION_INTRO_WAIT)
		chr.SetRotation(0.0)
		chr.Hide()

	def __SelectGender(self, gender):		
		for button in self.genderButton:
			button.SetUp()
		self.genderButton[gender].Down()
		self.gender = gender
		if gender == MAN:
			for i in xrange(SLOT_COUNT):
				chr.SelectInstance(self.__GetSlotChrID(0, i))
				chr.Show()
			for i in xrange(SLOT_COUNT):
				chr.SelectInstance(self.__GetSlotChrID(1, i))
				chr.Hide()
		else:
			for i in xrange(SLOT_COUNT):
				chr.SelectInstance(self.__GetSlotChrID(0, i))
				chr.Hide()
			for i in xrange(SLOT_COUNT):
				chr.SelectInstance(self.__GetSlotChrID(1, i))
				chr.Show()					
		for id in xrange(BASE_CHR_ID + SLOT_COUNT * PAGE_COUNT):
			chr.DeleteInstance(id)		
		chr_id = self.__GetSlotChrID(self.gender, self.slot)		
		self.__MakeCharacter(chr_id, self.characters[self.gender][self.slot])
		self.__SelectShape(self.shape)
		
	def __SelectShape(self, shape):
		self.shape = shape	
		for i in xrange(len(self.shapeButton)):
			self.shapeButton[i].SetUp()
		self.shapeButton[shape].Down()	
		chr_id = self.__GetSlotChrID(self.gender, self.slot)		
		chr.SelectInstance(chr_id)		
		chr.ChangeShape(shape)		
		chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
		chr.SetLoopMotion(chr.MOTION_INTRO_WAIT)

	def GetSlotIndex(self):
		return self.slot

	def __SelectSlot(self, slot):
		if slot < 0:
			return
		if slot >= SLOT_COUNT:
			return		
		if self.slot == slot:
			return
		self.slot = slot
		if self.IsShow():
			snd.PlaySound("sound/ui/click.wav")
		chr_id = self.__GetSlotChrID(self.gender, slot)	
		for i in xrange(SLOT_COUNT):
			self.destNameAlpha[i] = 0.0
		self.destNameAlpha[slot] = 1.0		
		for id in xrange(BASE_CHR_ID + SLOT_COUNT * PAGE_COUNT):
			chr.DeleteInstance(id)			
		chr.SelectInstance(chr_id)		
		self.__MakeCharacter(chr_id, self.characters[self.gender][slot])
		self.__SelectShape(self.shape)
		self.__SelectGender(self.gender)
		
	def CreateCharacter(self):
		if -1 != self.reservingRaceIndex:
			return
		textName = self.editCharacterName.GetText()
		if False == self.__CheckCreateCharacter(textName):
			return			
		self.DisableWindow()		
		chr.SelectInstance(self.__GetSlotChrID(self.gender, self.slot))
		chr.PushOnceMotion(chr.MOTION_INTRO_SELECTED)
		self.reservingRaceIndex = chr.GetRace()
		self.reservingShapeIndex = self.shape
		self.reservingStartTime = app.GetTime()

	def CancelCreate(self):
		self.stream.SetSelectCharacterPhase()
		
	def __DecreaseSlotIndex(self):
		slotIndex = (self.GetSlotIndex() - 1 + SLOT_COUNT) % SLOT_COUNT
		self.__SelectSlot(slotIndex)

	def __IncreaseSlotIndex(self):
		slotIndex = (self.GetSlotIndex() + 1) % SLOT_COUNT
		self.__SelectSlot(slotIndex)		

	def __CheckCreateCharacter(self, name):
		if len(name) == 0:
			self.PopupMessage(localeInfo.CREATE_INPUT_NAME, self.EnableWindow)
			return False
		if name.find(localeInfo.CREATE_GM_NAME)!=-1:
			self.PopupMessage(localeInfo.CREATE_ERROR_GM_NAME, self.EnableWindow)
			return False
		if net.IsInsultIn(name):
			self.PopupMessage(localeInfo.CREATE_ERROR_INSULT_NAME, self.EnableWindow)
			return False
		return True		

	def OnCreateSuccess(self):
		self.stream.SetSelectCharacterPhase()

	def OnCreateFailure(self, type):
		if 1 == type:
			self.PopupMessage(localeInfo.CREATE_EXIST_SAME_NAME, self.EnableWindow)
		else:
			self.PopupMessage(localeInfo.CREATE_FAILURE, self.EnableWindow)
			
	def OnKeyDown(self, key):
		if 203 == key:
			self.__DecreaseSlotIndex()
		if 205 == key:
			self.__IncreaseSlotIndex()
		return TRUE		
			
	def OnUpdate(self):
		chr.Update()	
		for i in xrange(4):
			self.curNameAlpha[i] += (self.destNameAlpha[i] - self.curNameAlpha[i]) / 10.0
			self.NameList[i].SetAlpha(self.curNameAlpha[i])
		for page in xrange(PAGE_COUNT):
			for i in xrange(SLOT_COUNT):
				chr.SelectInstance(self.__GetSlotChrID(page, i))
				chr.Show()
		if -1 != self.reservingRaceIndex:
			if app.GetTime() - self.reservingStartTime >= 1.5:
				chrSlot=self.stream.GetCharacterSlot()
				textName = self.editCharacterName.GetText()
				raceIndex = self.reservingRaceIndex
				shapeIndex = self.reservingShapeIndex
				net.SendCreateCharacterPacket(chrSlot, textName, raceIndex, shapeIndex, 0, 0, 0, 0)
				self.reservingRaceIndex = -1

	def EmptyFunc(self):
		pass

	def PopupMessage(self, msg, func=0):
		if not func:
			func=self.EmptyFunc
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def OnPressExitKey(self):
		self.CancelCreate()
		return True
