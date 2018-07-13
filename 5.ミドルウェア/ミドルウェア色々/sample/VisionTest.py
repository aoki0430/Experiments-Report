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
    # ���i�����擾
    skeltons = client.GetLastMsg[Skeltons]()
    if skeltons:
        if skeltons.data.Count:
            rightUp = False
            leftUp = False
            rightFront = False
            leftFront = False
            rightSide = False
            leftSide = False

            # ��̍��W�Ɠ��̍��W����Ɏ�̏�Ԃ�����
            if skeltons.data[0].joints[Skelton.SKEL_RIGHT_HAND].y - skeltons.data[0].joints[Skelton.SKEL_HEAD].y > 0: rightUp = True;
            if skeltons.data[0].joints[Skelton.SKEL_LEFT_HAND].y - skeltons.data[0].joints[Skelton.SKEL_HEAD].y > 0: leftUp = True;

            if skeltons.data[0].joints[Skelton.SKEL_HEAD].z - skeltons.data[0].joints[Skelton.SKEL_RIGHT_HAND].z > 300: rightFront = True;
            if skeltons.data[0].joints[Skelton.SKEL_HEAD].z - skeltons.data[0].joints[Skelton.SKEL_LEFT_HAND].z > 300: leftFront = True;

            if skeltons.data[0].joints[Skelton.SKEL_RIGHT_HAND].x - skeltons.data[0].joints[Skelton.SKEL_RIGHT_SHOULDER].x < -300: rightSide = True;
            if skeltons.data[0].joints[Skelton.SKEL_LEFT_HAND].x - skeltons.data[0].joints[Skelton.SKEL_LEFT_SHOULDER].x > 300: leftSide = True;

            print "�E��F",
            if rightUp:
                print "��",
                order = SpeechOrder()
                order.utterace = ToBytes("�����͂Ԃ��؂�")
                client.Send( order )
                time.sleep(4)

            if rightFront:
                print "�O",
                order = SpeechOrder()
                order.utterace = ToBytes("��[�����ہ[�؁[��")
                client.Send( order )
                time.sleep(4)
            if rightSide:     print "��",
            print

            print "����F",
            if leftUp:
                print "��",
                order = SpeechOrder()
                order.utterace = ToBytes("�����͂Ԃ������ہ[")
                client.Send( order )
                time.sleep(4)
            if leftFront:   print "�O",
            if leftSide:    print "��",
            print

    # ���̌��o���ʎ�M
    objects = client.GetLastMsg[Objects]()
    if objects:
        for i in range( objects.data.Count ):
            print "���̌��o�@id:", objects.data[i].id, " pos:",objects.data[i].pos.x, objects.data[i].pos.y,objects.data[i].pos.z

    # �猟�o���ʎ�M
    faces = client.GetLastMsg[Faces]()
    if faces:
        for i in range( faces.data.Count ):
            print "�猟�o�@id:", faces.data[i].id, " pos:",faces.data[i].pos.x, faces.data[i].pos.y,faces.data[i].pos.z

    # �F���o���ʂ���M
    color = client.GetLastMsg[ColorBlobs]()
    if color:
        for i in range( color.data.Count ):
            print "�F���o�@id:" , color.data[i].id, " pos:",color.data[i].pos.x, color.data[i].pos.y, color.data[i].pos.z




