# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread
from numpy import *

# 画像の読み込み
gazo = imread( "kadai7.bmp", 0 )

# ヒストグラムを表示
figure()
hist( gazo.flatten(), 256, (0,255) )

a1 = 0 #左上
a2 = 0 #上真ん中
a3 = 0 #右上
a4 = 0 #左下
a5 = 0 #右下
a6 = 0 #真ん中

for y in range(0,358):
    for x in range(0,499):
        # 課題： 6つの図形の面積（画素数）を計算しなさい．
        #      レポートでは計算方法を分かりやすく説明しなさい．
        if gazo[y][x] == 0:
            a1 += 1
        elif gazo[y][x] ==76:
            a2 += 1
        elif gazo[y][x] == 122:
            a3 += 1
        elif gazo[y][x] == 164:
            a4 += 1
        elif gazo[y][x] == 200:
            a5 += 1
        elif gazo[y][x] == 229:
            a6 += 1
            
            
print(a1,a2,a3,a4,a5,a6)

# 画素値を表示
figure()
imshow(gazo, cmap="gray", vmin=0, vmax=255)
show()
