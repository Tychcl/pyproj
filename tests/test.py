import matplotlib.pyplot as plt
import numpy as np
import random

plt.rc('font', family='serif')

n = 2699
x = [0,0,0,0,0,0]

for i in range(n):
    h = random.randint(0,5)
    x[h]+=1

# Data for plotting
t = np.arange(0.0, 2.0, 0.01) #массив
s = 1 + np.sin(2 * np.pi * t) #массив

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid(ls=':')
plt.show()
print(t)