def isqrt(n: int) -> int:
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def solve(n: int, k: int) -> int:
    # 使用整数运算避免浮点误差：
    # answer = int((-1/2)*isqrt(8*k + 8*n + 9) + n + 3/2)
    #        = n + 1 - ceil(isqrt(8k+8n+9)/2)
    s = isqrt(8 * k + 8 * n + 9)
    answer = n + 1 - (s // 2 if s % 2 == 0 else (s // 2 + 1))
    return answer


def main(n: int):
    """
    根据规模 n 生成测试数据，并输出原程序的结果。
    这里构造一个中等规模的 k，保证 0 <= k <= n(n+1)/2：
    例如取 k = n*(n+1)//4（约为最大值的一半）。
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    # 生成测试数据 k
    k = n * (n + 1) // 4

    ans = solve(n, k)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：可以修改这里的 n 来测试不同规模
    main(10)