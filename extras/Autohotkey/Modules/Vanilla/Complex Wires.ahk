#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

CompWiresAlways := Array()
CompWiresAlways.Insert(1, {Code: 1010})
CompWiresAlways.Insert(1, {Code: 0000})
CompWiresAlways.Insert(1, {Code: 0010})

CompWiresEven := Array()
CompWiresEven.Insert(1, {Code: 1000})
CompWiresEven.Insert(1, {Code: 0100})
CompWiresEven.Insert(1, {Code: 1100})
CompWiresEven.Insert(1, {Code: 1101})

CompWiresParallel := Array()
CompWiresParallel.Insert(1, {Code: 1110})
CompWiresParallel.Insert(1, {Code: 0101})
CompWiresParallel.Insert(1, {Code: 0111})

CompWiresBatteries := Array()
CompWiresBatteries.Insert(1, {Code: 0011})
CompWiresBatteries.Insert(1, {Code: 1001})
CompWiresBatteries.Insert(1, {Code: 1011})



Gui, Destroy
Gui, New
Gui, Font, s10
Gui, Add, Checkbox, vCWRcolour, Wire has RED colouring.
Gui, Add, Checkbox, vCWBcolour, Wire has BLUE colouring.
Gui, Add, Checkbox, vCWStar, Wire has a ★ symbol.
Gui, Add, Checkbox, vCWLED, LED is on.
Gui, Add, Button, x12 y120 gmodule, Return
Gui, Add, Button, default x+80 y120 gWireCheck, Check
Gui, Show, w200 h150
Return

WireCheck:
Gui, Submit, NoHide
CompWires := CWRcolour CWBcolour CWStar CWLED
Loop % CompWiresAlways.Length() {
	If (CompWires = CompWiresAlways[A_Index].Code) {
		Msgbox, 64, %Title%, Cut the wire!
		Reset()
		Return
	}
}
If (odd = 0) {
	Loop % CompWiresEven.Length() {
		If (CompWires = CompWiresEven[A_Index].Code) {
			Msgbox, 64, %Title%, Cut the wire!
			Reset()
			Return
		}
	}
}
If (parallel = 1) {
	Loop % CompWiresParallel.Length() {
		If (CompWires = CompWiresParallel[A_Index].Code) {
			Msgbox, 64, %Title%, Cut the wire!
			Reset()
			Return
		}
	}
}
If (battery > 1) {
	Loop % CompWiresBatteries.Length() {
		If (CompWires = CompWiresBatteries[A_Index].Code) {
			Msgbox, 64, %Title%, Cut the wire!
			Reset()
			Return
		}
	}
}
Msgbox, 64, %Title%, Do NOT cut the wire!
Reset()
Return

Reset()
{
	GuiControl,, CWRcolour, 0
	GuiControl,, CWBcolour, 0
	GuiControl,, CWStar, 0
	GuiControl,, CWLED, 0
	GuiControl, Focus, CWRcolour
}