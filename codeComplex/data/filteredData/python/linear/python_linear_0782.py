#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

def main(n):
    # 1. 生成测试数据：长度为 n 的非负整数数组 a
    #   可以根据需要调整生成规则，这里生成 0~n 之间的随机整数
    a = [random.randint(0, n) for _ in range(n)]

    # 以下为原逻辑的无 input 封装版本
    a.sort()
    cnt = 0

    # 尝试把一对相等的数中的一个减 1（只做一次）
    for i in range(0, len(a) - 1):
        if a[i] == a[i + 1]:
            a[i] -= 1
            cnt += 1
            break

    # 若存在负数，直接判定为 cslnb
    if a[0] < 0:
        print('cslnb')
        return

    # 再次检查是否还有相等元素
    for i in range(0, len(a) - 1):
        if a[i] == a[i + 1]:
            print('cslnb')
            return

    # 计算总步数
    for i, x in enumerate(a):
        cnt += x - i

    # 奇偶性判断
    print('sjfnb' if (cnt & 1) else 'cslnb')


if __name__ == '__main__':
    # 示例：调用 main(5)，规模为 5
    main(5)