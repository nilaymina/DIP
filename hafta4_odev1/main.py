
import cv2
import numpy as np

resim = cv2.imread("bw.jpeg", 0)
cv2.imshow("Orijinal Resim", resim)

yumusamis = cv2.GaussianBlur(resim, (3, 3), 0)
cv2.imshow("Gauss Filtresi", yumusamis)

filtre = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

sonuc = cv2.filter2D(yumusamis, -1, filtre)

cv2.imshow("Prewitt Filtresi", sonuc)

cv2.waitKey(0)

