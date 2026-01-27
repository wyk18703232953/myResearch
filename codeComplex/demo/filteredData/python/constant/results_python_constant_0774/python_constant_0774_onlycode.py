def solve():
    n = int(input())
    for d in [2,4]:
        if n % d != 0:
            continue
        temp = int((n//d) ** (0.5))
        temp -= 1
        while temp*temp < n//d:
            temp += 1
        if temp*temp == n//d:
            print("YES")
            return
    print("NO")
for _ in range(int(input())):
    solve()
