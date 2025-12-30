#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random

def main(n: int):
    """
    n: 规模参数，用于生成测试数据
    本例中原程序需要两个整数 n, k，
    这里将：
        n_input = n
        k_input 随机生成于 [0, n] 区间内
    """
    # 生成测试数据
    n_input = n
    k_input = random.randint(0, n)

    start = time.time()

    result = (2 * n_input + 3 - int((9 + 8 * (n_input + k_input)) ** 0.5)) // 2
    print(result)

    finish = time.time()
    # 若需要查看运行时间可取消下一行注释
    # print(finish - start)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)