import cv2
import numpy as np

resim = cv2.imread("/Users/user/Desktop/opencv_odev/hafta3_odev2/dag.jpeg", 0)

histogram = [0] * 256

for i in range(resim.shape[0]):
    for j in range(resim.shape[1]):
        histogram[resim[i, j]] += 1

cdf = [0] * 256
cdf[0] = histogram[0]

for i in range(1, 256):
    cdf[i] = cdf[i - 1] + histogram[i]

cdf_min = 0

for i in range(256):
    if cdf[i] > 0:
        cdf_min = cdf[i]
        break

yeni_resim = np.zeros_like(resim)

for i in range(resim.shape[0]):
    for j in range(resim.shape[1]):
        eski_deger = resim[i, j]

        yeni_deger = int(
            (cdf[eski_deger] - cdf_min) /
            (resim.size - cdf_min) * 255
        )

        yeni_resim[i, j] = yeni_deger

cv2.imwrite("esitlenmis.jpg", yeni_resim)

cv2.imshow("Eski", resim)
cv2.imshow("Yeni", yeni_resim)

cv2.waitKey(0)