#Lorderon Client Dev by Lordbecvold
import ui
import app
import net
import chat
import localeInfo
import player
import uiCommon

class MarbleShopWindow(ui.ScriptWindow):
	MARBLES_LIST = (
			("Divoký Pìšák ", 501, 5000000),
			("Divoký poddaný ", 502, 5000000),
			("Silný divoký pìšák ", 551, 5000000),
			("Silný divoký poddaný ", 552, 5000000),
			("Silný divoký General ", 554, 5000000),
		)


	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = 0
		self.price = 0
		self.alertDialog = None
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Show(self):
		self.__LoadWindow()
		ui.ScriptWindow.Show(self)
		
	def __LoadWindow(self):
		if self.isLoaded == 1:
			return		
		self.isLoaded = 1
		try:
			pyScrLoader = ui.PythonScriptLoader()			
			pyScrLoader.LoadScriptFile(self, "UIScript/MarbleShop.py")
		except:
			import exception
			exception.Abort("MarbleShopWindow.LoadWindow.LoadObject")		
		try:
			getObject = self.GetChild
			
			self.titleBar = getObject("TitleBar")
			self.marblesList = getObject("MarblesListBox")
			self.buyButton = getObject("BuyButton")
			self.marbleCount = getObject("MarbleCount")
			self.resumeMarbleName = getObject("ResumeMarbleName")
			self.resumeMarbleCount = getObject("ResumeMarbleCount")
			self.CNT_Minus = getObject("CNT_Minus")
			self.CNT_Plus = getObject("CNT_Plus")
			self.resumeMarbleGold = getObject("ResumeMarbleGold")			
		except:
			import exception
			exception.Abort("MarbleShopWindow.LoadWindow.BindObject")		
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.buyButton.SetEvent(ui.__mem_func__(self.OnPressBuyButton))
		self.CNT_Minus.SetEvent(ui.__mem_func__(self.OnPressMinusButton))
		self.CNT_Plus.SetEvent(ui.__mem_func__(self.OnPressPlusButton))		
		for marble in self.MARBLES_LIST:
			self.marblesList.AppendItem(Item(marble[0]))			
		self.marblesList.SelectIndex(0)
		
	def OnUpdate(self):
		marbleName = self.marblesList.GetSelectedItem().GetText()
		marbleCount = self.marbleCount.GetText()
		if marbleName != "":
			self.resumeMarbleName.SetText(str(marbleName))
		if int(marbleCount) > 0:
			self.resumeMarbleCount.SetText(str(marbleCount))		
		for marble in xrange(len(self.MARBLES_LIST)):
			if self.marblesList.GetSelectedItem().GetText() == self.MARBLES_LIST[marble][0]:
				self.resumeMarbleGold.SetText(str(localeInfo.NumberToMoneyString(self.MARBLES_LIST[marble][2]*int(marbleCount))))
				self.price = self.MARBLES_LIST[marble][2]*int(marbleCount)
		
	def OnPressPlusButton(self):
		marbleCount = int(self.marbleCount.GetText())
		if marbleCount == 10:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Maximum kulièek co mùžeš koupit je 10. ")
			return
		self.marbleCount.SetText(str(marbleCount+1))
		
	def OnPressMinusButton(self):
		marbleCount = int(self.marbleCount.GetText())
		if marbleCount == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Minimum kulièek co mùžeš koupit 1. ")
			return
		self.marbleCount.SetText(str(marbleCount-1))
		
	def OnPressBuyButton(self):
		itemCount = self.marbleCount.GetText()
		marbleIndex = self.marblesList.GetSelectedItem().GetText()		
		alertDialog = uiCommon.QuestionDialog()
		alertDialog.SetWidth(385)
		alertDialog.SetText("Chceš koupit %s %dx for %s?" % (str(marbleIndex), int(itemCount), localeInfo.NumberToMoneyString(self.price)))
		alertDialog.SetAcceptEvent(lambda arg1=str(marbleIndex), arg2=int(itemCount): self.OnBuyMarble(arg1, arg2))
		alertDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseAlertDialog))
		alertDialog.Open()
		self.alertDialog = alertDialog
		
	def OnCloseAlertDialog(self):
		if not self.alertDialog:
			return
		self.alertDialog.Close()
		self.alertDialog = None
	
	def OnBuyMarble(self, marbleIndex, itemCount):
		self.OnCloseAlertDialog()
		if marbleIndex == "":
			return		
		for marble in xrange(len(self.MARBLES_LIST)):
			if marbleIndex == self.MARBLES_LIST[marble][0]:
				itemVnum = self.MARBLES_LIST[marble][1]
				if itemCount > 0:
					net.SendChatPacket("/buy_marble_item %d %d" % (int(itemVnum), itemCount))
					break
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Nemáš vybranou kulièku. ")
					break

	def Destroy(self):
		self.alertDialog = None
		self.ClearDictionary()
		
	def Close(self):
		if self.alertDialog:
			self.OnCloseAlertDialog()
 		self.Hide()
 	
	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
		
class Item(ui.ListBoxEx.Item):
	def __init__(self, text):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=text
		self.textLine=self.__CreateTextLine(text[:50])
	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)
	def GetText(self):
		return self.text
	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 7*len(self.textLine.GetText()) + 4, height)
	def __CreateTextLine(self, text):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)
		textLine.SetText(text)
		textLine.Show()
		return textLine
		