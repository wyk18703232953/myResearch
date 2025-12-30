import random

mod = 10**9 + 7
INF = float('inf')


def main(n):
    # 生成测试数据：长度为 n 的数组，元素为 0~10^9 的随机整数
    a = [random.randint(0, 10**9) for _ in range(n)]

    # 初始逆序对奇偶性
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                res = 1 - res

    # 生成若干随机区间查询，数量可随 n 调整
    q = max(1, n // 2)
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        m = r - l + 1
        swap = m * (m - 1) // 2
        if swap % 2:
            res = 1 - res
        print('odd' if res else 'even')