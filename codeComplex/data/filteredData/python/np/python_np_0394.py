import random

def main(n):
    # 生成测试数据：n 行，m 列，每个元素为 [1, 10^9] 的随机整数
    # 可根据需要修改 m 或值域
    m = 5  # 固定列数，也可以改为函数参数
    A = [[random.randint(1, 10**9) for _ in range(m)] for _ in range(n)]

    lo, hi = 1 << 32, -1 << 32
    for i in range(n):
        lo = min(min(A[i]), lo)
        hi = max(max(A[i]), hi)

    best = -1
    ans = [-1, -1]

    def possible(x):
        nonlocal best, ans
        # 检查是否存在两行，使得每个列中至少有一个 >= x
        M = [-1] * (1 << m)

        for i in range(n):
            mask = 0
            for j in range(m):
                if A[i][j] >= x:
                    mask |= (1 << j)
            M[mask] = i

        full = (1 << m) - 1
        for m0 in range(1 << m):
            if M[m0] == -1:
                continue
            for m1 in range(1 << m):
                if M[m1] == -1:
                    continue
                if (m0 | m1) == full:
                    if best < x:
                        best = x
                        ans = [M[m0] + 1, M[m1] + 1]
                    return True
        return False

    # 二分答案
    possible(hi)
    possible(lo)

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if possible(mid):
            lo = mid
        else:
            hi = mid

    print(ans[0], ans[1])


if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)