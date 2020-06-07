cfStart:
ColourFlash := 
ColourFlash := Array()

InputBox, cfWords, %Title%, Enter first letter of the words shown in sequence.,,,, 0, 0
InputBox, cfColours, %Title%, Enter first letter of the colours shown in sequence.,,,, 0, 0
Clipboard := cfWords " " cfColours ; --------------------------------------------------------------DONT FORGET TO REMOVE--------
If (StrLen(cfWords) != StrLen(cfColours)) {
	MsgBox, 64, %Title%, List lengths don't match!
	goto cfStart
	Return
}

;cfWords :=   "brbrmgmw"
;cfColours := "grymygbw"


StringUpper, cfWords, cfWords
StringUpper, cfColours, cfColours

cfWord := StrSplit(cfWords) ; Split string into array of characters
cfColour := StrSplit(cfColours) ; Split string into array of characters
cfLength := StrLen(cfWords) ; Length
loop % cfLength {
	cfMerge := cfMerge cfWord[A_Index] cfColour[A_Index] ; create combined string of "Word" + "Colour"
	Same := ((cfWord[A_Index] = cfColour[A_Index]) ? (1) : (0)) ; Determine if Word and Colour are the same
	ColourFlash.Insert(A_Index, {Word: cfWord[A_Index], Colour: cfColour[A_Index], Same: Same}) ; Store Word, Colour and Same in array
}

; --------------------------------------------------RED------------------------------------------------------------------

If (ColourFlash[cfLength].Colour = "R") { ;												--If ends in color R--
	StringReplace cfWords, cfWords, G, G, UseErrorLevel ; 								Count word G
	If (ErrorLevel >= 3) ;																If there's at least 3 G words
	{
		occurrence := 0
		loop % cfLength {
			If (InStr(ColourFlash[A_Index].Word, "G") OR InStr(ColourFlash[A_Index].Colour, "G")) {
				occurrence+=1
			}
			If (occurrence = 3) { ;														Press YES 3rd occurrence of G word or colour
				MsgBox, 64, %Title%, Press YES on entry %A_Index%
				goto module
			}
		}
	}
	StringReplace cfColours, cfColours, B, B, UseErrorLevel ; 							Count colour B
	If (ErrorLevel = 1) { ;																If there's exactly 1 B colours
		loop % cfLength {
			If (ColourFlash[A_Index].Word = "M") { ;									Press NO on the word magenta
				MsgBox, 64, %Title%, Press NO on entry %A_Index%
				goto module
			}
		}
	}
	loop % cfLength {
		If (ColourFlash[A_Index].Word = "W" OR ColourFlash[A_Index].Colour = "W") { ;	Otherwise press last white word or colour
			place := A_Index
		}
	}
	MsgBox, 64, %Title%, Press YES on entry %place%
	goto module

; ------------------------------------------------YELLOW-----------------------------------------------------------------

} Else If (ColourFlash[cfLength].Colour = "Y") { ;										--If ends in colour Y-- 
	loop % cfLength {
		If (ColourFlash[A_Index].Word = "B" AND ColourFlash[A_Index].Colour = "G") { ; 	If word blue is green
			place := InStr(cfWords, "G",,,3) ;											Press 3rd G word
			MsgBox, 64, %Title%, Press YES on entry %place%
			goto module
		}
	}
	loop % cfLength {
		If (ColourFlash[A_Index].Word = "W" AND ColourFlash[A_Index].Colour = "W" OR ColourFlash[A_Index].Word = "W" AND ColourFlash[A_Index].Colour = "R") {
			occurrence := 0 ;															If word white is white or red^^^^^^
			loop % cfLength {
				occurrence := ((ColourFlash[A_Index].Same = 0) ? (occurrence+1) : (occurrence))
				If (occurrence = 2) {
					MsgBox, 64, %Title%, Press YES on entry %A_Index%
					goto module
				}
			}
		}
	}
	occurrence := 0
	loop % cfLength {
		If (ColourFlash[A_Index].Word = "M" OR ColourFlash[A_Index].Colour = "M") { ;	count instances of M
			occurrence+=1
		}
	}
	MsgBox, 64, %Title%, Press NO on entry %occurrence% ;								press NO on totals entry
	goto module

; ----------------------------------------------------GREEN-------------------------------------------------------------

} Else If (ColourFlash[cfLength].Colour = "G") { ;										--If ends in colour G--
	loop % cfLength {
		If (ColourFlash[A_Index].Word = ColourFlash[A_Index-1].Word AND ColourFlash[A_Index].Colour != ColourFlash[A_Index-1].Colour) {
			MsgBox, 64, %Title%, Press NO on entry 5
			goto module
		}
	}
	StringReplace cfWords, cfWords, M, M, UseErrorLevel ; 								Count word M
	If (ErrorLevel >= 3) {
		loop % cfLength {
			If (ColourFlash[A_Index].Word = "Y" OR ColourFlash[A_Index].Colour = "Y") {
				MsgBox, 64, %Title%, Press NO on entry %A_Index%
				goto module
			}
		}
	}
	loop % cfLength {
		If (ColourFlash[A_Index].Same = 1) {
			MsgBox, 64, %Title%, Press YES on entry %A_Index%
			goto module
		}
	}

; ------------------------------------------------------BLUE-------------------------------------------------------------

} Else If (ColourFlash[cfLength].Colour = "B") { ;										--If ends in colour B--
	occurrence := 0
	loop % cfLength {
		If (ColourFlash[A_Index].Same = 0) {
			occurrence+=1
		}
		If (occurrence >= 3) {
			loop % cfLength {
				If (ColourFlash[A_Index].Same = 0) {
					MsgBox, 64, %Title%, Press YES on entry %A_Index%
					goto module
				}
			}
		}
	}
	loop % cfLength {
		If (ColourFlash[A_Index].Word = "R" AND ColourFlash[A_Index].Colour = "Y" OR ColourFlash[A_Index].Word = "Y" AND ColourFlash[A_Index].Colour = "W") {
			loop % cfLength {
				If (ColourFlash[A_Index].Word = "W" AND ColourFlash[A_Index].Colour = "R") {
					MsgBox, 64, %Title%, Press NO on entry %A_Index%
					goto module
				}
			}
		}
	}
	loop % cfLength {
		If (ColourFlash[A_Index].Word = "G" OR ColourFlash[A_Index].Colour = "G") { ;	Otherwise press last green word or colour
			place := A_Index
		}
	}
	MsgBox, 64, %Title%, Press YES on entry %place%
	goto module

; ------------------------------------------------MAGENTA----------------------------------------------------------------

} Else If (ColourFlash[cfLength].Colour = "M") { ;										--If ends in colour M--
	loop % cfLength {
		If (ColourFlash[A_Index].Colour = ColourFlash[A_Index-1].Colour AND ColourFlash[A_Index].Word != ColourFlash[A_Index-1].Word) {
			MsgBox, 64, %Title%, Press YES on entry 3 ;									Consecutive colour, different words ^^^
			goto module
		}
	}
	StringReplace cfColours, cfWords, Y, Y, UseErrorLevel
	temp := ErrorLevel
	StringReplace cfColours, cfColours, B, B, UseErrorLevel
	If (temp > ErrorLevel) { ;															word Y > colour B
		loop % cfLength {
			If (ColourFlash[A_Index].Word = "Y") { ;									Press last yellow word
				place := A_Index
			}
		}
		MsgBox, 64, %Title%, Press NO on entry %place%
		goto module
	}
	loop % cfLength {
		If (cfColours[A_Index].Colour = cfColours[7].Word) {
			MsgBox, 64, %Title%, Press NO on entry %A_Index%
			goto module
		}
	} 

; ----------------------------------------------------WHITE--------------------------------------------------------------

} Else If (ColourFlash[cfLength].Colour = "W") { ;										--If ends in colour W--
	If (cfColours[3].Colour = cfColours[4].Word OR cfColours[3].Colour = cfColours[5].Word) {
		loop % cfLength {
			If (cfColours[A_Index].Word = "B" OR cfColours[A_Index].Colour = "B") {
				MsgBox, 64, %Title%, Press NO on entry %A_Index%
				goto module
			}
		}
	}
	loop % cfLength {
		If (cfColours[A_Index].Word = "Y" AND cfColours[A_Index].Colour = "R") {
			loop % cfLength {
				If (ColourFlash[A_Index].Colour = "B") { ;									Press last blue colour
					place := A_Index
				}
			}
			MsgBox, 64, %Title%, Press YES on entry %place%
			goto module
		}
	}
	MsgBox, 64, %Title%, Press NO
	goto module
}
MsgBox, 64, %Title%, No answer found
goto cfStart
Return