import random

def main(n):
    # 根据 n 生成测试数据
    # 约定：m = min(8, n) 保证 4^m 可计算（原算法复杂度 O((nm+4^m)logA)）
    # 元素值范围 [0, 1e9]
    if n <= 0:
        return

    m = min(8, n)
    max_val = int(1e9)
    random.seed(0)

    # 生成 n 行 m 列的数组，每个元素是 [0, max_val] 的整数
    arr = tuple(
        tuple(random.randint(0, max_val) for _ in range(m))
        for _ in range(n)
    )

    lower_bound = 0
    upper_bound = max_val + 1
    mask = (1 << m) - 1
    ans = (0, 0)

    def can_upper(mid):
        nonlocal ans
        # 构造每一行在阈值 mid 下的 bitmask
        d = dict()
        for i in range(n):
            bit = 0
            for j in range(m):
                if arr[i][j] >= mid:
                    bit |= 1 << j
            d[bit] = i

        keys = tuple(d.keys())
        for i in range(len(keys)):
            a1 = keys[i]
            for j in range(i, len(keys)):
                a2 = keys[j]
                if (a1 | a2) == mask:
                    ans = (d[a1], d[a2])
                    return True
        return False

    # 二分答案
    while upper_bound - lower_bound > 1:
        middle = (upper_bound + lower_bound) >> 1
        if can_upper(middle):
            lower_bound = middle
        else:
            upper_bound = middle

    # 输出答案（1-based）
    print(ans[0] + 1, ans[1] + 1)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)