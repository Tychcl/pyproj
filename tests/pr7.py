import random
from pprint import pprint
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import math

#Исходные переменные
n = 2699
x = [0,0,0,0,0,0]

#Таблица
t = PrettyTable()
t.field_names = []
t.hrules=True
t.vrules=True

#Вычисления
for i in range(n):
    h = random.randint(0,5)
    x[h]+=1

#Создание таблицы и графиков
t.add_column("X",list(map(lambda z: z+1, range(len(x)))))
t.add_column("Ni",[i for i in x])
t.add_column("Pi",list(map(lambda z: str(z)+"/"+str(n), [i for i in x])))

#Вывод
print(t)
print("X - Значение\nNi - Частота\nPi - Частость")
print(f"\nМода: {x.index(max(x))+1}, Медиана: 3, 4")

t = list(map(lambda z: str(z+1), range(len(x)))) #массив
s = x #массив
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(t,x)
for i in x:
    plt.annotate(str(i),xy=(x.index(i)-0.45,i+5))
plt.ylim(0,600)
plt.show()

print("\nСистема F(x):")
print(f"0, x<0")
for i in range(0,5):
    print(f"{sum(x[0:i])}/{n}, {i}<=x<{i+1}")
print(f"1, 5<=x<6")

gg = 0
for i in range(5):
    gg += x[i]*(i+1)
print(f"\nXв = {round(gg/n,2)}")
xb = round(gg/n,2)

gg = 0
for i in range(5):
    gg += (x[i]**2)*(i+1)
Db = round((gg/n)-xb**2,2)
print(f"\nDв = {Db}")
print(f"\nБв = {math.sqrt(Db)}")
print(f"\nS2 = {n/(n-1)*Db}")
print(f"\nS = {math.sqrt(n/(n-1)*Db)}")
print(f"\nV = {(math.sqrt(Db))/xb}")
print(f"\nd = {(math.sqrt(Db))/xb}")
#https://matplotlib.online/project?id=0