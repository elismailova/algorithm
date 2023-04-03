#сортировка выбором
a = list(map(int, input().split()))
N = len(a)

for i in range(N-1):
    minim = a[i] #начальное минимальное
    ind = i #индекс минимального
    for j in range(i+1, N):
        if a[j] < minim: #поиск минимального
            minim = a[j]
            ind = j
        if ind != i: #перестановка
            t = a[i]
            a[i] = a[ind]
            a[ind] = t
print(a)

