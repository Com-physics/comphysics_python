#importig module
import numpy as np
from scipy.integrate import odeint as od
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#Declaring variables and assigning values
sigma=10.0
b=8/3.0
r=28.0
#Lorentz attractor equation
f = lambda x,t: [sigma*(x[1]-x[0]), r*x[0]-x[1]-x[0]*x[2], x[0]*x[1]-b*x[2]]
t=np.linspace(0,20,2000); y0=[5.0,5.0,5.0]
solution= od(f,y0,t)
#Call the plotting function to plot Lorentz attractor aka Butterfly effect
X=solution[:,0]; Y=solution[:,1]; Z=solution[:,2]
fig= plt.figure()
ax= fig.add_subplot(projection='3d')
plt.plot(X,Y,Z)
plt.show()