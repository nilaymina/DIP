import cv2
import numpy as np
import time

resim = cv2.imread("duvar.jpeg", 0)

baslangic = time.time()
canny = cv2.Canny(resim, 100, 200)
canny_sure = time.time() - baslangic

prewitt = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

baslangic = time.time()
sonuc1 = cv2.filter2D(resim, cv2.CV_32F, prewitt)
sonuc1 = cv2.convertScaleAbs(sonuc1)
prewitt_sure = time.time() - baslangic

sobel = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])

baslangic = time.time()
sonuc2 = cv2.filter2D(resim, cv2.CV_32F, sobel)
sonuc2 = cv2.convertScaleAbs(sonuc2)
sobel_sure = time.time() - baslangic

laplacian = np.array([
    [ 0,  1, 0],
    [ 1, -4, 1],
    [ 0,  1, 0]
])

baslangic = time.time()
sonuc3 = cv2.filter2D(resim, cv2.CV_32F, laplacian)
sonuc3 = cv2.convertScaleAbs(sonuc3)
laplacian_sure = time.time() - baslangic

cv2.imshow("Orijinal Resim", resim)
cv2.imshow("Canny", canny)
cv2.imshow("Prewitt", sonuc1)
cv2.imshow("Sobel", sonuc2)
cv2.imshow("Laplacian", sonuc3)

print("Canny suresi:", canny_sure)
print("Prewitt suresi:", prewitt_sure)
print("Sobel suresi:", sobel_sure)
print("Laplacian suresi:", laplacian_sure)

cv2.waitKey(0)

