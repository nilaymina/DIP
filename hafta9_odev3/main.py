import time
import cv2
import numpy as np

width, height = 7680, 4320
input_path = "ornek_8k_resim.bmp"
output_path = "duzenlenmis_8k_resim.bmp"

ornek_8k_resim = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
cv2.imwrite(input_path, ornek_8k_resim)

del ornek_8k_resim

resim = cv2.imread(input_path, cv2.IMREAD_COLOR)

start_time = time.perf_counter()

duzenlenmis_8k_resim = resim // 2

end_time = time.perf_counter()
elapsed_time_ms = (end_time - start_time) * 1000

cv2.imwrite(output_path, duzenlenmis_8k_resim)

print(f"Görüntü Boyutu : {resim.shape[1]}x{resim.shape[0]} ({resim.shape[2]} kanal)")
print(f"Toplam Piksel  : {resim.shape[0] * resim.shape[1]:,}")
print(f"İşlem Süresi   : {elapsed_time_ms:.4f} ms ({end_time - start_time:.6f} saniye)")