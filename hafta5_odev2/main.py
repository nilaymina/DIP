import cv2

resim = cv2.imread("renkli_duvar.jpeg")

mavi, yesil, kirmizi = cv2.split(resim)

def calcHist(kanal):
    histogram = [0] * 256

    for satir in kanal:
        for piksel in satir:
            histogram[piksel] += 1

    return histogram

hist_mavi = calcHist(mavi)
hist_yesil = calcHist(yesil)
hist_kirmizi = calcHist(kirmizi)

print("Mavi kanal histogramı:", hist_mavi)
print("Yeşil kanal histogramı:", hist_yesil)
print("Kırmızı kanal histogramı:", hist_kirmizi)