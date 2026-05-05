a = [8, 4, 9, 5]
n = len(a)

for i in range(n-1, 0 , -1):
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)