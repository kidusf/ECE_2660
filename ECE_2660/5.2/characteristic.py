import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

multisim_data=pd.read_csv("5.2Multisim.csv")
multisim_data.columns=["voltage", "current"]
v=multisim_data["voltage"]
i=multisim_data["current"]
q = 1.60218*10**-19 #charge of an electron
k = 1.38065*10**-23 #some constant I don't remember
T = 298 #temperature

I_s = 10**-13 #saturation current
n = 1 #emission coefficient
V_t = n*k*T/q #thermal voltage
I_d=I_s*(np.exp(v/V_t)-1) #diode charcteristic equation
plt.plot(v, I_d, color="blue", linewidth=2)
plt.plot(v, i, color="red", linestyle="dashed", linewidth=2)
plt.xlim(-4.5, 4.5) 
plt.ylim(-50e-6, 500e-6)
plt.title("Diode Characteristic")
plt.xlabel("Diode Voltage, V_{D}(Volts)")
plt.ylabel("Diode Current, I_{D}(Amps)")
plt.legend(["Analytical", "Numerical"])
plt.show()