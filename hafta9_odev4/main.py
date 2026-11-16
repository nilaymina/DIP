import cv2
import numpy as np

resim_bgr = cv2.imread("mavi.jpg")
resim_rgb = cv2.cvtColor(resim_bgr, cv2.COLOR_BGR2RGB)
cv2.imwrite("mavi_rgb.bmp", resim_bgr)
resim_hsv = cv2.cvtColor(resim_bgr, cv2.COLOR_BGR2HSV)
resim_yuv = cv2.cvtColor(resim_bgr, cv2.COLOR_BGR2YUV)
resim_lab = cv2.cvtColor(resim_bgr, cv2.COLOR_BGR2Lab)
cv2.imwrite("mavi_hsv.bmp", resim_hsv)
yukseklik, genislik, _ = resim_rgb.shape
resim_hsi = np.zeros((yukseklik, genislik, 3), dtype=np.uint8)
rgb_norm = resim_rgb.astype(np.float32) / 255.0
cv2.imwrite("mavi_yuv.bmp", resim_yuv)

for y in range(yukseklik):
    for x in range(genislik):
        R, G, B = rgb_norm[y, x]
        I = (R + G + B) / 3.0
        sum_rgb = R + G + B
        if sum_rgb > 0:
            S = 1.0 - (3.0 / sum_rgb) * min(R, G, B)
        else:
            S = 0.0
        num = 0.5 * ((R - G) + (R - B))
        den = np.sqrt((R - G)**2 + (R - B) * (G - B)) + 1e-6
        theta = np.arccos(np.clip(num / den, -1.0, 1.0))
        if B <= G: H = theta
        else: H = 2 * np.pi - theta
        H = H / (2 * np.pi)
        resim_hsi[y, x, 0] = int(H * 255)
        resim_hsi[y, x, 1] = int(S * 255)
        resim_hsi[y, x, 2] = int(I * 255)

cv2.imwrite("mavi_cielab.bmp", resim_lab)
cv2.imwrite("mavi_hsi.bmp", resim_hsi)