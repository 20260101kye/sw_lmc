T = int(input())

for _ in range(T):
    s = input()
    stack = []
    is_valid = True
    
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:  
            if stack:
                stack.pop()
            else:
                is_valid = False
                break
    
    if stack:
        is_valid = False
    
    if is_valid:
        print("YES")
    else:
        print("NO")