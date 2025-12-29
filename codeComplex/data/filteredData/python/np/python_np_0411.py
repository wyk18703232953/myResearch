from collections import defaultdict
import random


def check(mid, m, a):
    d = defaultdict(int)
    for idx, row in enumerate(a):
        bits = []
        for val in row:
            bits.append('1' if val >= mid else '0')
        bit_str = ''.join(bits)
        d[int(bit_str, 2)] = idx

    full_mask = (1 << m) - 1
    keys = list(d.keys())
    for i in keys:
        for j in keys:
            if i | j == full_mask:
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
    return ans


def main(n):
    # 生成参数：m 为特征数，这里简单设为 5（可按需修改或随机）
    m = 5

    # 生成测试数据 a：n 行 m 列的随机整数矩阵
    # 数值范围与原代码的二分范围兼容 [0, 10**9]
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    # 执行原逻辑
    result = binary_search(-1, 10**9 + 1, m, a)

    # 输出结果（两个下标）
    print(*result)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此处调整
    main(4)