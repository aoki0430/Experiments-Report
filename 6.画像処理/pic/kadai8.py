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

sum = [0,0,0,0,0,0]
length = [0,0,0,0,0,0]
line = [240, 220, 200, 160, 120, 50]

for z in range (6):
    c = 0
    gazo2 = zeros( (358,499) )#ラプラシアンフィルタ
    for y in range(1,357):
        for x in range(1,498):
            if gazo[y][x] < line[z]:
                gazo2[y][x] = 0
            else:
                gazo2[y][x] = 255

    gazo3 = zeros( (358,499) )#２値化
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
                    gasochi += gazo2[y+yy-1][x+xx-1] * filter[yy][xx]
                    
            gasochi = int(gasochi) 
            if gasochi<0:
                gasochi = 0
            elif gasochi>255:
                gasochi = 255
            gazo3[y][x] = gasochi
            
    for y in range(0,358):
        for x in range(0,499):
            if gazo3[y][x] == 255:
                c += 1
    sum[z] = c

for i in range (6):
    if z == 5:
        length[i] = sum[i]
    else:
        length[i] = sum[i] - sum[i+1]
    print(i)

print(sum)
print(length)
# 画素値を表示

figure()
imshow(gazo, cmap="gray", vmin=0, vmax=255)
figure()
imshow(gazo2, cmap="gray", vmin=0, vmax=255)
figure()
imshow(gazo3, cmap="gray", vmin=0, vmax=255)


show()
