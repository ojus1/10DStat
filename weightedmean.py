N = int(input())
X = [int(i) for i in input().split()]
W = [int(i) for i in input().split()]

s = 0
for i in range(0,len(X)) :
    s += X[i] * W[i]
s = s / sum(W)
print(round(s,1))
