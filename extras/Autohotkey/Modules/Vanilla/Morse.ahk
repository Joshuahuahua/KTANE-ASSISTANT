#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

MorseDictionary := Array()
MorseDictionary.Insert(1, {Code: "LSSS S ", Word: "BEATS", Frequency: "3.600MHz"})
MorseDictionary.Insert(1, {Code: "LSSS SS ", Word: "BISTRO", Frequency: "3.552MHz"})
MorseDictionary.Insert(1, {Code: "LSSS LLL LL ", Word: "BOMBS", Frequency: "3.565MHz"})
MorseDictionary.Insert(1, {Code: "LSSS LLL LSSL ", Word: "BOXES", Frequency: "3.535MHz"})
MorseDictionary.Insert(1, {Code: "LSSS SLS S ", Word: "BREAK", Frequency: "3.572MHz"})
MorseDictionary.Insert(1, {Code: "LSSS SLS SS ", Word: "BRICK", Frequency: "3.575MHz"})
MorseDictionary.Insert(1, {Code: "SSLS ", Word: "FLICK", Frequency: "3.555MHz"})
MorseDictionary.Insert(1, {Code: "SSSS ", Word: "HALLS", Frequency: "3.515MHz"})
MorseDictionary.Insert(1, {Code: "SLSS ", Word: "LEAKS", Frequency: "3.542MHz"})
MorseDictionary.Insert(1, {Code: "SSS SSSS ", Word: "SHELL", Frequency: "3.505MHz"})
MorseDictionary.Insert(1, {Code: "SSS SLSS ", Word: "SLICK", Frequency: "3.522MHz"})
MorseDictionary.Insert(1, {Code: "SSS L S ", Word: "STEAK", Frequency: "3.582MHz"})
MorseDictionary.Insert(1, {Code: "SSS L SS ", Word: "STING", Frequency: "3.592MHz"})
MorseDictionary.Insert(1, {Code: "SSS L SLS ", Word: "STROBE", Frequency: "3.545MHz"})
MorseDictionary.Insert(1, {Code: "L ", Word: "TRICK", Frequency: "3.532MHz"})
MorseDictionary.Insert(1, {Code: "SSSL ", Word: "VECTOR", Frequency: "3.595MHz"})



Gui, Destroy

Gui, New
Gui, Font, s15
Gui, Add, Text,,
(

Use "S" and "L" for SHORT `( • `) and LONG `( - `) beeps.
Use "Space" for pauses.
Start after the long pause.
)
Gui, Add, Edit, gCheck vMorse
Gui, Add, Button, default xm gmodule, Ok	; xm puts it at the bottom left corner.
Gui, Show, w510
Return

Check:
{
	Gui, Submit, NoHide
	Loop % MorseDictionary.Length() {
		If (Morse = MorseDictionary[A_Index].Code) {
			Word := MorseDictionary[A_Index].Word
			Frequency := MorseDictionary[A_Index].Frequency
			Msgbox, 64, %Title%, The word is: %Word%`nThe frequency is: %Frequency%
			goto module
		}
	}
}
Return