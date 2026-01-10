def main(n):
    # 映射含义：
    # n -> n (长度 b)，m = n (长度 g)，保证规模一致，便于复杂度分析
    if n < 2:
        # 至少需要两个元素以满足原逻辑中 b[-2] 的访问
        n = 2
    m = n

    # 构造确定性数据：
    # b: 递增序列，含负数和正数，覆盖多种情况
    # g: 递增序列，相对 b 做平移，保证可触达三种分支
    b = [i - (n // 2) for i in range(n)]
    if n % 3 == 0:
        # 使 min(g) < max(b) 分支触发
        g = [i - (n // 2) - 1 for i in range(m)]
    elif n % 3 == 1:
        # 使 min(g) == max(b) 分支触发
        g = [b[-1] + i for i in range(m)]
    else:
        # 使 min(g) > max(b) 分支触发
        g = [b[-1] + 1 + i for i in range(m)]

    Sum = 0
    for j in range(n):
        Sum += b[j] * m
    b.sort()
    for i in range(m):
        Sum += max(0, g[i] - b[-1])
    if min(g) < max(b):
        print(-1)
    elif min(g) == max(b):
        print(Sum)
    else:
        Sum += b[-1] - b[-2]
        print(Sum)


if __name__ == "__main__":
    main(10)