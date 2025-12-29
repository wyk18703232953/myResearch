import random

from collections import Counter, defaultdict, deque

DEBUG = False


def bisect_f(f, lo, hi):
    if DEBUG:
        assert f(lo) and not f(hi)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if f(mid):
            lo = mid
        else:
            hi = mid
        if DEBUG:
            assert f(lo) and not f(hi)
    if DEBUG:
        assert hi - lo == 1
        assert f(lo) and not f(hi)
    return lo


def solve(N, M, arrs):
    def isPossible(target):
        possible = set()
        for arr in arrs:
            mask = 0
            for pos, x in enumerate(arr):
                if x >= target:
                    mask += 1 << pos
            possible.add(mask)
        allMask = (1 << M) - 1
        for mask1 in possible:
            for mask2 in possible:
                if mask1 | mask2 == allMask:
                    return (mask1 << 8) + mask2
        return 0

    lo = min(arrs[0])
    hi = 10 ** 9 + 1
    index = bisect_f(isPossible, lo, hi)

    mask1, mask2 = divmod(isPossible(index), 1 << 8)
    ans = [-1, -1]
    for i, arr in enumerate(arrs):
        mask = 0
        for pos, x in enumerate(arr):
            if x >= index:
                mask += 1 << pos
        if mask == mask1:
            ans[0] = str(i + 1)
        if mask == mask2:
            ans[1] = str(i + 1)
    return " ".join(ans)


def main(n):
    # 生成规模为 n 的测试数据：
    # 假定 N = n，M 为一个不大于 8 的值（原代码用到 1 << 8 存 mask）
    N = n
    M = min(8, max(1, n if n <= 8 else 5))  # 简单设定 M，避免过大

    # 生成 arrs：每个元素是 [1, 1e9] 之间的随机整数
    rng = random.Random(0)
    arrs = [[rng.randint(1, 10 ** 9) for _ in range(M)] for _ in range(N)]

    ans = solve(N, M, arrs)
    print(ans)


if __name__ == "__main__":
    # 示例：用 n = 5 运行
    main(5)