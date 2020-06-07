#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Symbol1 := ""
Symbol2 := ""
Symbol3 := ""
Symbol4 := ""

Global Symbols := Array()

Symbols.Insert(1, {Name: "Omega", Character: "Ω", Value: 27})
Symbols.Insert(1, {Name: "Straight H", Character: "Ҋ", Value: 26})
Symbols.Insert(1, {Name: "AE", Character: "æ", Value: 25})
Symbols.Insert(1, {Name: "Not Equal", Character: "҂", Value: 24})
Symbols.Insert(1, {Name: "Black Star", Character: "★", Value: 23})
Symbols.Insert(1, {Name: "Alien 3", Character: "Ѯ", Value: 22})
Symbols.Insert(1, {Name: "C", Character: "Ͼ", Value: 21})
Symbols.Insert(1, {Name: "Trident", Character: "ψ", Value: 20})
Symbols.Insert(1, {Name: "Smiley Face", Character: "ټ", Value: 19})
Symbols.Insert(1, {Name: "B", Character: "Ѣ", Value: 18})
Symbols.Insert(1, {Name: "P", Character: "¶", Value: 17})
Symbols.Insert(1, {Name: "Six", Character: "Ϭ", Value: 16})
Symbols.Insert(1, {Name: "R", Character: "Ԇ", Value: 15})
Symbols.Insert(1, {Name: "X", Character: "Җ", Value: 14})
Symbols.Insert(1, {Name: "Butt", Character: "Ѽ", Value: 13})
Symbols.Insert(1, {Name: "Copyright", Character: "©", Value: 12})
Symbols.Insert(1, {Name: "?", Character: "¿", Value: 11})
Symbols.Insert(1, {Name: "White Star", Character: "☆", Value: 10})
Symbols.Insert(1, {Name: "Squiggle", Character: "Ҩ", Value: 9})
Symbols.Insert(1, {Name: "E", Character: "Ӭ", Value: 8})
Symbols.Insert(1, {Name: "Backwards C", Character: "Ͽ", Value: 7})
Symbols.Insert(1, {Name: "Curly H", Character: "ϗ", Value: 6})
Symbols.Insert(1, {Name: "Alien", Character: "Ѭ", Value: 5})
Symbols.Insert(1, {Name: "Lightning", Character: "Ϟ", Value: 4})
Symbols.Insert(1, {Name: "Landa", Character: "ƛ", Value: 3})
Symbols.Insert(1, {Name: "A", Character: "Ѧ", Value: 2})
Symbols.Insert(1, {Name: "Paddle", Character: "Ϙ", Value: 1})

SymbolColumn1 := [1,2,3,4,5,6,7]
SymbolColumn2 := [8,1,7,9,10,6,11]
SymbolColumn3 := [12,13,9,14,15,3,10]
SymbolColumn4 := [16,17,18,5,14,11,19]
SymbolColumn5 := [20,19,18,21,17,22,23]
SymbolColumn6 := [16,8,24,25,20,26,27]

Gui, Destroy
Global ColumnTally := [0,0,0,0,0,0]

UserInput() ;									Assign the 4 symbols (words)
;Symbol3 = Backwards C ; 7
;Symbol2 = Alien ; 5
;Symbol1 = Curly H ; 6
;Symbol4 = A ; 2

Loop 4 {
	Reassign(A_Index) ;							Assign the 4 symbols (numbers)
}
Loop 4
{
	FindColumn(A_Index) ;						Check symbols with colums
	Loop 6 {
		If (ColumnTally[A_Index] = 4) {
			CorrectColumn := A_Index ;			Assign the correct column
		}
	}
}
If (CorrectColumn = "") {
	MsgBox, 64, %Title%, The correct column was not found!
	Goto module
}
Reordered := ReOrder(Symbol1, Symbol2, Symbol3, Symbol4, CorrectColumn)
MsgBox, 64, %Title%, Press the symbols in this order..., 2
Loop 4 {
	ReReassign1 := ReReassign(Reordered[A_Index]) ;						Assign the 4 symbols (numbers)
}
goto module


tooltip ; #################################################################################################################################################
UserInput()
{
	Loop 4 {
		InputBox, Symbol%A_Index%, Title, Symbol %A_Index%
		If (Symbol%A_Index% = "6") {
			Symbol%A_Index% := "Six"
		}
		StringUpper, Symbol%A_Index%, Symbol%A_Index%, T
	}
}
Reassign(num)
{
	Loop % Symbols.Length() {
		If (Symbol%num% = Symbols[A_Index].Name) {
			Symbol%num% := Symbols[A_Index].Value
		}
	}
}
FindColumn(num)
{
	Loop, 6 {
		ArrayCount := A_Index
		Loop 7 {
			If (Symbol%num% = SymbolColumn%ArrayCount%[A_Index]) {
				ColumnTally[ArrayCount]+=1
			}
		}
	}
}
ReOrder(Symbol1, Symbol2, Symbol3, Symbol4, CorrectColumn)
{
	NumCount := 1
	Loop 7 {
		CorrectColumnNum := SymbolColumn%CorrectColumn%[A_Index] ;				Cycling through the correct columns' values
		If (CorrectColumnNum = Symbol1 OR CorrectColumnNum = Symbol2 OR CorrectColumnNum = Symbol3 OR CorrectColumnNum = Symbol4) {
			OrderedNum%NumCount% := CorrectColumnNum
			NumCount+=1
			If (NumCount = 5) {
				Return [OrderedNum1, OrderedNum2, OrderedNum3, OrderedNum4]
			}
		}
	}
}
ReReassign(symbol)
{
	Loop % Symbols.Length() {
		If (symbol = Symbols[A_Index].Value) {
			ReReassignWords := Symbols[A_Index].Name
			Msgbox % ReReassignWords
		}
	}
}