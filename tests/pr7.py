import random
from pprint import pprint
from prettytable import PrettyTable

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
print(f"Мода: {max(x)}, Медиана: 3, 4")