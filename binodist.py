def fact(x) :
    f = 1
    for i in range(1,x+1) :
        f *= i
    return f
r1,r2 = input().split()
r1,r2 = float(r1),float(r2)

pB = r1/(r1+r2)
pG = 1.0 - pB

temp = 0.0
for i in range(3,6+1) :
    temp += fact(6)/(fact(i) * fact(6-i)) * pow(pB,i) * pow(pG,6-i)
print(round(temp,3))
