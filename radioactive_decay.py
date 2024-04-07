# Importing the module
import numpy as np
import matplotlib.pyplot as plt 
# Starting value
y = 1
# Number of iterations (not less than 200)
n = 300
# Stepsize
h = 0.01
# Collect data
tv = [0]
yv = [y]
# Starting a loop for a specified range of iterations i.e. from 1 to 200
for i in range(1, n+1):
    f = -y # Converting the starting value to negative and assigning it into newly decalred memory
    y = y + f * h
    tv.append(i*h) # append the calculated data to the t_values variable i.e. empty list
    yv.append(y) # append the calculated data to the y_values variable
    print(y) # Print the value for reference
# Plotting part
np.exp(-n*h) 
tt = np.linspace(0, n*h, n)
ty = 1*np.exp(-tt)
plt.plot(tt,ty, 'red')

plt.xlabel('time')
plt.ylabel('Counts per minute')
plt.scatter(tv, yv)
plt.show()
