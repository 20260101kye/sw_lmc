month = int(input("월을 입력하세요: "))


# 달력 제목 출력
print("일 월 화 수 목 금 토")

# 각 달의 일수
# 0월은 없으니까 0을 앞에 넣어서
# days[1] = 1월의 일수, days[2] = 2월의 일수처럼 쓰기
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 요일 번호
# 일=0, 월=1, 화=2, 수=3, 목=4, 금=5, 토=6
start = 4   # 1월 1일은 목요일이니까 4

# 입력한 달 전까지의 날짜 수를 더해서 시작 요일 구하기
for i in range(1, month):
    start = (start + days[i]) % 7


# 첫 주에서 시작 요일 전까지 빈칸 출력
for _ in range(start):
    print("  ", end=" ")

# 날짜 출력
for day in range(1, days[month] + 1):
    print(f"{day:2}", end=" ")

    # 토요일까지 출력했으면 줄 바꿈
    if (start + day) % 7 == 0:
        print()