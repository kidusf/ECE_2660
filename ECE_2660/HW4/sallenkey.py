import numpy as np

resistors_in_kit=np.array([10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82, 100, 120, 150, 180, 220, 270, 330, 470, 560, 
680, 820, 1000, 1200, 1500, 1800, 2200, 2700, 3300, 4700, 5600, 6800, 8200, 12000, 15000, 
18000, 22000, 27000, 33000, 47000, 56000, 68000, 82000, 120000, 150000,
 180000, 220000, 270000, 330000, 470000, 560000, 680000, 820000, 1000000], dtype=np.double)
capacitors_in_kit=np.array([0.01*(10**-6), 0.1*(10**-6), 0.47*(10**-6)], dtype=np.double)

desired_freq=500
desired_quality=0.6

r1=resistors_in_kit
r2=resistors_in_kit
c1=capacitors_in_kit
c2=capacitors_in_kit
tolerance_freq=10
tolerance_quality=0.1
for i in range(len(r1)):
    for j in range(len(r2)):
        for k in range(len(c1)):
            for l in range(len(c2)):
                actual_freq=1/(2*np.pi*np.sqrt(r1[i]*r2[j]*c1[k]*c2[l]))
                actual_quality=np.sqrt(r1[i]*r2[j]*c1[k]*c2[l])/((r1[i]+r2[j])*c2[l])

                if(np.abs(actual_quality-desired_quality)<tolerance_quality and np.abs(actual_freq-desired_freq)<tolerance_freq):
                    print(r1[i], r2[j], c1[k], c2[l], actual_freq, actual_quality)
