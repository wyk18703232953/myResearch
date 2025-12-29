from math import factorial
import random

def main(n):
    # 1. 生成测试数据：根据规模 n 生成两个只包含 '+' 和 '-' 的字符串
    # 实际逻辑只与 '+' 和 '-' 的个数有关，这里让两个字符串长度都为 n
    choices = ['+', '-']
    s1 = ''.join(random.choice(choices) for _ in range(n))
    s2 = ''.join(random.choice(choices) for _ in range(n))

    # 2. 按原逻辑计算
    a = s1.count('+') - s2.count('+')
    b = s1.count('-') - s2.count('-')

    if a < 0 or b < 0:
        ans = 0.0
    else:
        total = a + b
        # 组合数 C(total, a)
        comb = factorial(total) / (factorial(a) * factorial(b))
        ans = comb / (2 ** total)

    print(f"{ans:.10f}")

if __name__ == "__main__":
    # 示例：可自行修改 n 以测试不同规模
    main(10)