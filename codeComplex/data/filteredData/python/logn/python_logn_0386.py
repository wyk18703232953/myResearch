def main(n):
    """
    将交互式程序改成可测试程序：
    - 不使用 input()
    - main(n) 内部生成测试数据并模拟交互
    - 返回找到的位置（或 -1），不打印
    """

    # ------------------ 测试数据生成与交互模拟部分 ------------------
    # 原题是交互式：对位置 i 询问得到某个值。这里我们构造一组数据 arr，
    # 并将 check(i) 改为访问 arr[i]，同时保留 memo 结构。

    # 约束：原程序在一开始要求：if n % 4 == 2: 输出 -1
    # 所以我们保持同样的策略：如果 n % 4 == 2，则直接返回 -1
    if n % 4 == 2:
        return -1

    # 生成测试数据：
    # 为了能运行原二分逻辑（要求 check(i) 与 check(i + n//2) 之间
    # 具有一定结构），这里给出一种简单构造：
    # 设有某个解 pos，使得 arr[pos] == arr[pos + n//2]。
    # 我们可以任意构造这样的数组。
    #
    # 为了保证 1 <= pos <= n//2，并且 pos + n//2 <= n
    # 取 pos = 1（也可以随机选取 [1, n//2] 范围内任意值）
    pos = 1

    # 构造 arr，长度 n+1，1-based
    arr = [0] * (n + 1)
    # 先填一些递增值
    for i in range(1, n + 1):
        arr[i] = i

    # 强制 arr[pos] == arr[pos + n//2]
    arr[pos + n // 2] = arr[pos]

    # ------------------ 以下为原逻辑（仅去除 input/print/flush） ------------------
    l = 1
    r = l + n // 2

    memo = [-1] * (n + 1)

    def check(i):
        if memo[i] == -1:
            # 原来通过交互得到值，现在直接访问 arr
            memo[i] = arr[i]
        return memo[i]

    while r >= l:
        a = check(l)
        b = check(l + n // 2)

        if a == b:
            return l

        mid = (l + r) >> 1

        c = check(mid)
        d = check(mid + n // 2)

        if c == d:
            return mid

        if (a < b and c < d) or (a > b and c > d):
            l = mid + 1

        else:
            r = mid

    # 理论上程序应在循环内部 return，不会走到这里
    return -1


# 简单自测
if __name__ == "__main__":
    # 随便测几个 n
    for n in [4, 6, 8, 12, 16]:
        ans = main(n)
        # print(f"n={n}, answer={ans}")
        pass