T = int(input())
for _ in range(T):
    N = int(input())

    if N%2 == 1:
        print("NO")
    else:
        N //= 2
        if N**(1/2) == int(N**(1/2)):
            print("YES")
        else:
            if N%2 == 1:
                print("NO")
            else:
                N //= 2
                if N**(1/2) == int(N**(1/2)):
                    print("YES")
                else:
                    print("NO")