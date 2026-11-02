import numpy as np
import matplotlib.pyplot as plt

def degerli_sinus_dalgası(vector, amplitude, frequency, phase, sample_rate):
    N = len(vector)
    
    if (N & (N - 1) != 0) or N == 0:
        raise ValueError("Vektörün boyutu 2'nin tam kuvveti olmalıdır!")
        
    t = np.arange(N) / sample_rate
    vector[:] = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    
    return t

N = 1024
ornekleme_frekansi = 1024 
sinus_vektoru = np.zeros(N)

genlik = 2.0                
frekans = 8.0              
faz_radyan = np.pi / 4      

zaman_vektoru = degerli_sinus_dalgası(sinus_vektoru, genlik, frekans, faz_radyan, ornekleme_frekansi)

plt.figure(figsize=(12, 5))
plt.plot(zaman_vektoru, sinus_vektoru, color='b', linewidth=2, label=f'{genlik}*sin(2π*{frekans}*t + π/4)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=0, color='k', linestyle='-')
plt.legend()
plt.tight_layout()
plt.show()