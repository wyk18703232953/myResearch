def main(n):
    """
    n: 规模参数，控制测试数据数量以及 n 的大小
    生成 n 组测试 (n_i, k_i)，并输出对应结果
    """

    def solve_case(n_, k_):
        lev = 1
        b = False
        if n_ >= 60:
            all_moves = 0
            b = True

        else:
            all_moves = (4 ** n_ - 1) // 3

        cnt = 1
        step = 0
        prev_need = 0
        while True:
            need = 2 * cnt - 1
            if k_ >= need and step < n_:
                k_ -= need
                all_moves -= need
                cnt *= 2
                step += 1
                prev_need = need

            else:
                if b:
                    # print('YES', n_ - step)
                    pass
                    break
                if all_moves < k_:
                    # print('NO')
                    pass
                    break
                all_moves -= (4 ** (n_ - step)) // 3 * need
                if all_moves >= k_ or b:
                    # print('YES', n_ - step)
                    pass
                    break

                else:
                    # print('NO')
                    pass
                    break

    # 根据规模 n 生成测试数据：
    # 这里生成 n 组测试，每组的 n_i, k_i 如下：
    # n_i 从 1 到 n（上限 100, 以免 4**n 溢出），k_i 为与 n_i 相关的中等大小值
    T = n
    max_n_val = min(100, n if n > 0 else 1)

    for i in range(T):
        n_i = (i % max_n_val) + 1  # 在 1..max_n_val 之间循环
        # 生成一个和 (4**n_i - 1)//3 同量级的 k_i
        if n_i >= 30:
            # 对于较大 n_i，直接用一个较大的常数（不会真的用到 all_moves 的准确值）
            k_i = 10**9 + i

        else:
            total_moves = (4 ** n_i - 1) // 3
            # 取 0.25~0.75 区间内的某个值
            k_i = total_moves * (1 + (i % 3)) // 4

        solve_case(n_i, k_i)


if __name__ == "__main__":
    # 示范调用，规模可自行调整
    main(5)