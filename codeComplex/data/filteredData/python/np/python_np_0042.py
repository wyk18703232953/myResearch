import math
import random

def main(n):
    # 生成测试数据：
    # a: 长度为 n，由 '+' 和 '-' 组成
    # b: 长度为 n，由 '+', '-', '?' 组成
    a = ''.join(random.choice(['+', '-']) for _ in range(n))
    b = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    posa = a.count('+') - a.count('-')
    posb = b.count('+') - b.count('-')
    q = b.count('?')
    dist = posa - posb
    ones = (abs(dist) + q) / 2

    if q < abs(dist) or ((dist + q) % 2):
        ans = 0.0
    else:
        ans = float(math.factorial(q) / (math.factorial(ones) * math.factorial(q - ones)))
        ans /= pow(2, q)

    print(f'{ans:.9f}')

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)