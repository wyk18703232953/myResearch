def main(n):
    # 将原来的 m 也作为规模的一个确定性函数
    # 这里取 m = 2^k - 1，其中 k = n//2，且限定在 [1, n]
    if n <= 0:
        return
    k = max(1, min(n, n // 2 if n // 2 > 0 else 1))
    m = (1 << k) - 1

    a = [0] * (n + 1)
    l, r = 1, n

    for i in range(1, n + 1):
        if m <= 1 << max((n - i - 1), 0):
            a[l] = i
            l += 1
        else:
            a[r] = i
            r -= 1
            m -= 1 << max((n - i - 1), 0)

    a.pop(0)
    print(" ".join(map(str, a)))


if __name__ == "__main__":
    # 示例调用：可按需修改 n
    main(10)