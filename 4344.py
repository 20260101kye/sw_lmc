C = int(input())

for _ in range(C):
    data = list(map(int, input().split()))
    
    N = data[0]         
    scores = data[1:]   
    
    avg = sum(scores) / N
    
    count = 0
    for score in scores:
        if score > avg:
            count += 1
    
    percent = (count / N) * 100
    print("{:.3f}%".format(percent))