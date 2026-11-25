import cv2
import matplotlib.pyplot as plt

left = cv2.imread("scene1.row3.col1.jpeg", 0)
right = cv2.imread("scene1.row3.col3.jpeg", 0)

stereoBM = cv2.StereoBM_create(
    numDisparities=64,
    blockSize=15
)
disparityBM = stereoBM.compute(left, right)

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

disparityBM = cv2.normalize(
    disparityBM, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U
)
disparitySGBM = cv2.normalize(
    disparitySGBM, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U
)

plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
plt.imshow(left, cmap="gray")
plt.title("Sol Görüntü")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(disparityBM, cmap="gray")
plt.title("StereoBM Disparity Map")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(disparitySGBM, cmap="gray")
plt.title("StereoSGBM Disparity Map")
plt.axis("off")

plt.tight_layout()
plt.show()