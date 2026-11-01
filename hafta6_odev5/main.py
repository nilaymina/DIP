import cv2
import numpy as np
import math

resim = cv2.imread("goz.jpg")
sonuc = resim.copy()
gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
gri = cv2.GaussianBlur(gri, (5, 5), 1.5)

kenarlar = cv2.Canny(gri, 80, 150)
yukseklik, genislik = gri.shape

min_yaricap = 10
max_yaricap = 60
acilar = range(0, 360, 5)

sin_degerleri = []
cos_degerleri = []

for aci in acilar:
    radyan = math.radians(aci)
    sin_degerleri.append(math.sin(radyan))
    cos_degerleri.append(math.cos(radyan))

oylama = np.zeros(
    (yukseklik, genislik, max_yaricap + 1),
    dtype=np.int32
)

y_idxs, x_idxs = np.nonzero(kenarlar)

for idx in range(len(x_idxs)):
    x = x_idxs[idx]
    y = y_idxs[idx]
    for r in range(min_yaricap, max_yaricap + 1):
        for i in range(len(sin_degerleri)):
            sin = sin_degerleri[i]
            cos = cos_degerleri[i]

            merkez_x1 = int(x - r * cos)
            merkez_y1 = int(y - r * sin)

            if (0 <= merkez_x1 < genislik and
                0 <= merkez_y1 < yukseklik):
                oylama[merkez_y1, merkez_x1, r] += 1

            merkez_x2 = int(x + r * cos)
            merkez_y2 = int(y + r * sin)

            if (0 <= merkez_x2 < genislik and
                0 <= merkez_y2 < yukseklik):
                oylama[merkez_y2, merkez_x2, r] += 1

esik = 15

y_coords, x_coords, r_indices = np.where(oylama >= esik)

for i in range(len(y_coords)):
    cy = y_coords[i]
    cx = x_coords[i]
    r = r_indices[i]
    
    cv2.circle(sonuc, (cx, cy), r, (0, 255, 0), 2)
    cv2.circle(sonuc, (cx, cy), 2, (0, 0, 255), -1)

cv2.imshow("Canny Kenarlar", kenarlar)
cv2.imshow("Es Merkezli Cemberler", sonuc)

cv2.waitKey(0)
cv2.destroyAllWindows()