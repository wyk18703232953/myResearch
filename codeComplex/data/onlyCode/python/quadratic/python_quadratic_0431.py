# https://codeforces.com/problemset/problem/1030/C

import sys

lines = sys.stdin.readlines()


def read_a_num(line):
    n = int(line.strip())
    return n


def read_a_str(line):
    line = line.strip()
    return line


def check_ticket(digits):
    for target in range(900):
        seg_i = 0
        seg_sum = 0
        next_flag = False
        for d in digits:
            int_d = int(d)
            if int_d > target:
                next_flag = True
                break
            elif seg_sum + int_d > target:
                if next_flag:
                    break
                next_flag = True
                continue
            elif int_d == target or seg_sum + int_d == target:
                seg_i += 1
                seg_sum = 0
            else:
                seg_sum += int_d

        if next_flag:
            continue

        if seg_i >= 2 and seg_sum == 0:
            return True

    return False


digits = read_a_str(lines[1])
if check_ticket(digits):
    print("yes")
else:
    print("no")
