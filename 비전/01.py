import numpy as np
import cv2

def showImage():
    img = cv2.imread('model.png', cv2.IMREAD_COLOR)
        
    cv2.imshow('model', img)
    cv2.waitKey(0) #키보드 입력이 있을때까지 기다려!
    cv2.destroyAllWindows()

#showImage()


def showImage2():
    img = cv2.imread('model.png', cv2.IMREAD_COLOR)
    
    cv2.nameWindow('model', cv2.WINDOW_NORMAL)    
    cv2.imshow('model', img)
    cv2.waitKey(0) #키보드 입력이 있을때까지 기다려!
    cv2.destroyAllWindows()

#showImage2()
    
    
def showImage3():
    img = cv2.imread('model.png', cv2.IMREAD_COLOR)
    cv2.imshow('model', img)
    
    k = cv2.waitKey(0) & 0xFF
    
    if k == 27 :
        cv2.destroyAllWindows()
    elif k == ord('c'):
        cv2.imwrite('model_copy.jpg',img)
        cv2.destroyAllWindows()
        
#showImage3()

import matplotlib.pyplot as plt

def showImage4():
    img = cv2.imread('model.png', cv2.IMREAD_GRAYSCALE)
    
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.title('model')
    plt.show()
    
showImage4()
