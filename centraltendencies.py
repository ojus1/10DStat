N = int(input())

X = [int(i) for i in input().split()]

def CalcMean(x : list) :
    temp = 0.0
    for i in x :
        temp += i
    return round(temp/len(x),1)

def CalcMode(x : list) :
    x.sort()
    f = 1
    modalF = 0
    small = x[0]
    frequencies = list()
    for i in range(0,len(x)) :
        for j in range(0,len(x)) :
            if x[i] == x[j] and i != j :
                f += 1
        frequencies.append([x[i],f])
        f = 1
    mode = frequencies[0]
    for i in range(0,len(frequencies)) :
        for j in range(0,len(frequencies)) :
            if frequencies[i][1] < frequencies[j][1] and i != j :
                mode = frequencies[j]
    return round(mode[0],1)

def CalcMedian(x : list) :
    x.sort()
    l = len(x)
    if l % 2 :
        i = (l - 1) // 2
        return x[i]
    else :
        t = x[(l-1)//2] + x[l//2]
        t = t/2
        return round(t,1)

print(CalcMean(X))
print(CalcMedian(X))
print(CalcMode(X))
