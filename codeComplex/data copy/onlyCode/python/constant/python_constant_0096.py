for _ in range(int(input())):
    n,m = sorted(map(int,input().split()))
    count = 0
    while n> 0:
        count+= m//n
        m = m%n
        n,m = sorted([n,m])
    print(count)
