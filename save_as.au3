$CmdLine[0] ; = 2 �����������������鸳ֵ
$CmdLine[1] ; = �ϴ��ļ�·��
;��10���ڵȴ��򿪴��ڳ���
WinWait("���Ϊ","",5)
;ControlFocus("title","text",ClassnameNN) ʶ��Window����
ControlFocus("���Ϊ", "","#32770")
;���ļ���������������뱾���ļ���·��
ControlSetText("���Ϊ", "", "Edit1", $CmdLine[1])
Sleep(2000)
;�����򿪰�ť
ControlClick("���Ϊ", "","Button2");