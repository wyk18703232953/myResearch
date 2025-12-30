from collections import defaultdict
import random


def main(n: int) -> int:
    """
    n: 规模，表示数组 X 的长度
    返回值：原程序最后输出的 dp2[-1]
    """
    # ---------- 生成测试数据 ----------
    # 这里生成 1 到 5 之间的随机整数作为示例
    # 如需固定数据，可改成固定数组或带种子的随机
    X = [random.randint(1, 5) for _ in range(n)]

    N = n
    dp1 = defaultdict(lambda: -1)
    M = 1001

    def ec(i, j):
        return i * M + j

    # 初始化长度为 1 的区间
    for i in range(N):
        dp1[ec(i, i + 1)] = X[i]

    # 预处理所有区间的“压缩值”
    for length in range(2, N + 1):
        for j in range(N - length + 1):
            for k in range(1, length):
                u, v = dp1[ec(j, j + k)], dp1[ec(j + k, j + length)]
                if u != -1 and v != -1 and u == v:
                    dp1[ec(j, j + length)] = u + 1
                    break

    # dp2: 最少分段数
    dp2 = [0] * (N + 1)
    for i in range(N):
        dp2[i + 1] = dp2[i] + 1
        for j in range(i + 1):
            if dp1[ec(j, i + 1)] == -1:
                continue
            dp2[i + 1] = min(dp2[i + 1], dp2[j] + 1)

    # 输出结果（也返回结果便于调用方使用）
    print(dp2[-1])
    return dp2[-1]


if __name__ == "__main__":
    # 示例：n = 10
    main(10)