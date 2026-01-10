def main(n):
    m = n
    a = [(i * 3 + 1) % (n + 5) + 1 for i in range(m)]
    a.sort()
    h = 0
    ans = 0
    for i in range(n - 1):
        ans += a[i] - 1
        if a[i] > h:
            h += 1
    if h < max(a):
        ans += h
    else:
        ans += a[-1] - 1
    print(ans)


if __name__ == "__main__":
    main(10)