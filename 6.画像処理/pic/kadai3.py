# encoding: utf8
from __future__ import unicode_literals
from pylab import *
from cv2 import imread

# 真っ黒の画像を生成
gazo = zeros( (10,10) )

# 画素値を表示
print "画素値"
print gazo

# 画像を表示
imshow(gazo, cmap="gray", vmin=0, vmax=255)

# 画像を変換
for x in range(10):
    for y in range(10):
        if (x<=8 and x>=1) and (y<=8 and y>=1) :
            gazo[y][x] = 255

print "変換後の画像"
print gazo

# 画像を表示
figure()
imshow(gazo, cmap="gray", vmin=0, vmax=255, interpolation="None")
show()
