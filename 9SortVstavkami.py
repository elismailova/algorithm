#сортировка вставками
a = list(map(int, input().split()))
N = len(a)

for i in range(1, N): #проходим от 2го элемента до последнего
    for j in range(i, 0, -1): # сраниваем элементы от того, на котором стоим с предыдущими
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break
print(a)

