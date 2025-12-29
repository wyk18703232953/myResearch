import random

INF = 10 ** 18
got = [INF] * 100005
hidden = []  # 用于模拟交互的隐藏数组（1-based）


def getnum(i: int) -> int:
    # 原交互函数的模拟：从 hidden 中读取值，并缓存
    if got[i] == INF:
        got[i] = hidden[i]
    return got[i]


def main(n: int):
    """
    n 为规模。这里我们自己生成一组测试数据 hidden[1..n]，并在其上运行原逻辑。

    原题为交互式：给定隐藏数组 a[1..n]，要求找一个 i，使得
        a[i] == a[i + n/2]  (n 为偶数，且最后答案存在时 n % 4 != 2)
    这里我们按照这种结构生成数据，以保证逻辑可运行。
    """
    global hidden, got
    got = [INF] * (n + 5)

    # 生成测试数据：
    # - 若 n % 2 == 1 无法构造一对 (i, i+n/2)，简单生成随机数组。
    # - 若 n % 2 == 0，则先随机生成前 n//2 个，再复制到后 n//2 个，使得对所有 i:
    #     hidden[i] == hidden[i + n//2]
    #   从而理论上任何 i 都是答案。
    hidden = [0] * (n + 1)  # 1-based

    if n % 2 == 1:
        # 奇数长度：简单生成随机测试
        for i in range(1, n + 1):
            hidden[i] = random.randint(0, 100)
    else:
        half = n // 2
        for i in range(1, half + 1):
            v = random.randint(0, 100)
            hidden[i] = v
            hidden[i + half] = v

    # 以下为原逻辑（去掉 input / print("?") 部分，只保留算法结构）
    if n % 4 == 2:
        # 原代码输出 "! -1"
        # 在这里我们返回 -1 表示无解
        return -1

    lo = 1
    hi = n // 2 + 1
    t1 = getnum(lo)
    t2 = getnum(hi)
    lo2 = t1 - t2  # a[1] - a[1 + n/2]
    hi2 = t2 - t1  # a[1 + n/2] - a[1]，其实是 -lo2

    if lo2 == 0:
        # 原代码输出 "! 1"
        return 1
    else:
        # 二分搜索 i in [1, n/2] 使得 getnum(i) == getnum(i + n/2)
        while lo < hi:
            mid = (lo + hi) // 2
            mid2 = getnum(mid) - getnum(mid + n // 2)
            if mid2 == 0:
                return mid
            # 与 lo2 同号则向右，否则向左
            if (lo2 > 0) == (mid2 > 0):
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


# 示例：自行调用 main(n)
# if __name__ == "__main__":
#     ans = main(8)
#     print("answer index:", ans)