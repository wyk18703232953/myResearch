import math
import random

def main(n):
    """
    n: 规模参数，用来生成测试数据中的 n。
    这里原始程序逻辑需要两个整数 n, k。
    我们用传入的 n 作为等式中的 n，
    并根据 n 生成一个合法范围内的 k。
    """
    # 生成测试数据：
    # 为了保证判别式非负，需要 0 <= k <= n(n+1)/2
    max_k = n * (n + 1) // 2
    # 随机选择一个 k
    k = random.randint(0, max_k)

    # 原始逻辑：
    # a = 1
    # b = -(2*n + 3)
    # c = n*(n+1) - 2*k
    # x = (-b - int(sqrt(b^2 - 4ac))) // (2a)
    a = 1
    b = -(2 * n + 3)
    c = n * (n + 1) - 2 * k
    disc = b * b - 4 * a * c
    x = (-b - int(math.isqrt(disc))) // (2 * a)

    # 输出结果（原代码只输出 x）
    print(f"n = {n}, k = {k}, x = {x}")

if __name__ == '__main__':
    # 示例：调用 main(10)
    main(10)