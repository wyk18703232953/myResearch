def main(n):
    # 这里我们需要一个 k，使得条件与原程序一致：
    # 原程序中：如果 (k*k - k)//2 + 1 < n 则输出 -1
    # 说明能处理的最大 n 为 (k*k - k)//2 + 1
    # 因此我们可以根据给定 n，先搜索一个合适的 k（若不存在则结果为 -1）

    # 辅助函数：对给定 n 和 k，按原逻辑计算答案
    def solve_for_k(n, k):
        if n == 1:
            return 0
        if (k * k - k) // 2 + 1 < n:
            return -1
        g, b = 0, k // 2
        while b != 0:
            while (
                g + b <= k
                and (k * k - k) // 2 + 1 - ((g + b) ** 2 - (g + b)) // 2 >= n
            ):
                g += b
            b //= 2
        return k - g

    # 生成测试数据：这里只给出 n，本题逻辑中需要一个合适的 k
    # 我们从 1 开始增大 k，直到找到能覆盖 n 的 k，或达到一定上界
    if n <= 0:
        print(-1)
        return

    # 简单上界估计：解 (k^2 - k)/2 + 1 >= n 得 k ~ sqrt(2n)
    # 为保守起见，取上界为 2 * int((2*n)**0.5) + 5
    import math

    k_upper = 2 * int(math.isqrt(2 * n)) + 5
    answer = -1
    chosen_k = None

    for k in range(1, k_upper + 1):
        if (k * k - k) // 2 + 1 >= n:
            chosen_k = k
            answer = solve_for_k(n, k)
            break

    if chosen_k is None:
        # 即使上界内没找到合适 k，则视为不可行
        print(-1)
    else:
        # 输出和原程序一致的结果
        print(answer)


# 示例：在本文件直接运行时，可以简单调用 main
if __name__ == "__main__":
    # 可以自行修改 n 测试
    test_n = 10
    main(test_n)