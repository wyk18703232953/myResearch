import math
import random

def valid(n, k, c1, c2):
    if c1 > n:
        return c2
    elif c2 > n:
        return c1
    ans_one = ((n - c1) * (n - c1 + 1) // 2) - c1
    if ans_one == k:
        return c1
    return c2

def f(n, k):
    b2 = (2 * n + 3)
    delta = int(math.sqrt(8 * n + 8 * k + 9))
    return valid(n, k, (b2 + delta) // 2, (b2 - delta) // 2)

def main(n):
    # 根据规模 n 生成测试数据：
    # 约束一个合理的 k 范围，这里取 [0, n*(n+1)//2] 作为示例
    max_k = n * (n + 1) // 2
    k = random.randint(0, max_k)
    result = f(n, k)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可按需修改 n
    main(10)