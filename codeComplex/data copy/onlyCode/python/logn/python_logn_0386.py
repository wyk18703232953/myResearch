from sys import stdout

n = int(input())

if n % 4 == 2:
    print('!', -1)
    exit(0)

l = 1
r = l + n // 2

memo = [-1] * (n + 1)

def check(i):
    if memo[i] == -1:
        print('?', i)
        stdout.flush()

        memo[i] = int(input())

    return memo[i]

while r >= l:
    a = check(l)
    b = check(l + n // 2)
    
    if a == b:
        print('!', l)
        exit(0)

    mid = (l + r) >> 1

    c = check(mid)
    d = check(mid + n // 2)

    if c == d:
        print('!', mid)
        exit(0)

    if (a < b and c < d) or (a > b and c > d):
        l = mid + 1

    else:
        r = mid

    

