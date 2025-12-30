import math
import random

def binom(n, m):
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))

def main(n):
    # 生成长度为 n 的正确字符串，只包含 '+' 和 '-'
    correct = ''.join(random.choice('+-') for _ in range(n))

    # 生成长度为 n 的接收字符串，包含 '+', '-', '?'
    received = ''.join(random.choice('+-?') for _ in range(n))

    plus_correct = correct.count('+')
    min_correct = correct.count('-')
    pos_correct = plus_correct - min_correct

    plus_received = received.count('+')
    min_received = received.count('-')
    unknown = received.count('?')
    pos_received = plus_received - min_received

    diff = abs(pos_correct - pos_received)

    if (diff + unknown) % 2 != 0 or diff > unknown:
        prob = 0.0
    else:
        m = (diff + unknown) // 2
        prob = binom(unknown, m) / (2 ** unknown)

    print(prob)

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)