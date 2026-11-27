import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

left = cv2.imread("scene1.row3.col1.jpeg", 0)
right = cv2.imread("scene1.row3.col3.jpeg", 0)

edges_left = cv2.Canny(left, 100, 200)
edges_right = cv2.Canny(right, 100, 200)

def sparse_stereo(left, right, edges_left, edges_right):
    height, width = left.shape
    block_size = 7
    max_disparity = 64
    half = block_size // 2

    disparity = np.zeros((height, width), dtype=np.uint8)

    for y in range(half, height - half):
        for x in range(max_disparity + half, width - half):
            if edges_left[y, x] == 0:
                continue

            left_block = left[y-half:y+half+1, x-half:x+half+1].astype(int)
            min_diff = 999999
            best_d = 0

            for d in range(max_disparity):
                if edges_right[y, x-d] == 0:
                    continue

                right_block = right[y-half:y+half+1, x-d-half:x-d+half+1].astype(int)
                diff = np.sum(np.abs(left_block - right_block))

                if diff < min_diff:
                    min_diff = diff
                    best_d = d

            if min_diff != 999999:
                disparity[y, x] = best_d

    return disparity

def block_matching(left, right):
    height, width = left.shape
    block_size = 7
    max_disparity = 64
    half = block_size // 2

    disparity = np.zeros((height, width), dtype=np.uint8)

    for y in range(half, height - half):
        for x in range(max_disparity + half, width - half):
            left_block = left[y-half:y+half+1, x-half:x+half+1]
            min_diff = 999999
            best_d = 0

            for d in range(max_disparity):
                right_block = right[y-half:y+half+1, x-d-half:x-d+half+1]
                diff = np.sum(np.abs(left_block.astype(int) - right_block.astype(int)))

                if diff < min_diff:
                    min_diff = diff
                    best_d = d

            disparity[y, x] = best_d

    return disparity

t1 = time.time()
disparitySparse = sparse_stereo(left, right, edges_left, edges_right)
sparse_time = time.time() - t1

t2 = time.time()
disparityDense = block_matching(left, right)
dense_time = time.time() - t2

t3 = time.time()
stereoBM = cv2.StereoBM_create(numDisparities=64, blockSize=15)
disparityBM = stereoBM.compute(left, right)
bm_time = time.time() - t3

t4 = time.time()
block_size = 5
stereoSGBM = cv2.StereoSGBM_create(
    minDisparity=0,
    numDisparities=64,
    blockSize=block_size,
    P1=8 * 1 * block_size ** 2,
    P2=32 * 1 * block_size ** 2,
    mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
)
disparitySGBM = stereoSGBM.compute(left, right)
sgbm_time = time.time() - t4

disparitySparse = cv2.normalize(disparitySparse, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
disparityDense = cv2.normalize(disparityDense, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
disparityBM = cv2.normalize(disparityBM, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
disparitySGBM = cv2.normalize(disparitySGBM, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

plt.figure(figsize=(14, 7))

plt.subplot(2, 3, 1)
plt.imshow(edges_left, cmap="gray")
plt.title("Canny Edge Detection")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(disparitySparse, cmap="gray")
plt.title("Sparse Stereo (Manual)")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(disparityDense, cmap="gray")
plt.title("Dense Stereo - Manual BM")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(disparityBM, cmap="gray")
plt.title("Dense Stereo - OpenCV BM")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(disparitySGBM, cmap="gray")
plt.title("Dense Stereo - OpenCV SGBM")
plt.axis("off")

plt.tight_layout()
plt.show()

print("Sparse Stereo (Manual):", round(sparse_time, 4), "seconds")
print("Dense Stereo (Manual BM):", round(dense_time, 4), "seconds")
print("Dense Stereo (OpenCV BM):", round(bm_time, 4), "seconds")
print("Dense Stereo (OpenCV SGBM):", round(sgbm_time, 4), "seconds")