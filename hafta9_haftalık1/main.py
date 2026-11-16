import cv2
import numpy as np

video = cv2.VideoCapture(0)
okundu, onceki_cerceve = video.read()

if not okundu:
    video.release()
    exit()

onceki_gray = cv2.cvtColor(onceki_cerceve, cv2.COLOR_BGR2GRAY)
onceki_gray = cv2.GaussianBlur(onceki_gray, (21, 21), 0)

MIN_PIXEL_COUNT = 1500
lower_skin = np.array([0, 133, 77], dtype=np.uint8)
upper_skin = np.array([255, 173, 127], dtype=np.uint8)

while True:
    okundu, cerceve = video.read()
    if not okundu:
        break

    gray = cv2.cvtColor(cerceve, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    diff = cv2.absdiff(onceki_gray, gray)
    motion_mask = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]
    motion_mask = cv2.dilate(motion_mask, None, iterations=2)

    changed_pixels = cv2.countNonZero(motion_mask)

    if changed_pixels > MIN_PIXEL_COUNT:
        roi = cv2.bitwise_and(cerceve, cerceve, mask=motion_mask)

        ycrcb_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2YCrCb)
        skin_mask = cv2.inRange(ycrcb_roi, lower_skin, upper_skin)
        skin_mask = cv2.bitwise_and(skin_mask, motion_mask)

        output = roi.copy()
        output[skin_mask > 0] = [0, 255, 0]
    else:
        output = np.zeros_like(cerceve)

    cv2.imshow("ROI", output)
    onceki_gray = gray.copy()

    if cv2.waitKey(1) == ord("q"):
        break

video.release()
