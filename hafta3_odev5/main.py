import cv2
import numpy as np

resim = cv2.imread("salt_and_pepper.png")

hazir_medyan = cv2.medianBlur(resim, 5)


def medyan_filtre_5x5(goruntu):
  h, w = goruntu.shape[:2]
  cikti = goruntu.copy()

  for i in range(2, h - 2):
    for j in range(2, w - 2):
      kernel = goruntu[i - 2 : i + 3, j - 2 : j + 3]
      cikti[i, j] = np.median(kernel, axis=(0, 1))

  return cikti


ozel_medyan = medyan_filtre_5x5(resim)

cv2.imshow("Orijinal Goruntu", resim)
cv2.imshow("Hazir Medyan", hazir_medyan)
cv2.imshow("Ozel Medyan Filtre", ozel_medyan)

cv2.waitKey(0)  
