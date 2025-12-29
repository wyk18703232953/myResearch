import random

def main(n: int):
    """
    n: 问题规模，用来控制生成测试数据的范围
    输出：按照原程序逻辑打印结果
    """
    # 1. 生成测试数据
    # 为了保证有意义的测试，m 至少为 1，k,l 在 [0, n] 范围内
    m = random.randint(1, max(1, n))     # 避免除以 0
    k = random.randint(0, max(1, n))
    l = random.randint(0, max(1, n))

    # 原始逻辑
    if (l + k) % m == 0:
        c = (l + k) // m
    else:
        c = (l + k) // m + 1

    if m * c > n:
        print(-1)
    else:
        print(c)

if __name__ == "__main__":
    # 举例：以 n=100 运行一次
    main(100)