days = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
after = int(input("며칠 후가 궁금하신가요? > "))
result = days[after % 7]
print(result)a