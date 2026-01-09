#! /usr/bin/env python
# -*- coding: utf-8 -*-

def solve(n, k, v):
    if n >= 50:
        # print("YES " + str(n - 1))
        pass
        return
    critical = 1
    excess = 0
    while n > 0:
        if excess >= k:
            # print("YES " + str(n))
            pass
            return
        if critical > k:
            # print("NO")
            pass
            return
        k -= critical
        n -= 1
        excess += (critical * 2 - 1) * v[n]
        critical = (critical * 2 + 1)
    if excess >= k:
        # print("YES " + str(n))
        pass
        return
    # print("NO")
    pass


def main(n):
    # 预计算 v，与原程序一致
    v = [0, 1]
    for _ in range(50):
        a = 1 + 4 * v[-1]
        v.append(a)

    # 根据规模 n 生成测试用例：
    # 生成 n 组 (n_i, k_i)，这里令 n_i = i+1，k_i = v[min(i+1, 50)] 的线性规模数据
    for i in range(n):
        ni = i + 1
        idx = min(ni, 50)
        ki = v[idx]
        solve(ni, ki, v)


if __name__ == "__main__":
    # 可自行修改 n 的默认规模
    main(5)