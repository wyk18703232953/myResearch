def cntbit(n: int) -> int:
    ans = 0
    while n:
        ans += 1
        n //= 2
    return ans


def solve(l: int, r: int) -> int:
    c1 = cntbit(l)
    c2 = cntbit(r)
    if c2 > c1:
        return 2 ** c2 - 1
    else:
        x = l ^ r
        c = cntbit(x)
        return 2 ** c - 1


def main(n: int):
    """
    按规模 n 生成 (l, r) 测试数据，并输出结果。
    这里示例生成方式为：
      l = 2^(n-1), r = 2^n - 1  (n >= 1)
    若 n < 1，则使用默认 (l, r) = (1, 1)。
    """
    if n < 1:
        l, r = 1, 1
    else:
        l = 1 << (n - 1)       # 2^(n-1)
        r = (1 << n) - 1       # 2^n - 1

    result = solve(l, r)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(5)，按规模 5 生成测试数据并输出结果
    main(5)