def mus(x: int) -> int:
    c = 0
    while x > 0:
        c += x % 10
        x //= 10
    return c

def count_valid(n: int, s: int) -> int:
    ans = s + 10 - s % 10 if s % 10 != 0 else s
    while ans - mus(ans) < s:
        ans += 10
    if ans > n:
        return 0

    else:
        return n - ans + 1

def main(n: int) -> int:
    """
    使用规模参数 n 自动生成测试数据，并返回原程序的输出结果。
    测试数据生成策略（可按需修改）：
    - n: 由调用者传入
    - s: 取为 n // 2 作为一个中等规模的阈值
    """
    s = n // 2
    return count_valid(n, s)

if __name__ == "__main__":
    # 示例：运行 main(10**18) 或其他规模
    example_n = 10**6
    # print(main(example_n))
    pass