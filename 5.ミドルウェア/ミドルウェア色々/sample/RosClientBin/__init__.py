
import clr
clr.AddReferenceToFileAndPath( "RosClientBin/RosClient" )
from RosSharp import *
from System.Collections.Generic import *

def ToString( bytes ):
    return RosClient.ToString( bytes )

def ToBytes( s ):
    return RosClient.ToBytes( s )


if 0:

    class List:
        def Add():
            pass
        def Count():
            pass
        def Remove():
            pass
        def Clear():
            pass

    class RosClient:
        def GetMsg():
            pass
        def GetLastMsg():
            pass
        def Send( data ):
            pass
        def Publish():
            pass
        def Subscribe():
            pass


    class ByteArray:

        data = List()
    class ColorBlob:

        id = 0
        pos = 0
        rect = 0
        score = 0.1
    class ColorBlobs:

        data = List()
    class Faces:

        data = List()
    class Image:

        width = 0
        height = 0
        image = List()
        depth = List()
    class ImageWriter:

        filename = ""
    class Joypad:

        analog1X = 0.1
        analog1Y = 0.1
        analog2X = 0.1
        analog2Y = 0.1
        up = True
        down = True
        right = True
        left = True
        butons = List()
    class Object:

        id = 0
        pos = 0
    class ObjectData:

        id = 0
        pos = 0
    class Objects:

        data = List()
    class Pos3D:

        x = 0.1
        y = 0.1
        z = 0.1
    class Rect:

        left = 0
        top = 0
        right = 0
        bottom = 0
    class RobotInfo:

        posx = 0.1
        posy = 0.1
        heading = 0.1
        ismoving = True
        isClisionDetectedL = True
        isClisionDetectedC = True
        isClisionDetectedR = True
        isCliffDetectedL = True
        isCliffDetectedC = True
        isCliffDetectedR = True
    class RobotOrder:

        ORDER_MOVE=0
        ORDER_MOVE_FORWARD=1
        ORDER_ROTATE=2
        ORDER_STOP=3
        ORDER_MOVE_DIST=4
        ORDER_ROTATE_ANGLE=5
        kind = 0
        data = List()
    class SkeltonData:

        SKEL_HEAD=0
        SKEL_NECK=1
        SKEL_TORSO=2
        SKEL_WAIST=3
        SKEL_RIGHT_COLLAR=4
        SKEL_RIGHT_SHOULDER=5
        SKEL_RIGHT_ELBOW=6
        SKEL_RIGHT_WRIST=7
        SKEL_RIGHT_HAND=8
        SKEL_RIGHT_FINGERTIP=9
        SKEL_LEFT_COLLAR=10
        SKEL_LEFT_SHOULDER=11
        SKEL_LEFT_ELBOW=12
        SKEL_LEFT_WRIST=13
        SKEL_LEFT_HAND=14
        SKEL_LEFT_FINGERTIP=15
        SKEL_RIGHT_HIP=16
        SKEL_RIGHT_KNEE=17
        SKEL_RIGHT_ANKLE=18
        SKEL_RIGHT_FOOT=19
        SKEL_LEFT_HIP=20
        SKEL_LEFT_KNEE=21
        SKEL_LEFT_ANKLE=22
        SKEL_LEFT_FOOT=23
        id = 0
        joints = List()
    class Skeltons:

        data = List()
    class SpeechInfo:

        recSpeech = List()
        isSpeaking = True
    class SpeechOrder:

        utterace = List()
    class Test:

        n = 0
        str = ""
        f = 0.1
    class Test2:

        n = 0
        str = ""
    class VisionInfo:

        skeltons = List()
        objects = List()
        faces = List()
