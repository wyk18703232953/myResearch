import random

def main(n):
    # 生成测试数据：
    # 约定：
    #   1 <= m, k, l <= n
    #   并且适当生成一部分一定无解的情况用于测试
    m = random.randint(1, max(1, n))
    k = random.randint(0, n)     # 允许为 0
    l = random.randint(0, n)     # 允许为 0

    # 原逻辑
    k += l
    x = (k + m - 1) // m
    if m * x > n:
        print(-1)
    else:
        print(x)

if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模参数调用
    main(10)