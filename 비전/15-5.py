import numpy as np
import cv2
    
def pyramid():
    
    A = cv2.imread('사과.png')
    B = cv2.imread('오렌지.png')
    
    
    B = cv2.resize(B, dsize = (A.shape[1], A.shape[0]),
                   interpolation = cv2.INTER_CUBIC)
    
    G = A.copy()
    gpA = [G]
    for i in range(6):
        G = cv2.pyrDown(G)
        gpA.append(G)
        
    G = B.copy()
    gpB = [G]
    for i in range(6):
        G = cv2.pyrDown(G)
        gpB.append(G)
        
    lpA = [gpA[5]]
    for i in range(5, 0, -1):
        GE = cv2.pyrUp(gpA[i])
        L = cv2.subtract(gpA[i-1], GE)
        lpA.append(L)
        
    lpB = [gpB[5]]
    for i in range(5, 0, -1):
        GE = cv2.pyrUp(gpB[i])
        L = cv2.subtract(gpB[i-1], GE)
        lpB.append(L)
        
    LS = []
    for la, lb in zip(lpA, lpB):
        rows, cols, dpt = la.shape
        ls = np.hstack((la[:, :int(cols/2)], lb[:,int(cols/2):]))
        LS.append(ls)
        
    ls_ = LS[0]
    for i in range(1,6):
        ls_ = cv2.pyrUp(ls_)
        ls_ = cv2.add(ls_, LS[i])
        
    real = np.hstack((A[:, :int(cols / 2)], B[:, int(cols / 2):]))
        
    cv2.imshow('Pyramid_blending2.jpg', ls_)
    cv2.imshow('Direct_blending.jpg', real)
    
pyramid()