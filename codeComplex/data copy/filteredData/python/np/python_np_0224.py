def find(a, b):
    cc = 2
    for i in range(1, (1 << len(a))):
        sx = 0
        minn = 100000000
        maxn = -1
        for j in range(0, len(a)):
            if i & (1 << j):
                sx += a[j]
                minn = min(minn, a[j])
                maxn = max(maxn, a[j])
        if sx >= b[1] and sx <= b[2] and (maxn - minn) >= b[3]:
            cc += 1
    if cc < 2:
        return 2
    else:
        return cc - 2


def main(n):
    if n < 1:
        n = 1
    a = [i % 10 + 1 for i in range(1, n + 1)]
    total_sum = sum(a)
    b0 = 0
    b1 = total_sum // 3
    b2 = (2 * total_sum) // 3
    b3 = (n // 3) if n >= 3 else 0
    b = [b0, b1, b2, b3]
    result = find(a, b)
    print(result)


if __name__ == "__main__":
    main(10)