from math import factorial
import random

def main(n: int):
    # 1. 生成测试数据
    # 生成长度为 n 的 drazil，只包含 '+' 和 '-'
    drazil = ''.join(random.choice(['+', '-']) for _ in range(n))

    # 生成长度为 n 的 dreamoon，包含 '+', '-', '?' 三种情况
    dreamoon = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    # 2. 原逻辑计算
    net_drazil = 0
    net_dreamoon = 0
    uncretain_count = 0

    for ch in drazil:
        if ch == '-':
            net_drazil -= 1
        else:
            net_drazil += 1

    for ch in dreamoon:
        if ch == '-':
            net_dreamoon -= 1
        elif ch == '+':
            net_dreamoon += 1
        else:  # '?'
            uncretain_count += 1

    x = (uncretain_count + (net_drazil - net_dreamoon)) // 2
    y = (uncretain_count - (net_drazil - net_dreamoon)) // 2

    if abs(x) + abs(y) != uncretain_count or x < 0 or x > uncretain_count:
        print(0.0)
    else:
        out = factorial(uncretain_count) // (factorial(x) * factorial(uncretain_count - x))
        print(out / (2 ** uncretain_count))


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)