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

n = int(input())
X = [int(i) for i in input().split()]
F = [int(i) for i in input().split()]

S = list()
N = sum(F)


for i in range(0,n) :
    for j in range(0,F[i]) :
        S.append(X[i])

S.sort()

if len(S) % 2  != 1 :
    lower = S[0:len(S)//2]
    upper = S[len(S)//2:len(S)]
else :
    lower = S[0:(len(S) - 1)//2]
    upper = S[(len(S) + 1)//2 :len(S)]

q1 = CalcMedian(lower)
q3 = CalcMedian(upper)

print(float(q3-q1))
