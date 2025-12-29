#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def solve(a):
    n = len(a)
    s = set(a)
    a.sort()
    ans = []
    for i in range(n):
        for j in range(31):
            tmp = [a[i]]
            x = a[i] + 2 ** j
            y = a[i] + 2 ** (j + 1)
            if x in s:
                tmp.append(x)
            if y in s:
                tmp.append(y)
            if len(tmp) > 1:
                if len(ans) == 0:
                    ans.append(tmp)
                else:
                    if len(tmp) > len(ans[0]):
                        ans[0] = tmp
    if len(ans) == 0:
        return [a[0]]
    return ans[0]

def main(n):
    # 根据 n 生成测试数据：n 个在[-10^9, 10^9]之间的随机整数
    random.seed(0)
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    res = solve(a)
    print(len(res))
    print(*res)


if __name__ == "__main__":
    # 示例：可修改这里的 n 进行测试
    main(10)