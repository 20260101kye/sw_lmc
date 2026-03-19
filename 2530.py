A, B, C = map(int,input().split())
D = (int(input()))
ResultTime = (A * 3600) + (B * 60) + C + D
print(((ResultTime//3600)%24), ((ResultTime%3600)//60), (ResultTime%60))