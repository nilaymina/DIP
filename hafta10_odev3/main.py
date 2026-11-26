import cv2
import numpy as np
import matplotlib.pyplot as plt

left = cv2.imread("scene1.row3.col1.jpeg", 0)
right = cv2.imread("scene1.row3.col3.jpeg", 0)


def block_matching(left, right, method):
    height, width = left.shape

    block_size = 7
    max_disparity = 32
    half = block_size // 2

    disparity = np.zeros((height, width), dtype=np.uint8)

    for y in range(half, height - half):
        for x in range(max_disparity + half, width - half):
            left_block = left[
                y - half : y + half + 1,
                x - half : x + half + 1
            ].astype(float)

            best_score = None
            best_disparity = 0

            for d in range(max_disparity):
                right_block = right[
                    y - half : y + half + 1,
                    x - d - half : x - d + half + 1
                ].astype(float)

                if method == "SAD":
                    score = np.sum(
                        np.abs(left_block - right_block)
                    )
                elif method == "SSD":
                    score = np.sum(
                        (left_block - right_block) ** 2
                    )
                elif method == "ZNCC":
                    left_centered = left_block - np.mean(left_block)
                    right_centered = right_block - np.mean(right_block)

                    pay = np.sum(left_centered * right_centered)

                    payda = np.sqrt(
                        np.sum(left_centered ** 2) *
                        np.sum(right_centered ** 2)
                    )

                    if payda == 0:
                        score = -1
                    else:
                        score = pay / payda

                if method == "ZNCC":
                    if best_score is None or score > best_score:
                        best_score = score
                        best_disparity = d
                else:
                    if best_score is None or score < best_score:
                        best_score = score
                        best_disparity = d

            disparity[y, x] = best_disparity

    return disparity


sad = block_matching(left, right, "SAD")
ssd = block_matching(left, right, "SSD")
zncc = block_matching(left, right, "ZNCC")

sad = cv2.normalize(sad, None, 0, 255, cv2.NORM_MINMAX)
ssd = cv2.normalize(ssd, None, 0, 255, cv2.NORM_MINMAX)
zncc = cv2.normalize(zncc, None, 0, 255, cv2.NORM_MINMAX)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(left, cmap="gray")
plt.title("Sol Görüntü")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(sad, cmap="gray")
plt.title("SAD Disparity Map")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(ssd, cmap="gray")
plt.title("SSD Disparity Map")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(zncc, cmap="gray")
plt.title("ZNCC Disparity Map")
plt.axis("off")

plt.tight_layout()
plt.show()