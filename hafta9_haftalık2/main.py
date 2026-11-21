import cv2
import numpy as np
import os

dataset = "dataset"

resim_sayisi = 0

for klasor_path, alt_klasorler, dosyalar in os.walk(dataset):

    for dosya in dosyalar:

        if dosya.lower().endswith((".jpg", ".jpeg")):

            resim_path = os.path.join(klasor_path, dosya)

            resim = cv2.imread(resim_path)

            if resim is None:
                continue

            resim_sayisi += 1

            hsv_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2HSV)

            alt_kirmizi_filtre = cv2.inRange(hsv_resim, np.array([0, 70, 50]), np.array([10, 255, 255]))
            ust_kirmizi_filtre = cv2.inRange(hsv_resim, np.array([170, 70, 50]), np.array([180, 255, 255]))

            hsv_filtre = cv2.bitwise_or(alt_kirmizi_filtre, ust_kirmizi_filtre)

            ycrcb_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2YCrCb)

            ycrcb_filtre = cv2.inRange(
                ycrcb_resim,
                np.array([0, 140, 0]),
                np.array([255, 255, 135])
            )

            rgb_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)

            kirmizi_kanal, yesil_kanal, mavi_kanal = cv2.split(rgb_resim)

            rgb_filtre = (
                (kirmizi_kanal > 100) &
                (kirmizi_kanal > yesil_kanal * 1.35) &
                (kirmizi_kanal > mavi_kanal * 1.35)
            ).astype(np.uint8) * 255

            combined_filtre = cv2.bitwise_or(hsv_filtre, ycrcb_filtre)
            combined_filtre = cv2.bitwise_or(combined_filtre, rgb_filtre)

            gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
            gri_resim = cv2.GaussianBlur(gri_resim, (5, 5), 1.5)

            daireler = cv2.HoughCircles(
                gri_resim,
                cv2.HOUGH_GRADIENT,
                dp=1.2,
                minDist=20,
                param1=100,
                param2=25,
                minRadius=5,
                maxRadius=0
            )

            isaret_sayisi = 0

            if daireler is not None:

                for merkez_x, merkez_y, yaricap in np.round(daireler[0]).astype(int):

                    kirmizi_piksel_sayisi = 0
                    toplam_piksel_sayisi = 0

                    for aci in np.linspace(0, 2 * np.pi, 120):

                        piksel_x = int(merkez_x + yaricap * np.cos(aci))
                        piksel_y = int(merkez_y + yaricap * np.sin(aci))

                        if 0 <= piksel_x < resim.shape[1] and 0 <= piksel_y < resim.shape[0]:

                            toplam_piksel_sayisi += 1

                            if combined_filtre[piksel_y, piksel_x] > 0:
                                kirmizi_piksel_sayisi += 1

                    if toplam_piksel_sayisi > 0 and (kirmizi_piksel_sayisi / toplam_piksel_sayisi) >= 0.25:
                        isaret_sayisi += 1

            if isaret_sayisi > 0:
                print(dosya, "->", isaret_sayisi, "adet isaret tespit edildi.")
            else:
                print(dosya, "-> isaret tespit edilmedi.")