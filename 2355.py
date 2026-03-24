A, B = map(int, input().split())

start = min(A, B)
end = max(A, B)

n = end - start + 1
print(n*(start+end)//2)