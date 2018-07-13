# coding: shift-jis
import os
os.system("title SimpleSender.py")
from RosClientBin import *

client = RosClient()
client.Connect( "localhost" , "11311" )
client.Publish[ByteArray]()

while 1:
    print "何か入力してください"
    str = raw_input()           # 文字列の入力

    msg = ByteArray()           # データを送信するための箱を用意
    msg.data = ToBytes( str )   # 箱にデータ（文字列）を入れる
    client.Send( msg )          # 送信





