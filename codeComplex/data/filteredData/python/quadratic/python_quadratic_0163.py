def solve(n, k, p):
    group = [None] * 256
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

            else:
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
    # print(" ".join(map(str, r)))
    pass


def main(n):
    # 输入规模含义：
    # n 为数组 p 的长度，k 固定设为 10（可按需调整）
    k = 10
    # 生成确定性的测试数据，p 中元素范围在 [0, 255] 内
    # 使用简单算术构造，确保可控且可规模化
    p = [(i * 37 + 13) % 256 for i in range(n)]
    solve(n, k, p)


if __name__ == "__main__":
    # 示例：使用 n = 100 作为测试规模
    main(100)