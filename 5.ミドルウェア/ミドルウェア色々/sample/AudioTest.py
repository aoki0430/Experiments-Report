# coding: shift-jis
import os
os.system("title AudioTest.py")
from RosClientBin import *
import time

client = RosClient()
client.Connect( "localhost" , "11311" )
client.Subscribe[SpeechInfo]()
client.Publish[SpeechOrder]()

while 1:
    # �����F�����ʂ̎擾
    info = client.GetLastMsg[SpeechInfo]()

    if info:
        print ToString(info.recSpeech), info.isSpeaking
        if ToString(info.recSpeech).find("����ɂ���")!=-1:
            # �������b���߂𑗐M
            order1 = SpeechOrder()
            order1.utterace = ToBytes("����ɂ���")
            order2 = RobotOrder()
            order2.kind = RobotOrder.ORDER_ROTATE;
            order2.data.Add( 1.0 );

            robotstop = RobotOrder()
            robotstop.kind = RobotOrder.ORDER_STOP;

            client.Send( order1 )
            client.Send( order2 )
            time.sleep(9)
            client.Send( robotstop )

        if ToString(info.recSpeech).find("���悤�Ȃ�")!=-1:
            # �������b���߂𑗐M
            order1 = SpeechOrder()
            order1.utterace = ToBytes("�΂��΂�")

            robotright = RobotOrder()
            robotright.kind = RobotOrder.ORDER_ROTATE;
            robotright.data.Add( -0.5 );

            robotleft = RobotOrder()
            robotleft.kind = RobotOrder.ORDER_ROTATE;
            robotleft.data.Add( 0.5 );

            robotstop = RobotOrder()
            robotstop.kind = RobotOrder.ORDER_STOP;

            client.Send( order1 )
            for i in range(2):
                client.Send( robotright )
                time.sleep(3)
                client.Send( robotleft )
                time.sleep(3)
            client.Send( robotstop )

        if ToString(info.recSpeech).find("����")!=-1:
            # �������b���߂𑗐M
            order1 = SpeechOrder()
            order1.utterace = ToBytes("�����m��܂���")
            order2 = RobotOrder()
            order2.kind = RobotOrder.ORDER_ROTATE;
            order2.data.Add( 1.0 );

            robotstop = RobotOrder()
            robotstop.kind = RobotOrder.ORDER_STOP;

            robotforward = RobotOrder()
            robotforward.kind = RobotOrder.ORDER_MOVE_FORWARD;
            robotforward.data.Add( 0.1 );

            client.Send( order1 )
            client.Send( order2 )
            time.sleep(4.5)
            client.Send( robotforward )
            time.sleep(2)
            client.Send( robotstop )

        if ToString(info.recSpeech).find("�O�ւ�����")!=-1:
            # �������b���߂𑗐M
            order1 = RobotOrder()
            order2 = SpeechOrder()
            order1.kind = RobotOrder.ORDER_MOVE_FORWARD;
            order1.data.Add( 0.1 );
            order2.utterace = ToBytes("����")
            client.Send( order2 )
            client.Send( order1 )

        if ToString(info.recSpeech).find("�~�܂�")!=-1:
            # �������b���߂𑗐M
            order1 = RobotOrder()
            order2 = SpeechOrder()
            order1.kind = RobotOrder.ORDER_STOP;
            order2.utterace = ToBytes("����")
            client.Send( order2 )
            client.Send( order1 )
