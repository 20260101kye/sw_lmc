N, K = map(int, input().split())

max_num = 0

for i in range(1, K + 1):
    num = N * i
    reversed_num = int(str(num)[::-1]) 
    if reversed_num > max_num:
        max_num = reversed_num

print(max_num)