import cv2

resim = cv2.imread("kontrast.jpg", 0)

min_deger = resim.min()
max_deger = resim.max()

sonuc = (resim.astype(float) - min_deger) * 255 / (max_deger - min_deger)
sonuc = sonuc.astype("uint8")

cv2.imshow("Orijinal", resim)
cv2.imshow("Kontrast Germe", sonuc)

cv2.waitKey(0)