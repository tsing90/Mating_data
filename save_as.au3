$CmdLine[0] ; = 2 参数的总数量，不虚赋值
$CmdLine[1] ; = 上传文件路径
;在10秒内等待打开窗口出现
WinWait("另存为","",5)
;ControlFocus("title","text",ClassnameNN) 识别Window窗口
ControlFocus("另存为", "","#32770")
;向“文件名”输入框内输入本地文件的路径
ControlSetText("另存为", "", "Edit1", $CmdLine[1])
Sleep(2000)
;单击打开按钮
ControlClick("另存为", "","Button2");