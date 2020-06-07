#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

tips := true

ColourVowel := Array()
ColourNoVowel := Array()

ColourVowel.Insert(1, {Colour: "Red", NoStrike: "Blue", OneStrike: "Yellow", TwoStrike: "Green"})
ColourVowel.Insert(1, {Colour: "Blue", NoStrike: "Red", OneStrike: "Green", TwoStrike: "Red"})
ColourVowel.Insert(1, {Colour: "Green", NoStrike: "Yellow", OneStrike: "Blue", TwoStrike: "Yellow"})
ColourVowel.Insert(1, {Colour: "Yellow", NoStrike: "Green", OneStrike: "Red", TwoStrike: "Blue"})
ColourNoVowel.Insert(1, {Colour: "Red", NoStrike: "Blue", OneStrike: "Red", TwoStrike: "Yellow"})
ColourNoVowel.Insert(1, {Colour: "Blue", NoStrike: "Yellow", OneStrike: "Blue", TwoStrike: "Green"})
ColourNoVowel.Insert(1, {Colour: "Green", NoStrike: "Green", OneStrike: "Yellow", TwoStrike: "Blue"})
ColourNoVowel.Insert(1, {Colour: "Yellow", NoStrike: "Red", OneStrike: "Green", TwoStrike: "Red"})


Gui, Destroy
If (tips = true) {
	Msgbox, 64, %Title%,
	(
###########
------ TIP ------
###########
If you have NO strikes:

Vowel: Red <--> Blue  |  Green <--> Yellow
No Vowel: Red --> Blue  |  Blue --> Yellow  |  Yellow --> Red  |  Green = Green
	)
}

Gui, New
Gui, Add, Button, x5 y5 w140 h50, Red
Gui, Add, Button, x150 y5 w140 h50, Blue
Gui, Add, Button, x5 y60 w140 h50, Green
Gui, Add, Button, x150 y60 w140 h50, Yellow
Gui, Add, Text, x5, How many countdown strikes are there?:
Gui, Add, Edit
Gui, Add, UpDown, x5 vStrike Range0-2, 0
Gui, Add, Button, default xm gmodule, Done	; xm puts it at the bottom left corner.
Gui, Show, w300 h200
Return

ButtonRed:
Bcolour := ((Bcolour = "") ? ("Red") : (Bcolour))
ButtonBlue:
Bcolour := ((Bcolour = "") ? ("Blue") : (Bcolour))
ButtonGreen:
Bcolour := ((Bcolour = "") ? ("Green") : (Bcolour))
ButtonYellow:
Bcolour := ((Bcolour = "") ? ("Yellow") : (Bcolour))

Gui, Submit, NoHide
If (vowel = 1) {
	Loop % ColourVowel.Length() {
		If (Bcolour = ColourVowel[A_Index].Colour) {
			If (Strike = 0) {
				Msgbox % "Press " ColourVowel[A_Index].NoStrike
			}
			Else If (Strike = 1) {
				Msgbox % "Press " ColourVowel[A_Index].OneStrike
			}
			Else {
				Msgbox % "Press " ColourVowel[A_Index].TwoStrike
			}
		}
	}
} Else {
	Loop % ColourNoVowel.Length() {
		If (Bcolour = ColourNoVowel[A_Index].Colour) {
			If (Strike = 0) {
				Msgbox % "Press " ColourNoVowel[A_Index].NoStrike
			}
			Else If (Strike = 1) {
				Msgbox % "Press " ColourNoVowel[A_Index].OneStrike
			}
			Else {
				Msgbox % "Press " ColourNoVowel[A_Index].TwoStrike
			}
		}
	}
}
Bcolour =
Return