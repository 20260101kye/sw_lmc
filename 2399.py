N = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 0
prefix_sum = 0

for i in range(N):
    result += arr[i] * i - prefix_sum
    prefix_sum += arr[i]

print(result * 2)