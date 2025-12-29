import math
import bisect
import random

def main(n):
    # 生成测试数据：
    # 1) 生成一个递增数组 A，长度为 n
    # 2) 生成一个非负整数 U
    #
    # 为了与原算法逻辑匹配，A 需为非降序列，使用随机递增方式构造
    if n < 3:
        print(-1)
        return

    # 构造递增数组 A
    A = []
    cur = 0
    for _ in range(n):
        cur += random.randint(0, 5)  # 每步增加 0~5，保持非降
        A.append(cur)

    # 构造 U，范围设置为数组大致跨度
    total_span = A[-1] - A[0]
    if total_span <= 0:
        U = 0
    else:
        U = random.randint(0, total_span)

    # 原始逻辑开始
    Ans = -1
    for i in range(n - 2):
        x = A[i]
        y_val = x + U
        z = bisect.bisect_left(A, y_val, lo=i + 2, hi=n)

        if z == n:
            z -= 1

        if A[z] <= x + U:
            a = A[z]
        elif z - 1 >= i + 1 and A[z - 1] <= x + U:
            a = A[z - 1]
        else:
            continue

        if a == A[i]:  # 防止除零
            continue

        b = (a - A[i + 1]) / (a - A[i])
        Ans = max(Ans, b)

    print(Ans)


if __name__ == "__main__":
    # 示例：调用 main，规模自定
    main(10)