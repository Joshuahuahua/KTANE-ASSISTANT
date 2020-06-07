#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

WireSequenceRed := Array()
WireSequenceBlue := Array()
WireSequenceBlack := Array()
CountSequence%WireColour% := 0

WireSequenceRed.Insert(1, {Letter: "B"}) ; Red
WireSequenceRed.Insert(1, {Letter: "AB"})
WireSequenceRed.Insert(1, {Letter: "ABC"})
WireSequenceRed.Insert(1, {Letter: "AC"})
WireSequenceRed.Insert(1, {Letter: "B"})
WireSequenceRed.Insert(1, {Letter: "AC"})
WireSequenceRed.Insert(1, {Letter: "A"})
WireSequenceRed.Insert(1, {Letter: "B"})
WireSequenceRed.Insert(1, {Letter: "C"})

WireSequenceBlue.Insert(1, {Letter: "A"}) ; Blue
WireSequenceBlue.Insert(1, {Letter: "AC"})
WireSequenceBlue.Insert(1, {Letter: "C"})
WireSequenceBlue.Insert(1, {Letter: "BC"})
WireSequenceBlue.Insert(1, {Letter: "B"})
WireSequenceBlue.Insert(1, {Letter: "A"})
WireSequenceBlue.Insert(1, {Letter: "B"})
WireSequenceBlue.Insert(1, {Letter: "AC"})
WireSequenceBlue.Insert(1, {Letter: "B"})

WireSequenceBlack.Insert(1, {Letter: "C"}) ; Black
WireSequenceBlack.Insert(1, {Letter: "C"})
WireSequenceBlack.Insert(1, {Letter: "AB"})
WireSequenceBlack.Insert(1, {Letter: "BC"})
WireSequenceBlack.Insert(1, {Letter: "B"})
WireSequenceBlack.Insert(1, {Letter: "AC"})
WireSequenceBlack.Insert(1, {Letter: "B"})
WireSequenceBlack.Insert(1, {Letter: "AC"})
WireSequenceBlack.Insert(1, {Letter: "ABC"})


Gui, Destroy
Gui, New
Gui -Resize -MinimizeBox
Gui, Add, Text, x5 y5, Wire Sequencing
Gui, Add, Text, x16 y25, Input wires`ntop to bottom
Gui, Add, Text, x5 y63, Colour
Gui, Add, Edit, x40 y60 w50 vWireColour
Gui, Add, Text, x5 y89, Letter
Gui, Add, Edit, x40 y85 w50 vWireLetter
Gui, Add, Button, default x5 y120 gButtonWSCheck, Check
Gui, Add, Button, x50 y120 gmodule, Return
Gui, Show, w95 h145
Return

ButtonWSCheck:
Gui, Submit, NoHide

CountSequence%WireColour%+=1
SequenceValue := WireSequence%WireColour%[CountSequence%WireColour%].Letter
; ToolTip, Red: %CountSequenceRed%`nBlue: %CountSequenceBlue%`nBlack: %CountSequenceBlack%`nCurrent: %WireColour% %WireLetter%`nString: %SequenceValue%, 0, 0
IfInString, SequenceValue, %WireLetter%, {
	Msgbox, 64, %Title%, Cut the wire!
}
Else {
	Msgbox, 64, %Title%, Do NOT cut the wire!
}
GuiControl,, WireColour
GuiControl,, WireLetter
GuiControl, Focus, WireColour
Return
