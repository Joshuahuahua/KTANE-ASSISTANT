#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Knobs := Array()
Knobs.Insert(1, {Number: "0", DirectionW: "Left", DirectionN: 4})
Knobs.Insert(1, {Number: "1", DirectionW: "Left", DirectionN: 4})
Knobs.Insert(1, {Number: "3", DirectionW: "Down", DirectionN: 3})
Knobs.Insert(1, {Number: "4", DirectionW: "Up", DirectionN: 1})
Knobs.Insert(1, {Number: "5", DirectionW: "Down", DirectionN: 3})
Knobs.Insert(1, {Number: "5U", DirectionW: "Right", DirectionN: 2})

Gui, Destroy
Gui, New
Gui -Resize -MinimizeBox
Gui, Font, s15
Gui, Add, Text, x27 y5, --- Knobs ---
Gui, Add, Text, x13 y30, Where is "UP"?
Gui, Add, DropDownList, x30 y60 w100 vUpPosition Choose1, Up|Down|Left|Right
Gui, Add, Text, x7 y100, How many lights`nare lit? (left side)
Gui, Add, Edit, x52 y160 w50 vKlights Limit2
Gui, Add, Button, default x48 y220 gKnob, Done
Gui, Show, w160 h270
Return

Knob:
Gui, Submit
Gui, Destroy
Loop % Knobs.Length() {
	If (UpPosition = Knobs[A_Index].DirectionW) { ;		Converts UpPosition into a number
		UpPosition := Knobs[A_Index].DirectionN - 1
	}
}
Loop % Knobs.Length() {
	If (Klights = Knobs[A_Index].Number) { ;			Determines the direction of knob (number)
		Direction := Knobs[A_Index].DirectionN
	}
}
Direction := Direction + UpPosition ;					Adds UpPosition to Knob dirction
If (Direction > 4) { ;									Wraps value
	Direction-=4
}
Loop % Knobs.Length() {
	If (Direction = Knobs[A_Index].DirectionN) { ;			Converts Direction into a string
		Direction := Knobs[A_Index].DirectionW
	}
}
Msgbox Make the knob face %Direction%
goto module
Return




/*

0 or 1 LEFT
3 DOWN
4 UP
5 in a U shape, meaning the blue​ ​is unlit RIGHT
5 but not in a U shape DOWN