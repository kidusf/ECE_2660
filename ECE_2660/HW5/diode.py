import numpy as np
import matplotlib.pyplot as plt

def computeNext(vd):
    return np.log(-vd/(I_s*R_th)+V_th/(I_s*R_th)+1)*V_t
V_th=4.85
R_th=3299
q = 1.60218*10**-19
k = 1.38065*10**-23
T = 298

I_s = 10**-13
n = 1
V_t = n*k*T/q
tolerance = 10**-6
V_d=np.linspace(0, 0.65, num=10000)
I_d=I_s*(np.exp(V_d/V_t)-1)
load_line=(V_th-V_d)/(R_th)
plt.plot(V_d, I_d, color="blue", linestyle="dashed")
plt.plot(V_d, load_line, color="red")
V_d=0.001
V_d_next=computeNext(V_d)
iterations=0

while(np.abs(V_d_next-V_d)>tolerance and iterations<200):
    V_d=V_d_next
    V_d_next=computeNext(V_d)
    iterations+=1
I_d=I_s*(np.exp(V_d/V_t)-1)
plt.scatter(V_d, I_d, color="black")
plt.legend(["Diode Characteristic", "Load Line", "Q-Point"])
plt.title("Vth=4.85 V, Rth=3299 ohms")
plt.xlabel("Vd (Volts)")
plt.ylabel("Id (Amps)")
point="("+str(np.round(V_d, 7))+", "+str(np.round(I_d, 7))+")"
plt.annotate(xy=(V_d, I_d), text=point, xytext=(V_d-0.2, I_d))
plt.show()