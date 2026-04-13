K, L = map(int, input().split())

students = {}

for i in range(L):
    num = input()
    students[num] = i 
    
result = sorted(students.items(), key=lambda x: x[1])

for i in range(min(K, len(result))):
    print(result[i][0])