import numpy as np
import cv2

def contour():
    
    img = cv2.imread('model.png')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _  = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    cnt = contours[82]
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)
    
    cv2.drawContours(img, [cnt], 0, (0,0,255), 1)
    
    print('contour 면적: ', area)
    print('contour 길이: ', perimeter)
    
    cv2.imshow('contour', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
contour()
