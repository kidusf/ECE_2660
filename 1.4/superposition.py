import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
waveforms_data=pd.read_csv("1.4expdata5.csv")
waveforms_data.columns=["time", "voltage", "voltage2"]
waveforms_data.drop(columns=["voltage2"], inplace=True)
waveforms_data=waveforms_data[waveforms_data["time"]>0]
multisim_data=pd.read_csv("1.4numerical2.xlsx - Sheet1.csv")
multisim_data.columns=["time", "voltage"]
freq=220
v1=2*np.sin(2*np.pi*freq*waveforms_data["time"])
v2=2*np.sin(2*np.pi*freq*waveforms_data["time"]-np.pi/2)
r1=10000
r2=r1
r3=r1
vo1=(r2*r3*v1)/(r1*r2+r2*r3+r1*r3)
vo2=(r1*r3*v2)/(r1*r2+r2*r3+r1*r3)
v=vo1+vo2
plt.plot(waveforms_data["time"], v, color="red", linewidth=2)
plt.plot(multisim_data["time"], multisim_data["voltage"], color="blue", linestyle="dashed",linewidth=2)
plt.plot(waveforms_data["time"], waveforms_data["voltage"], color="black", linestyle="dashed")
plt.title("Voltage of the superposition wave")
plt.xlabel("time, t (seconds)")
plt.ylabel("Voltage, V (volts) ")
plt.legend(["Analytical", "Numerical", "Experimental"])
plt.show()