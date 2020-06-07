
; REMOVE _'s IN DISPLAY TABLE

#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

WOFGrid := Array()
WOFGrid.Insert(1, {Word: "", Position: "BL"})
WOFGrid.Insert(1, {Word: "BLANK", Position: "MR"})
WOFGrid.Insert(1, {Word: "C", Position: "TR"})
WOFGrid.Insert(1, {Word: "CEE", Position: "BR"})
WOFGrid.Insert(1, {Word: "DISPLAY", Position: "BR"})
WOFGrid.Insert(1, {Word: "FIRST", Position: "TR"})
WOFGrid.Insert(1, {Word: "HOLD_ON", Position: "BR"})
WOFGrid.Insert(1, {Word: "LEAD", Position: "BR"})
WOFGrid.Insert(1, {Word: "LEED", Position: "BL"})
WOFGrid.Insert(1, {Word: "LED", Position: "ML"})
WOFGrid.Insert(1, {Word: "NO", Position: "BR"})
WOFGrid.Insert(1, {Word: "NOTHING", Position: "ML"})
WOFGrid.Insert(1, {Word: "OKAY", Position: "TR"})
WOFGrid.Insert(1, {Word: "READ", Position: "MR"})
WOFGrid.Insert(1, {Word: "REED", Position: "BL"})
WOFGrid.Insert(1, {Word: "RED", Position: "MR"})
WOFGrid.Insert(1, {Word: "SAYS", Position: "BR"})
WOFGrid.Insert(1, {Word: "SEE", Position: "BR"})
WOFGrid.Insert(1, {Word: "THEIR", Position: "MR"})
WOFGrid.Insert(1, {Word: "THERE", Position: "BR"})
WOFGrid.Insert(1, {Word: "THEY_ARE", Position: "ML"})
WOFGrid.Insert(1, {Word: "THEY_RE", Position: "BL"})
WOFGrid.Insert(1, {Word: "UR", Position: "TL"})
WOFGrid.Insert(1, {Word: "YES", Position: "ML"})
WOFGrid.Insert(1, {Word: "YOU", Position: "MR"})
WOFGrid.Insert(1, {Word: "YOU_ARE", Position: "BR"})
WOFGrid.Insert(1, {Word: "YOUR", Position: "MR"})
WOFGrid.Insert(1, {Word: "YOU_RE", Position: "MR"})

BLANK := ["WAIT","RIGHT","OKAY","MIDDLE","BLANK"]
DONE := ["SURE","UH_HUH","NEXT","WHAT?","YOUR","UR","YOU_RE","HOLD","LIKE","YOU","U","YOU_ARE","UH_UH","DONE"]
FIRST := ["LEFT","OKAY","YES","MIDDLE","NO","RIGHT","NOTHING","UHHH","WAIT","READY","BLANK","WHAT","PRESS","FIRST"]
HOLD := ["YOU_ARE","U","DONE","UH_UH","YOU","UR","SURE","WHAT?","YOU_RE","NEXT","HOLD"]
LEFT := ["RIGHT","LEFT"]
LIKE := ["YOU_RE","NEXT","U","UR","HOLD","DONE","UH_UH","WHAT?","UH_HUH","YOU","LIKE"]
MIDDLE := ["BLANK","READY","OKAY","WHAT","NOTHING","PRESS","NO","WAIT","LEFT","MIDDLE"]
NEXT := ["WHAT?","UH_HUH","UH_UH","YOUR","HOLD","SURE","NEXT"]
NO := ["BLANK","UHHH","WAIT","FIRST","WHAT","READY","RIGHT","YES","NOTHING","LEFT","PRESS","OKAY","NO"]
NOTHING := ["UHHH","RIGHT","OKAY","MIDDLE","YES","BLANK","NO","PRESS","LEFT","WHAT","WAIT","FIRST","NOTHING"]
OKAY := ["MIDDLE","NO","FIRST","YES","UHHH","NOTHING","WAIT","OKAY"]
PRESS := ["RIGHT","MIDDLE","YES","READY","PRESS"]
READY := ["YES","OKAY","WHAT","MIDDLE","LEFT","PRESS","RIGHT","BLANK","READY"]
RIGHT := ["YES","NOTHING","READY","PRESS","NO","WAIT","WHAT","RIGHT"]
SURE := ["YOU_ARE","DONE","LIKE","YOU_RE","YOU","HOLD","UH_HUH","UR","SURE"]
U := ["UH_HUH","SURE","NEXT","WHAT?","YOU_RE","UR","UH_UH","DONE","U"]
UH_HUH := ["UH_HUH"]
UH_UH := ["UR","U","YOU_ARE","YOU_RE","NEXT","UH_UH"]
UHHH := ["READY","NOTHING","LEFT","WHAT","OKAY","YES","RIGHT","NO","PRESS","BLANK","UHHH"]
UR := ["DONE","U","UR"]
WAIT := ["UHHH","NO","BLANK","OKAY","YES","LEFT","FIRST","PRESS","WHAT","WAIT"]
WHAT := ["UHHH","WHAT"]
WHAT? := ["YOU","HOLD","YOU_RE","YOUR","U","DONE","UH_UH","LIKE","YOU_ARE","UH_HUH","UR","NEXT","WHAT?"]
YES := ["OKAY","RIGHT","UHHH","MIDDLE","FIRST","WHAT","PRESS","READY","NOTHING","YES"]
YOU_ARE := ["YOUR","NEXT","LIKE","UH_HUH","WHAT?","DONE","UH_UH","HOLD","YOU","U","YOU_RE","SURE","UR","YOU_ARE"]
YOU := ["SURE","YOU_ARE","YOUR","YOU_RE","NEXT","UH_HUH","UR","HOLD","WHAT?","YOU,"]
YOUR := ["UH_UH","YOU_ARE","UH_HUH","YOUR"]
YOU_RE := ["YOU","YOU_RE"]



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


Compile := WOFBIG "-" WOFTL "-" WOFTR "-" WOFML "-" WOFMR "-" WOFBL "-" WOFBR
Compile := StrReplace(Compile, A_Space, "_")
Compile := StrReplace(Compile, "'", "_")
Decompile := StrSplit(Compile, "-")

WOFBIG := Decompile[1]
WOFTL := Decompile[2]
WOFTR := Decompile[3]
WOFML := Decompile[4]
WOFMR := Decompile[5]
WOFBL := Decompile[6]
WOFBR := Decompile[7]




Loop % WOFGrid.Length() {
	If (WOFBig = WOFGrid[A_Index].Word) {
		Position := WofGrid[A_Index].Position
	}
}
Word := WOF%Position%
Length := %Word%.Length()
Loop, %Length% {
	List := %Word%[A_Index]
	If (WOFTL = List OR WOFTR = List OR WOFML = List OR WOFMR = List OR WOFBL = List OR WOFBR = List) {
		
		If (List = "YOU_RE" OR List = "THEY_RE") {
			List := StrReplace(List, "_", "'")
		}
		List := StrReplace(List, "_", A_Space)
		Msgbox Press %List%
		Break
	}
}
GuiControl,, WOFBig
GuiControl,, WOFTL
GuiControl,, WOFTR
GuiControl,, WOFML
GuiControl,, WOFMR
GuiControl,, WOFBL
GuiControl,, WOFBR
GuiControl, Focus, WOFBig
Return