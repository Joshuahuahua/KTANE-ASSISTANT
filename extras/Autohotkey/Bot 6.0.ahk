#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance, force

/* ##################################################################################################
 												PATCH NOTES
   ##################################################################################################

All indevidual modules have been combined into the main script.
Fixed capitals (if, goto, else)
Added the cool "THE CODE" thing

TO DO:
Finish the Maze module
Separate scripts into indevidual files and incorperate them as a #Include
*/

Tooltip ; 888888888888 88        88 88888888888  
Tooltip ;      88      88        88 88           
Tooltip ;      88      88        88 88           
Tooltip ;      88      88aaaaaaaa88 88aaaaa      
Tooltip ;      88      88""""""""88 88"""""      
Tooltip ;      88      88        88 88           
Tooltip ;      88      88        88 88           
Tooltip ;      88      88        88 88888888888  
Tooltip ;                                        
Tooltip ;                                        
Tooltip ;                                                        
Tooltip ;   ,ad8888ba,   ,ad8888ba,   88888888ba,   88888888888  
Tooltip ;  d8"'    `"8b d8"'    `"8b  88      `"8b  88           
Tooltip ; d8'          d8'        `8b 88        `8b 88           
Tooltip ; 88           88          88 88         88 88aaaaa      
Tooltip ; 88           88          88 88         88 88"""""      
Tooltip ; Y8,          Y8,        ,8P 88         8P 88           
Tooltip ;  Y8a.    .a8P Y8a.    .a8P  88      .a8P  88           
Tooltip ;   `"Y8888Y"'   `"Y8888Y"'   88888888Y"'   88888888888 


Title := "KTANE BOT 5.0"
Menu, TRAY, Icon, icon.ico

; ##################################################################################################
; 												SETUP
; ##################################################################################################

Msgbox, 64, %Title%, Greetings`, I'm Josh's %Title%
Msgbox, 68, %Title%, Ready to start?
IfMsgBox, No
{
	ExitApp
}

start:
Gui, New
Gui, Font, s10

Gui, Add, Text,, How many AA (Small) batteries are there?:
Gui, Add, Edit
Gui, Add, UpDown, vAA Range0-10, 0 ;											AA Batteries

Gui, Add, Text,, How many D (Big) batteries are there?:
Gui, Add, Edit
Gui, Add, UpDown, vB Range0-10, 0 ;												B Batteries

Gui, Add, Text,, What do the LIT indicator(s) say?:
Gui, Add, Edit, Uppercase r3 vLITIndicator ;									LIT Indicators

Gui, Add, Text,, What do the NON-LIT indicator(s) say?:
Gui, Add, Edit, Uppercase r3 vNONIndicator ;									NON-LIT Indicators

Gui, Add, Text,, What is the Serial Number?:
Gui, Add, Edit, Uppercase vSerialNumber ;										SERIAL NUMBER

Gui, Add, Checkbox, vdvi, DVI Port? ;											DVI-D PORT
Gui, Add, Checkbox, vparallel, Parallel Port? ;									PARALLEL PORT
Gui, Add, Checkbox, vps2, PS/2 Port? (Keyboard) ;								PS/2 PORT
Gui, Add, Checkbox, vrj45, RJ-45 Port? (Ethernet) ;								RJ-45 PORT
Gui, Add, Checkbox, vserial, Serial Port? (VGA) ;								SERIAL PORT
Gui, Add, Checkbox, vrca, Parallel Port? ;										STEREO RCA PORT

Gui, Add, Button, default x10, OK	; xm puts it at the bottom left corner.
Gui, Show, w300 h600
Return


ButtonOK:
Gui, Submit
Gui, Destroy

odd := (SubStr(SerialNumber, -0) & 1) != 1 ? (0) : (1)
If SerialNumber contains A,E,I,O,U
{ vowel := 0
} else { vowel := 1
}

holder := (AA/2)+B
battery := AA+B
StringReplace, LITIndicator, LITIndicator, `n, , All
StringReplace, NONIndicator, NONIndicator, `n, , All
IndicatorAll := LITIndicator NONIndicator
StringReplace, IndicatorAll, IndicatorAll, `n, , All
StringReplace, IndicatorAll, IndicatorAll, {Space}, , All

;AA %AA%
;B %B%
;Batteries %battery%
;LIT %LITIndicator%
;NON-LIT %NONIndicator%
;Odd %odd%
;Vowel %vowel%
; %dvi%
; %parallel%
; %ps2%
; %rj45%
; %serial%
; %rca%
; (() ? () : ())

; ###############################################################################################################################
module:

InputBox, Selection, %Title%, Please Type Module
Selection := ((Selection = "WOF") ? ("Who's On First") : (Selection))
Selection := StrReplace(Selection, A_Space, "")

if IsLabel(Selection) {
    Goto %Selection%
} Else {
	Msgbox, 64, %Title%, No module found.
	goto module
}
Return
Quit:
ExitApp
; ##########################################       VANILLA     ##################################################################
Button:
#Include, Modules/Vanilla/Button.ahk ;			WORKING
Wires:
#Include, Modules/Vanilla/Simple Wires.ahk ;	WORKING
Colours:
#Include, Modules/Vanilla/Simon Says.ahk ;		WORKING
Words:
#Include, Modules/Vanilla/Who's On First.ahk ;	WORKING
Symbols:
#Include, Modules/Vanilla/Symbols.ahk ;			WORKING
Memory:
#Include, Modules/Vanilla/Memory.ahk ;			WORKING
Morse:
#Include, Modules/Vanilla/Morse.ahk ;			WORKING
CompWires:
#Include, Modules/Vanilla/Complex Wires.ahk ;	WORKING
WireSequence:
#Include, Modules/Vanilla/Sequence.ahk ;		WORKING
Password:
#Include, Modules/Vanilla/Password.ahk ;		WORKING
Maze:
#Include, Modules/Vanilla/Maze.ahk ;			WORKING
Knobs:
#Include, Modules/Vanilla/Knob.ahk ;			WORKING
; ###############################################################################################################################
ColourFlash:
#Include, Modules/Colour Flash.ahk ;			WORKING
PianoKeys:
#Include, Modules/Piano Keys.ahk ;				WORKING
;FestivePianoKeys:
;#Include, Modules/Festive Piano Keys.ahk ;		WORKING
;CruelPianoKeys:
;#Include, Modules/Cruel Piano Keys.ahk ;		WORKING









; ###############################################################################################################################
GuiClose:
ExitApp

^Esc::ExitApp
^+r::Reload
^r::
{
	Gui, Destroy
	goto module
	Return
}