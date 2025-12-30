import random

def main(n):
    # 生成测试数据
    # 规模 n 即原代码中的 N
    N = n

    # 为了生成合理的 M 和 L，使得 0 < L[1] < L[2] < ... < L[N] < M
    # 这里设定 M 为 10 * N，L 为 [1, 2, ..., N] 的一个随机递增序列
    M = 10 * N
    # 先生成递增的基准序列，再随机扰动一下，使其仍递增
    base = list(range(1, N + 1))
    # 为避免破坏递增性，这里直接使用 base 作为一个合法的递增序列
    L = base[:]  # L[0..N-1]

    # 将原始逻辑封装进来
    L = [0] + L + [M]  # 对应原程序的 L 处理：首尾加 0 和 M
    sumL = [0]
    ans = -10**30

    for i in range(1, N + 1):
        sumL.append(sumL[-1] - (-1) ** i * L[i])

    for i in range(1, N + 1):
        if L[i] > L[i - 1] + 1:
            ans = max(ans, 2 * sumL[i - 1] - sumL[-1] - (-1) ** i * (L[i] - 1))
        if L[i] < L[i + 1] - 1:
            ans = max(ans, 2 * sumL[i] - sumL[-1] + (-1) ** i * (L[i] + 1))

    if N % 2 == 0:
        result = max(ans, sumL[-1] + M)
    else:
        result = max(ans + M, sumL[-1])

    print(result)


# 示例：调用 main(5)
if __name__ == "__main__":
    main(5)