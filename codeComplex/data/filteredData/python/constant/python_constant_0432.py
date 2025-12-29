import math
import random

def main(n):
    # 生成测试数据：k 的取值范围根据原逻辑合理设定
    # 原代码逻辑对 k 的判断有：n == k, k > 2*n, 以及与 n、k-1、k//2 的比较
    # 因此将 k 生成在 [1, 3*n] 范围内较合适
    k = random.randint(1, 3 * n)

    # 原始逻辑
    if n == k:
        print(math.ceil(n / 2) - 1)
    elif k > 2 * n:
        print(0)
    else:
        print(min(n, k - 1) - k // 2)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需调整
    main(10)