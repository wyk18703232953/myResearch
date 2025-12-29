import math
import random


def binary_search(good, left, right, delta=1, right_true=False):
    limits = [left, right]
    while limits[1] - limits[0] > delta:
        mid = (limits[0] + limits[1]) / 2 if delta != 1 else (limits[0] + limits[1]) // 2
        if good(mid):
            limits[int(right_true)] = mid
        else:
            limits[int(~right_true)] = mid
    if good(limits[int(right_true)]):
        return limits[int(right_true)]
    else:
        return False


def solve_a(n, m, a, b):
    def good(k):
        for i in range(n):
            k -= (m + k) / a[i]
            k -= (m + k) / b[i]
        return k >= 0

    ans = binary_search(good, 0.0, 10 ** 9 + 1.0, delta=10 ** (-6), right_true=True)
    if not ans:
        return -1
    else:
        return ans


def main(n):
    # 生成规模为 n 的测试数据
    # n：数组长度
    # m：在一个合理范围内随机
    # a, b：每个元素至少为 1，避免除零
    random.seed(0)
    m = random.randint(1, 10 ** 6)
    a = [random.randint(1, 10 ** 6) for _ in range(n)]
    b = [random.randint(1, 10 ** 6) for _ in range(n)]

    ans = solve_a(n, m, a, b)
    print(ans)


# 示例：手动调用
# main(5)