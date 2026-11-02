import cv2
import numpy as np
import matplotlib.pyplot as plt

def dft_1d(signal):
    N = signal.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * k * n / N)
    return np.dot(W, signal)

def dft_2d(image):
    image = np.asarray(image, dtype=float)
    M, N = image.shape
    F = np.zeros((M, N), dtype=complex)
    for x in range(M):
        F[x, :] = dft_1d(image[x, :])
    for y in range(N):
        F[:, y] = dft_1d(F[:, y])
    return F

def extract_harmonic_matrix(image_path, resize_dim=(64, 64)):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Görüntü okunamadı. Dosya yolunu kontrol edin.")
    image_resized = cv2.resize(image, resize_dim)
    F = dft_2d(image_resized)
    F_shifted = np.fft.fftshift(F)
    harmonic_matrix = 20 * np.log(np.abs(F_shifted) + 1)
    return harmonic_matrix

if __name__ == "__main__":
    dosya_yolu = "fourier.jpg"
    try:
        harmonik_matris = extract_harmonic_matrix(dosya_yolu)
        plt.figure(figsize=(6, 6))
        plt.imshow(harmonik_matris, cmap='gray')
        plt.title("Harmonik Matris (Genlik Spektrumu)")
        plt.axis('off')
        plt.show()
    except Exception as e:
        print("Hata:", e)