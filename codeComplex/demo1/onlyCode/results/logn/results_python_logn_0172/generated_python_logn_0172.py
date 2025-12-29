#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bin_search(n):
    if n == 1:
        return 1
    l = 0
    r = n
    while r - 1 > l:
        mid = (l + r) // 2
        val = mid * (mid + 1) // 2
        if val == n:
            return mid
        elif val > n:
            r = mid
        else:
            l = mid
    return l


def main(n):
    """
    规模参数 n 用来生成一组 (n, k) 测试数据，并执行原逻辑。
    这里设定：
        k = max(1, n) 作为一组合理的测试规模（可按需要调整生成策略）。
    返回值为原程序的输出结果。
    """
    # 生成测试数据：示例选择 k = n（至少要有 k >= 1）
    k = max(1, n)

    if k * (k - 1) // 2 < n - 1:
        return -1
    elif n == 1:
        return 0
    elif n <= k:
        return 1
    else:
        return k - 1 - bin_search(k * (k - 1) // 2 - n + 1)


if __name__ == "__main__":
    # 示例：调用 main(10) 并打印结果
    print(main(10))