#Lorderon Client Dev by Lordbecvold
import ui
import player
import skill
import chat
import net
import mouseModule
import wndMgr

SOUL_STONE_VNUM = 50513

class SoulStoneBoard(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.hasStone = FALSE
		self.stoneCell = -1
		self.selectedSkillSlot = -1
		self.skillIndexBySlot = {}
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/SoulStoneBoard.py")
		except:
			import exception
			exception.Abort("SoulStoneBoard.LoadWindow.LoadScript")
		try:
			GetObject=self.GetChild
			self.board = GetObject("board")
			self.stoneSlot = GetObject("stone_slot")
			self.skillSlot = GetObject("skill_slot")
			self.btnSingle = GetObject("button_single")
			self.btnAll = GetObject("button_all")
		except:
			import exception
			exception.Abort("SoulStoneBoard.LoadWindow.BindObject")
		self.board.SetCloseEvent(self.Close)
		self.stoneSlot.SetSelectEmptySlotEvent(self.OnDropStoneSlot)
		self.stoneSlot.SetSelectItemSlotEvent(self.OnDropStoneSlot)
		self.skillSlot.SetUnselectItemSlotEvent(self.OnUseSkillSlot)
		self.skillSlot.SetUseSlotEvent(self.OnUseSkillSlot)
		self.btnSingle.SAFE_SetEvent(self.OnClickSingleButton)
		self.btnAll.SAFE_SetEvent(self.OnClickAllButton)
		self.skillSlot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)

	def Destroy(self):
		self.Close()

	def Open(self, inventorySlotIndex):
		self.stoneCell = inventorySlotIndex
		if not self.IsShow():
			self.selectedSkillSlot = -1
		self.RefreshStoneSlot()
		if self.RefreshSkillSlot() == FALSE:
			return
		else:
			self.OnUseSkillSlot(0)
		self.SetCenterPosition()
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def RefreshSlot(self):
		self.RefreshStoneSlot()

	def RefreshStoneSlot(self):
		itemVnum = player.GetItemIndex(self.stoneCell)
		itemCount = player.GetItemCount(self.stoneCell)
		if itemCount == 1:
			itemCount = 0
		if itemVnum != SOUL_STONE_VNUM:
			self.stoneSlot.ClearSlot(0)
			self.hasStone = FALSE
		else:
			self.stoneSlot.SetItemSlot(0, itemVnum, itemCount)
			self.hasStone = TRUE
		return self.hasStone

	def RefreshSkillSlot(self):
		skillCount = 0
		slot = self.skillSlot
		self.skillIndexBySlot = {}
		indexDict = self.skillIndexBySlot
		foundSelected = FALSE
		for i in xrange(slot.GetSlotCount()):
			skillIndex = player.GetSkillIndex(i + 1)
			slot.ClearSlot(i)
			slot.HideSlotBaseImage(i)
			if skillIndex == 0:
				continue
			skillLevel = player.GetSkillLevel(i + 1)
			skillGrade = player.GetSkillGrade(i + 1)
			if skillGrade != skill.SKILL_GRADE_COUNT - 1:
				continue
			slot.SetSkillSlotNew(skillCount, skillIndex, skillGrade, skillLevel)
			slot.SetSlotCountNew(skillCount, skillGrade, skillLevel)
			slot.ShowSlotBaseImage(skillCount)
			if self.selectedSkillSlot == skillIndex:
				foundSelected = TRUE
				slot.ActivateSlot(skillCount)
			else:
				slot.DeactivateSlot(skillCount)
			indexDict[skillCount] = skillIndex
			skillCount += 1
		if foundSelected == FALSE:
			self.selectedSkillSlot = -1
		if skillCount == 0:
			return FALSE
		slot.SetSize(32 * skillCount + 5 * (skillCount - 1), slot.GetHeight())
		slot.UpdateRect()
		return TRUE

	def RefreshSkill(self):
		if self.RefreshSkillSlot() == FALSE:
			self.Close()

	def OnDropStoneSlot(self, slotIndex):
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()
			if player.SLOT_TYPE_INVENTORY != attachedSlotType:
				return
			if attachedItemIndex != SOUL_STONE_VNUM:
				return
			self.stoneCell = attachedSlotPos
			self.RefreshStoneSlot()
			mouseModule.mouseController.DeattachObject()

	def OnUseSkillSlot(self, slotIndex):
		skillIndex = self.skillIndexBySlot[slotIndex]
		if self.selectedSkillSlot == skillIndex:
			self.selectedSkillSlot = -1
		else:
			self.selectedSkillSlot = skillIndex
		self.RefreshSkillSlot()

	def OnClickSingleButton(self):
		if self.hasStone == FALSE:
			return
		if self.selectedSkillSlot == -1:
			return
		net.SendSoulStoneUsePacket(self.selectedSkillSlot, self.stoneCell, FALSE)

	def OnClickAllButton(self):
		if self.hasStone == FALSE:
			return
		if self.selectedSkillSlot == -1:
			return
		net.SendSoulStoneUsePacket(self.selectedSkillSlot, self.stoneCell, TRUE)
