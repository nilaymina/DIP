import numpy as np
import matplotlib.pyplot as plt

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

plt.figure(figsize=(12, 6))
plt.plot(t, orijinal_sinyal, color='g', linewidth=2, label='Orijinal Sinyal', alpha=0.7)
plt.plot(t, gurultulu_sinyal, color='r', linewidth=1, label=f'Gürültülü Sinyal (Oran: {oran})', alpha=0.8)
plt.title('Orijinal ve Gürültü Eklenmiş Sinyal Karşılaştırması')
plt.xlabel('Zaman (Saniye)')
plt.ylabel('Genlik')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=0, color='k', linestyle='-')
plt.legend()
plt.tight_layout()
plt.show()