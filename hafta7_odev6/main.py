import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, x)

def idft(X):
    N = len(X)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(2j * np.pi * k * n / N)
    return np.real(np.dot(e, X)) / N

def frekans_filtresi(frekans_uzayi, esik_deger):
    N = len(frekans_uzayi)
    genlikler = 2 * np.abs(frekans_uzayi) / N
    genlikler[0] = np.abs(frekans_uzayi[0]) / N
    if N % 2 == 0:
        genlikler[N // 2] = np.abs(frekans_uzayi[N // 2]) / N
    maske = genlikler >= esik_deger
    filtrelenmis = np.zeros(N, dtype=complex)
    filtrelenmis[maske] = frekans_uzayi[maske]
    return filtrelenmis

def harmonik_vektor_elde_et(frekans_uzayi, ornekleme_frekansi):
    N = len(frekans_uzayi)
    yari_N = N // 2
    harmonik = 2 * np.abs(frekans_uzayi[:yari_N]) / N
    harmonik[0] = np.abs(frekans_uzayi[0]) / N
    frekans_ekseni = np.arange(yari_N) * (ornekleme_frekansi / N)
    return frekans_ekseni, harmonik

N = 1024
fs = 1024
t = np.arange(N) / fs
oran = 0.3
esik = 2.0

s1_temiz = 12.0 * np.sin(2 * np.pi * 50.0 * t)
s1_gurultulu = s1_temiz + np.random.uniform(-1, 1, size=N) * 12.0 * oran

s2_temiz = 5.0 * np.sin(2 * np.pi * 30.0 * t)
s2_gurultulu = s2_temiz + np.random.uniform(-1, 1, size=N) * 5.0 * oran

dft_s1 = dft(s1_gurultulu)
f1, h1 = harmonik_vektor_elde_et(dft_s1, fs)

dft_s2 = dft(s2_gurultulu)
f2, h2 = harmonik_vektor_elde_et(dft_s2, fs)

s_toplam = s1_gurultulu + s2_gurultulu
dft_toplam = dft(s_toplam)
f, h_toplam = harmonik_vektor_elde_et(dft_toplam, fs)

filtrelenmis_dft = frekans_filtresi(dft_toplam, esik)
geri_catilmis_sinyal = idft(filtrelenmis_dft)
f_filtre, h_filtre = harmonik_vektor_elde_et(filtrelenmis_dft, fs)

plt.figure(figsize=(14, 16))

plt.subplot(5, 1, 1)
plt.plot(f1, h1, color='blue')
plt.title('Birinci Sinyalin Harmonik Vektörü (50 Hz)')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.xlim(0, 100)
plt.grid(True)

plt.subplot(5, 1, 2)
plt.plot(f2, h2, color='orange')
plt.title('İkinci Sinyalin Harmonik Vektörü (30 Hz)')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.xlim(0, 100)
plt.grid(True)

plt.subplot(5, 1, 3)
plt.plot(t, s_toplam, color='red')
plt.title('Gürültülü Toplam Sinyal (Zaman Uzayı)')
plt.xlabel('Zaman (Saniye)')
plt.ylabel('Genlik')
plt.xlim(0, 0.2)
plt.grid(True)

plt.subplot(5, 1, 4)
plt.bar(f, h_toplam, color='blue', width=0.8)
plt.title('Toplam Sinyalin Harmonik Vektörü (DFT)')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Genlik')
plt.xlim(0, 100)
plt.grid(True, axis='y')

plt.subplot(5, 1, 5)
plt.plot(t, geri_catilmis_sinyal, color='green')
plt.title(f'Filtrelenmiş ve Yeniden Oluşturulmuş Sinyal (Eşik = {esik})')
plt.xlabel('Zaman (Saniye)')
plt.ylabel('Genlik')
plt.xlim(0, 0.2)
plt.grid(True)

plt.tight_layout()
plt.show()