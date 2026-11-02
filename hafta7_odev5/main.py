import numpy as np
import matplotlib.pyplot as plt

def dft_temel_ogrenci_seviyesi(sinyal):
    N = len(sinyal)
    frekans_uzayi = np.zeros(N, dtype=complex)
    
    for k in range(N):
        toplam = 0.0 + 0.0j
        
        for n in range(N):
            aci = -2.0 * np.pi * k * n / N
            ustel_carpan = complex(np.cos(aci), np.sin(aci))
            toplam += sinyal[n] * ustel_carpan
            
        frekans_uzayi[k] = toplam
        
    return frekans_uzayi

def harmonik_vektor_elde_et(sinyal, ornekleme_frekansi):
    N = len(sinyal)
    frekans_uzayi = dft_temel_ogrenci_seviyesi(sinyal)
    yari_N = N // 2
    
    harmonik_vektor = np.abs(frekans_uzayi[:yari_N]) / yari_N
    frekans_ekseni = np.arange(yari_N) * (ornekleme_frekansi / N)
    return frekans_ekseni, harmonik_vektor

N = 1024
ornekleme_frekansi = 1024 
t = np.arange(N) / ornekleme_frekansi
gurultu_orani = 0.3

sinyal_1 = 12.0 * np.sin(2 * np.pi * 50.0 * t)
rastgele_gurultu_1 = np.random.uniform(-1, 1, size=N) * 12.0 * gurultu_orani
sinyal_1_gurultulu = sinyal_1 + rastgele_gurultu_1

sinyal_2 = 5.0 * np.sin(2 * np.pi * 30.0 * t)
rastgele_gurultu_2 = np.random.uniform(-1, 1, size=N) * 5.0 * gurultu_orani
sinyal_2_gurultulu = sinyal_2 + rastgele_gurultu_2

toplam_sinyal = sinyal_1_gurultulu + sinyal_2_gurultulu

frekanslar, dft_1 = harmonik_vektor_elde_et(sinyal_1_gurultulu, ornekleme_frekansi)
frekanslar, dft_2 = harmonik_vektor_elde_et(sinyal_2_gurultulu, ornekleme_frekansi)
frekanslar, dft_toplam = harmonik_vektor_elde_et(toplam_sinyal, ornekleme_frekansi)

plt.figure(figsize=(14, 12))

plt.subplot(4, 1, 1)
plt.bar(frekanslar, dft_1, color='b', width=0.8)
plt.title('Sinyal 1 DFT (50 Hz, Genlik: 12)')
plt.ylabel('Genlik')
plt.xlim(0, 80)
plt.grid(True, linestyle='--', alpha=0.7, axis='y')

plt.subplot(4, 1, 2)
plt.bar(frekanslar, dft_2, color='g', width=0.8)
plt.title('Sinyal 2 DFT (30 Hz, Genlik: 5)')
plt.ylabel('Genlik')
plt.xlim(0, 80)
plt.grid(True, linestyle='--', alpha=0.7, axis='y')

plt.subplot(4, 1, 3)
plt.plot(t, toplam_sinyal, color='purple', linewidth=1.5)
plt.title('Toplam Sinyal (Zaman Uzayı)')
plt.xlabel('Zaman (Saniye)')
plt.ylabel('Genlik')
plt.xlim(0, 0.2) 
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(4, 1, 4)
plt.bar(frekanslar, dft_toplam, color='r', width=0.8)
plt.title('Toplam Sinyalin DFT Sonucu (Harmonik Vektör)')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.xlim(0, 80)
plt.grid(True, linestyle='--', alpha=0.7, axis='y')

plt.tight_layout()
plt.show()