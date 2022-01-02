Set oshell = CreateObject ("Wscript.shell")

Dim strCMD
strCMD = "cmd cd /c D:\DSI\PROGRAM\RUNSERVER.bat"
oShell.Run strCMD
strCMD = "cmd cd /c D:\DSI\PROGRAM\RUNURL.bat"
oShell.Run strCMD, 0, false