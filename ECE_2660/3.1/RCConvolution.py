
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

multisim_data=pd.read_csv("Multisim3.1.csv")
multisim_data.columns=["time", "voltage"]
waveforms_data=pd.read_csv("Module3_3.1.csv")
waveforms_data.columns=multisim_data.columns
waveforms_data=waveforms_data[(waveforms_data["time"]>=0) & ((waveforms_data["time"]<=0.01))]
t=multisim_data["time"]
pi=np.pi
freq=2000*pi
r=16*1000
c=0.1*(10**-6)
tau_o=r*c   
left_side=np.cos(freq*t)*tau_o*np.exp(-t/tau_o)*(np.exp(t/tau_o)+freq*tau_o*np.sin(freq*t)-np.cos(freq*t))/(((freq*tau_o)**2)+1)
right_side=np.sin(freq*t)*tau_o*np.exp(-t/tau_o)*(freq*tau_o*np.exp(t/tau_o)-freq*tau_o*np.cos(freq*t)-np.sin(freq*t))/(((freq*tau_o)**2)+1)
y=1/tau_o*(left_side+right_side)

plt.plot(t, y, color="red", linewidth=2)
plt.plot(t, multisim_data["voltage"], linestyle="dashed", color="blue", linewidth=2)
plt.plot(waveforms_data["time"], waveforms_data["voltage"], linestyle="dashed", color="black")
plt.title("Transient Response of the Output Signal. Created by Kidus Fasil.")
plt.xlabel("Time, t(seconds)")
plt.ylabel("Voltage, V(volts")
plt.legend([ "analytical", "numerical", "experimental"])
plt.show()