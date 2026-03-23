Wonsup = int(input())
Sehi = int(input())
Sangun = int(input())
Sung = int(input())
Kangsu = int(input())

if Wonsup<40:
    Wonsup = 40
if Sehi<40:
    Sehi = 40
if Sangun<40:
    Sangun = 40
if Sung<40:
    Sung = 40
if Kangsu < 40:
    Kangsu = 40
    
S = (Wonsup + Sehi + Sangun + Sung + Kangsu)//5
print(S)