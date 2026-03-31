n=int(input())

if(n==2):
    day=28
elif n in [ 1, 3, 5, 7, 9, 11]:
    day=31
else:
    day=30
startday=[0, 4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]
start=startday[n]


print('일 월 화 수 목 금 토')

for _ in range (start):
    print("  ", end =" ")
for i in range(1, day+1):
    if(i>0 and i<10):
        print(" "+ str(i), end=" ")
    else:
        print(i, end=" ")

    if (start+i) % 7 == 0:
        print()