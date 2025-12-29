import math
import random

def C(a, b):
    return math.factorial(a) // (math.factorial(b) * math.factorial(a - b))

def main(n: int):
    """
    n 为字符串长度（题目中两行字符串等长）
    自动生成测试数据并计算结果。
    """

    # 生成目标串 a：只包含 '+' 和 '-'
    # 尽量均匀随机
    a = [random.choice(['+', '-']) for _ in range(n)]

    # 生成含 '?' 的串 b：
    # 每个位置独立随机为 '+', '-', 或 '?'
    choices = ['+', '-', '?']
    b = [random.choice(choices) for _ in range(n)]

    x = y = d = 0
    ans = 0
    power = 0

    for i in range(len(a)):
        if a[i] == '+':
            x += 1
        if a[i] == '-':
            x -= 1
        if b[i] == '?':
            d += 1
        if b[i] == '+':
            y += 1
        if b[i] == '-':
            y -= 1

    plus, minus = d, 0
    for _ in range(0, d + 1):
        k = C(d, plus)
        if y + (plus - minus) == x:
            ans += k
        power += k
        plus -= 1
        minus += 1

    # 输出格式与原题一致
    print("{0:.12f}".format(ans / power if power != 0 else 0.0))

# 示例：当直接运行本文件时，可调用 main
if __name__ == "__main__":
    main(10)