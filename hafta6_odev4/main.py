import cv2
import numpy as np
import math

resim = cv2.imread("goz.jpg")
sonuc = resim.copy()
gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
gri = cv2.GaussianBlur(gri, (5, 5), 1.5)

kenarlar = cv2.Canny(gri, 80, 150)
yukseklik, genislik = gri.shape

min_yaricap = 15
max_yaricap = 80
acilar = range(0, 360, 10)

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

for y in range(yukseklik):
    for x in range(genislik):
        if kenarlar[y, x] == 0:
            continue

        for r in range(min_yaricap, max_yaricap + 1):
            for i in range(len(sin_degerleri)):
                sin = sin_degerleri[i]
                cos = cos_degerleri[i]

                merkez_x = int(x - r * cos)
                merkez_y = int(y - r * sin)

                if (0 <= merkez_x < genislik and
                    0 <= merkez_y < yukseklik):
                    oylama[merkez_y, merkez_x, r] += 1

                merkez_x = int(x + r * cos)
                merkez_y = int(y + r * sin)

                if (0 <= merkez_x < genislik and
                    0 <= merkez_y < yukseklik):
                    oylama[merkez_y, merkez_x, r] += 1


esik = 20

for y in range(yukseklik):
    for x in range(genislik):
        for r in range(min_yaricap, max_yaricap + 1):
            if oylama[y, x, r] >= esik:
                cv2.circle(sonuc, (x, y), r, (0, 255, 0), 2)
                cv2.circle(sonuc, (x, y), 2, (0, 0, 255), -1)

cv2.imshow("Kenarlar", kenarlar)
cv2.imshow("Bulunan Cemberler", sonuc)

cv2.waitKey(0)
cv2.destroyAllWindows()