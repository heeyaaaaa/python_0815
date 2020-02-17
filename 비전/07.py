import numpy as np
import cv2


img2 = cv2.imread('img2.jpg')
img2 = cv2.resize(img2,(288,512))

def addImage(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)
    img2 = cv2.resize(img2,dsize=(512,288))
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    
    add_img1 = img1 + img2
    add_img2 = cv2.add(img1, img2)
    
    cv2.imshow('img1+img2', add_img1)
    cv2.imshow('add(img1,img2)', add_img2)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#addImage('model.png', 'img2.jpg')

#이미지 블렌딩

def onMouse(x):
    pass

def imgBlending(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)
    img2 = cv2.resize(img2,dsize=(512,288))
    cv2.namedWindow('ImgPane')
    cv2.createTrackbar('MIXING', 'ImgPane', 0,100, onMouse)
    mix = cv2.getTrackbarPos('MIXING', 'ImgPane')
    
    while True:
        img = cv2.addWeighted(img1, float(100-mix)/100, img2, float(mix)/100,0)
        cv2.imshow('ImgPane', img)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        
        mix = cv2.getTrackbarPos('MIXING', 'ImgPane')
        
    cv2.destroyAllWindows()
    
#imgBlending('model.png', 'img2.jpg')

#이미지 비트 연산
    
def bitOperation(hpos, vpos):
    img1 = cv2.imread('img2.jpg')
    img2 = cv2.imread('logo.png')
    
    #로고를 사진 왼쪽 윗부분에 두기 위해 해당 영역 지정하기
    rows, cols, channels = img2.shape
    roi = img1[vpos:rows+vpos, hpos: cols+hpos]
    
    #로고를 위한 마스크와 역마스크 생성하기
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    
    #ROI에서 로고에 해당하는 부분만 검정색으로 만들기
    img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
    
    #로고 이미지에서 로고 부분만 추출하기
    img2_fg = cv2.bitwise_and(img2, img2, mask = mask)
    
    #로고 이미지 배경을 cv2.add로 투명으로 만들고 ROI에 로고 이미지 넣기
    dst = cv2.add(img1_bg, img2_fg)
    img1[vpos: rows+vpos, hpos: cols+hpos] = dst
    
    cv2.imshow('result', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
bitOperation(10,10)
