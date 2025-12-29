import math
import random

def solutions(a, b, c):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - math.sqrt(d)) / (2 * a)
    sol2 = (-b + math.sqrt(d)) / (2 * a)
    if sol1 < 0 < sol2:
        return sol2
    elif sol2 < 0 < sol1:
        return sol1
    else:
        return 0

def main(n):
    # 根据规模 n 生成测试数据，这里简单设定：
    # c, m 为 1..n 范围内的随机整数
    c = random.randint(1, n)
    m = random.randint(1, n)

    result = int(c - solutions(1, 3, -(2 * c + 2 * m)))
    print(result)

if __name__ == "__main__":
    # 示例：使用 n = 100 作为规模
    main(100)