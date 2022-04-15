import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read in the exported data
data=pd.read_csv("6.3Multisim.csv")
#drop the unneccesary columns
data.drop(columns=[ 'X--Trace 2::[-I(Rd:2) | I(PR1)]', 'Unnamed: 2', 'Unnamed: 5', 'X--Trace 3::[V(1) | V(PR3)]'], inplace=True)

#renaming the columns
data.columns=["Vdd", "Vds", "Ids", "Vd"]
#drain source voltage on the MOSFET
Vds=data["Vds"]
#drain current on the MOSFET
Ids=data["Ids"]
#the dc value of VDD
Vdd=5
#voltage on the drain of the MOSFET
Vd=data["Vd"]
#the resistor connected to the drain
Rd=1000
#load line
Id=(5-Vd)/Rd
#plot characteristic and load line
plt.plot(Vds, Ids)
plt.plot(Vds, Id)
#annotate the plot
plt.legend(["MOSFET Characteristic", "Load Line"])
plt.title("Q Point Verification")
plt.xlabel("Vds(Volts)")
plt.ylabel("Ids(Amps)")
plt.show()