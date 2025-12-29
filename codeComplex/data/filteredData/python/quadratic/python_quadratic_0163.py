import random

def solve(n, k, p):
    group = 256 * [None]
    r = p[:]
    for i, pi in enumerate(p):
        if group[pi] is not None:
            r[i] = group[pi][0]
        else:
            lo = pi
            while lo >= 0 and pi - lo < k and group[lo] is None:
                lo -= 1
            if lo < 0 or pi - lo == k:
                lo += 1
                hi = pi + 1
            else:  # group[lo] is not None
                if pi - group[lo][0] < k:
                    lo = group[lo][0]
                    hi = pi + 1
                else:
                    lo += 1
                    hi = pi + 1
            lohi = (lo, hi)
            for j in range(lo, hi):
                group[j] = lohi
            r[i] = group[pi][0]
    print(" ".join(map(str, r)))


def main(n):
    # 根据 n 生成测试数据
    # 约束：p[i] 需要在 [0, 255] 区间内，否则原算法中的 group 数组会越界
    k = random.randint(1, 256)     # 生成 1~256 的随机 k
    p = [random.randint(0, 255) for _ in range(n)]
    solve(n, k, p)


if __name__ == "__main__":
    # 示例：调用 main(10) 生成规模为 10 的测试数据并运行
    main(10)