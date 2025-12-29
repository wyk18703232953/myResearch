def solve_once(n_raw, k_raw):
    n = n_raw - 1
    k = k_raw - 1
    if n == 0:
        return 0

    def main_core(n, k):
        s = k * (k + 1) // 2
        if s < n:
            return -1
        l = 1
        r = k
        while l <= r:
            mid = (l + r) // 2
            curr = s - (mid * (mid - 1)) // 2
            if curr == n:
                return k - mid + 1
            elif curr < n:
                r = mid - 1
            else:
                l = mid + 1
        return k - l + 2

    return main_core(n, k)


def main(n):
    """
    按规模 n 生成测试数据并运行。
    这里假设：
      - k_raw 取为 n（可根据需要调整测试数据生成策略）
      - n_raw 取为 n
    可根据题目实际限制，调整生成策略。
    """
    n_raw = n
    k_raw = n
    ans = solve_once(n_raw, k_raw)
    print(ans)


if __name__ == "__main__":
    # 示例：对若干规模进行测试
    for n in [1, 2, 5, 10, 20]:
        main(n)