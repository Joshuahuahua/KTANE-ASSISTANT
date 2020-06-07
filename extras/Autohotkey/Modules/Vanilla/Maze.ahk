#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Maze := Array()
Maze.Insert(1, {P1: "15", P2: "32", Num: 9})
Maze.Insert(1, {P1: "34", P2: "41", Num: 8})
Maze.Insert(1, {P1: "21", P2: "26", Num: 7})
Maze.Insert(1, {P1: "35", P2: "51", Num: 6})
Maze.Insert(1, {P1: "46", P2: "53", Num: 5})
Maze.Insert(1, {P1: "11", P2: "14", Num: 4})
Maze.Insert(1, {P1: "44", P2: "64", Num: 3})
Maze.Insert(1, {P1: "24", P2: "52", Num: 2})
Maze.Insert(1, {P1: "12", P2: "63", Num: 1})

Gui, Destroy

InputBox, Coord1, %Title%, First Coord (XY = 12)
InputBox, Coord2, %Title%, First Coord (XY = 12)
Coord1 := StrReplace(Coord1, A_Space, "")
Coord2 := StrReplace(Coord2, A_Space, "")

Loop % Maze.Length() {
	If (Coord1 = Maze[A_Index].P1 AND Coord2 = Maze[A_Index].P2 OR Coord1 = Maze[A_Index].P2 AND Coord2 = Maze[A_Index].P1) {
		SplashImage, Modules\MazeImages\Maze%A_Index%.PNG, B X0 Y0,,, MazeOverlay
		WinSet, Transparent , 200, MazeOverlay
		Msgbox, 64, %Title%, Press "M" to remove overlay.
		goto module
		Return
	}
}
Msgbox, 64, %Title%, No mazes were found!

goto module
Return
~m::SplashImage, OFF