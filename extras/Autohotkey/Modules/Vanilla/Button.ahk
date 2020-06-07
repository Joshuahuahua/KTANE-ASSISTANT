#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

Gui, Destroy
Inputbox, BColour, %Title%, What colour is the button?
StringLower, BColour, BColour
Inputbox, BWord, %Title%, What word is on the button?
StringLower, BWord, BWord



If (BColour = "red" AND BWord = "hold") OR (BWord = "detonate" AND battery > 1) {
	Msgbox, 64, %Title%, Press then immediatly release the button!
	goto module
	Return
}
If (battery > 2) {
	IfInString, LITIndicator, FRK
	{
		Msgbox, 64, %Title%, Press then immediatly release the button!
		goto module
		Return
	}
}
Msgbox, 64, %Title%, Hold the button down!

Inputbox, stripe, %Title%, What colour is the stripe?
StringLower, stripe, stripe

MsgBox % ((stripe = "blue") ? ("Release when countdown timer has a 4 in any position") : ( ((stripe = "yellow") ? ("Release when countdown timer has a 5 in any position") : ("Release when countdown timer has a 1 in any position"))))
goto module
Return
