#Lorderon Client Dev by Lordbecvold
import app
import net
import player
import item
import ui
import uiToolTip
import mouseModule
import localeinfo
import uiCommon
import constInfo
import snd
import wndMgr
import chat

REFINE_VNUM = [
	player.REFINE_VNUM_POTION_LOW,
	player.REFINE_VNUM_POTION_MEDIUM,
	player.REFINE_VNUM_POTION_EXTRA
]

REFINE_PERCENTAGE = [
	player.REFINE_PERCENTAGE_LOW,
	player.REFINE_PERCENTAGE_MEDIUM,
	player.REFINE_PERCENTAGE_EXTRA
]

REFINE_MODE = {
	0 : 0,
	1 : 0,
	2 : 0
}

REFINE_TOTAL_PERCENTAGE = {
	"update" : 0
}

def IS_UPGRADE_ITEM(itemVnum):
	for i in xrange(3):
		if itemVnum == REFINE_VNUM[i]:
			return TRUE
	return FALSE

class RefineDialog(ui.ScriptWindow):
	makeSocketSuccessPercentage = ( 100, 33, 20, 15, 10, 5, 0 )
	upgradeStoneSuccessPercentage = ( 30, 29, 28, 27, 26, 25, 24, 23, 22 )
	upgradeArmorSuccessPercentage = ( 99, 66, 33, 33, 33, 33, 33, 33, 33 )
	upgradeAccessorySuccessPercentage = ( 99, 88, 77, 66, 33, 33, 33, 33, 33 )
	upgradeSuccessPercentage = ( 99, 66, 33, 33, 33, 33, 33, 33, 33 )

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadScript()
		self.scrollItemPos = 0
		self.targetItemPos = 0

	def __LoadScript(self):
		self.__LoadQuestionDialog()
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/refinedialog.py")
		except:
			import exception
			exception.Abort("RefineDialog.__LoadScript.LoadObject")
		try:
			self.board = self.GetChild("Board")
			self.titleBar = self.GetChild("TitleBar")
			self.successPercentage = self.GetChild("SuccessPercentage")
			self.GetChild("AcceptButton").SetEvent(self.OpenQuestionDialog)
			self.GetChild("CancelButton").SetEvent(self.Close)
		except:
			import exception
			exception.Abort("RefineDialog.__LoadScript.BindObject")
		toolTip = uiToolTip.ItemToolTip()
		toolTip.SetParent(self)
		toolTip.SetPosition(15, 38)
		toolTip.SetFollow(FALSE)
		toolTip.Show()
		self.toolTip = toolTip
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadQuestionDialog(self):
		self.dlgQuestion = ui.ScriptWindow()
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self.dlgQuestion, "uiscript/questiondialog2.py")
		except:
			import exception
			exception.Abort("RefineDialog.__LoadQuestionDialog.LoadScript")
		try:
			GetObject=self.dlgQuestion.GetChild
			GetObject("message1").SetText(localeinfo.REFINE_DESTROY_WARNING)
			GetObject("message2").SetText(localeinfo.REFINE_WARNING2)
			GetObject("accept").SetEvent(ui.__mem_func__(self.Accept))
			GetObject("cancel").SetEvent(ui.__mem_func__(self.dlgQuestion.Hide))
		except:
			import exception
			exception.Abort("SelectCharacterWindow.__LoadQuestionDialog.BindObject")

	def Destroy(self):
		self.ClearDictionary()
		self.board = 0
		self.successPercentage = 0
		self.titleBar = 0
		self.toolTip = 0
		self.dlgQuestion = 0

	def GetRefineSuccessPercentage(self, scrollSlotIndex, itemSlotIndex):
		if -1 != scrollSlotIndex:
			if player.IsRefineGradeScroll(scrollSlotIndex):
				curGrade = player.GetItemGrade(itemSlotIndex)
				itemIndex = player.GetItemIndex(itemSlotIndex)
				item.SelectItem(itemIndex)
				itemType = item.GetItemType()
				itemSubType = item.GetItemSubType()
				if item.ITEM_TYPE_METIN == itemType:
					if curGrade >= len(self.upgradeStoneSuccessPercentage):
						return 0
					return self.upgradeStoneSuccessPercentage[curGrade]
				elif item.ITEM_TYPE_ARMOR == itemType:
					if item.ARMOR_BODY == itemSubType:
						if curGrade >= len(self.upgradeArmorSuccessPercentage):
							return 0
						return self.upgradeArmorSuccessPercentage[curGrade]
					else:
						if curGrade >= len(self.upgradeAccessorySuccessPercentage):
							return 0
						return self.upgradeAccessorySuccessPercentage[curGrade]
				else:
					if curGrade >= len(self.upgradeSuccessPercentage):
						return 0
					return self.upgradeSuccessPercentage[curGrade]
		for i in xrange(player.METIN_SOCKET_MAX_NUM+1):
			if 0 == player.GetItemMetinSocket(itemSlotIndex, i):
				break
		return self.makeSocketSuccessPercentage[i]

	def Open(self, scrollItemPos, targetItemPos):
		self.scrollItemPos = scrollItemPos
		self.targetItemPos = targetItemPos
		percentage = self.GetRefineSuccessPercentage(scrollItemPos, targetItemPos)
		if 0 == percentage:
			return
		self.successPercentage.SetText(localeinfo.REFINE_SUCCESS_PROBALITY % (percentage))
		itemIndex = player.GetItemIndex(targetItemPos)
		self.toolTip.ClearToolTip()
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(targetItemPos, i))
		self.toolTip.AddItemData(itemIndex, metinSlot)
		self.UpdateDialog()
		self.SetTop()
		self.Show()

	def UpdateDialog(self):
		newWidth = self.toolTip.GetWidth() + 30
		newHeight = self.toolTip.GetHeight() + 98
		self.board.SetSize(newWidth, newHeight)
		self.titleBar.SetWidth(newWidth-15)
		self.SetSize(newWidth, newHeight)
		(x, y) = self.GetLocalPosition()
		self.SetPosition(x, y)

	def OpenQuestionDialog(self):
		percentage = self.GetRefineSuccessPercentage(-1, self.targetItemPos)
		if 100 == percentage:
			self.Accept()
			return
		self.dlgQuestion.SetTop()
		self.dlgQuestion.Show()

	def Accept(self):
		if app.ENABLE_REFINE_RENEWAL:
			net.SendRefinePacket(self.targetItemPos, self.type)
		else:
			net.SendRefinePacket(self.targetItemPos, self.type)
			self.Close()
				
	def Close(self):
		self.dlgQuestion.Hide()
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

class RefineDialogNew(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.isLoaded = FALSE

	def __Initialize(self):
		self.dlgQuestion = None
		self.children = []
		self.vnum = 0
		self.targetItemPos = 0
		self.dialogHeight = 0
		self.percentage = 0
		self.total_percentage = 0
		self.cost = 0
		self.type = 0

	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/refinedialog.py")
		except:
			import exception
			exception.Abort("RefineDialog.__LoadScript.LoadObject")
		try:
			self.board = self.GetChild("Board")
			self.titleBar = self.GetChild("TitleBar")
			self.probText = self.GetChild("SuccessPercentage")
			self.probIncreaseText = self.GetChild("SuccessPercentageIncreased")
			self.costText = self.GetChild("Cost")			
			self.slot = self.GetChild("Slot")			
			self.designMode = self.GetChild("DesignIncrease")		
			self.button_accept = self.GetChild("AcceptButton")
			self.GetChild("AcceptButton").SetEvent(self.OpenQuestionDialog)
			self.GetChild("CancelButton").SetEvent(self.CancelRefine)
		except:
			import exception
			exception.Abort("RefineDialog.__LoadScript.BindObject")	
		self.slot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		self.slot.SetUnselectItemSlotEvent(ui.__mem_func__(self.__OnSelectItemSlot))
		self.slot.SetUseSlotEvent(ui.__mem_func__(self.__OnSelectItemSlot))
		self.slot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.slot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		self.toolTipNext = uiToolTip.ItemToolTip()
		self.toolTipNext.HideToolTip()
		self.toolTipCur = uiToolTip.ItemToolTip()
		self.toolTipCur.HideToolTip()
		self.tooltipMode = uiToolTip.ItemToolTip()
		self.tooltipMode.HideToolTip()
		self.toolTipMaterial = uiToolTip.ItemToolTip()
		self.toolTipMaterial.HideToolTip()
		self.slotCurrent, self.slotAfter, self.numberSlotImage, self.imgPotion = {}, {}, {}, {}
		posY = 61
		for i in xrange(3):
			self.slotCurrent[i] = ui.MakeImageBox(self, "d:/ymir work/ui/public/Slot_Base.sub", 25*2, posY)
			self.slotAfter[i] = ui.MakeImageBox(self, "d:/ymir work/ui/public/Slot_Base.sub", 105*2-20, posY)
			posY += 32
		xPos = 4
		name = "icon/item/potion_refine_hide_"
		for i in xrange(3):
			self.numberSlotImage[i] = ui.MakeImageBox(self.designMode, "d:/ymir work/ui/public/Slot_Base.sub", xPos, 25)
			self.imgPotion[i] = ui.MakeImageBox(self.designMode, name + str(i+1) + ".tga", xPos + 3, 25)
			xPos += 80
		self.itemImageCur = ui.MakeImageBox(self, "d:/ymir work/ui/public/Slot_Base.sub", 49, 60)
		self.itemImageNext = ui.MakeImageBox(self, "d:/ymir work/ui/public/Slot_Base.sub", 105*2-20, 60)
		self.materialList = []
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.CancelRefine))
		if app.ENABLE_REFINE_RENEWAL:
			self.checkBox = ui.CheckBox()
			self.checkBox.SetParent(self)
			self.checkBox.SetPosition(160, 42)
			self.checkBox.SetWindowHorizontalAlignCenter()
			self.checkBox.SetWindowVerticalAlignBottom()
			self.checkBox.SetEvent(ui.__mem_func__(self.AutoRefine), "ON_CHECK", True)
			self.checkBox.SetEvent(ui.__mem_func__(self.AutoRefine), "ON_UNCKECK", False)
			self.checkBox.SetCheckStatus(constInfo.IS_AUTO_REFINE)
			self.checkBox.SetTextInfo("Zrychlené vylepšování")
			self.checkBox.Show()
		self.isLoaded = TRUE

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __MakeItemSlot(self,c):
		itemslot = ui.SlotWindow()
		itemslot.SetParent(self)
		itemslot.SetSize(32, 32)
		itemslot.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
		itemslot.AppendSlot(c, 0, 0, 32, 32)
		itemslot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		itemslot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		itemslot.RefreshSlot()
		itemslot.Show()
		self.children.append(itemslot)
		return itemslot

	def __MakeThinBoard(self):
		thinBoard = ui.ThinBoard()
		thinBoard.SetParent(self)
		thinBoard.Show()
		self.children.append(thinBoard)
		return thinBoard

	def Destroy(self):
		self.ClearDictionary()
		self.dlgQuestion = None
		self.board = 0
		self.probText = 0
		self.probIncreaseText = 0
		self.costText = 0
		self.titleBar = 0
		self.toolTipNext = 0
		self.toolTipCur = 0
		self.itemImageCur = 0
		self.itemImageNext = 0
		self.children = []
		self.materialList = []
		self.toolTipMaterial = 0
		self.slotCurrent = None
		self.slotAfter = None
		self.numberSlotImage = None
		self.imgPotion = None
		REFINE_TOTAL_PERCENTAGE["update"] = 0

	if app.ENABLE_REFINE_RENEWAL:
		def __InitializeOpen(self):
			self.children = []
			self.vnum = 0
			self.targetItemPos = 0
			self.dialogHeight = 0
			self.cost = 0
			self.percentage = 0
			self.type = 0
			self.xRefineStart = 0
			self.yRefineStart = 0	

	def Open(self, targetItemPos, nextGradeItemVnum, cost, prob, type):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		if app.ENABLE_REFINE_RENEWAL:
			self.__InitializeOpen()
		else:
			self.__Initialize()
		self.targetItemPos = targetItemPos
		self.vnum = nextGradeItemVnum
		self.cost = cost
		self.percentage = prob
		self.type = type
		self.Clear()
		self.probText.SetText(localeinfo.REFINE_CURRENT_PERCENTAGE % (self.percentage))
		self.costText.SetText("%s" % (localeinfo.NumberToMoneyString(self.cost)))
		self.toolTipNext.ClearToolTip()
		self.toolTipCur.ClearToolTip()
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(targetItemPos, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(player.GetItemAttribute(targetItemPos, i))
		self.toolTipCur.SetInventoryItem(targetItemPos)
		self.toolTipNext.AddRefineItemData(nextGradeItemVnum, metinSlot, attrSlot)
		curItemIndex = player.GetItemIndex(targetItemPos)
		if curItemIndex != 0:
			item.SelectItem(curItemIndex)
			try:
				self.itemImageCur.LoadImage(item.GetIconImageFileName())
			except:
				dbg.TraceError("Refine.CurrentItem.LoadImage - Failed to find item data")
		item.SelectItem(nextGradeItemVnum)
		self.itemImageNext.LoadImage(item.GetIconImageFileName())
		self.dialogHeight = 72
		self.UpdateDialog()
		self.SetTop()
		self.Show()
		
	def Clear(self):
		for it in xrange(3):
			REFINE_MODE[it] = 0
			self.slot.ClearSlot(it)
		REFINE_TOTAL_PERCENTAGE["update"] = 0

	def Close(self):
		self.dlgQuestion = None
		self.Clear()
		self.Hide()

	def AppendMaterial(self, vnum, count):
		grid = self.__MakeItemSlot(len(self.materialList))
		grid.SetPosition(293-35, self.dialogHeight)
		grid.SetItemSlot(len(self.materialList), vnum, 0)
		self.materialList.append(vnum)
		thinBoard = self.__MakeThinBoard()
		thinBoard.SetPosition(293, self.dialogHeight)
		thinBoard.SetSize(191, 20)
		textLine = ui.TextLine()
		textLine.SetParent(thinBoard)
		textLine.SetFontName(localeinfo.UI_DEF_FONT)
		if player.GetItemCountByVnum(vnum) < count:
			textLine.SetPackedFontColor(0xffdddddd)
		else:
			textLine.SetPackedFontColor(0xffdddddd)
		textLine.SetText("%s x %02d" % (item.GetItemName(), count))
		textLine.SetOutline()
		textLine.SetFeather(FALSE)
		textLine.SetWindowVerticalAlignCenter()
		textLine.SetVerticalAlignCenter()
		if localeinfo.IsARABIC():
			(x,y) = textLine.GetTextSize()
			textLine.SetPosition(x, 0)
		else:
			textLine.SetPosition(15, 0)
		textLine.Show()
		self.children.append(textLine)
		self.dialogHeight += 34
		self.UpdateDialog()

	def UpdateDialog(self):
		if localeinfo.IsARABIC():
			self.board.SetPosition(500, 0)
			(x, y) = self.titleBar.GetLocalPosition()
			self.titleBar.SetPosition(500 - 15, y)
		self.board.SetSize(500, 250)
		self.titleBar.SetWidth(500-15)
		self.SetSize(500, 250)
		(x, y) = self.GetLocalPosition()
		self.SetPosition(x, y)

	def OpenQuestionDialog(self):
		totalPerc = self.percentage + REFINE_TOTAL_PERCENTAGE["update"]
		if 100 == totalPerc:
			self.Accept()
			return
		if 5 == self.type:
			self.Accept()
			return
		dlgQuestion = uiCommon.QuestionDialog2()
		dlgQuestion.SetText2(localeinfo.REFINE_WARNING2)
		dlgQuestion.SetAcceptEvent(ui.__mem_func__(self.Accept))
		dlgQuestion.SetCancelEvent(ui.__mem_func__(dlgQuestion.Close))
		if 3 == self.type:
			dlgQuestion.SetText1(localeinfo.REFINE_DESTROY_WARNING_WITH_BONUS_PERCENT_1)
			dlgQuestion.SetText2(localeinfo.REFINE_DESTROY_WARNING_WITH_BONUS_PERCENT_2)
		elif 2 == self.type:
			dlgQuestion.SetText1(localeinfo.REFINE_DOWN_GRADE_WARNING)
		else:
			dlgQuestion.SetText1(localeinfo.REFINE_DESTROY_WARNING)
		dlgQuestion.Open()
		self.dlgQuestion = dlgQuestion

	def Accept(self):
		totalPerc = self.percentage + REFINE_TOTAL_PERCENTAGE["update"]
		net.SendRefinePacket(self.targetItemPos, self.type, REFINE_MODE[0], REFINE_MODE[1], REFINE_MODE[2], totalPerc)
		self.Close()

	if app.ENABLE_REFINE_RENEWAL:	
		def AutoRefine(self, checkType, autoFlag):
			constInfo.IS_AUTO_REFINE = autoFlag
		
		def CheckRefine(self, isFail):
			if constInfo.IS_AUTO_REFINE == True:
				if constInfo.AUTO_REFINE_TYPE == 1:
					if constInfo.AUTO_REFINE_DATA["ITEM"][0] != -1 and constInfo.AUTO_REFINE_DATA["ITEM"][1] != -1:
						scrollIndex = player.GetItemIndex(constInfo.AUTO_REFINE_DATA["ITEM"][0])
						itemIndex = player.GetItemIndex(constInfo.AUTO_REFINE_DATA["ITEM"][1])
						if scrollIndex == 0 or (itemIndex % 10 == 8 and not isFail):
							self.Close()
						else:
							net.SendItemUseToItemPacket(constInfo.AUTO_REFINE_DATA["ITEM"][0], constInfo.AUTO_REFINE_DATA["ITEM"][1])
				elif constInfo.AUTO_REFINE_TYPE == 2:
					npcData = constInfo.AUTO_REFINE_DATA["NPC"]
					if npcData[0] != 0 and npcData[1] != -1 and npcData[2] != -1 and npcData[3] != 0:
						itemIndex = player.GetItemIndex(npcData[1], npcData[2])
						if (itemIndex % 10 == 8 and not isFail) or isFail:
							self.Close()
						else:
							net.SendGiveItemPacket(npcData[0], npcData[1], npcData[2], npcData[3])
				else:
					self.Close()
			else:
				self.Close()
				
	def OnUpdate(self):
		if self.itemImageCur:
			if self.itemImageCur.IsIn():
				self.toolTipCur.ShowToolTip()
			else:
				self.toolTipCur.HideToolTip()
		if self.itemImageNext:
			if self.itemImageNext.IsIn():
				self.toolTipNext.ShowToolTip()
			else:
				self.toolTipNext.HideToolTip()
		self.probIncreaseText.SetText(localeinfo.REFINE_INCREASE_PERCENTAGE % (REFINE_TOTAL_PERCENTAGE["update"]))

	def CancelRefine(self):
		net.SendRefinePacket(255, 255, 0, 0, 0, 0)
		self.Close()
		if app.ENABLE_REFINE_RENEWAL:
			constInfo.AUTO_REFINE_TYPE = 0
			constInfo.AUTO_REFINE_DATA = {
				"ITEM" : [-1, -1],
				"NPC" : [0, -1, -1, 0]
			}

	def OnPressEscapeKey(self):
		self.CancelRefine()
		return TRUE

	def OverInItem(self, slot):
		if self.toolTipMaterial:
			self.toolTipMaterial.SetItemToolTip(self.materialList[slot])

	def OverOutItem(self):
		if self.toolTipMaterial:
			self.toolTipMaterial.HideToolTip()

	def __OnSelectEmptySlot(self, selectedSlotPos):
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()
			mouseModule.mouseController.DeattachObject()
			if player.SLOT_TYPE_INVENTORY != attachedSlotType:
				return
			if IS_UPGRADE_ITEM(player.GetItemIndex(attachedSlotPos)):
				item.SelectItem(self.vnum)
				if item.GetItemType() == item.ITEM_TYPE_METIN:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.REFINE_ERROR_ADD_PERC_STONES)
					return
				if attachedItemCount > 1 or attachedItemCount <= 0:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.REFINE_ERROR_ITEM_COUNT)
					return
				for it in xrange(3):
					if selectedSlotPos == it and attachedItemIndex != REFINE_VNUM[it]:
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.REFINE_ERROR_ITEM_VNUM)
						return
				for it in xrange(3):
					if selectedSlotPos == it:
						if self.percentage + REFINE_TOTAL_PERCENTAGE["update"] + REFINE_PERCENTAGE[it] > 100:
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.REFINE_ERROR_ITEM_OVERFLOW_PERCENTAGE)
							return
						REFINE_MODE[it] = 1
						REFINE_TOTAL_PERCENTAGE["update"] += REFINE_PERCENTAGE[it]
				self.slot.ClearSlot(selectedSlotPos)
				self.slot.SetItemSlot(selectedSlotPos, player.GetItemIndex(attachedSlotPos), player.GetItemCount(attachedSlotPos))
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeinfo.REFINE_ERROR_ITEM_VNUM)

	def __OnSelectItemSlot(self, selectedSlotPos):
		for it in xrange(3):
			if selectedSlotPos == it:
				self.slot.ClearSlot(selectedSlotPos)
				REFINE_MODE[it] = 0
				REFINE_TOTAL_PERCENTAGE["update"] -= REFINE_PERCENTAGE[it]

	def __OnOverInItem(self, slotIndex):
		for it in xrange(3):
			if slotIndex == it:
				self.tooltipMode.SetItemToolTip(REFINE_VNUM[it])

	def __OnOverOutItem(self):
		if self.tooltipMode:
			self.tooltipMode.HideToolTip()
			