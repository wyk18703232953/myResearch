import math
import random

def main(n: int):
    # 生成测试数据：
    # s1 只含 '+' 和 '-'，长度为 n
    # s2 含 '+', '-', '?'，长度为 n
    # 保证规模由 n 控制（这里用长度为 n 的字符串）
    chars_s1 = ['+', '-']
    chars_s2 = ['+', '-', '?']

    s1 = ''.join(random.choice(chars_s1) for _ in range(n))
    s2 = ''.join(random.choice(chars_s2) for _ in range(n))

    # 原逻辑
    s1p = s1.count("+")
    s1m = s1.count("-")
    s2p = s2.count("+")
    s2m = s2.count("-")
    s2q = 0
    if '?' in s2:
        s2q = s2.count("?")
    if s2q == 0:
        if s1p == s2p and s1m == s2m:
            print(f"{1:.12f}")
        else:
            print(f"{0:.12f}")
    else:
        if s1p >= s2p and s1m >= s2m:
            ways = math.factorial(s2q) / (
                math.factorial(s1p - s2p) * math.factorial(s1m - s2m)
            )
            print(f"{ways / (2 ** s2q):.12f}")
        else:
            print(f"{0:.12f}")


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)