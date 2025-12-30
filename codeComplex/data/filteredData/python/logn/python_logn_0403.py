def main(n):
    import math
    import random

    # 1. 根据规模 n 生成测试数据
    # 为了让规模 n 有意义，这里用它作为 N 的大小上界
    # 并随机生成 M, K, L，保证 1 <= M <= N，且有一定概率存在解
    if n <= 1:
        n = 2

    N = n
    M = random.randint(1, N)       # 1 <= M <= N
    K = random.randint(0, N)       # 0 <= K <= N
    L = random.randint(0, N)       # 0 <= L <= N

    # 2. 原逻辑处理（注意：原代码使用的是浮点二分）
    # 若 M * (N / M) - K < L 则无解
    if M * (N / M) - K < L:
        print(-1)
        return

    def solve(curr):
        return curr * M - K >= L

    l = 0.0
    r = N / M
    # 若要模拟原代码的 while r - l > 1，需要注意这是浮点比较
    while r - l > 1:
        mid = (r + l) / 2
        if solve(mid):
            r = mid
        else:
            l = mid

    print(r)


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)