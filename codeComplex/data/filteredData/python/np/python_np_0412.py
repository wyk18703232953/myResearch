from collections import defaultdict
import random

def check(mid, m, a):
    d = defaultdict(int)
    for idx, row in enumerate(a):
        string = ''.join('1' if val >= mid else '0' for val in row)
        d[int(string, 2)] = idx
    full = (1 << m) - 1
    keys = list(d.keys())
    for i in keys:
        for j in keys:
            if i | j == full:
                return [d[i], d[j]]
    return []


def binary_search(lo, hi, m, a):
    ans = []
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        x = check(mid, m, a)
        if x:
            lo = mid
            ans = [x[0] + 1, x[1] + 1]
        else:
            hi = mid - 1
    mid = lo + (hi - lo + 1) // 2
    x = check(mid, m, a)
    if x:
        ans = [x[0] + 1, x[1] + 1]
    return ans


def generate_test_data(n, m, value_lo=0, value_hi=10**9):
    # 生成 n 行 m 列的随机整数矩阵 a
    a = [
        [random.randint(value_lo, value_hi) for _ in range(m)]
        for _ in range(n)
    ]
    return a


def main(n):
    # 这里根据规模 n 自动设定 m（列数），也可根据需要修改策略
    # 示例：令 m 在 [1, min(10, n)] 范围内
    m = max(1, min(10, n))

    # 生成测试数据 a: n 行 m 列
    a = generate_test_data(n, m)

    # 执行原逻辑：在 [0, 10**9] 范围内二分
    result = binary_search(0, 10**9, m, a)

    # 输出结果
    print(*result)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(5)