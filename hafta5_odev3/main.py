import cv2

resim = cv2.imread("renkli_duvar.jpeg")

gri_resim1 = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gri Goruntu1", gri_resim1)
cv2.waitKey(0)








resim = cv2.imread("renkli_duvar.jpeg")

def griyeCevir(resim):
    yukseklik, genislik, kanal = resim.shape

    gri = resim[:, :, 0] * 0.114 + resim[:, :, 1] * 0.587 + resim[:, :, 2] * 0.299

    return gri.astype("uint8")

gri_resim2 = griyeCevir(resim)

cv2.imshow("Gri Goruntu2", gri_resim2)
cv2.waitKey(0)

hata = 0
for i in range(gri_resim1.shape[0]):
    for j in range(gri_resim1.shape[1]):
        hata += abs(int(gri_resim1[i, j]) - int(gri_resim2[i, j]))
print("Hata degeri =", hata)


