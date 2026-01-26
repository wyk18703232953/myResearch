import math

def main(n):
    """
    n: 测试组数规模（或用于生成测试数据的上界）
    逻辑：对生成的 n 个整数进行原程序中的判定，并输出结果。
    这里简单地将测试数据设置为：a_i = i (1 <= i <= n)
    """
    out = []
    # 生成测试数据：1, 2, ..., n
    for val in range(1, n + 1):
        # 原程序中每个测试用例对单个 n 进行处理
        cur = val

        o1 = math.isqrt(cur // 2)
        o2 = math.isqrt(cur // 4)

        if 2 * o1 * o1 == cur or 4 * o2 * o2 == cur:
            out.append('YES')

        else:
            out.append('NO')

    # print('\n'.join(out))
    pass
if __name__ == "__main__":
    # 示例：当规模为 10 时，处理测试数据 1..10
    main(10)