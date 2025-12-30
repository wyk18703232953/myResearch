from functools import lru_cache
import random

P = 10**9 + 7

def main(n):
    # 1. 生成测试数据
    # 为了保证与原程序 for i in range(15) 的兼容性，n 不应超过 15
    # 这里不强制限制，但当 n > 15 时，calc 中只会考虑前 15 个任务
    N = n

    # 随机生成总时间 T 和 N 个 (t, g)
    # t: 1..10, g: 0..2 的小整数“组别”
    T = random.randint(1, 10 * N)
    X = []
    for _ in range(N):
        t = random.randint(1, 10)
        g = random.randint(0, 2)
        X.append((t, g))

    @lru_cache(maxsize=None)
    def calc(x, pr, t):
        if t < 0:
            return 0
        if t == 0:
            return 1
        if x == 0:
            return 0

        ans = 0
        # 原代码固定遍历 0..14，这里改为遍历 0..N-1
        for i in range(N):
            if x & (1 << i):
                if X[i][1] != pr:
                    y = x ^ (1 << i)
                    ans = (ans + calc(y, X[i][1], t - X[i][0])) % P
        return ans

    # 计算并输出结果
    result = calc((1 << N) - 1, -1, T)
    print(result)


if __name__ == "__main__":
    # 示例：以 n = 5 运行
    main(5)