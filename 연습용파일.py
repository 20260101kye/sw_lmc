month = int(input())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
startday = 4
print("일 월 화 수 목 금 토")

#startday 구하기
for i in range(1, month):
    startday = (startday + days[i]) % 7

#startday 전까지 공백
for _ in range(startday):
    print("  ", end = " ")

#날짜 출력
for day in range(1, days[month]+1):
    print(f"{day:2}", end = " ")

    if (startday + day) % 7 == 0:
        print( )