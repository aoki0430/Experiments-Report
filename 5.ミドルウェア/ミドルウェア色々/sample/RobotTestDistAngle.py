# coding: shift-jis
import sys
import os
os.system("title RobotTestDistAngle.py")
from RosClientBin import *
import time
import System
import msvcrt



client = RosClient()
client.Connect( "127.0.0.1" , "11311" )
client.Publish[RobotOrder]()
client.Subscribe[RobotInfo]()

##################
print "直進"
order = RobotOrder()
order.kind = RobotOrder.ORDER_MOVE_DIST
order.data.Add(0.5)
client.Send( order )

while 1:
    time.sleep(2)
    info = client.GetLastMsg[RobotInfo]()
    if info:
        if info.ismoving==False:
            "停止"
            break
        else:
            print "移動中"

##################
print "回転"
order = RobotOrder()
order.kind = RobotOrder.ORDER_ROTATE_ANGLE
order.data.Add(1.507)
client.Send( order )

while 1:
    time.sleep(2)
    info = client.GetLastMsg[RobotInfo]()
    if info:
        if info.ismoving==False:
            "停止"
            break
        else:
            print "移動中"

##################
print "逆回転"
order = RobotOrder()
order.kind = RobotOrder.ORDER_ROTATE_ANGLE
order.data.Add(-1.507)
client.Send( order )


while 1:
    time.sleep(2)
    info = client.GetLastMsg[RobotInfo]()
    if info:
        if info.ismoving==False:
            "停止"
            break
        else:
            print "移動中"

##################
print "後進"
order = RobotOrder()
order.kind = RobotOrder.ORDER_MOVE_DIST
order.data.Add(-0.5)
client.Send( order )

while 1:
    time.sleep(2)
    info = client.GetLastMsg[RobotInfo]()
    if info:
        if info.ismoving==False:
            "停止"
            break
        else:
            print "移動中"



