#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.



x = 4

msgbox % Ceil(x/2)
ExitApp




Gui, Destroy
Gui, New
Gui, Font, s13
Gui -Resize -MinimizeBox
Gui, Add, Text, x40 y5, Who's On First?
Gui, Add, Edit, x15 y30 w170 vWOFBig Uppercase
Gui, Add, Edit, x15 y70 w80 vWOFTL Uppercase
Gui, Add, Edit, x105 y70 w80 vWOFTR Uppercase
Gui, Add, Edit, x15 y110 w80 vWOFML Uppercase
Gui, Add, Edit, x105 y110 w80 vWOFMR Uppercase
Gui, Add, Edit, x15 y150 w80 vWOFBL Uppercase
Gui, Add, Edit, x105 y150 w80 vWOFBR Uppercase
Gui, Font, s10
Gui, Add, Button, x20 y190 w70 default gButtonWOF, Check
Gui, Add, Button, x110 y190 w70 gmodule, Return
Gui, Show, w200 h230
Return

ButtonWOF:
Gui, Submit, NoHide

Msgbox, %WOFBIG% %WOFTL% %WOFTR% %WOFML% %WOFMR% %WOFBL% %WOFBR%

Compile := WOFBIG "-" WOFTL "-" WOFTR "-" WOFML "-" WOFMR "-" WOFBL "-" WOFBR
msgbox % Compile
Compile := StrReplace(Compile, A_Space, "_")
msgbox % Compile
Compile := StrReplace(Compile, "'", "_")
msgbox % Compile
Decompile := StrSplit(Compile, "-")

loop % Decompile.Length() {
	msgbox % A_Index " " Decompile[A_Index]
}
WOFBIG := Decompile[1]
WOFTL := Decompile[2]
WOFTR := Decompile[3]
WOFML := Decompile[4]
WOFMR := Decompile[5]
WOFBL := Decompile[6]
WOFBR := Decompile[7]

Msgbox, %WOFBIG% %WOFTL% %WOFTR% %WOFML% %WOFMR% %WOFBL% %WOFBR%

module:
ExitApp




Bcolour =
;goto ButtonBlue

result := "UNDEFINED"
num = 2

MsgBox % ((num = 1) ? ("1") : ("not 1"))

MsgBox % ((num = 1) ? ("1") : ( ((num = 2) ? ("2") : ("neither 1 or 2"))))


result := ((num = 1) ? (1) : (0))
msgbox % result





ButtonRed:
Bcolour := ((Bcolour = "") ? ("Red") : (Bcolour))
ButtonBlue:
Bcolour := ((Bcolour = "") ? ("Blue") : (Bcolour))
ButtonGreen:
Bcolour := ((Bcolour = "") ? ("Green") : (Bcolour))
ButtonYellow:
Bcolour := ((Bcolour = "") ? ("Yellow") : (Bcolour))

msgbox % Bcolour
ExitApp

; (() ? () : ())