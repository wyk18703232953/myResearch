def main(n):
    # n is used as the number of test cases T
    # For each test case i (1-based), we deterministically generate:
    #   n_i = 1 + (i % 50)        -> keeps n_i within a small range including boundary 34
    #   k_i = 1 + (i * 3)         -> grows linearly with i
    # This preserves variety while being fully deterministic and scalable with n.
    def solve_generated(T):
        for i in range(1, T + 1):
            n_i = 1 + (i % 50)
            k_i = 1 + i * 3

            n_val, k_val = n_i, k_i
            if n_val > 34 or k_val == 1:
                # print('YES', n_val - 1)
                pass

            else:
                f = [0]
                for _ in range(0, n_val):
                    f.append(f[-1] * 4 + 1)
                min_step = 1
                max_step = 1 + f[n_val - 1]
                out_range = 3
                flag = True
                for j in range(0, n_val):
                    if min_step <= k_val <= max_step:
                        # print('YES', n_val - j - 1)
                        pass
                        flag = False
                        break
                    max_step += out_range
                    min_step += out_range
                    out_range = out_range * 2 + 1
                    if n_val - 2 - j >= 0:
                        max_step += (out_range - 2) * f[n_val - 2 - j]

                if flag:
                    # print('NO')
                    pass

    solve_generated(n)


if __name__ == "__main__":
    main(10)