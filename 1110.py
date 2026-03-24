N = int(input())
original = N
count = 0

while True:
    tens = N//10
    ones = N%10
    
    new_num = ones * 10 + (tens+ones)%10
    
    count += 1
    N =new_num
    
    if N == original:
        break
        
print(count)