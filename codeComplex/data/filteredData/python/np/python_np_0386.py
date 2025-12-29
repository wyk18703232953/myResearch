import random
from collections import defaultdict

M = 998244353
EPS = 1e-6
ALPHA = 'abcdefghijklmnopqrstuvwxyz'


def ok(here, n, m, a):
    have = defaultdict(lambda: -1)
    for j in range(n):
        b = a[j]
        s = ''
        for x in b:
            if x >= here:
                s += '1'
            else:
                s += '0'
        have[int(s, 2)] = j

    full = (1 << m) - 1
    # 原代码写死 300，这里改为 1<<m 更合理，也兼容大 m
    upper = 1 << m
    for i in range(upper):
        if have[i] == -1:
            continue
        for j in range(upper):
            if (i | j) == full and have[j] != -1:
                return (have[i] + 1, have[j] + 1)

    return -1


def main(n):
    """
    n: 规模参数，用作行数。
       自动生成测试数据：
       - m = min(8, max(1, n.bit_length())) 适中维度
       - a 为 n x m 的整数矩阵，每个元素在 [0, 10^9] 内
    """

    # 根据 n 生成测试数据
    # 这里选择一个与 n 相关的 m，避免 2^m 过大
    if n <= 0:
        return

    m = min(8, max(1, n.bit_length()))
    max_val = 10 ** 9

    random.seed(0)
    a = [[random.randint(0, max_val) for _ in range(m)] for _ in range(n)]

    low = 0
    high = max_val
    ans = (-1, -1)

    while low <= high:
        mid = low + (high - low) // 2
        here = ok(mid, n, m, a)
        if here != -1:
            ans = here
            low = mid + 1
        else:
            high = mid - 1

    print(*ans)


if __name__ == "__main__":
    # 示例：用 n=10 运行
    main(10)