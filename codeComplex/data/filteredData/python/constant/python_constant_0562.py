import math
import random

def main(n):
    """
    n 作为规模参数，用于生成测试数据：
    - n: 总糖果数的上限
    自动生成 m, k, l，并执行原逻辑。
    """

    # 合理生成测试数据
    # 保证 n 至少为 1，防止无效数据
    n = max(1, n)

    # 生成 n, m, k, l
    # 原程序中 n 是输入之一，这里用规模参数控制上限，实际 n_input 随机生成
    n_input = random.randint(1, n)
    m = random.randint(1, max(1, n // 2))  # 每人需要 m，控制一下范围
    k = random.randint(0, n)               # 已有的数量
    l = random.randint(0, n)               # 需要额外的数量

    one_friend = (k + l) // m + int((k + l) % m != 0)
    if one_friend * m > n_input:
        result = -1
    else:
        result = one_friend

    print(result)


if __name__ == '__main__':
    # 示例：使用 n=100 作为规模
    main(100)