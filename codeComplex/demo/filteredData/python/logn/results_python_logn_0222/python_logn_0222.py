def main(n):
    # 确定性生成原程序中的 n 和 s
    # 原程序输入结构：两个整数 n, s
    # 这里将 n 视为“输入规模”，并构造 s < n 的情况以保持程序逻辑有效
    N = max(1, n)
    S = N // 2  # 保证 S < N，当 N > 1 时

    n_val, s = N, S

    if s >= n_val:
        # print(0)
        pass

    else:
        ans = 0

        def sod(x):
            s_str = str(x)
            ret = 0
            for ch in s_str:
                ret += int(ch)
            return ret

        for nd in range(s, s + 1000):
            if nd - sod(nd) >= s:
                ans += 1
            if nd == n_val:
                break
            if nd == (s + 369):
                ans += (n_val - nd)
                break
        # print(ans)
        pass
if __name__ == "__main__":
    main(100000)