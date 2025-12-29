#!/usr/bin/env python3
import random

def win1(n, k, a, l, r):
    if n == k or r[k + 1] == n or l[n - k] == 1:
        return True
    for i in range(2, n - k + 1):
        if l[i - 1] == 1 and r[i + k] == n and a[i - 1] == a[i + k]:
            return True
    return False

def win2(n, k, a, l, r):
    if 2 * k < n:
        return False
    for i in range(2, n - k + 1):
        if l[i - 1] != 1 or r[i + k] != n:
            return False
    return True

def main(n):
    # 生成规模为 n 的测试数据
    # k 在 [1, n] 范围内随机选取
    k = random.randint(1, n)
    # a 为 1~9 的随机数字串，长度为 n（1-based 存放在 a[1..n]）
    a = [0]
    for _ in range(n):
        a.append(random.randint(0, 9))

    l = [0 for _ in range(n + 1)]
    r = [0 for _ in range(n + 1)]

    l[1], r[n] = 1, n
    for i in range(2, n + 1):
        if a[i - 1] == a[i]:
            l[i] = l[i - 1]
        else:
            l[i] = i
        if a[n - i + 1] == a[n - i + 2]:
            r[n - i + 1] = r[n - i + 2]
        else:
            r[n - i + 1] = n - i + 1

    if win1(n, k, a, l, r):
        print("tokitsukaze")
    elif win2(n, k, a, l, r):
        print("quailty")
    else:
        print("once again")

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的取值
    main(10)