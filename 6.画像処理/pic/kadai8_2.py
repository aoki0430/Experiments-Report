# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread
from numpy import *

# 画像の読み込み
gazo = imread( "kadai8.bmp", 0 )

# ヒストグラムを表示
figure()
hist( gazo.flatten(), 256, (0,255) )

# 課題： 6つの図形の輪郭線の長さ（画素数）を計算しなさい．
#      レポートでは計算方法を分かりやすく説明しなさい．
# ヒント：　二段階の処理が必要．．．

a1 = 0 #左上
a2 = 0 #上真ん中
a3 = 0 #右上
a4 = 0 #左下
a5 = 0 #右下
a6 = 0 #真ん中

gazo2 = zeros( (358,499) )#２値化
for y in range(1,357):
    for x in range(1,498):

        filter = [
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0]
            ]

        gasochi = 0
        for xx in range(3):
            for yy in range(3):
                # ここでfilterの値をgazoに掛ける
                gasochi += gazo[y+yy-1][x+xx-1] * filter[yy][xx]
                
        gasochi = int(gasochi) 
        if gasochi<0:
            gasochi = 0
        elif gasochi > 255:
            gasochi = 255
        gazo2[y][x] = gasochi
        
gazo3 = zeros( (358,499) )#ラプラシアンフィルタ
for y in range(1,357):
    for x in range(1,498):
        if gazo2[y][x] < 100:
            gazo3[y][x] = 0
        else:
            gazo3[y][x] = 255

        
for y in range(0,358):
    for x in range(0,499):
        if gazo3[y][x] == 255:
            a1 += 1

print(a1)

# 画素値を表示
print(a1)

figure()
imshow(gazo, cmap="gray", vmin=0, vmax=255)
figure()
imshow(gazo2, cmap="gray", vmin=0, vmax=255)
figure()
imshow(gazo3, cmap="gray", vmin=0, vmax=255)


show()
