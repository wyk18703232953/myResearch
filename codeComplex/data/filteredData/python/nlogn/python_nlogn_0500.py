def main(n):
    m = n * (n // 2) * 10
    sun, su, ans = 0, 0, 0
    dif = []
    for i in range(1, n + 1):
        a = i * 5
        b = i * 3
        sun += a
        su += b
        dif.append(a - b)
    if su > m:
        print(-1)
    elif sun == m:
        print(0)
    else:
        dif.sort()
        j = n - 1
        while sun > m and j >= 0:
            sun -= dif[j]
            ans += 1
            j -= 1
        print(ans)

if __name__ == "__main__":
    main(10)