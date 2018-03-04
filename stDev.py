def CalcMean(x : list) :
    temp = 0.0
    for i in x :
        temp += i
    return round(temp/len(x),1)

N = int(input())
X = [int(i) for i in input().split()]

mean = CalcMean(X)

temp = 0
for i in range(0,len(X)) :
    temp += (X[i] - mean) ** 2

standardDeviation = (temp/len(X)) ** (0.5)
print(standardDeviation)
