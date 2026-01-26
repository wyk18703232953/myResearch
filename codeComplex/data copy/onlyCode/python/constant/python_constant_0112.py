# https://codeforces.com/problemset/problem/313/A

n = int(input())

if n > 0:
    print(n)
else:
    n = n * -1
    x = n % 10
    y = (n // 10) % 10

    if x > y:
        print(-(n // 10))
    else:
        print(-((n // 100)* 10 + x))
