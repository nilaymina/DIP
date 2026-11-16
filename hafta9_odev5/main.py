import cv2
import numpy as np

resim = cv2.imread("insan.jpeg")

B, G, R = cv2.split(resim.astype(np.int16))

maske_rgb = (
    (R > 95) & (G > 40) & (B > 20) &
    ((np.maximum(np.maximum(R, G), B) - np.minimum(np.minimum(R, G), B)) > 15) &
    (np.abs(R - G) > 15) &
    (R > G) & (R > B)
)

sonuc_rgb = resim.copy()
sonuc_rgb[~maske_rgb] = [0, 0, 255]

ycrcb = cv2.cvtColor(resim, cv2.COLOR_BGR2YCrCb)
maske_ycrcb = cv2.inRange(ycrcb, np.array([0, 133, 77]), np.array([255, 173, 127]))

sonuc_ycrcb = resim.copy()
sonuc_ycrcb[maske_ycrcb == 0] = [0, 0, 255]

hsv = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)
maske_hsv1 = cv2.inRange(hsv, np.array([0, 30, 60]), np.array([20, 255, 255]))
maske_hsv2 = cv2.inRange(hsv, np.array([170, 30, 60]), np.array([179, 255, 255]))
maske_hsv = cv2.bitwise_or(maske_hsv1, maske_hsv2)

sonuc_hsv = resim.copy()
sonuc_hsv[maske_hsv == 0] = [0, 0, 255]

cv2.imshow("Orijinal", resim)
cv2.imshow("RGB Sonuc", sonuc_rgb)
cv2.imshow("YCbCr Sonuc", sonuc_ycrcb)
cv2.imshow("HSV Sonuc", sonuc_hsv)

cv2.waitKey(0)
