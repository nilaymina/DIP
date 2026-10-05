import cv2

resim = cv2.imread("/Users/user/Desktop/opencv_odev/hafta3_odev3/dag.jpeg", 0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

yeni_resim = clahe.apply(resim)

cv2.imwrite("clahe_hazir.jpg", yeni_resim)

cv2.imshow("Orijinal", resim)
cv2.imshow("CLAHE", yeni_resim)

cv2.waitKey(0)