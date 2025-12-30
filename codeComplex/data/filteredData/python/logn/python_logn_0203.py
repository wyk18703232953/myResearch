def main(n):
    """
    根据规模 n 生成测试数据，并计算满足条件的数量。
    原逻辑：给定 n, s，统计 [1..n] 中满足 x - sum_digits(x) > s 的 x 的个数。
    这里根据 n 自动生成 s（例如取 s = n // 2，且保证 s % 9 != 0）。
    返回结果 ans。
    """

    # ---------- 生成测试数据 ----------
    # 示例策略：s 与 n 同量级，且保证 s % 9 != 0（原代码中若 s % 9 == 0 会做特殊处理）
    s = max(0, n // 2)
    if s % 9 == 0:
        s += 1

    # ---------- 原逻辑函数定义 ----------
    def ok(m):
        s0 = m
        for ch in str(m):
            s0 -= int(ch)
        # 原代码为 True if s0 > s else False
        return s0 > s

    def check(m):
        # 在 m 附近做一次精细检查，返回最终答案
        for i in range(max(0, m - 5), m + 6):
            if ok(i):
                return max(0, n - i + 1)
        return 0

    def binary_search(c1, c2):
        # 在 [c1, c2) 上找第一个 ok 的位置附近，随后调用 check
        m = (c1 + c2 + 1) // 2
        while abs(c1 - c2) > 1:
            m = (c1 + c2 + 1) // 2
            if ok(m):
                c2 = m
            else:
                c1 = m
        ans_inner = check(m)
        return ans_inner

    # ---------- 调整 s（保留原始行为） ----------
    if not s % 9:
        s -= 1

    # ---------- 调用并返回结果 ----------
    ans = binary_search(0, n + 1)
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：调用 main(10**6) 等
    main(10**6)