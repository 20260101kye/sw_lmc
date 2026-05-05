import random  # 랜덤 숫자

# 행렬 만들기
def make(N):
    m = []

    for i in range(N):
        row = []

        for j in range(N):
            num = random.randint(1, N*N*10 - 1)
            row.append(num)

        m.append(row)

    return m


# 출력 함수
def show(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(f"{m[i][j]:4}", end=" ")
        print()


# 전치 행렬 함수
def trans(a, N):
    result = []

    for i in range(N):
        row = []

        for j in range(N):
            row.append(a[j][i])  # 행과 열 바꾸기

        result.append(row)

    return result


# ===== 실행 =====
N = int(input("N 입력 (2~5): "))

A = make(N)  # 행렬 생성

print("\n원래 행렬")
show(A)

T = trans(A, N)  # 전치 행렬

print("\n전치 행렬")
show(T)