#SingleInstance Force

^b::
	Send, %Clipboard%
	Return
	
!Esc::
   Suspend, Permit
   SusToggle := !SusToggle
   If (SusToggle)
   {   
		Suspend, On
		TrayTip,, "Macro Paused"
   }
   Else
   {   
		Suspend Off
		TrayTip,, "Macro Unpaused"
   }
   Return