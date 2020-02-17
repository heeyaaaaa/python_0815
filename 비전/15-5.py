
import numpy as np
import cv2

# 라플라시안 피라미드

def pyramid():
    A = cv2.imread('사과.png')
    tmpA = A.copy()
    B = cv2.imread('오렌지.png')
    tmpB = B.copy()
    
    g_downA = []
    g_upA = []
    img_shapeA = []
    
    g_downB = []
    g_upB = []
    img_shapeB = []
    
    g_downA.append(tmpA)
    img_shapeA.append(tmpA.shape)
    
    g_downB.append(tmpB)
    img_shapeB.append(tmpB.shape)
    
    for i in range(6):
        tmp1 = cv2.pyrDown(tmpA)
        g_downA.append(tmp1)
        img_shapeA.append(tmp1.shape)
        tmpA = tmp1
          
    for i in range(6):
        tmpA = g_downA[i+1]
        tmp1 = cv2.pyrUp(tmpA)
        tmpA = cv2.resize(tmp1, dsize=(img_shapeA[i][1], img_shapeA[i][0]), interpolation = cv2.INTER_CUBIC)
        g_upA.append(tmpA)
    
    for i in range(6):
        tmp1 = cv2.pyrDown(tmpB)
        g_downB.append(tmp1)
        img_shapeB.append(tmp1.shape)
        tmpB = tmp1
          
    for i in range(6):
        tmpB = g_downB[i+1]
        tmp1 = cv2.pyrUp(tmpB)
        tmpB = cv2.resize(tmp1, dsize=(img_shapeB[i][1], img_shapeB[i][0]), interpolation = cv2.INTER_CUBIC)
        g_upB.append(tmpB)
    
    LS = []
    for i in range(6):
        tmpA = cv2.subtract(g_downA[i], g_upA[i])
        tmpB = cv2.subtract(g_downB[i], g_upB[i])
        rows, cols, dpt = tmpA.shape
        ls = np.hstack((tmpA[:, :int(cols/2)], tmpB[:, int(cols/2):]))
        LS.append(ls)

    ls_ = LS[5]
    for i in range(5):
        ls_ = cv2.pyrUp(ls_)
        ls_ = cv2.resize(ls_, dsize=(LS[4-i].shape[1], LS[4-i].shape[0]), interpolation = cv2.INTER_CUBIC)
        ls_ = cv2.add(ls_, LS[4-i])
        
    real = np.hstack((A[:, :int(A.shape[1] / 2)], B[:, int(A.shape[1] / 2):]))
        
    cv2.imshow('Pyramid_blending2.jpg', ls_)
    cv2.imshow('Direct_blending.jpg', real)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
pyramid()


