
import cv2
import numpy as np

resim = cv2.imread("duvar.jpeg", 0)
cv2.imshow("Orijinal Resim", resim)

yumusamis = cv2.GaussianBlur(resim, (3, 3), 0)
cv2.imshow("Gauss Filtresi", yumusamis)

filtre = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

sonuc = cv2.filter2D(yumusamis, cv2.CV_32F, filtre)
sonuc = cv2.convertScaleAbs(sonuc)
cv2.imshow("Prewitt Filtresi", sonuc)

cv2.waitKey(0)

