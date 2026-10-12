import cv2
import numpy as np

resim = cv2.imread("duvar.jpeg", 0)
cv2.imshow("Orijinal Resim", resim)

yumusamis = cv2.GaussianBlur(resim, (3, 3), 0)
cv2.imshow("Gauss Filtresi", yumusamis)

yatay = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])

dikey = np.array([
    [-1,  0,  1],
    [-2,  0,  2],
    [-1,  0,  1]
])

sonuc1 = cv2.filter2D(yumusamis, cv2.CV_32F, yatay)
sonuc1 = cv2.convertScaleAbs(sonuc1)

sonuc2 = cv2.filter2D(yumusamis, cv2.CV_32F, dikey)
sonuc2 = cv2.convertScaleAbs(sonuc2)

cv2.imshow("Yatay Sobel", sonuc1)
cv2.imshow("Dikey Sobel", sonuc2)

cv2.waitKey(0)

