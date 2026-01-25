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
    # 将 n 解释为数组长度，k 为一个与 n 相关的确定性窗口大小
    # p 为长度为 n 的整数数组，每个元素在 [0, 255] 范围内
    if n <= 0:
        return
    k = max(1, min(256, n // 2 if n > 1 else 1))
    p = [i % 256 for i in range(n)]
    solve(n, k, p)


if __name__ == "__main__":
    # 示例调用：使用 n = 10 作为输入规模
    main(10)