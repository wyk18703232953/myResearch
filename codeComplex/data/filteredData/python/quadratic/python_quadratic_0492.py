def main(n):
    # 构造确定性的 a, s
    a = [i % n for i in range(n)]
    s = [(n - 1 - i) % n for i in range(n)]

    d = []
    for q in range(n):
        d.append(a[q] + s[q])
    d = [n - q for q in d]
    for q in range(n):
        f = 0
        for q1 in range(q):
            if d[q1] > d[q]:
                f += 1
        g = 0
        for q1 in range(q + 1, n):
            if d[q1] > d[q]:
                g += 1
        if f != a[q] or g != s[q]:
            print('NO')
            break
    else:
        print('YES')
        print(*d)


if __name__ == "__main__":
    main(5)