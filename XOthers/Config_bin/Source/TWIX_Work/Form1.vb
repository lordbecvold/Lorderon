Imports System
Imports System.Runtime
Imports System.Runtime.InteropServices
Imports System.Management
Imports System.Resources
Imports System.IO
Public Class Form1
    Dim reso_string As String = ""
    Dim v1 As Integer
    Dim v2 As Integer
    Dim v3 As Integer
    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        Application.Exit()
    End Sub

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        v1 = 0
        v2 = 0
        v3 = 0
        Dim cd As New ClassDisplay(Screen.PrimaryScreen.DeviceName)
        For i As Integer = 0 To cd.ScreenResolutions.Count - 1
            resolution.Items.Add(cd.ScreenResolutions(i).Total)
        Next
        If File.Exists("config.cfg") Then
            For Each line1 In File.ReadAllLines("config.cfg")
                If line1.StartsWith("WIDTH") Then
                    For i As Integer = 0 To cd.ScreenWidth.Count - 1
                        If line1.EndsWith(cd.ScreenWidth(i).Total) Then
                            reso_string = cd.ScreenWidth(i).Total
                        End If
                    Next
                End If
                If line1.StartsWith("HEIGHT") Then
                    For i As Integer = 0 To cd.ScreenHeight.Count - 1
                        If line1.EndsWith(cd.ScreenHeight(i).Total) Then
                            If reso_string.Contains("x") Then
                            Else
                                reso_string = reso_string & "x" & cd.ScreenHeight(i).Total
                            End If
                        End If
                    Next
                End If
                If line1.StartsWith("BPP") Then
                    For Each a In "32|16".Split("|")
                        If line1.EndsWith(a) Then
                            reso_string = reso_string & " " & a & "bpp"
                        End If
                    Next
                    For item As Integer = 0 To resolution.Items.Count - 1

                        If resolution.Items(item).Contains(reso_string) Then

                            resolution.SelectedIndex = item
                        End If
                    Next
                End If
                If line1.StartsWith("MUSIC_VOLUME") Then
                    Dim x1 = line1.ToCharArray
                    music.Value = x1(x1.Length - 1).ToString
                End If
                If line1.StartsWith("VOICE_VOLUME") Then
                    Dim x1 = line1.ToCharArray
                    sfx.Value = x1(x1.Length - 1).ToString
                End If
                If line1.StartsWith("WINDOWED") Then
                    If line1.EndsWith("1") Then
                        windowed_1(True)
                    Else
                        windowed_1(False)
                    End If
                End If
            Next

        End If

    End Sub
    Public Sub windowed_1(ByVal yes As Boolean)
        If yes = True Then
            windowed.Checked = True
            fullscreen.Checked = False
        Else
            windowed.Checked = False
            fullscreen.Checked = True
        End If
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim s As StreamWriter = New StreamWriter("config.cfg")
        Dim tab As String = "   "

        If String.IsNullOrEmpty(resolution.Text) Then
            MessageBox.Show("Musíš vše vyplnit!", "Upozornění")
            s.Close()
        Else
            s.WriteLine("WIDTH" & tab & resolution.SelectedItem.ToString.Split("x")(0))
            'MessageBox.Show(resolution.SelectedItem.ToString.Split("x")(0))
            s.WriteLine("HEIGHT" & tab & resolution.SelectedItem.ToString.Split("x")(1).Split(" ")(0))
            s.WriteLine("BPP" & tab & resolution.SelectedItem.ToString.Split("x")(1).Split(" ")(1).Split("b")(0))
            s.WriteLine("FREQUENCY" & tab & "60")
            s.WriteLine("SOFTWARE_CURSOR		0")
            s.WriteLine("VISIBILITY" & tab & "1" + 1)
            s.WriteLine("SOFTWARE_TILING" & tab & "0")
            s.WriteLine("SHADOW_LEVEL" & tab & "5")
            s.WriteLine("MUSIC_VOLUME" & tab & music.Value)
            s.WriteLine("VOICE_VOLUME" & tab & sfx.Value)
            s.WriteLine("GAMMA" & tab & "3")
            s.WriteLine("USE_DEFAULT_IME" & tab & "0")
            If windowed.Checked = True Then
                s.WriteLine("WINDOWED" & tab & "1")
            Else
                s.WriteLine("WINDOWED" & tab & "0")
            End If
            s.Close()
            Application.Exit()
        End If
    End Sub

    Private Sub windowed_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles windowed.CheckedChanged
        If v1 = 0 Then
            v1 = 1
        Else
            If windowed.Checked = True Then
                MessageBox.Show("Toto nastavení může zpomalit hru.")
            End If
        End If


    End Sub

    Private Sub externalime_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs)
    End Sub

    Private Sub tnl_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs)

    End Sub


    Private Sub shadow_SelectedIndexChanged(sender As Object, e As EventArgs)

    End Sub

    Private Sub sfx_Scroll(sender As Object, e As ScrollEventArgs) Handles sfx.Scroll

    End Sub

    Private Sub GroupBox2_Enter(sender As Object, e As EventArgs) Handles GroupBox2.Enter

    End Sub

    Private Sub music_Scroll(sender As Object, e As ScrollEventArgs) Handles music.Scroll

    End Sub
End Class
Class ClassDisplay

    <StructLayout(LayoutKind.Sequential)> _
    Public Structure DEVMODE
        <MarshalAs(UnmanagedType.ByValTStr, SizeConst:=32)> _
        Public dmDeviceName As String
        Public dmSpecVersion As Short
        Public dmDriverVersion As Short
        Public dmSize As Short
        Public dmDriverExtra As Short
        Public dmFields As Integer

        Public dmOrientation As Short
        Public dmPaperSize As Short
        Public dmPaperLength As Short
        Public dmPaperWidth As Short

        Public dmScale As Short
        Public dmCopies As Short
        Public dmDefaultSource As Short
        Public dmPrintQuality As Short
        Public dmColor As Short
        Public dmDuplex As Short
        Public dmYResolution As Short
        Public dmTTOption As Short
        Public dmCollate As Short
        <MarshalAs(UnmanagedType.ByValTStr, SizeConst:=32)> _
        Public dmFormName As String
        Public dmLogPixels As Short
        Public dmBitsPerPel As Short
        Public dmPelsWidth As Integer
        Public dmPelsHeight As Integer

        Public dmDisplayFlags As Integer
        Public dmDisplayFrequency As Integer

        Public dmICMMethod As Integer
        Public dmICMIntent As Integer
        Public dmMediaType As Integer
        Public dmDitherType As Integer
        Public dmReserved1 As Integer
        Public dmReserved2 As Integer

        Public dmPanningWidth As Integer
        Public dmPanningHeight As Integer
    End Structure

    Private Declare Function EnumDisplaySettings Lib "user32.dll" _
      Alias "EnumDisplaySettingsA" ( _
      ByVal deviceName As String, _
      ByVal modeNum As Integer, _
      ByRef devMode As DEVMODE) As Integer

    Private Declare Function ChangeDisplaySettingsEx Lib "user32.dll" _
      Alias "ChangeDisplaySettingsExA" ( _
      ByVal lpszDeviceName As String, _
      ByRef lpDevMode As DEVMODE, _
      ByVal hwnd As Int32, _
      ByVal dwflags As Int32, _
      ByVal lParam As Int32) As Int32

    ' Struktur, die die Bildschirmauflösung beschreibt
    Public Structure ScreenResolution
        Public Resolution As Size
        Public ColorDeptI As Integer
        Public ColorDeptS As String
        Public Total As String
    End Structure

    Private ScreenRes As New List(Of ScreenResolution)
    Private Screenw As New List(Of ScreenResolution)
    Private Screenh As New List(Of ScreenResolution)
    Private deviceName As String

    ' dies kann ab .NET 2 einfacher mit 
    ' Screen.PrimaryScreen.Bounds abfegragt werden 
    Private Const ENUM_CURRENT_SETTINGS As Integer = -1

    ' entgültige Umstellung der Auflösung
    Private Const CDS_UPDATEREGISTRY As Integer = 1

    ' Umstellung der Auflösung testen
    Private Const CDS_TEST As Integer = 2

    Private Const DISP_CHANGE_SUCCESSFUL As Integer = 0
    Private Const DISP_CHANGE_RESTART As Integer = 1
    Private Const DISP_CHANGE_FAILED As Integer = -1

    Private Const DM_BITSPERPEL = &H40000
    Private Const DM_PELSWIDTH = &H80000
    Private Const DM_PELSHEIGHT = &H100000
    Private Const DM_DISPLAYFREQUENCY = &H400000

    ''' <summary>Sub New der ClassDisplay</summary>
    ''' <param name="devName">DeviceName des gewählten Bildschirmes.</param>
    Public Sub New(ByVal devName As String)
        deviceName = devName
        Dim dm As New DEVMODE()
        dm.dmDeviceName = New String(New Char(31) {})
        dm.dmFormName = New String(New Char(31) {})
        dm.dmSize = CShort(Marshal.SizeOf(dm))

        Dim counter As Integer = 0
        Do
            ' Durch Hochzählen des Counter werden alle Auflösungen ermittelt, 
            ' bis 0 zurückgegeben wird.
            ' Wenn counter als -1 (ENUM_CURRENT_SETTINGS) übergeben wird, 
            ' wird die aktuelle Auflösung ermittelt
            If EnumDisplaySettings(deviceName, counter, dm) <> 0 Then
                ' Farbtiefe
                Dim Colors As String
                Select Case dm.dmBitsPerPel
                    Case 4
                        Colors = "16 Farben"
                    Case 8
                        Colors = "256 Farben"
                    Case 16
                        Colors = "16bpp"
                        Dim sr As New ScreenResolution
                        sr.ColorDeptI = dm.dmBitsPerPel
                        sr.ColorDeptS = Colors
                        sr.Resolution = New Size(dm.dmPelsWidth, dm.dmPelsHeight)
                        sr.Total = dm.dmPelsWidth & "x" & dm.dmPelsHeight & " " & Colors
                        Dim sr1 As New ScreenResolution
                        sr1.ColorDeptI = dm.dmBitsPerPel
                        sr1.ColorDeptS = Colors
                        sr1.Resolution = New Size(dm.dmPelsWidth, dm.dmPelsHeight)
                        sr1.Total = dm.dmPelsWidth
                        Dim sr2 As New ScreenResolution
                        sr2.ColorDeptI = dm.dmBitsPerPel
                        sr2.ColorDeptS = Colors
                        sr2.Resolution = New Size(dm.dmPelsWidth, dm.dmPelsHeight)
                        sr2.Total = dm.dmPelsHeight
                        If ScreenRes.Contains(sr) = False Then
                            If dm.dmPelsWidth >= 800 Then
                                ScreenRes.Add(sr)
                                Screenw.Add(sr1)
                                Screenh.Add(sr2)
                            End If

                        End If

                        sr = Nothing
                    Case 24
                        Colors = "24-Bit"
                    Case 32
                        Colors = "32bpp"
                        Dim sr As New ScreenResolution
                        sr.ColorDeptI = dm.dmBitsPerPel
                        sr.ColorDeptS = Colors
                        sr.Resolution = New Size(dm.dmPelsWidth, dm.dmPelsHeight)
                        sr.Total = dm.dmPelsWidth & "x" & dm.dmPelsHeight & " " & Colors
                        Dim sr1 As New ScreenResolution
                        sr1.ColorDeptI = dm.dmBitsPerPel
                        sr1.ColorDeptS = Colors
                        sr1.Resolution = New Size(dm.dmPelsWidth, dm.dmPelsHeight)
                        sr1.Total = dm.dmPelsWidth
                        Dim sr2 As New ScreenResolution
                        sr2.ColorDeptI = dm.dmBitsPerPel
                        sr2.ColorDeptS = Colors
                        sr2.Resolution = New Size(dm.dmPelsWidth, dm.dmPelsHeight)
                        sr2.Total = dm.dmPelsHeight
                        If ScreenRes.Contains(sr) = False Then
                            If dm.dmPelsWidth >= 800 Then
                                ScreenRes.Add(sr)
                                Screenw.Add(sr1)
                                Screenh.Add(sr2)
                            End If

                        End If
                        sr = Nothing
                    Case Else
                        Colors = "Barvy nenalezeny!"
                End Select
                counter += 1
            Else
                Exit Do
            End If
        Loop
    End Sub

#Region "Public Functions/Subs"
    ''' <summary>Stellt die Bildschrimauflösung um.</summary>
    ''' <param name="res">Neue Auflösung als Size</param>
    ''' <param name="colorDept">Neue Farbtiefe als Integer</param>
    ''' <returns>True wenn die Umstellung erfolgreich war sonst False</returns>
    Public Function ChangeRes(ByVal res As Size, ByVal colorDept As Integer) As Boolean

        ' Struktur für die Übergabe vorbereiten
        Dim dm As New DEVMODE
        dm.dmFields = DM_PELSWIDTH Or DM_PELSHEIGHT Or _
          DM_BITSPERPEL Or DM_DISPLAYFREQUENCY
        dm.dmPelsHeight = res.Height
        dm.dmPelsWidth = res.Width
        dm.dmBitsPerPel = colorDept
        dm.dmDeviceName = New String(New Char(31) {})
        dm.dmFormName = New String(New Char(31) {})
        dm.dmSize = CShort(Marshal.SizeOf(dm))

        ' Auflösung umstellen
        Dim ret As Integer = ChangeDisplaySettingsEx(deviceName, dm, _
          0&, CDS_UPDATEREGISTRY, 0&)
        Select Case ret
            Case DISP_CHANGE_FAILED
                MessageBox.Show("Die Auflösung konnte nicht verändert werden !!!")
                Return False
            Case DISP_CHANGE_SUCCESSFUL
                Return True
            Case DISP_CHANGE_RESTART
                MessageBox.Show("Zur Umstellung der Auflösung muss " & _
                  "das System neu gebootet werden.")
                Return True
            Case Else
                Return False
        End Select
        dm = Nothing
        Return True
    End Function
#End Region

#Region "Properties"

    Public ReadOnly Property ScreenResolutions() As List(Of ScreenResolution)
        Get
            Return ScreenRes
        End Get
    End Property
    Public ReadOnly Property ScreenWidth() As List(Of ScreenResolution)
        Get
            Return Screenw
        End Get
    End Property
    Public ReadOnly Property ScreenHeight() As List(Of ScreenResolution)
        Get
            Return Screenh
        End Get
    End Property
#End Region

End Class
