import random  # 랜덤 숫자 사용

# 행렬 만드는 함수 (랜덤으로 채우기)
def make(N):
    m = []  # 전체 행렬

    for i in range(N):  # 줄 만들기
        row = []  # 한 줄

        for j in range(N):  # 숫자 채우기
            num = random.randint(1, N*N*10 - 1)  # 랜덤 숫자
            row.append(num)  # 줄에 추가

        m.append(row)  # 행렬에 추가

    return m  # 완성된 행렬


# 행렬 출력 함수 (예쁘게 출력)
def show(m):
    for i in range(len(m)):  # 줄 반복
        for j in range(len(m)):  # 숫자 반복
            print(f"{m[i][j]:4}", end=" ")  # 자리 맞춰 출력
        print()  # 줄 바꿈


# 행렬 곱하기 함수
def mul(a, b, N):
    result = []

    for i in range(N):  # 행
        row = []

        for j in range(N):  # 열
            total = 0  # 한 칸 값

            for k in range(N):  # 계산용 반복
                total = total + a[i][k] * b[k][j]  # 핵심 계산

            row.append(total)  # 결과 넣기

        result.append(row)

    return result


# 행렬 더하기 함수
def add(a, b, N):
    result = []

    for i in range(N):
        row = []

        for j in range(N):
            row.append(a[i][j] + b[i][j])  # 같은 위치 더하기

        result.append(row)

    return result


#실행
N = int(input("N 입력 (2~5): "))

A = make(N)  # A생성
B = make(N)  # B생성
C = make(N)  # C 생성

print("\nA")
show(A)

print("\nB")
show(B)

print("\nC")
show(C)

AB = mul(A, B, N)  # A * B
result = add(AB, C, N)  # (A * B) + C

print("\nA x B")
show(AB)

print("\n(A x B) + C")
show(result)