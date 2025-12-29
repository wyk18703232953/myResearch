#!usr/bin/python

import random

def main(n):
    # 生成测试数据：
    # a 为长度 n 的随机数字串，首位不为 0
    # b 为长度在 [1, n] 的随机数字串，首位不为 0
    if n <= 0:
        return

    def gen_number(length):
        if length <= 0:
            return "0"
        first = str(random.randint(1, 9))
        rest = "".join(str(random.randint(0, 9)) for _ in range(length - 1))
        return first + rest

    a_len = n
    b_len = random.randint(1, n)
    a = gen_number(a_len)
    b = gen_number(b_len)

    # 原逻辑开始
    length_of_a = len(a)
    length_of_b = len(b)
    found_digit = False
    chk_finnish = False
    appended_digit_count = 0
    n_count = {}
    num = []
    for i in range(0, 10):
        n_count[i] = 0

    for i in range(0, length_of_a):
        c = int(a[i])
        n_count[c] += 1

    if length_of_a < length_of_b:
        num = sorted(a, reverse=True)
        for i in range(0, length_of_a):
            print(num[i], end="")
    else:
        for i in range(0, length_of_b):
            digit = int(b[i])
            if n_count[digit] > 0:
                num.append(digit)
                n_count[digit] -= 1
                appended_digit_count += 1
            else:
                j = digit - 1
                while j > -1:
                    if n_count[j] > 0:
                        num.append(j)
                        appended_digit_count += 1
                        n_count[j] -= 1
                        found_digit = True
                        chk_finnish = True
                        break
                    j -= 1

                if found_digit:
                    j = 9
                    while j > -1:
                        if n_count[j] > 0:
                            digit_count = n_count[j]
                            for k in range(0, digit_count):
                                num.append(j)
                                n_count[j] -= 1
                                appended_digit_count += 1
                        j -= 1
                    if chk_finnish:
                        break
                else:
                    found_digit = False
                    while found_digit is False:
                        pop_up = num[appended_digit_count - 1]
                        del num[-1]
                        j = pop_up - 1
                        n_count[pop_up] += 1
                        appended_digit_count -= 1
                        while j > -1:
                            if n_count[j] > 0:
                                num.append(j)
                                appended_digit_count += 1
                                n_count[j] -= 1
                                found_digit = True
                                break
                            j -= 1
                    j = 9
                    while j > -1:
                        if n_count[j] > 0:
                            digit_count = n_count[j]
                            for k in range(0, digit_count):
                                num.append(j)
                                appended_digit_count += 1
                        j -= 1
                    break

        for i in range(0, length_of_b):
            print(num[i], end="")

if __name__ == "__main__":
    # 可以在此处修改 n 来进行测试
    main(10)