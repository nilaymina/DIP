import cv2
import numpy as np

resim = cv2.imread("duvar.jpeg", 0)
yumusamis = cv2.GaussianBlur(resim, (3, 3), 0)

log = np.array([
    [ 0,  0, -1, -1, -1,  0,  0],
    [ 0, -2, -3, -3, -3, -2,  0],
    [-1, -3,  5,  5,  5, -3, -1],
    [-1, -3,  5, 16,  5, -3, -1],
    [-1, -3,  5,  5,  5, -3, -1],
    [ 0, -2, -3, -3, -3, -2,  0],
    [ 0,  0, -1, -1, -1,  0,  0]
])

sonuc1 = cv2.filter2D(resim, cv2.CV_32F, log)
sonuc1 = cv2.convertScaleAbs(sonuc1)
cv2.imshow("LoG 7x7", sonuc1)

prewitt = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

sonuc2 = cv2.filter2D(resim, cv2.CV_32F, prewitt)
sonuc2 = cv2.convertScaleAbs(sonuc2)

sonuc3 = cv2.filter2D(yumusamis, cv2.CV_32F, prewitt)
sonuc3 = cv2.convertScaleAbs(sonuc3)

cv2.imshow("Prewitt - Gauss Yok", sonuc2)
cv2.imshow("Prewitt - Gauss Var", sonuc3)

sobel = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])

sonuc4 = cv2.filter2D(resim, cv2.CV_32F, sobel)
sonuc4 = cv2.convertScaleAbs(sonuc4)

sonuc5 = cv2.filter2D(yumusamis, cv2.CV_32F, sobel)
sonuc5 = cv2.convertScaleAbs(sonuc5)

cv2.imshow("Sobel - Gauss Yok", sonuc4)
cv2.imshow("Sobel - Gauss Var", sonuc5)

laplacian = np.array([
    [ 0,  1, 0],
    [ 1, -4, 1],
    [ 0,  1, 0]
])

sonuc6 = cv2.filter2D(resim, cv2.CV_32F, laplacian)
sonuc6 = cv2.convertScaleAbs(sonuc6)

sonuc7 = cv2.filter2D(yumusamis, cv2.CV_32F, laplacian)
sonuc7 = cv2.convertScaleAbs(sonuc7)

cv2.imshow("Laplacian - Gauss Yok", sonuc6)
cv2.imshow("Laplacian - Gauss Var", sonuc7)

cv2.waitKey(0)
