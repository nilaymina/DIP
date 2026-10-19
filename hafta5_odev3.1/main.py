import cv2

resim = cv2.imread("renkli_duvar.jpeg")

gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gri Goruntu", gri_resim)
cv2.waitKey(0)