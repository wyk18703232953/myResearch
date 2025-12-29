# -*- coding: utf-8 -*-
"""
改写说明：
- 去掉了 input()
- 将逻辑封装为 main(n)
- 根据 n 生成测试数据：随机生成两个长度为 n 的数字串 a_str、b_str
- 返回结果字符串 sol 以及测试数据 (a_str, b_str)
"""

import random

def comp(a, b):
    x = len(a)
    s1 = ''
    s2 = ''
    for i in range(x):
        s1 += str(a[i])
        s2 += str(b[i])
    if s1 > s2:
        return 1
    else:
        return 0

def main(n):
    # 生成测试数据：两个长度为 n 的数字串
    # 每位是 0~9 的随机数字，保持与原程序的行为一致（接受任意数字串）
    a_str = ''.join(str(random.randint(0, 9)) for _ in range(n))
    b_str = ''.join(str(random.randint(0, 9)) for _ in range(n))

    a = list(a_str)
    b = list(b_str)

    cnt = [0] * 10
    n_len = len(a)
    m_len = len(b)
    sol = ''

    for i in range(n_len):
        a[i] = int(a[i])
        cnt[a[i]] += 1

    if n_len != m_len:
        a.sort(reverse=True)
        for i in a:
            sol += str(i)
    else:
        a.sort()

        for i in range(n_len):
            b[i] = int(b[i])
        for i in range(n_len - 1):
            for j in range(i, n_len):
                if a[i] < a[j]:
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
                    if comp(a, b):
                        temp = a[i]
                        a[i] = a[j]
                        a[j] = temp

        for i in a:
            sol += str(i)

    # 返回结果和测试数据，调用者可自行 print
    return sol, a_str, b_str


# 示例：仅当直接运行该文件时执行测试
if __name__ == "__main__":
    n = 5
    result, a_test, b_test = main(n)
    print("a =", a_test)
    print("b =", b_test)
    print("sol =", result)