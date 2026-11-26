import cv2
import matplotlib.pyplot as plt
import numpy as np

left = cv2.imread("scene1.row3.col1.jpeg", 0)
right = cv2.imread("scene1.row3.col3.jpeg", 0)

left = cv2.resize(left, (0, 0), fx=0.25, fy=0.25)
right = cv2.resize(right, (0, 0), fx=0.25, fy=0.25)

h, w = left.shape

max_d = 32
window = 5

P1 = 200
P2 = 800

cost = np.zeros((h, w, max_d), dtype=np.float32)

for d in range(max_d):
    fark = np.zeros((h, w), dtype=np.float32)

    if d == 0:
        fark = np.abs(left.astype(np.float32) - right.astype(np.float32))
    else:
        fark[:, d:] = np.abs(
            left[:, d:].astype(np.float32) - right[:, :-d].astype(np.float32)
        )

    cost[:, :, d] = cv2.boxFilter(
        fark, -1, (window, window), normalize=False
    )

    if d > 0:
        cost[:, :d, d] = 1000000


def aggregate(cost, dy, dx):
    h, w, D = cost.shape
    result = np.zeros_like(cost)

    ys = range(h) if dy >= 0 else range(h - 1, -1, -1)
    xs = range(w) if dx >= 0 else range(w - 1, -1, -1)

    for y in ys:
        for x in xs:
            py = y - dy
            px = x - dx

            if py < 0 or py >= h or px < 0 or px >= w:
                result[y, x] = cost[y, x]
                continue

            onceki = result[py, px]
            min_onceki = np.min(onceki)

            for d in range(D):
                ayni = onceki[d]

                sol = onceki[d - 1] + P1 if d > 0 else 1000000
                sag = onceki[d + 1] + P1 if d < D - 1 else 1000000

                farkli = min_onceki + P2

                result[y, x, d] = (
                    cost[y, x, d] + min(ayni, sol, sag, farkli) - min_onceki
                )

    return result


toplam = np.zeros_like(cost)

yonler = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for dy, dx in yonler:
    toplam += aggregate(cost, dy, dx)

disparity = np.argmin(toplam, axis=2).astype(np.uint8)

disparity_goruntu = cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(left, cmap="gray")
plt.title("Sol Görüntü")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(disparity_goruntu, cmap="gray")
plt.title("SGBM")
plt.axis("off")

plt.tight_layout()
plt.show()