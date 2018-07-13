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

        # ���{�b�g�֖��߂𑗐M
        order.kind = RobotOrder.ORDER_MOVE;

        # ���i���x�Ɖ�]���x
        speed = 0
        rotate = 0

        if abs(joy.analog1Y) > 0.01:
            speed = joy.analog1Y * 0.2

        if abs(joy.analog1X) > 0.01:
            rotate = -joy.analog1X

        order.data.Add( speed );    # ���i���x
        order.data.Add( rotate );   # ��]���x
        client.Send( order );

        print"x:", order.data[0] , "y" , order.data[1]

    info = client.GetLastMsg[RobotInfo]()
    if info:
        print "x:", info.posx , " y:" , info.posy , " theta:" , info.heading
        print "�Փ�(���C���S�C�E):" , info.isClisionDetectedL , info.isClisionDetectedC , info.isClisionDetectedR
        print "--------------------------------------------"

    sleep(0.3)



