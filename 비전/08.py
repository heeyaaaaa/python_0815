import numpy as np
import cv2

def hsv():
    blue = np.uint8([[[255,0,0]]])
    green = np.uint8([[[0,255,0]]])
    red = np.uint8([[[0,0,255]]])
    
    hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
    
    print('HSV for BLUE: ', hsv_blue)
    print('HSV for GREEN: ', hsv_green)
    print('HSV for RED: ', hsv_red)
    
    
#hsv()
    
def tracking():
    try:
        print('카메라를 구동합니다.')
        cap = cv2.VideoCapture(0)
    except:
        print('카메라 구동 실패')
        return
    
    while True:
        ret, frame = cap.read()
        
        #BGR을 HSV모드로 전환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #HSV에서 BGR로 가정할 범위를 정의함
        lower_blue = np.array([110,100,100])
        upper_blue = np.array([130,255,255])
        
        lower_green = np.array([50,100,100])
        upper_green = np.array([70,255,255])
        
        lower_red = np.array([-10,100,100])
        upper_red = np.array([10,255,255])
        
        #HSV 이미지에서 청색만, 또는 초록색만 또는 빨간색만 추출하기 위한 임계값
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        
        #mask와 원본 이미지를 비트 연산함
        res1 = cv2.bitwise_and(frame, frame, mask = mask_blue)
        res2 = cv2.bitwise_and(frame, frame, mask = mask_green)
        res3 = cv2.bitwise_and(frame, frame, mask = mask_red)
        
        cv2.imshow('original', frame)
        cv2.imshow('BLUE', res1)
        cv2.imshow('GREEN', res2)
        cv2.imshow('RED', res3)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        
    cv2.destroyAllWindows()
    
tracking()
        