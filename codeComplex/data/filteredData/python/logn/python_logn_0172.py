#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bin_search(n):
    if n == 1:
        return 1
    l = 0
    r = n
    while (r - 1 > l):
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
    根据规模 n 生成一组 (n, k) 测试数据并计算原程序输出。
    这里选择 k = n 作为一组合理测试数据（保证与原逻辑兼容）。
    返回值为原程序应输出的整数结果。
    """
    k = n  # 根据规模 n 生成测试数据，这里简单设为 k = n

    if k * (k - 1) // 2 < n - 1:
        return -1
    elif n == 1:
        return 0
    elif n <= k:
        return 1
    else:
        return k - 1 - bin_search(k * (k - 1) // 2 - n + 1)


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    n = 10
    print(main(n))