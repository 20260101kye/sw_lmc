s = input()

while len(s)%3 != 0:
    s = "0" + s
    
for i in range(0, len(s), 3):
    part = s[i:i+3]
    print(int(part, 2), end='')