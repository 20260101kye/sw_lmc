N = int(input())

if N == 1:
    print('*')
else:
    for i in range(2 * N):
        if i % 2 == 0:
            print(('* ' * ((N + 1) // 2)).rstrip())
        else:
            print(' *' * (N // 2))