# coding: shift-jis
import os
os.system("title SimpleReciever.py")
from RosClientBin import *

client = RosClient()
client.Connect( "localhost" , "11311" )
client.Subscribe[ByteArray]()

while 1:
    msg = client.GetLastMsg[ByteArray]()

    if msg:
        print ToString(msg.data)
