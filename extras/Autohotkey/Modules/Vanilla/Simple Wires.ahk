#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Gui, Destroy
Gui, New
Gui, Add, Text, x5 y5, Wire 1:
Gui, Add, Edit, x5 y20 w70 r1 vwire1
Gui, Add, Text, x5 y50, Wire 2:
Gui, Add, Edit, x5 y65 w70 r1 vwire2
Gui, Add, Text, x5 y95, Wire 3:
Gui, Add, Edit, x5 y110 w70 r1 vwire3
Gui, Add, Text, x5 y140, Wire 4:
Gui, Add, Edit, x5 y155 w70 r1 vwire4
Gui, Add, Text, x5 y185, Wire 5:
Gui, Add, Edit, x5 y200 w70 r1 vwire5
Gui, Add, Text, x5 y230, Wire 6:
Gui, Add, Edit, x5 y245 w70 r1 vwire6
Gui, Add, Button, default x5 y275 w70 gCheckWires, Ok	; xm puts it at the bottom left corner.
Gui, Show, w150 h300
Return

CheckWires:
Gui, Submit
Gui, Destroy

red := 0
yellow := 0
black := 0
blue := 0
white := 0
wireTotal := 0
Wires := 0

Wires := Array()
Wires.Insert(1, {Colour: wire6, WireNum: 6})
Wires.Insert(1, {Colour: wire5, WireNum: 5})
Wires.Insert(1, {Colour: wire4, WireNum: 4})
Wires.Insert(1, {Colour: wire3, WireNum: 3})
Wires.Insert(1, {Colour: wire2, WireNum: 2})
Wires.Insert(1, {Colour: wire1, WireNum: 1})

Loop % Wires.Length() {
	If (Wires[A_Index].Colour = "red") {
		red+=1
	}
	If (Wires[A_Index].Colour = "yellow") {
		yellow+=1
	}
	If (Wires[A_Index].Colour = "black") {
		black+=1
	}
	If (Wires[A_Index].Colour = "blue") {
		blue+=1
	}
	If (Wires[A_Index].Colour = "white") {
		white+=1
	}
	If !(Wires[A_Index].Colour = "") {
		wireTotal+=1
	}
}

If (wireTotal < 3) {
	Msgbox, 64, %Title%, You must have at least 3 wires!
	goto CheckWires
}
If (wireTotal = 3)
{
	if (red = 0) {
		Msgbox, 64, %Title%, Cut the second wire!
	}
	else if (wire3 = "white") {
		Msgbox, 64, %Title%, Cut the last wire!
	}
	else if (blue > 1) {
		Msgbox, 64, %Title%, Cut the last blue wire!
	}
	else {
		Msgbox, 64, %Title%, Cut the last wire!
	}
}
If (wireTotal = 4) {
	if (red > 1 AND odd = 1) {
		Msgbox, 64, %Title%, Cut the last RED wire!
	}
	else if (wire4 = "yellow" AND red = 0 OR blue = 1) {
		Msgbox, 64, %Title%, Cut the first wire!
	}
	else if (yellow > 1) {
		Msgbox, 64, %Title%, Cut the last wire!
	}
	else {
		Msgbox, 64, %Title%, Cut the second wire!
	}
}
If (wireTotal = 5) {
	if (wire5 = "black" AND odd = 1) {
		Msgbox, 64, %Title%, Cut the fourth wire!
	}
	else if (red = 1 AND yellow > 1) {
		Msgbox, 64, %Title%, Cut the first wire!
	}
	else if (black = 0) {
		Msgbox, 64, %Title%, Cut the second wire!
	}
	else {
		Msgbox, 64, %Title%, Cut the first wire!
	}
}
If (wireTotal = 6) {
	if (yellow = 0 AND odd = 1) {
		Msgbox, 64, %Title%, Cut the third wire!
	}
	else if (yellow = 1 AND white > 1) {
		Msgbox, 64, %Title%, Cut the fourth wire!
	}
	else if (red = 0) {
		Msgbox, 64, %Title%, Cut the last wire!
	}
	else {
		Msgbox, 64, %Title%, Cut the fourth wire!
	}
}
goto module
Return