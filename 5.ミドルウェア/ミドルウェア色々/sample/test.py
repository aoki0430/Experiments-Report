# coding: shift-jis
from RosClientBin import *

client = RosClient()
client.Connect( "localhost" , "11311" )
client.Subscribe[SpeechInfo]()
client.Publish[SpeechOrder]()

print "\n".join(dir(RobotOrder.ORDER_MOVE))

