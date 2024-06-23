import math
x = [509,425,441,482,420,422]
n=2699
Xb = sum(map(lambda z: z*(x.index(z)+1),x))/n
Db = (sum(map(lambda z: z*(x.index(z)+1)**2,x))-(Xb**2))/n
Bb = math.sqrt(Db)
S2 = (n/(n-1))*Db
S = math.sqrt(S2)
V = Bb/Xb
d = sum(list(map(lambda z: round(((x.index(z)+1)-Xb)*z,2),x)))
print(d)