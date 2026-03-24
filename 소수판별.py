import time

n = int(input("자연수를 입력하세용> "))

start_time = time.time()

start_time = time.time()
for i in range(2, n) :
    if n % i == 0 :
        print("{N}은 {I}로 나누어 떨어집니다.".format(N = n, I = i))
        break
else :
    print("{N}은 소수입니다.".format(N = n))


print("걸린 시간 :", time.time() - start_time)
