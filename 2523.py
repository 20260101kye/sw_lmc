star = int(input())
for i in range(1,star+1):
    print('*' *i)
for i in range(star-1, 0, -1):
    print('*'*i)

# range(star-1, 0, -1): star-1(해당)부터 -1씩 내려감. 0직전까지