#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

global odd := odd, holder := holder, rca := rca, LITIndicator := LITIndicator, battery := battery, SerialNumber := SerialNumber

odd := 0
holder := 2
rca := 0
LITIndicator := 0
battery := 0
SerialNumber := 0

PianoKeys := Array()
PianoKeys.Insert({Condition: "", Symbols: "Flat", Required: "Even", Sequence: "Bb Bb Bb Bb Gb Ab Bb Ab Bb"})
PianoKeys.Insert({Condition: "OR", Symbols: "Common Time, Sharp", Required: "H2", Sequence: "Eb Eb D D Eb Eb D Eb Eb D D Eb"})
PianoKeys.Insert({Condition: "AND", Symbols: "Natural, Fermata", Required: "", Sequence: "E F# F# F# E E E"})
PianoKeys.Insert({Condition: "OR", Symbols: "Cut Time, Turn", Required: "RCA", Sequence: "Bb A Bb F Eb Bb A Bb F Eb"})
PianoKeys.Insert({Condition: "", Symbols: "Clef", Required: "SND", Sequence: "E E E C E G G"})
PianoKeys.Insert({Condition: "OR", Symbols: "Trill, Fermata, Common Time", Required: "B3", Sequence: "C# D E F C# D E F Bb A"})
PianoKeys.Insert({Condition: "AND", Symbols: "Flat, Sharp", Required: "", Sequence: "G G C G G C G C"})
PianoKeys.Insert({Condition: "OR", Symbols: "Cut Time, Trill", Required: "S378", Sequence: "A E F G F E D D F A"})
PianoKeys.Insert({Condition: "OR", Symbols: "Natural, Turn, Clef", Required: "", Sequence: "G G G Eb Bb G Eb Bb G"})
PianoKeys.Insert({Condition: "NO", Symbols: "", Required: "", Sequence: "B D A G A B D A"})

InputBox, pkSymbols, %Title%, Please list all symbols shown.
StringUpper, pkSymbols, pkSymbols, T

loop % PianoKeys.Length() {
	Key := A_Index
	If (Pianokeys[A_Index].Condition != "AND") {
		SymbolArray := StrSplit(Pianokeys[A_Index].Symbols, ",", A_Space)
		Loop % SymbolArray.Length() {
			If InStr(pkSymbols, SymbolArray[A_Index]) {
				If (FurtherRequirements(Pianokeys[Key].Required) = True) {
					String := Pianokeys[Key].Sequence
					MsgBox, 64, %Title%, Input the sequence: `n %String%
					ExitApp
				}
			}
		}
	}
	If (Pianokeys[A_Index].Condition = "AND") {
		SymbolArray := StrSplit(Pianokeys[A_Index].Symbols, ",", A_Space)
		msgbox % "1: " SymbolArray[1] " 2: " SymbolArray[2] 
		If InStr(pkSymbols, SymbolArray[1]) AND InStr(pkSymbols, SymbolArray[2]) {
			msgbox yep`, that worked
			msgbox % Pianokeys[A_Index].Required
			test := FurtherRequirements(Pianokeys[A_Index].Required)
			msgbox % test
			If (FurtherRequirements(Pianokeys[A_Index].Required) = True) {
				String := Pianokeys[Key].Sequence
				MsgBox, 64, %Title%, Input the sequence: `n %String%
				ExitApp
			}
		}
	}
}
ExitApp

FurtherRequirements(Required)
{
	If (Required = "") {
		Return True
	} Else If (Required = "Even") {
		answer := ((odd = 0) ? (True) : (False))
		Return answer
	} Else {
		Return False
	}
}

/*

Even
H2
""
RCA
SND
B3
"
S378
"
"




























loop % PianoKeys.Length()
{
	If InStr(pkSymbols, "Flat") {
		msgbox 1
		ExitApp
	} Else If InStr(pkSymbols, "Common Time") OR InStr(pkSymbols, "Sharp") {
		msgbox 2
		ExitApp
	} Else If InStr(pkSymbols, "Natural") AND InStr(pkSymbols, "Fermata") {
		msgbox 3
		ExitApp
	} Else If InStr(pkSymbols, "Half Time") OR InStr(pkSymbols, "Turn") {
		msgbox 4
		ExitApp
	} Else If InStr(pkSymbols, "Clef") {
		msgbox 5
		ExitApp
	} Else If InStr(pkSymbols, "Trill") OR InStr(pkSymbols, "Fermata") OR InStr(pkSymbols, "Common Time") {
		msgbox 6
		ExitApp
	} Else If InStr(pkSymbols, "Flat") AND InStr(pkSymbols, "Sharp") {
		msgbox 7
		ExitApp
	} Else If InStr(pkSymbols, "Half Time") AND InStr(pkSymbols, "Trill") {
		msgbox 8
		ExitApp
	} Else If InStr(pkSymbols, "Natural") OR InStr(pkSymbols, "Turn") OR InStr(pkSymbols, "Clef") {
		msgbox 9
		ExitApp
	} Else {
		msgbox 10
		ExitApp
	}
}
ExitApp
