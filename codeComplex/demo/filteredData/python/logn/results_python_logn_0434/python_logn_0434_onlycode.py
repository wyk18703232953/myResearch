#!/usr/bin/python
# encoding:UTF-8
# Filename:Base.py

import sys
import random

from itertools import permutations, combinations
from math import sqrt, fabs, ceil
from collections import namedtuple

# ------Util Const--------

in_file_path = "input.txt"
output_file_path = "output.txt"

SUBMIT = True


def read_num(fin, num_type=int):
    tmp_list = [num_type(x) for x in fin.readline().strip().split()]
    if len(tmp_list) == 1:
        return tmp_list[0]
    else:
        return tuple(tmp_list)


# A
# def solve(fin, fout):
#     n, k = read_num(fin)
#     print(ceil((n * 8.0) / k) + ceil((n * 2.0) / k) + ceil((n * 5.0) / k))

# B
# def solve(fin):
#     n = read_num(fin)
#     for _ in range(0, n):
#         l, r = read_num(fin)
#         if (r - l + 1) % 2 == 0:
#             if l % 2 == 0:
#                 print(int(-(r - l + 1) / 2))
#             else:
#                 print(int((r - l + 1) / 2))
#         else:
#             if l % 2 == 0:
#                 print(int(-(r - l) / 2 + r))
#             else:
#                 print(int((r - l) / 2 - r))

# C
# def solve(fin):
#     def count_color(x, y, xx, yy):
#         # return _w(x, y, xx, yy), _b(x, y, xx, yy)
#         if x > xx or y > yy:
#             return 0, 0
#         t = (xx - x + 1) * (yy - y + 1)
#         if t % 2 == 0:
#             return t // 2, t // 2
#         else:
#             if (x + y) % 2 == 0:
#                 return t - t // 2, t // 2
#             else:
#                 return t // 2, t - t // 2
#
#     T = read_num(fin)
#     for _ in range(0, T):
#         # print('Test: ',T)
#         n, m = read_num(fin)
#         x1, y1, x2, y2 = read_num(fin)
#         x3, y3, x4, y4 = read_num(fin)
#         w, _ = count_color(1, 1, n, m)
#         if (max(x1, x3) > min(x2, x4)) or (max(y1, y3) > min(y2, y4)):
#             tmp_w, tmp_b = count_color(x1, y1, x2, y2)
#             w += tmp_b
#             tmp_w, tmp_b = count_color(x3, y3, x4, y4)
#             w -= tmp_w
#         else:
#             tmp_w, tmp_b = count_color(x1, y1, x2, y2)
#             w += tmp_b
#             tmp_w, tmp_b = count_color(x3, y3, x4, y4)
#             w -= tmp_w
#             tmp_x_list = sorted([x1, x2, x3, x4])
#             tmp_y_list = sorted([y1, y2, y3, y4])
#             x5, x6 = tmp_x_list[1], tmp_x_list[2]
#             y5, y6 = tmp_y_list[1], tmp_y_list[2]
#             tmp_w, tmp_b = count_color(x5, y5, x6, y6)
#             w -= tmp_b
#         print(w, n * m - w)

def solve(fin):
    T = read_num(fin)
    for _ in range(0, T):
        n, k = read_num(fin)
        if n > 34 or k == 1:
            print('YES', n - 1)
        else:
            f = [0]
            for _ in range(0, n):
                f.append(f[-1] * 4 + 1)
            min_step = 1
            max_step = 1 + f[n - 1]
            # print(f)
            # print(f[n - 1])
            out_range = 3
            flag = True
            for i in range(0, n):
                # print(min_step, max_step)
                if min_step <= k <= max_step:
                    print('YES', n - i - 1)
                    flag = False
                    break
                max_step += out_range
                min_step += out_range
                out_range = out_range * 2 + 1
                if n - 2 - i >= 0:
                    # print(out_range - 2, f[n - 2 - i])
                    max_step += (out_range - 2) * f[n - 2 - i]

            if flag:
                print('NO')


if __name__ == '__main__':
    if SUBMIT:
        solve(sys.stdin)
    else:
        solve(open(in_file_path, 'r'))
