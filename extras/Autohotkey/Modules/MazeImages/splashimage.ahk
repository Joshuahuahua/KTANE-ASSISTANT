#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

SplashImage, Maze1.PNG, B X0 Y0,,, MazeOverlay

WinSet, Transparent , 155, MazeOverlay
sleep 1000
SplashImage, OFF
sleep 1000
ExitApp