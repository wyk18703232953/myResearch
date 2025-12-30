from math import factorial as fact
import random


def main(n: int):
    """
    n 作为规模参数，用来生成测试数据：
    - 目标串 a：长度为 n，由 '+' 和 '-' 构成
    - 当前串 b：长度为 n，由 '+', '-', '?' 构成
    """
    # 生成长度为 n 的目标串 a（只有 + 和 -）
    a = ''.join(random.choice(['+', '-']) for _ in range(n))

    # 生成长度为 n 的当前串 b（+, -, ?）
    b = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    aplus = a.count('+')
    aminus = len(a) - aplus

    bplus = b.count('+')
    bminus = b.count('-')
    bjolly = len(b) - bplus - bminus  # 即 '?' 的数量

    if bplus > aplus or bminus > aminus:
        print(0)
    else:
        c = aplus - bplus
        # 使用组合数 C(bjolly, c) / 2**bjolly
        res = fact(bjolly) / fact(bjolly - c) / fact(c) / 2 ** bjolly
        print(res)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)