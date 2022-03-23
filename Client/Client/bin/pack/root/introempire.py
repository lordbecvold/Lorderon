#Lorderon Client Dev by Lordbecvold
import ui
import net
import wndMgr
import dbg
import app
import event
import _weakref
import uiScriptLocale

LOCALE_PATH = "uiscript/"+uiScriptLocale.CODEPAGE+"_"

class SelectEmpireWindow(ui.ScriptWindow):
	class EmpireButton(ui.Window):

		def __init__(self, owner, arg):
			ui.Window.__init__(self)
			self.owner = owner
			self.arg = arg

		def OnMouseOverIn(self):
			self.owner.OnOverInEmpire(self.arg)

		def OnMouseOverOut(self):
			self.owner.OnOverOutEmpire(self.arg)

		def OnMouseLeftButtonDown(self):
			self.owner.OnSelectEmpire(self.arg)

	def __init__(self, stream):
		print "NEW EMPIRE WINDOW  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_EMPIRE, self)
		self.stream=stream
		self.descIndex=0
		self.empireArea = {}
		self.empireAreaButton = {}

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_EMPIRE, 0)
		print "---------------------------------------------------------------------------- DELETE EMPIRE WINDOW"

	def Close(self):
		print "---------------------------------------------------------------------------- CLOSE EMPIRE WINDOW"		
		self.ClearDictionary()
		self.exitButton = None
		self.empireArea = None
		self.empireAreaButton = None
		self.KillFocus()
		self.Hide()
		app.HideCursor()
		event.Destroy()

	def Open(self):
		print "OPEN EMPIRE WINDOW ----------------------------------------------------------------------------"
		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("SelectEmpireWindow")
		self.Show()	
		if not self.__LoadScript("twix_work/selectempirewindow/selectempirewindow.py"):
			dbg.TraceError("SelectEmpireWindow.Open - __LoadScript Error")
			return
		self.__CreateButtons()
		app.ShowCursor()

	def __CreateButtons(self):
		for key, img in self.empireArea.items():
			(x, y) = img.GetGlobalPosition()
			btn = self.EmpireButton(_weakref.proxy(self), key)
			btn.SetParent(self)
			btn.SetPosition(x, y)
			btn.SetSize(img.GetWidth(), img.GetHeight())
			btn.Show()
			self.empireAreaButton[key] = btn

	def OnOverInEmpire(self, arg):
		if arg == 1:
			self.ascalon.LoadImage('twix_work/selectempirewindow/mildos_1.tga')
		else:
			self.mildos.LoadImage('twix_work/selectempirewindow/ascalon_1.tga')
			
	def OnOverOutEmpire(self, arg):
		if arg == 1:
			self.ascalon.LoadImage('twix_work/selectempirewindow/mildos_0.tga')
		else:
			self.mildos.LoadImage('twix_work/selectempirewindow/ascalon_0.tga')
			
	def OnSelectEmpire(self, arg):
		arg1 = arg
		if arg1 == 2:
			arg1 = 2
		self.empireID = arg1
		net.SendSelectEmpirePacket(self.empireID)
		self.stream.SetCreateCharacterPhase()

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)	
		except:
			import exception
			exception.Abort("SelectEmpireWindow.__LoadScript.LoadObject")
		try:
			GetObject=self.GetChild
			self.exitButton = self.GetChild("exit_button")
			self.ascalon = GetObject("Ascalon")
			self.mildos = GetObject("Mildos")
			self.empireArea[1] = self.ascalon
			self.empireArea[2] = self.mildos
		except:
			import exception
			exception.Abort("SelectEmpireWindow.__LoadScript.BindObject")		
		self.exitButton.SetEvent(ui.__mem_func__(self.ClickExitButton))			
		return 1
		
	def ClickExitButton(self):
		self.stream.SetLoginPhase()		

	def OnUpdate(self):
		pass

	def OnPressEscapeKey(self):
		self.ClickExitButton()
		return TRUE
		
	def OnPressExitKey(self):
		self.ClickExitButton()
		return TRUE

class ReselectEmpireWindow(SelectEmpireWindow):
	def ClickSelectButton(self):
		net.SendSelectEmpirePacket(self.empireID)
		self.stream.SetCreateCharacterPhase()

	def ClickExitButton(self):
		self.stream.SetSelectCharacterPhase()
