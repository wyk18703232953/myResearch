def main(n):
    # 映射规则：
    # 将原程序中的 n, k 映射为：
    #   n_input = n
    #   k = max(1, n)  （保证规模随 n 增长，且 k >= 1）
    n_input = n
    k = max(1, n)

    ub = k * (k + 1) // 2 - k + 1

    if n_input > ub:
        # print(-1)
        pass
    elif n_input == ub:
        # print(k - 1)
        pass
    elif n_input == 1:
        # print(0)
        pass
    elif n_input <= k:
        # print(1)
        pass

    else:
        st = 1
        en = k - 1
        target = n_input - 1
        ub = k * (k - 1) // 2
        p = lambda x: ub - x * (x - 1) // 2
        ans = -1

        while st <= en:
            md = (st + en) // 2
            if p(md) <= target:
                ans = md
                en = md - 1

            else:
                st = md + 1

        if p(ans) == target:
            # print(k - ans)
            pass

        else:
            # print(k - ans + 1)
            pass
if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次调用
    main(10)