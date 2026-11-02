import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.signal import medfilt

def gurultu_ekle(vektor, gurultu_orani):
    if not (0.0 <= gurultu_orani <= 1.0):
        raise ValueError("Gürültü oranı 0 ile 1 arasında olmalıdır!")
        
    genlik = np.max(np.abs(vektor))
    rastgele_gurultu = np.random.uniform(-1, 1, size=len(vektor)) * genlik * gurultu_orani
    gurultulu_vektor = vektor + rastgele_gurultu
    
    return gurultulu_vektor

N = 1024
t = np.arange(N) / 1024
orijinal_sinyal = 2.0 * np.sin(2 * np.pi * 8.0 * t)  

oran = 0.3
gurultulu_sinyal = gurultu_ekle(orijinal_sinyal, oran)

gauss_filtrelenmis = gaussian_filter1d(gurultulu_sinyal, sigma=1.0, truncate=2.0)
medyan_filtrelenmis = medfilt(gurultulu_sinyal, kernel_size=5)

plt.figure(figsize=(12, 12))

plt.subplot(3, 1, 1)
plt.plot(t, orijinal_sinyal, color='g', linewidth=2, label='Orijinal Sinyal')
plt.plot(t, gurultulu_sinyal, color='r', linewidth=1, label=f'Gürültülü Sinyal (Oran: {oran})', alpha=0.6)
plt.title('Orijinal ve Gürültü Eklenmiş Sinyal')
plt.ylabel('Genlik')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, orijinal_sinyal, color='g', linewidth=2, label='Orijinal Sinyal (Referans)', alpha=0.5)
plt.plot(t, gauss_filtrelenmis, color='b', linewidth=2, label='Gauss Filtresi (kernel=5, sigma=1.0)')
plt.title('Gauss Filtresi İle Temizlenmiş Sinyal')
plt.ylabel('Genlik')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, orijinal_sinyal, color='g', linewidth=2, label='Orijinal Sinyal (Referans)', alpha=0.5)
plt.plot(t, medyan_filtrelenmis, color='purple', linewidth=2, label='Medyan Filtresi (window=5)')
plt.title('Medyan Filtresi İle Temizlenmiş Sinyal')
plt.xlabel('Zaman (Saniye)')
plt.ylabel('Genlik')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.tight_layout()
plt.show()