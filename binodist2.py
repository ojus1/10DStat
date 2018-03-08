def fact(x) :
    f = 1
    for i in range(1,x+1) :
        f *= i
    return f

p = 0.12
temp = 0.0
for i in range(0,2+1) :
    temp += fact(10)/(fact(i) * fact(10-i)) * pow(p,i) * pow(1-p,10-i)
print(round(temp,3))
print(round(1 - temp + fact(10)/(fact(2) * fact(10-2)) * pow(p,2) * pow(1-p,10-2),3))
