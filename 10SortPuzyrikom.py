#сортировка пузырьком
a = list(map(int, input().split()))
N = len(a)

for i in range(0, N-1): #количество итераций
    for j in range(0, N-1-i): #проход по неотсортированным элементам массива
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
