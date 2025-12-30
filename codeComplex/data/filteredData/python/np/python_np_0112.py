import math
import random

def main(n):
    # 生成测试数据：根据规模 n 生成两个长度为 n 的字符串，仅由 '+' 和 '-' 构成
    a = [random.choice(['+', '-']) for _ in range(n)]
    b = [random.choice(['+', '-']) for _ in range(n)]

    p = a.count('+') - b.count('+')
    m = a.count('-') - b.count('-')

    if m < 0 or p < 0:
        print(0)
        return

    l = math.factorial(p + m) / (math.factorial(p) * math.factorial(m))
    print(l * (0.5 ** (p + m)))


if __name__ == "__main__":
    # 示例：可在此处修改 n 测试不同规模
    main(10)