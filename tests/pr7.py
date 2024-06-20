import random
from pprint import pprint
from prettytable import PrettyTable
import matplotlib.pyplot as plt

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
print(f"Мода: {x.index(max(x))+1}, Медиана: 3, 4")

t = list(map(lambda z: str(z+1), range(len(x)))) #массив
s = x #массив
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(t,x)
for i in x:
    plt.annotate(str(i),xy=(x.index(i)-0.45,i+5))
plt.ylim(0,600)
plt.show()

#https://matplotlib.online/project?id=0