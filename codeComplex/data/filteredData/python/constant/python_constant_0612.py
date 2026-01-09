def calc(x: int) -> int:
    if x <= 0:
        return 0
    if x & 1:
        return -x + calc(x - 1)
    return x // 2


def main(n: int):
    """
    n: 生成 n 组 (a, b) 测试数据并输出 calc(b) - calc(a - 1)
    测试数据规则：
      对于第 i 组 (1 ≤ i ≤ n)：
        a = 1 + (i - 1) * 2
        b = a + i
    确保 a <= b，且都为正整数
    """
    for i in range(1, n + 1):
        a = 1 + (i - 1) * 2
        b = a + i
        # print(calc(b) - calc(a - 1))
        pass
if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)