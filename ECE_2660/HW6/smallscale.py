import numpy as np
import matplotlib.pyplot as plt

def gain(freq):
    return 20*np.log10(k*(freq/(freq+w_g))*((freq+w_s_z)/(freq+w_s_p))*(freq/(freq+w_d)))
f=np.linspace(start=0.001, stop=1000000, num=10000000)
pi=np.pi
s=2*pi*1j*f
w_g=2*pi*0.936
w_d=2*pi*0.108
w_s_z=0.0102*2*pi
w_s_p=10.071*2*pi
k=0.000499
H=-k*(s/(s+w_g))*((s+w_s_z)/(s+w_s_p))*(s/(s+w_d))
H=20*np.log10(np.abs(H))
plt.semilogx(f, H, linewidth=2, color="red")
plt.title("Frequency Response of the Amplifier")
plt.xlabel("Frequency, f(HZ)")
plt.ylabel("Magnitude(dB)")
plt.annotate(xy=(w_s_p/(2*pi),gain(w_s_p) ), text="Pole", xytext=(w_s_p/(2*pi),gain(w_s_p) ), arrowprops=dict(color='k',width=0.5))
plt.annotate(xy=(w_s_z/(2*pi),gain(w_s_z) ), text="Zero", xytext=(w_s_z/(2*pi),gain(w_s_z) ), arrowprops=dict(color='k',width=0.5))
plt.annotate(xy=(w_d/(2*pi), gain(w_d)), text="Pole", xytext=(w_d/(2*pi), gain(w_d)), arrowprops=dict(color='k',width=0.5))
plt.annotate(xy=(w_g/(2*pi), gain(w_g)), text="Pole", xytext=(w_g/(2*pi), gain(w_g)), arrowprops=dict(color='k',width=0.5))
plt.show()