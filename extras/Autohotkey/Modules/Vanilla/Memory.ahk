#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

Global memNum, numBig

Mem1 := ""
Mem2 := ""
Mem3 := ""
Mem4 := ""
Mem5 := ""
MemPos1 := 0 ; Remember selected positions.
MemPos2 := 0
MemPos3 := 0
MemPos4 := 0
MemPos5 := 0
MemVal1 := 0 ; Remember actual values.
MemVal2 := 0
MemVal3 := 0
MemVal4 := 0
MemVal5 := 0

; There are the following methods used to determine the result:
; 1. "position" - press the nth number.
; 2. "literal" - press the actual number given.
; 3. "stage" - press the number in the given stage at the current number's position.

MemoryStage11 := { method: "position", value: 2 }
MemoryStage12 := { method: "position", value: 2 }
MemoryStage13 := { method: "position", value: 3 }
MemoryStage14 := { method: "position", value: 4 }

MemoryStage21 := { method: "literal", value: "4" }
MemoryStage22 := { method: "stage", stage: 1, value: "position" }
MemoryStage23 := { method: "position", value: 1 }
MemoryStage24 := { method: "stage", stage: 1, value: "position" }

MemoryStage31 := { method: "stage", stage: 2, value: "label" }
MemoryStage32 := { method: "stage", stage: 1, value: "label" }
MemoryStage33 := { method: "position", value: 3 }
MemoryStage34 := { method: "literal", value: "4" }

MemoryStage41 := { method: "stage", stage: 1, value: "position" }
MemoryStage42 := { method: "position", value: 1 }
MemoryStage43 := { method: "stage", stage: 2, value: "position" }
MemoryStage44 := { method: "stage", stage: 2, value: "position" }

MemoryStage51 := { method: "stage", stage: 1, value: "label" }
MemoryStage52 := { method: "stage", stage: 2, value: "label" }
MemoryStage53 := { method: "stage", stage: 4, value: "label" }
MemoryStage54 := { method: "stage", stage: 3, value: "label" }

Loop 5 {
	GatherData(A_Index)
}
goto module
Return

GatherData(iStage)
{
	Mem%iStage% := ""

	Gui, Destroy
	Gui, round:New,, Round %iStage%
	Gui -Resize -MinimizeBox
	Gui, round:Add, Text,, Input the big number followed`n    by the 4 smaller numbers.`n            NO SPACES
	Gui, round:Add, Edit, gnumBig vnumBig x25 y70 w20
	Gui, round:Add, Edit, vmemNum x55 y70 w80
	Gui, round:Add, Button, default xm gSubmit1, Ok	; xm puts it at the bottom left corner.
	Gui, round:Show, w158
	WinWait, A
	WinWaitClose
	Return

	Submit1:
	Gui, Submit
	Gui, Destroy
	ProcessStage(iStage)
	Return

}


ProcessStage(iStage)
{
	Local sMethod, sValue, sStage, iValue, iPrevStage, sPrevString
	Mem%iStage% := "" . memNum ; Remember the string of 4 numbers given for this stage.
	sMethod := MemoryStage%iStage%%numBig%.method ; The method used for this number in this stage. Method can be "position", "literal", etc.
	; msgbox % "Stage=" . iStage . ", method=" . sMethod
	
	If (sMethod = "position") {
		iValue := MemoryStage%iStage%%numBig%.value ; position in the string.
		msgbox % "Press " . SubStr(Mem%iStage%, iValue, 1)
		MemPos%iStage% := iValue ; Remember the position.
		MemVal%iStage% := SubStr(Mem%iStage%, iValue, 1) 
	} Else If (sMethod = "literal") {
		sValue := MemoryStage%iStage%%numBig%.value ; actual value to press.
		msgbox % "Press " . sValue
		MemPos%iStage% := InStr(memNum, sValue) ; The position of this literal in the string.
		MemVal%iStage% := sValue
	} Else If (sMethod = "stage") {
		iPrevStage := MemoryStage%iStage%%numBig%.stage ; Stage to refer back to (in MemX).
		sPrevString := Mem%iPrevStage%
		sSubMethod := MemoryStage%iStage%%numBig%.value ; "label" or "position"
		If (sSubMethod = "position") {
			sValue := SubStr(memNum, MemPos%iPrevStage%, 1)
			MemVal%iStage% := sValue
			msgbox % "Press " . sValue
			MemPos%iStage% := InStr(memNum, sValue) ; The position of this value in the string.
		} Else If (sSubMethod = "label") {
			sValue := MemVal%iPrevStage%
			MemVal%iStage% := sValue
			msgbox % "Press " . sValue
			MemPos%iStage% := InStr(memNum, sValue) ; The position of this value in the string.
		}
	}
}

Return

numBig:
send {Tab}
Return