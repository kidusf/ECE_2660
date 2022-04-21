import numpy as np

resistors_in_kit=np.array([10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82, 100, 120, 150, 180, 220, 270, 330, 470, 560, 
680, 820, 1000, 1200, 1500, 1800, 2200, 2700, 3300, 4700, 5600, 6800, 8200, 12000, 15000, 
18000, 22000, 27000, 33000, 47000, 56000, 68000, 82000, 120000, 150000,
 180000, 220000, 270000, 330000, 470000, 560000, 680000, 820000, 1000000], dtype=np.double)
capacitors_in_kit=np.array([0.01*(10**-6), 0.1*(10**-6), 0.47*(10**-6)], dtype=np.double)

r1=resistors_in_kit
r2=resistors_in_kit
r3=resistors_in_kit
c1=capacitors_in_kit

freq_threshold=1000
tolerance=100

for i in range(len(r1)):
    for j in range(len(r2)):
        for k in range(len(r3)):
            for l in range(len(c1)):
                actual_freq=(1/(4*r1[i]*c1[l]))*r3[k]/r2[j]
                if((actual_freq-freq_threshold)<=tolerance and actual_freq-freq_threshold>=0 and r2[j]/r3[k]>=1):
                    print(r1[i], r2[j], r3[k], c1[l], actual_freq, r2[j]/r3[k])
