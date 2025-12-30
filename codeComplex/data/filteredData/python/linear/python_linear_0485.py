import random

def main(n):
    # 生成测试数据：n 个区间 [l, r]
    # 这里生成的区间左端点 l 在 [0, 10^6) 内，
    # 区间长度在 [0, 10^6) 内，即 r = l + len
    intervals = []
    for _ in range(n):
        l = random.randint(0, 10**6)
        length = random.randint(0, 10**6)
        r = l + length
        intervals.append((l, r))

    # 以下为原逻辑的无 input() 版本
    l1 = l2 = -1
    r1 = r2 = 1 << 30
    il = ir = -1  # 分别记录最大全左端点和最小右端点所在区间的下标

    for i, (l, r) in enumerate(intervals):
        if l > l1:
            il, l1, l2 = i, l, l1
        elif l > l2:
            l2 = l

        if r < r1:
            ir, r1, r2 = i, r, r1
        elif r < r2:
            r2 = r

    if il != ir:
        ans = max(0, max(r2 - l2, r1 - l2, r2 - l1))
    else:
        ans = max(0, r2 - l2)

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)