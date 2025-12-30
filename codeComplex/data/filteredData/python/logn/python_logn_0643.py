import math
import random

def main(n):
    """
    n: 规模参数，用于生成测试数据 N, K
    逻辑：根据题意，原代码读取 N, K 并输出 int(N - x)，其中
          x = (-3 + sqrt(9 + 4 * (2N + 2K))) / 2
    这里用 n 生成一组随机的 (N, K)，再执行同样逻辑。
    """

    # 根据规模 n 生成测试数据 N, K（示例策略，可按需调整）
    # 保证 N, K 为正整数
    random.seed(0)  # 固定随机种子，便于复现
    N = max(1, n)
    # 生成一个与 n 同数量级的 K
    K = random.randint(1, max(1, 2 * n))

    # 原逻辑
    x = (-3 + math.sqrt(9 + 4 * (2 * N + 2 * K))) / 2
    ans = int(N - x)

    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)