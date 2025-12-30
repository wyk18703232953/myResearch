import random
import math

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def main(n):
    # 根据 n 生成测试数据
    # 这里示例：l 中为 1~10^9 的随机数，c 中为 1~10^6 的随机费用
    # 可按需要调整生成策略
    random.seed(0)
    l = [random.randint(1, 10**9) for _ in range(n)]
    c = [random.randint(1, 10**6) for _ in range(n)]

    a = {0: 0}
    b = [0]

    for i in range(n):
        # 固定当前已有的 gcd 集合长度，避免在循环中动态扩展导致逻辑错误
        current_b = list(b)
        for p in current_b:
            d = gcd(p, l[i])
            cost = a[p] + c[i]
            if d not in a:
                a[d] = cost
                b.append(d)
            elif a[d] > cost:
                a[d] = cost

    if 1 not in a:
        a[1] = -1

    # 原程序是 print(a[1])，这里返回结果
    return a[1]


if __name__ == "__main__":
    # 示例：调用 main(5)，仅用于运行演示
    n = 5
    result = main(n)
    print(result)