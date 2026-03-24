A, B = map(int, input().split())
C = int(input())
total = ((A*60)+B+C)
hour = (((A*60)+B+C)//60)%24
minute = ((A*60)+B+C)%60
print(hour, minute)