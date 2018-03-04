def CalcMedian(x : list) :
    x.sort()
    l = len(x)
    if l % 2 :
        i = (l - 1) // 2
        return x[i]
    else :
        t = x[l//2 - 1] + x[l//2]
        t = t/2
        return t


N = int(input())
X = [int(i) for i in input().split()]
X.sort()
if len(X) % 2  != 1 :
    lower = X[0:len(X)//2]
    upper = X[len(X)//2:len(X)]
else :
    lower = X[0:(len(X) - 1)//2]
    upper = X[(len(X) + 1)//2:len(X)]


q1 = CalcMedian(lower)
q2 = CalcMedian(X)
q3 = CalcMedian(upper)

print(int(q1))
print(int(q2))
print(int(q3))
