import math
import random


def main(n: int):
    """
    n: 用作测试规模参数，这里用来生成测试数据 (n, k)
    约定：
      - n 为原题中的 n
      - k 由规模参数 n 随机生成：1 <= k <= n
    """
    # 生成测试数据
    N = n if n > 0 else 1
    K = random.randint(1, N)

    # 原始逻辑：n, k 已从 input() 改为使用生成的 N, K
    ans = N - int((math.sqrt(9 + 8 * (N + K)) - 3) / 2)
    print(ans)


if __name__ == "__main__":
    # 示例：使用规模 10 调用
    main(10)