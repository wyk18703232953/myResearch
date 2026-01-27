cases = int(input())
while cases:
    cases -= 1
    a, b = map(int, input().split())

    ans = 0
    while a > 0 and b > 0:
        if a < b:
            a, b = b, a
        ans += a//b
        a = a % b

    print(ans)
