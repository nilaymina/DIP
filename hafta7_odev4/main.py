import numpy as np
import matplotlib.pyplot as plt

def ayrik_fourier_donusumu(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    
    e = np.exp(-2j * np.pi * k * n / N)
    dft_sonucu = np.dot(e, x)
    return dft_sonucu

def harmonik_vektor_elde_et(sinyal, ornekleme_frekansi):
    N = len(sinyal)
    if (N & (N - 1) != 0) or N == 0:
        raise ValueError("Vektör uzunluğu 2'nin kuvveti olmalıdır!")
        
    frekans_uzayi = ayrik_fourier_donusumu(sinyal)
    yari_N = N // 2
    
    harmonik_vektor = np.abs(frekans_uzayi[:yari_N]) / yari_N
    frekans_ekseni = np.arange(yari_N) * (ornekleme_frekansi / N)
    
    return frekans_ekseni, harmonik_vektor

N = 1024
ornekleme_frekansi = 1024
t = np.arange(N) / ornekleme_frekansi

orijinal_sinyal = 2.0 * np.sin(2 * np.pi * 8.0 * t)

gurultu_orani = 0.3
rastgele_gurultu = np.random.uniform(-1, 1, size=N) * 2.0 * gurultu_orani
gurultulu_sinyal = orijinal_sinyal + rastgele_gurultu

frekanslar, orijinal_harmonik = harmonik_vektor_elde_et(orijinal_sinyal, ornekleme_frekansi)
frekanslar, gurultulu_harmonik = harmonik_vektor_elde_et(gurultulu_sinyal, ornekleme_frekansi)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.bar(frekanslar, orijinal_harmonik, color='g', width=0.6)
plt.title('Gürültüsüz Sinyal - DFT Sonucu (Sütun Grafiği)')
plt.ylabel('Genlik')
plt.xlim(0, 50) 
plt.grid(True, linestyle='--', alpha=0.7, axis='y')

plt.subplot(2, 1, 2)
plt.bar(frekanslar, gurultulu_harmonik, color='r', width=0.6)
plt.title('Gürültülü Sinyal - DFT Sonucu (Sütun Grafiği)')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.xlim(0, 50)
plt.grid(True, linestyle='--', alpha=0.7, axis='y')

plt.tight_layout()
plt.show()