import cv2

resim = cv2.imread("renkli_duvar.jpeg")

mavi, yesil, kirmizi = cv2.split(resim)

hist_mavi = cv2.calcHist([mavi], [0], None, [256], [0, 256])
hist_yesil = cv2.calcHist([yesil], [0], None, [256], [0, 256])
hist_kirmizi = cv2.calcHist([kirmizi], [0], None, [256], [0, 256])

print("Mavi kanal histogramı:")
print(hist_mavi)

print("Yeşil kanal histogramı:")
print(hist_yesil)

print("Kırmızı kanal histogramı:")
print(hist_kirmizi)