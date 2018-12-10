# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread

# 画像を読み込み
gazo = imread( "kadai6.bmp", 0 )

# 画像を表示
imshow(gazo, cmap="gray", vmin=0, vmax=255, interpolation="None")

# ヒストグラムを表示
figure()
hist( gazo.flatten(), 256, (0,255) )

# 画像を変換
gazo2 = zeros((240,384))
for x in range(384):
    for y in range(240):
        gazo2[y][x] = (255*(gazo[y][x]-120)/30) + 0

# 画像を表示
figure()
imshow(gazo2, cmap="gray", vmin=0, vmax=255, interpolation="None")

# ヒストグラムを表示
figure()
hist( gazo2.flatten(), 256, (0,255) )
show()
