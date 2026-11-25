
import cv2
import numpy as np
import matplotlib.pyplot as plt

left = cv2.imread("scene1.row3.col1.jpeg", 0)
right = cv2.imread("scene1.row3.col3.jpeg", 0)

def block_matching(left, right):
    height, width = left.shape

    block_size = 7
    max_disparity = 64
    half = block_size // 2

    disparity = np.zeros((height, width), dtype=np.uint8)

    for y in range(half, height - half):
        for x in range(max_disparity + half, width - half):
            left_block = left[
                y-half:y+half+1,
                x-half:x+half+1
            ]

            min_difference = float("inf")
            best_disparity = 0

            for d in range(max_disparity):
                right_block = right[
                    y-half:y+half+1,
                    x-d-half:x-d+half+1
                ]

                difference = np.sum(
                    np.abs(
                        left_block.astype(int) -
                        right_block.astype(int)
                    )
                )

                if difference < min_difference:
                    min_difference = difference
                    best_disparity = d

            disparity[y, x] = best_disparity

    return disparity

disparity = block_matching(left, right)

disparity = cv2.normalize(
    disparity, None, 0, 255,
    cv2.NORM_MINMAX, dtype=cv2.CV_8U
)

plt.imshow(disparity, cmap="gray")
plt.title("Block Matching")
plt.axis("off")
plt.show()