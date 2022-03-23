from turtle import color, width
import pandas as pd 

import numpy as np
import matplotlib.pyplot as plt

multisim_data_lp=pd.read_csv("LowPassMultisim.csv")
multisim_data_hp=pd.read_csv("HighPassMultisim.csv")
multisim_data_lp.columns=["frequency", "amplitude"]
multisim_data_hp.columns=multisim_data_lp.columns
bode=input("High pass or Low pass?\n")
if(bode.lower()=="low"):
    f=multisim_data_lp["frequency"]
    pi=np.pi
    s=2*pi*f*1j
    r1=47*1000
    r2=2.2*1000
    c1=0.1*10**-6
    c2=0.01*10**-6
    corner_freq=1/(np.sqrt(r1*r2*c1*c2))
    Q=np.sqrt(r1*r2*c1*c2)/((r1+r2)*c2)
    H=(corner_freq**2)/(s**2+s*(corner_freq/Q)+corner_freq**2)
    H=20*np.log10(H)
    plt.semilogx(f, H, linewidth=2, color="red")
    plt.semilogx(f, 20*np.log10(multisim_data_lp["amplitude"]), linewidth=2, color="blue", linestyle="dashed")
    x=493
    y=-3.36
    plt.scatter(x, y, s=20)
    plt.annotate(xy=(x, y), text="(493, -3.36)", xytext=(493, 0), arrowprops=dict(color='k',width=0.5))
    plt.title("Bode Plot of the Low Pass Filter")
#plt.semilogx(waveforms_data["frequency"],waveforms_data["amplitude"], color="black", linestyle="dashed")
if(bode.lower()=="high"):
    f=multisim_data_hp["frequency"]
    pi=np.pi
    s=2*pi*f*1j
    r1=1.8*1000
    r2=3.3*1000
    c1=0.1*10**-6
    c2=0.1*10**-6
    corner_freq=1/(np.sqrt(r1*r2*c1*c2))
    Q=np.sqrt(r1*r2*c1*c2)/((c1+c2)*r1)
    H=(s**2)/(s**2+s*(corner_freq/Q)+corner_freq**2)
    H=20*np.log10(H)
    plt.semilogx(f, H, linewidth=2, color="red")
    plt.semilogx(f, 20*np.log10(multisim_data_hp["amplitude"]), linewidth=2, color="blue", linestyle="dashed")
    x=653
    y=-3.36
    plt.scatter(x, y, s=20)
    plt.annotate(xy=(x, y), text="(653, -3.36)", xytext=(653, 0), arrowprops=dict( color='k',width=0.5))
    plt.title("Bode Plot of the High Pass Filter")
plt.legend(["analytical", "numerical"])
plt.xlabel("Frequency, f(Hz)")
plt.ylabel("Magnitude(dB)")
plt.show()