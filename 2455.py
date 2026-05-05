A, B = map(int, input().split())
C, D = map(int, input().split())
E, F = map(int, input().split())
G, H = map(int, input().split())
X = B - C + D 
Y = X - E + F 
Z = Y - G + H
print(max(B, X, Y, Z))