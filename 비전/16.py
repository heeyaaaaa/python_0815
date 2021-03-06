import numpy as np
import cv2

def contour():
    img = cv2.imread('globe.png')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = img.copy()
    
    
    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    
    contours, _  = cv2.findContours(thr, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    contours2, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    print(len(contours))
    
    cv2.drawContours(img, contours, -1, (0,0,255), 1)
    cv2.drawContours(img2, contours2, -1, (0,255,0), 1)
    
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)
    cv2.imshow('contour2',img2)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
contour()