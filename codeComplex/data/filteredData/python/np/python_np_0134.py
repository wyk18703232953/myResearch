import random
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main(n):
    # 1. 生成测试数据
    # 这里假设 l 和 c 的取值范围为 1~10**9，可根据需要调整
    random.seed(0)  # 固定种子，保证可复现
    l = [random.randint(1, 10**9) for _ in range(n)]
    c = [random.randint(1, 10**9) for _ in range(n)]

    # 2. 原始逻辑
    a = {0: 0}

    for i in range(n):
        b = a.copy()
        for g, cost_so_far in a.items():
            d = gcd(g, l[i])
            cost = cost_so_far + c[i]
            if d not in b or b[d] > cost:
                b[d] = cost
        a = b

    if 1 not in a:
        a[1] = -1

    # 3. 输出结果
    print(a[1])

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)