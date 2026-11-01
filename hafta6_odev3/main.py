
import cv2
import numpy as np

resim = cv2.imread("goz.jpg")
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

kenarlar = cv2.Canny(gray, 100, 200)
median_uygulanmis = cv2.medianBlur(kenarlar, 3)

resim_cember = resim.copy()

cemberler = cv2.HoughCircles(
    median_uygulanmis, 
    cv2.HOUGH_GRADIENT, 
    dp=1, 
    minDist=50, 
    param1=200, 
    param2=30, 
    minRadius=10, 
    maxRadius=100
)

if cemberler is not None:
    circles = np.uint16(np.around(cemberler ))
    for i in circles[0, :]:
        merkez = (i[0], i[1])
        yaricap = i[2]
        
        cv2.circle(resim_cember, merkez, yaricap, (0, 255, 0), 2)
        cv2.circle(resim_cember, merkez, 2, (0, 0, 255), 3)

cv2.imshow("Canny Kenarlar", kenarlar)
cv2.imshow("Median Filtreli Kenarlar", median_uygulanmis)
cv2.imshow("Bulunan Cemberler", resim_cember)

cv2.waitKey(0)
cv2.destroyAllWindows()