r = [44,42,40,40,38,38,37,39]
u = [26,26,27,28,24,26,30,28]
s = 8
p=22

print("Функция доходов g(t)=r(t)-u(t)")
g = []
for i in range(len(r)):
    g.append(r[i]-u[i])
    print(f"g({i}) = {r[i]} - {u[i]} = {r[i]-u[i]}")


    