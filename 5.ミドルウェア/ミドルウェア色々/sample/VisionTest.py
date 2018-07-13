# coding: shift-jis
import os
os.system("title VisionTest.py")
from RosClientBin import *
import time

client = RosClient()
client.Connect( "localhost" , "11311" )
client.Subscribe[Skeltons]()
client.Subscribe[Objects]()
client.Subscribe[Faces]()
client.Subscribe[ColorBlobs]()

while 1:
    # 骨格情報を取得
    skeltons = client.GetLastMsg[Skeltons]()
    if skeltons:
        if skeltons.data.Count:
            rightUp = False
            leftUp = False
            rightFront = False
            leftFront = False
            rightSide = False
            leftSide = False

            # 手の座標と頭の座標を基準に手の状態を識別
            if skeltons.data[0].joints[Skelton.SKEL_RIGHT_HAND].y - skeltons.data[0].joints[Skelton.SKEL_HEAD].y > 0: rightUp = True;
            if skeltons.data[0].joints[Skelton.SKEL_LEFT_HAND].y - skeltons.data[0].joints[Skelton.SKEL_HEAD].y > 0: leftUp = True;

            if skeltons.data[0].joints[Skelton.SKEL_HEAD].z - skeltons.data[0].joints[Skelton.SKEL_RIGHT_HAND].z > 300: rightFront = True;
            if skeltons.data[0].joints[Skelton.SKEL_HEAD].z - skeltons.data[0].joints[Skelton.SKEL_LEFT_HAND].z > 300: leftFront = True;

            if skeltons.data[0].joints[Skelton.SKEL_RIGHT_HAND].x - skeltons.data[0].joints[Skelton.SKEL_RIGHT_SHOULDER].x < -300: rightSide = True;
            if skeltons.data[0].joints[Skelton.SKEL_LEFT_HAND].x - skeltons.data[0].joints[Skelton.SKEL_LEFT_SHOULDER].x > 300: leftSide = True;

            print "右手：",
            if rightUp:
                print "上",
                order = SpeechOrder()
                order.utterace = ToBytes("あいはぶあぺん")
                client.Send( order )
                time.sleep(4)

            if rightFront:
                print "前",
                order = SpeechOrder()
                order.utterace = ToBytes("んーあっぽーぺーん")
                client.Send( order )
                time.sleep(4)
            if rightSide:     print "横",
            print

            print "左手：",
            if leftUp:
                print "上",
                order = SpeechOrder()
                order.utterace = ToBytes("あいはぶああっぽー")
                client.Send( order )
                time.sleep(4)
            if leftFront:   print "前",
            if leftSide:    print "横",
            print

    # 物体検出結果受信
    objects = client.GetLastMsg[Objects]()
    if objects:
        for i in range( objects.data.Count ):
            print "物体検出　id:", objects.data[i].id, " pos:",objects.data[i].pos.x, objects.data[i].pos.y,objects.data[i].pos.z

    # 顔検出結果受信
    faces = client.GetLastMsg[Faces]()
    if faces:
        for i in range( faces.data.Count ):
            print "顔検出　id:", faces.data[i].id, " pos:",faces.data[i].pos.x, faces.data[i].pos.y,faces.data[i].pos.z

    # 色検出結果を受信
    color = client.GetLastMsg[ColorBlobs]()
    if color:
        for i in range( color.data.Count ):
            print "色検出　id:" , color.data[i].id, " pos:",color.data[i].pos.x, color.data[i].pos.y, color.data[i].pos.z




