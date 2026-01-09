def main(n):
    if n < 2:
        return
    if n % 2 == 1:
        n -= 1
        if n < 2:
            return

    # 构造确定性输入 b，长度为 n//2
    half = n // 2
    b = [i * 2 + 1 for i in range(half)]

    a = [0] * n

    minV = 0
    maxV = b[0]

    m = n // 2

    a[n - 1] = b[0]

    i = 1
    j = n - 2

    while i < m:
        if b[i] - minV > 0 and b[i] - minV <= maxV:
            a[i] = minV
            a[j] = b[i] - minV
            maxV = min(maxV, b[i] - minV)

        else:
            a[i] = b[i] - maxV
            a[j] = maxV
            minV = max(minV, b[i] - maxV)

        i += 1
        j -= 1

    # print(' '.join(map(str, a)))
    pass
if __name__ == "__main__":
    main(10)