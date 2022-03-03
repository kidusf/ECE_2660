import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

multisim_data=pd.read_csv("3.2Numerical.csv")
multisim_data.columns=["time", "voltage"]
t=multisim_data["time"]
w_o=2000*np.pi
y=0.807255*np.cos(w_o*t-np.pi/180*23.8051)
plt.plot(t, y, color="red", linewidth=2, linestyle="dashed")
plt.plot(t, multisim_data["voltage"], color="blue")
plt.xlabel("Time, t(seconds)")
plt.ylabel("Voltage, V(volts")
plt.title("Transient Response of the RL Filter")
plt.legend(["Analytical", "Numerical"])
plt.show()