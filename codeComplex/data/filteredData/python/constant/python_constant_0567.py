import math

def main(n):
    # 解释输入结构：
    # 原程序读取四个整数：n, m, k, l
    # 这里将 n 作为最大规模参数，
    # 构造一个确定性的四元组 (N, M, K, L)
    #
    # 规模含义：
    # - N 作为原问题的 n（总数）
    # - M 作为原问题的 m（每组大小），保证 M>=1
    # - K, L 均与 n 线性相关，保证 0 <= K, L <= N
    #
    # 这种构造保证：
    # - 对相同的 n，生成的数据完全确定
    # - 输入规模随 n 线性放大，便于时间复杂度实验

    if n < 4:
        N = 4

    else:
        N = n

    M = max(1, N // 3)
    K = N // 4
    L = N // 5

    n_val, m, k, l = N, M, K, L

    ost = n_val - k
    need = (l + k)
    if ost < l or need > n_val:
        # print(-1)
        pass
        return
    ans = (l + k - 1) // m + 1
    if ans * m - k >= l and ans * m <= n_val:
        # print(ans)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)