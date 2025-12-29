#!/usr/bin/python
# encoding:UTF-8

import random

from math import ceil


def read_num_from_list(data, idx, num_type=int):
    tmp_list = [num_type(x) for x in data[idx].strip().split()]
    if len(tmp_list) == 1:
        return tmp_list[0], idx + 1
    else:
        return tuple(tmp_list), idx + 1


def solve(fin_lines):
    out_lines = []
    idx = 0
    T, idx = read_num_from_list(fin_lines, idx)
    for _ in range(T):
        (n, k), idx = read_num_from_list(fin_lines, idx)
        if n > 34 or k == 1:
            out_lines.append(f"YES {n - 1}")
        else:
            f = [0]
            for _ in range(n):
                f.append(f[-1] * 4 + 1)
            min_step = 1
            max_step = 1 + f[n - 1]
            out_range = 3
            flag = True
            for i in range(0, n):
                if min_step <= k <= max_step:
                    out_lines.append(f"YES {n - i - 1}")
                    flag = False
                    break
                max_step += out_range
                min_step += out_range
                out_range = out_range * 2 + 1
                if n - 2 - i >= 0:
                    max_step += (out_range - 2) * f[n - 2 - i]

            if flag:
                out_lines.append("NO")
    return out_lines


def main(n):
    """
    n: 规模，用来控制测试数据规模
       这里令 T = n，且对每个测试用例随机生成 (n_i, k_i)
    """
    random.seed(0)

    T = n
    lines = [str(T)]
    for _ in range(T):
        # 生成 n_i 在 [1, 50]，保证覆盖 n > 34 和 n <= 34 两种情况
        ni = random.randint(1, 50)
        # 生成 k_i 在 [1, 10^9]
        ki = random.randint(1, 10**9)
        lines.append(f"{ni} {ki}")

    results = solve(lines)
    for line in results:
        print(line)


if __name__ == '__main__':
    # 示例：规模 5
    main(5)