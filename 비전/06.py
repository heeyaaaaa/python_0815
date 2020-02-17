import numpy as np
import cv2

img = cv2.imread('model.png')
px = img[280,200]
print(px)

print(img.shape)
print(img.size)
print(img.dtype)
cv2.imshow('original', img)

subimg = img[100:200, 300:500]
cv2.imshow('cutting', subimg)

img[100:200, 0:200] = subimg

print(img.shape)
print(subimg.shape)

cv2.imshow('modified', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#이미지 채널 분할 및 합치기

b, g, r = cv2.split(img)

print(img[100,100])
print(b[100,100], g[100,100], r[100,100])

cv2.imshow('blue channel', b)
cv2.imshow('green channel', g)
cv2.imshow('red channel', r)

cv2.waitKey(0)
cv2.destroyAllWindows()
