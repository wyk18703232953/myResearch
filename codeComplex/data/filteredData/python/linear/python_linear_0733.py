def main(n):
    # 生成测试数据：随规模 n 选一个合法的 k（0 <= k <= n）
    # 并保证 (n - k) 为偶数，方便复用原逻辑 (n-k)//2
    if n == 0:
        return  # 无输出
    # 这里简单生成一个 k：若 n 为偶数，则取 k = n//2；若 n 为奇数，则取 k = n//2 + 1
    # 这样 (n - k) 为偶数且 0 <= k <= n
    k = n // 2 if n % 2 == 0 else n // 2 + 1

    d = (n - k) // 2
    s = 0
    res = []
    while s != n:
        if (s + 1) % (d + 1) == 0:
            res.append("1")
        else:
            res.append("0")
        s += 1
    print("".join(res))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)