#Kidus Fasil
#kf5fr


#Libraries used(Very similar functionality to MATLAB)
import numpy as np
import matplotlib.pyplot as plt

#computes the voltage of the diode for the next iteration
def computeNext(vd):
    return np.log(-vd/(I_s*R_th)+V_th/(I_s*R_th)+1)*V_t

V_th=4.851 #thevenin voltage
R_th=2800 #thevenin resistance
q = 1.60218*10**-19 #charge of an electron
k = 1.38065*10**-23 #some constant I don't remember
T = 298 #temperature

I_s = 10**-13 #saturation current
n = 1 #emission coefficient
V_t = n*k*T/q #thermal voltage
tolerance = 10**-6 #the minimum error between V_d and V_d_next

#create the diode characteristic and load line plot first
V_d=np.linspace(0, 0.65, num=10000) 
I_d=I_s*(np.exp(V_d/V_t)-1) #diode charcteristic equation
load_line=(V_th-V_d)/(R_th) #load line equation
#plotting the two curves
plt.plot(V_d, I_d, color="blue", linestyle="dashed")
plt.plot(V_d, load_line, color="red")

V_d=0.001 #initial guess for V_d
V_d_next=computeNext(V_d)

#loop that keeps computing V_d and V_d next until it converges to a value
while(np.abs(V_d_next-V_d)>tolerance):
    V_d=V_d_next
    V_d_next=computeNext(V_d)
#redefine I_d as the Q point
I_d=I_s*(np.exp(V_d/V_t)-1)
#create the Q point on the plot
plt.scatter(V_d, I_d, color="black")
#Formatting the plot
plt.legend(["Diode Characteristic", "Load Line", "Q-Point"])
plt.title("Vth=4.851 V, Rth=2800 ohms")
plt.xlabel("Vd (Volts)")
plt.ylabel("Id (Amps)")
point="("+str(np.round(V_d, 7))+", "+str(np.round(I_d, 7))+")"
#annotation of the Q point
plt.annotate(xy=(V_d, I_d), text=point, xytext=(V_d-0.2, I_d))
plt.show()