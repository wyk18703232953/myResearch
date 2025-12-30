import math
import random

def solve(a: str, b: str) -> float:
    c = 0
    d = 0
    q = 0

    for ch in a:
        if ch == "+":
            c += 1
        elif ch == "-":
            c -= 1

    for ch in b:
        if ch == "+":
            d += 1
        elif ch == "-":
            d -= 1
        else:
            q += 1

    if c == d:
        # 这里的原代码使用了 q/2 而不是 q//2，保持与原代码一致
        return (math.factorial(q) /
                (math.factorial(q / 2) * math.factorial(q / 2))) / (2 ** q)
    else:
        mx = d + q
        mn = d - q
        if c > mx or c < mn:
            return 0.0
        else:
            ans = c - d
            if ans > 0:
                return (math.factorial(q) /
                        (math.factorial(((q - ans) / 2) + ans) *
                         math.factorial((q - ans) / 2))) / (2 ** q)
            else:
                return (math.factorial(q) /
                        (math.factorial((q - ans) / 2) *
                         math.factorial(((q - ans) / 2) + ans))) / (2 ** q)


def main(n: int):
    # 生成测试数据：
    # a: 长度为 n，由 '+' 和 '-' 随机组成
    # b: 长度为 n，由 '+', '-', '?' 随机组成
    symbols_a = ['+', '-']
    symbols_b = ['+', '-', '?']

    a = ''.join(random.choice(symbols_a) for _ in range(n))
    b = ''.join(random.choice(symbols_b) for _ in range(n))

    result = solve(a, b)
    print(result)


if __name__ == "__main__":
    # 示例：使用 n = 10 运行一次
    main(10)