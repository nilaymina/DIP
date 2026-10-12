import cv2
import numpy as np

resim = cv2.imread("duvar.jpeg", 0)

yumusamis = cv2.GaussianBlur(resim, (3, 3), 0)
cv2.imshow("Gauss Filtresi", yumusamis)

laplacian = np.array([
    [0,  1, 0],
    [1, -4, 1],
    [0,  1, 0]
])

sonuc1 = cv2.filter2D(yumusamis, cv2.CV_32F, laplacian)
sonuc1 = cv2.convertScaleAbs(sonuc1)
cv2.imshow("Laplacian", sonuc1)

prewitt = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

sonuc2 = cv2.filter2D(yumusamis, cv2.CV_32F, prewitt)
sonuc2 = cv2.convertScaleAbs(sonuc2)
cv2.imshow("Prewitt", sonuc2)

sobel = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])

sonuc3 = cv2.filter2D(yumusamis, cv2.CV_32F, sobel)
sonuc3 = cv2.convertScaleAbs(sonuc3)
cv2.imshow("Sobel", sonuc3)

cv2.waitKey(0)

