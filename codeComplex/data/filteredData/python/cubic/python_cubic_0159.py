from collections import defaultdict
import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里生成 1 到 9 的随机整数序列
    N = n
    X = [random.randint(1, 9) for _ in range(N)]

    dp1 = defaultdict(lambda: -1)
    M = 1001

    def ec(i, j):
        return i * M + j

    # 初始化长度为1的区间
    for i in range(N):
        dp1[ec(i, i + 1)] = X[i]

    # 预处理所有区间 [j, j+i)
    for length in range(2, N + 1):
        for j in range(N - length + 1):
            for k in range(1, length):
                u = dp1[ec(j, j + k)]
                v = dp1[ec(j + k, j + length)]
                if u != -1 and v != -1 and u == v:
                    dp1[ec(j, j + length)] = u + 1
                    break

    # 区间 DP 统计答案
    INF = 10 ** 18
    dp2 = [INF] * (N + 1)
    dp2[0] = 0

    for i in range(N):
        for j in range(i + 1):
            if dp1[ec(j, i + 1)] == -1:
                continue
            dp2[i + 1] = min(dp2[i + 1], dp2[j] + 1)

    # 输出结果（可以根据需要同时输出测试数据）
    print(dp2[-1])


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)