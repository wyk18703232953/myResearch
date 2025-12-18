n,k = map(int, input().split())

l = 0
r = n
while True:
    m = int((l+r)/2)    # предполагаю сколько конфет она съела
    S = int(((n-m)**2 + n - 3 * m)/2)  # сколько конфет осталось
    if S == k:
        print(m)
        break
    elif S < k:
        r = m
    else:
        l = m