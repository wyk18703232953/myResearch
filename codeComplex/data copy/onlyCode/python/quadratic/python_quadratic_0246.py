n,a,b = list( map(int, input().split()))

if min(a,b) >1:
    print('NO')
    exit()

m = max(a,b)

if m == 1:
    if n == 1:
        print('YES')
        print(0)
        exit()
    elif n < 4:
        print('NO')
        exit()
    else:
        print('YES')
        for row in range(n):
            line = ['0']*n
            if row >0:
                line[row-1] = '1'
            if row <n-1:
                line[row+1] = '1'
            print(''.join(line))
    exit()

print('YES')

if a == 1:
    c = '1'
    d = '0'
else:
    c = '0'
    d = '1'
for row in range(n):
    if row < m-1:
        line = [c]*n
    else:
        line = [c]*(m-1)+ [d]*(n-m+1)
    line[row] = '0'

    print(''.join(line))
