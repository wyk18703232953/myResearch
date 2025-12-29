import random

mod = 10**9 + 7
mod1 = 998244353

# 原代码中大量全局和函数未被实际使用，这里仅保留核心逻辑 hnbhai 的功能

def digit_at_position(n: int) -> str:
    """
    等价于原 hnbhai 中对给定 n (1-based) 查找“1234567891011...”拼接序列中第 n 个字符。
    """
    d, num = 0, 1
    # 找到所在位数段
    while num <= n:
        num += 9 * (d + 1) * (10 ** d)
        d += 1
    # 回退到该位数段的起始位置
    num -= 9 * d * (10 ** (d - 1))
    # 找到所在整数
    base = 10 ** (d - 1)
    index_in_block = n - num  # 0-based index within this d-digit block
    number = base + index_in_block // d
    s = str(number)
    return s[index_in_block % d]


def main(n: int):
    """
    n 为规模参数。
    根据 n 生成测试数据，并调用 digit_at_position 逻辑。

    测试数据设计：
      - 对于 n <= 0：不进行任何输出。
      - 对于 n > 0：
          * 生成 q = n 个查询位置（第 k 个字符），
            每个位置在 [1, max_pos] 中随机选取，
            其中 max_pos 设置为 10^6 以保证运行速度。
          * 对每个查询位置，输出对应的字符。
    """
    if n <= 0:
        return

    max_pos = 10**6
    q = n

    # 生成 q 个查询位置
    positions = [random.randint(1, max_pos) for _ in range(q)]

    # 对每个位置输出对应字符
    for pos in positions:
        ch = digit_at_position(pos)
        print(ch)


if __name__ == "__main__":
    # 示例：当作为脚本运行时，可自己设定一个规模，比如 n = 5
    main(5)