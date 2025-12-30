from math import gcd
from random import randint

M = mod = 10 ** 9 + 7


def main(n: int):
    """
    规模 n：
    - 生成长度为 n 的数组 l, c
    - l[i] ∈ [1, 10^9]
    - c[i] ∈ [1, 10^9]
    运行原逻辑并打印结果
    """

    # 生成测试数据：保证存在 gcd 为 1 的情况，避免总是 -1
    # 方案：先生成任意数组，然后强制把最后两个数设为互质
    l = [randint(1, 10 ** 9) for _ in range(n)]
    c = [randint(1, 10 ** 9) for _ in range(n)]

    if n >= 2:
        a = randint(2, 10 ** 6)
        b = a + 1  # a 与 a+1 一定互质
        l[-2] = a
        l[-1] = b
    elif n == 1:
        # 单个数时，只能强制为 1 才能有答案
        l[0] = 1

    # 下面是原逻辑
    element = l[0]
    for i in range(1, n):
        element = gcd(element, l[i])

    if element != 1:
        print(-1)
        return

    myset = {}
    for ind, val in enumerate(l):
        # 为防止迭代过程中修改 dict，使用当前键列表
        current_keys = list(myset.keys())
        for g in current_keys:
            temp = gcd(g, val)
            new_cost = myset[g] + c[ind]
            if temp not in myset:
                myset[temp] = new_cost
            else:
                myset[temp] = min(myset[temp], new_cost)

        if val not in myset:
            myset[val] = c[ind]
        else:
            myset[val] = min(myset[val], c[ind])

    print(myset[1])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)