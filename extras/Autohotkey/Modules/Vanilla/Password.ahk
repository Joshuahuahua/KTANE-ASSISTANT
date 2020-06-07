#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

PasswordObject := ["ABOUT", "AFTER", "AGAIN", "BELOW", "COULD", "EVERY", "FIRST", "FOUND", "GREAT", "HOUSE", "LARGE", "LEARN", "NEVER", "OTHER", "PLACE", "PLANT", "POINT", "RIGHT", "SMALL", "SOUND", "SPELL", "STILL", "STUDY", "THEIR", "THERE", "THESE", "THING", "THINK", "THREE", "WATER", "WHERE", "WHICH", "WORLD", "WOULD", "WRITE"]

Gui, Destroy
InputBox, Combo1, %Title%, Letters in Combo 1
InputBox, Combo2, %Title%, Letters in Combo 2
InputBox, Combo3, %Title%, Letters in Combo 3
InputBox, Combo4, %Title%, Letters in Combo 4
StringUpper, Combo1, Combo1
StringUpper, Combo2, Combo2
StringUpper, Combo3, Combo3
StringUpper, Combo4, Combo4


Loop % PasswordObject.Length() {
	Word := PasswordObject[A_Index]
	StringMid, Letter1, Word, 1, 1
	StringMid, Letter2, Word, 2, 1
	StringMid, Letter3, Word, 3, 1
	StringMid, Letter4, Word, 4, 1
	If (InStr(Combo1,Letter1) AND InStr(Combo2,Letter2) AND InStr(Combo3,Letter3) AND InStr(Combo4,Letter4)) {
		Msgbox, 64, %Title%, %Word%!
		Break
	}
}

Goto module
Return