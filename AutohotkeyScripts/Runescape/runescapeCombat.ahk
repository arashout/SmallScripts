#SingleInstance, Force
^f::
WinActivate, RuneScape
startX := A_ScreenWidth/4
startY := A_ScreenHeight/4
endX := startX*3
endY := startY*3

while(!GetKeyState("Space")){
	ImageSearch, X, Y, %startX%, %startY%, %endX%, %endY%, *5 smallGoblinVillage.png
	if(ErrorLevel){

	}
	if(ErrorLevel){

	}
	else{
		MouseMove, X, Y
		Sleep, 300
		ImageSearch nx,ny,%startX%, %startY%,%endX%, %endY%,attackPopup.png ;Attack ToolTip
		if(ErrorLevel){

		}
		else{
			MouseClick, , X, Y,
			Sleep, 600
			Loop{
				ImageSearch nx,ny,%startX%, %startY%,%endX%, %endY%,attackedRed.png
				if(ErrorLevel){
					break
				}
				else{
					Sleep, 100
				}
			}
		}
	}

}
return

^i::
WinActivate, RuneScape
startX := A_ScreenWidth/4
startY := A_ScreenHeight/4
endX := startX*3
endY := startY*3
;Start Looking for loot drops
ImageSearch, lootX, lootY, %startX%, %startY%, %endX%, %endY%,*10 smallCoins.png
if(ErrorLevel){
	msgbox,,,not found bones
}
Else{
	MouseMove, lootX, lootY, 
	ImageSearch, trashX, trashY, %startX%, %startY%, %endX%, %endY%, takeCoins.png
	if(ErrorLevel){

	}
	else{
		MouseClick, ,lootX, lootY, 
	}
}
return