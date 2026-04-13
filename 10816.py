N = int(input())
cards = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

count = {}

for num in cards:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for x in targets:
    if x in count:
        print(count[x], end=' ')
    else:
        print(0, end=' ')