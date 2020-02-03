import numpy as np
import cv2

def showImage():
    img = cv2.imread('model.png', cv2.IMREAD_COLOR)
        
    cv2.imshow('model', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage()
