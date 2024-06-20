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
t = list(map(lambda z: str(z+1), range(len(x)))) #массив
s = x #массив
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(t,x)
for i in x:
    plt.annotate(str(i),xy=(x.index(i)-0.45,i))
    print(x.index(i)+1, i )
plt.ylim(0,600)
plt.show()
print(t)