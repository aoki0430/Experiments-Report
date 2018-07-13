# coding: shift-jis
import os
os.system("title RobotTest.py")
from RosClientBin import *
from msvcrt import *

client = RosClient()
client.Connect( "localhost" , "11311" )
client.Subscribe[RobotInfo]()
client.Publish[RobotOrder]()

while 1:
    if kbhit():
        c = 0
        while kbhit():
            c = ord(getch())

        order = RobotOrder()
        if c==72:# ��
            print "���i"
            order.kind = RobotOrder.ORDER_MOVE_FORWARD;
            order.data.Add( 0.1 );
        elif c==80:# ��
            print "��i"
            order.kind = RobotOrder.ORDER_MOVE_FORWARD;
            order.data.Add( -0.1 );
        elif c==75: # ��
            print "����]"
            order.kind = RobotOrder.ORDER_ROTATE;
            order.data.Add( 0.5 );
        elif c==77: # ��
            print "�E��]"
            order.kind = RobotOrder.ORDER_ROTATE;
            order.data.Add( -0.5 );
        else:
            print "��~";
            order.kind = RobotOrder.ORDER_STOP;

        client.Send( order )

    info = client.GetLastMsg[RobotInfo]()
    if info:
        print "x:", info.posx , " y:" , info.posy , " theta:" , info.heading
        print "�Փ�(���C���S�C�E):" , info.isClisionDetectedL , info.isClisionDetectedC , info.isClisionDetectedR
        print "--------------------------------------------"




