import random
import math

def gcd(a, b):
    # 使用内置 math.gcd 替代递归实现（等价）
    return math.gcd(a, b)

def main(n):
    # 根据 n 生成测试数据
    # 可以根据需要调整数据范围
    random.seed(0)
    l = [random.randint(1, 10**6) for _ in range(n)]
    c = [random.randint(1, 10**6) for _ in range(n)]

    a = {0: 0}

    for i in range(n):
        b = a.copy()
        for g, cost_g in a.items():
            d = gcd(g, l[i])
            cost = cost_g + c[i]
            if d not in b or b[d] > cost:
                b[d] = cost
        a = b

    if 1 not in a:
        a[1] = -1
    print(a[1])


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改
    main(5)