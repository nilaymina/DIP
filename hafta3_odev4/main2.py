import cv2
import numpy as np

resim = cv2.imread("/Users/user/Desktop/opencv_odev/hafta3_odev4/dag.jpeg", 0)
satir, sutun = resim.shape
sonuc = np.zeros_like(resim)

for i in range(1, satir - 1):
    for j in range(1, sutun - 1):
        toplam = 0

        for x in range(-1, 2):
            for y in range(-1, 2):
                toplam += int(resim[i + x, j + y])

        sonuc[i, j] = toplam // 9

cv2.imwrite("filtrelenmis.jpg", sonuc)

cv2.imshow("Gurultulu Resim", resim)
cv2.imshow("Filtrelenmis Resim", sonuc)
print("Orijinal piksel:", resim[100, 100])
print("Filtrelenmiş piksel:", sonuc[100, 100])
cv2.waitKey(0)