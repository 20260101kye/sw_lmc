year = int(input("년도를 입력하세요. > "))

if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")