# coding: shift-jis
import os
os.system("title SimpleSender.py")
from RosClientBin import *

client = RosClient()
client.Connect( "localhost" , "11311" )
client.Publish[ByteArray]()

while 1:
    print "�������͂��Ă�������"
    str = raw_input()           # ������̓���

    msg = ByteArray()           # �f�[�^�𑗐M���邽�߂̔���p��
    msg.data = ToBytes( str )   # ���Ƀf�[�^�i������j������
    client.Send( msg )          # ���M





