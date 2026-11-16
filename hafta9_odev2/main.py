import os
import cv2

kaynak_foto = "mavi.jpg"
renkli_yol = "renkli_1000x1000.bmp"
gri_yol = "gri_1000x1000.bmp"

resim = cv2.imread(kaynak_foto, cv2.IMREAD_COLOR)

resim_1000 = cv2.resize(resim, (1000, 1000))
cv2.imwrite(renkli_yol, resim_1000)

renkli_resim = cv2.imread(renkli_yol, cv2.IMREAD_COLOR)

cv2.imshow("Renkli BMP Resim (1000x1000)", renkli_resim)

gri_resim = cv2.cvtColor(renkli_resim, cv2.COLOR_BGR2GRAY)
cv2.imwrite(gri_yol, gri_resim)

cv2.imshow("Gri Tonlu BMP Resim (1000x1000)", gri_resim)

renkli_boyut = os.path.getsize(renkli_yol)
gri_boyut = os.path.getsize(gri_yol)

print(f"Renkli Resim -> Boyut (Shape): {renkli_resim.shape} | Disk: {renkli_boyut:,} byte ({renkli_boyut / (1024**2):.2f} MiB)")
print(f"Gri Resim    -> Boyut (Shape): {gri_resim.shape}    | Disk: {gri_boyut:,} byte ({gri_boyut / 1024:.2f} KiB)")
print(f"Boyut Oranı  -> Renkli / Gri = {renkli_boyut / gri_boyut:.2f} kat")

cv2.waitKey(0)
