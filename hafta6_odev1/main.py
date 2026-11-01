import cv2
import numpy as np

resim = cv2.imread("yol.jpg")
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

kenarlar = cv2.Canny(gray, threshold1=100, threshold2=200)
median_uygulanmis = cv2.medianBlur(kenarlar, 3)

resim_standard_hough = resim.copy()
resim_probabilistic_hough = resim.copy()

lines = cv2.HoughLines(median_uygulanmis, 1, np.pi/180, 150)
if lines is not None:
    for line in lines:
        rho, theta = line.flatten()
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a * rho, b * rho

        x1, y1 = int(x0 + 1000*(-b)), int(y0 + 1000*(a))
        x2, y2 = int(x0 - 1000*(-b)), int(y0 - 1000*(a))
        cv2.line(resim_standard_hough, (x1, y1), (x2, y2), (0, 0, 255), 2)

lines_p = cv2.HoughLinesP(median_uygulanmis, 1, np.pi/180, 50, minLineLength=50, maxLineGap=10)
if lines_p is not None:
    for line in lines_p:
        x1, y1, x2, y2 = line.flatten()
        cv2.line(resim_probabilistic_hough, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Standart Hough', resim_standard_hough)
cv2.imshow('Probabilistic Hough', resim_probabilistic_hough)

cv2.waitKey(0)
cv2.destroyAllWindows()