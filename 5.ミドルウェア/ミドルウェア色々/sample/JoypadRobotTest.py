# coding: shift-jis
from RosClientBin import *
from math import *
from time import *

client = RosClient()
client.Connect( "localhost" , "11311" )
client.Subscribe[Joypad]()
client.Subscribe[RobotInfo]()
client.Publish[RobotOrder]()

while 1:
    joy = client.GetLastMsg[Joypad]()
    if joy:
        order =  RobotOrder();

        # ロボットへ命令を送信
        order.kind = RobotOrder.ORDER_MOVE;

        # 直進速度と回転速度
        speed = 0
        rotate = 0

        if abs(joy.analog1Y) > 0.01:
            speed = joy.analog1Y * 0.2

        if abs(joy.analog1X) > 0.01:
            rotate = -joy.analog1X

        order.data.Add( speed );    # 直進速度
        order.data.Add( rotate );   # 回転速度
        client.Send( order );

        print"x:", order.data[0] , "y" , order.data[1]

    info = client.GetLastMsg[RobotInfo]()
    if info:
        print "x:", info.posx , " y:" , info.posy , " theta:" , info.heading
        print "衝突(左，中心，右):" , info.isClisionDetectedL , info.isClisionDetectedC , info.isClisionDetectedR
        print "--------------------------------------------"

    sleep(0.3)



