import math
import random

def main(n):
    # 1. 生成测试数据 M 和序列 a
    # 约定：生成一个严格递增的序列 a[1..n]，并生成 M > a[n]
    # 为了简单，生成差分在 [1, 10] 的递增序列
    diffs = [random.randint(1, 10) for _ in range(n + 1)]  # n+1 段：a[1..n] 和 M
    a = [0]
    cur = 0
    for d in diffs[:-1]:
        cur += d
        a.append(cur)
    M = cur + diffs[-1]  # 最后一个差值用于生成 M
    a.append(M)

    # 2. 逻辑与原程序一致
    t1 = []
    t2 = []
    for i in range(n + 1):
        if i % 2 == 0:
            t1.append(a[i + 1] - a[i])
        else:
            t2.append(a[i + 1] - a[i])
    t2.append(0)

    ans = sum(t1)
    p = 0
    q = sum(t2)
    for i in range(math.ceil(n / 2)):
        p = p + t1[i]
        q = q - t2[i - 1]
        ans = max(ans, p + q - 1)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)