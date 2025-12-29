def factorial(num: int):
    res = 1
    while num >= 1:
        res *= num
        num -= 1
    return res


def main(n: int):
    """
    n 为规模参数，用于生成测试数据：
    - actual 为长度为 n 的由 '+' 和 '-' 组成的字符串
    - processed 为在 actual 基础上随机替换部分字符为 '+' 或 '-' 的字符串，
      或者在一部分位置保留未知状态（这里用 '?' 表示未确定，模拟原题常见场景）。
    这里为了可复现、简单起见，不使用随机，而是按固定规则构造：
      actual: 前 n//2 个为 '+', 后 n - n//2 个为 '-'
      processed:
         前 n//4 个为 '+'
         中间 n//4 个为 '-'
         剩余位置为 '?'
    """

    # 生成 actual
    plus_count = n // 2
    minus_count = n - plus_count
    actual = '+' * plus_count + '-' * minus_count

    # 生成 processed（包含部分已确定的 '+' 和 '-'，其余为 '?'）
    quarter = n // 4
    second_quarter = n // 4
    known_plus = '+' * quarter
    known_minus = '-' * second_quarter
    unknown_len = n - quarter - second_quarter
    processed = known_plus + known_minus + '?' * unknown_len

    # 逻辑与原程序一致，只是将 processed 中的 '?' 视为未决定的位：
    # 在原题设中，一般 processed 中的 '+' 和 '-' 是已决定的，其他位置为 '?'，
    # 然后计算恰好达到 actual 的概率。
    # 此处沿用原代码逻辑：对 actual 和 processed 中已确定的部分进行统计。

    actualPos = actual.count('+')
    actualNeg = actual.count('-')
    processedPos = processed.count('+')
    processedNeg = processed.count('-')

    # 如果 processed 已确定的 '+' 或 '-' 超过 actual 中对应的数量，则概率为 0
    if processedPos > actualPos or processedNeg > actualNeg:
        print(0)
    # 如果已确定部分已经完全等于目标，则概率为 1
    elif processedPos == actualPos and processedNeg == actualNeg:
        print(1)
    else:
        remainPos = actualPos - processedPos
        remainNeg = actualNeg - processedNeg

        # 组合数 C(remainPos + remainNeg, remainPos) / 2^(remainPos + remainNeg)
        ans = (factorial(remainPos + remainNeg) /
               (factorial(remainPos) * factorial(remainNeg))) / (2 ** (remainPos + remainNeg))
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)