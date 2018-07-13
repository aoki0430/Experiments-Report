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
    # 音声認識結果の取得
    info = client.GetLastMsg[SpeechInfo]()

    if info:
        print ToString(info.recSpeech), info.isSpeaking
        if ToString(info.recSpeech).find("こんにちは")!=-1:
            # 音声発話命令を送信
            order1 = SpeechOrder()
            order1.utterace = ToBytes("こんにちは")
            order2 = RobotOrder()
            order2.kind = RobotOrder.ORDER_ROTATE;
            order2.data.Add( 1.0 );

            robotstop = RobotOrder()
            robotstop.kind = RobotOrder.ORDER_STOP;

            client.Send( order1 )
            client.Send( order2 )
            time.sleep(9)
            client.Send( robotstop )

        if ToString(info.recSpeech).find("さようなら")!=-1:
            # 音声発話命令を送信
            order1 = SpeechOrder()
            order1.utterace = ToBytes("ばいばい")

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

        if ToString(info.recSpeech).find("嫌い")!=-1:
            # 音声発話命令を送信
            order1 = SpeechOrder()
            order1.utterace = ToBytes("もう知りません")
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

        if ToString(info.recSpeech).find("前へすすめ")!=-1:
            # 音声発話命令を送信
            order1 = RobotOrder()
            order2 = SpeechOrder()
            order1.kind = RobotOrder.ORDER_MOVE_FORWARD;
            order1.data.Add( 0.1 );
            order2.utterace = ToBytes("了解")
            client.Send( order2 )
            client.Send( order1 )

        if ToString(info.recSpeech).find("止まれ")!=-1:
            # 音声発話命令を送信
            order1 = RobotOrder()
            order2 = SpeechOrder()
            order1.kind = RobotOrder.ORDER_STOP;
            order2.utterace = ToBytes("了解")
            client.Send( order2 )
            client.Send( order1 )
