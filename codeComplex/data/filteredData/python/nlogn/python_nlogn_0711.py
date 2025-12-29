# -*- coding: utf-8 -*-
"""
Converted version:
- No input()
- Encapsulated in main(n)
- Generates test data based on n
"""

import random

def main(n):
    # 生成规模为 n 的测试数据：非负整数数组
    # 为了尽量覆盖原逻辑的各种情况，随机生成在 0 ~ 2n 之间的数字
    arr = [random.randint(0, 2 * n) for _ in range(n)]
    arr.sort()

    stop = 0
    equal = -1
    tempcounter = 0

    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            equal = arr[i]
            tempcounter += 1
            if tempcounter == 2:
                break

    if tempcounter == 1 and equal != 0:
        for j in range(n):
            if arr[j] == equal - 1:
                print("cslnb")
                stop = 1
                break  # 原代码未 break，但一旦找到即可确定输出

    if tempcounter == 1 and equal == 0:
        print("cslnb")

    elif tempcounter < 2 and stop == 0:
        moves = arr[0]
        counter = 0

        for i in range(1, n):
            moves += arr[i] - i

        if counter == 0:
            if moves % 2 == 0:
                print("cslnb")
            else:
                print("sjfnb")

    elif stop == 0:
        print("cslnb")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)