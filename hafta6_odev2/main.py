import cv2
import numpy as np

resim = cv2.imread("yol.jpg")
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
kenarlar = cv2.Canny(gray, 100, 200)

h, w = kenarlar.shape
max_rho = int(np.sqrt(h**2 + w**2))
thetas = np.deg2rad(np.arange(0, 180))

cos_t = np.cos(thetas)
sin_t = np.sin(thetas)

oylama_islemi = np.zeros((2 * max_rho + 1, len(thetas)), dtype=np.uint32)
y_idx, x_idx = np.nonzero(kenarlar)

for i in range(len(x_idx)):
    x, y = x_idx[i], y_idx[i]
    for t in range(len(thetas)):
        rho = int(round(x * cos_t[t] + y * sin_t[t]))
        oylama_islemi[rho + max_rho, t] += 1

oylama_matris_resim = cv2.normalize(oylama_islemi, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
cv2.imwrite("oylama_matris.jpg", oylama_matris_resim)

sonuc = resim.copy()
rho_idx, t_idx = np.where(oylama_islemi > 130)

for i in range(len(rho_idx)):
    rho = rho_idx[i] - max_rho
    t = thetas[t_idx[i]]
    a, b = cos_t[t_idx[i]], sin_t[t_idx[i]]
    x0, y0 = a * rho, b * rho
    x1, y1 = int(x0 + 1000 * (-b)), int(y0 + 1000 * (a))
    x2, y2 = int(x0 - 1000 * (-b)), int(y0 - 1000 * (a))
    cv2.line(sonuc, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("Dogrular", sonuc)
cv2.imshow("Hough Oylama Matrisi", oylama_matris_resim)
cv2.imshow("Canny Kenarlar", kenarlar)


cv2.waitKey(0)
cv2.destroyAllWindows()