#!/usr/bin/env python
# coding: utf-8

def main(n: int):
    # 根据 n 生成两个大整数：
    # a：由 n 个 '9' 开头，后面接 n 个 '0'，最后加上 '1'
    # b：由 2n+1 个 '9' 组成
    #
    # 例如 n=3:
    # a = 9990001
    # b = 9999999

    if n <= 0:
        return

    a_str = '9' * n + '0' * n + '1'
    b_str = '9' * (2 * n + 1)

    a = int(a_str)
    b = int(b_str)

    # print(a)
    pass
    # print(b)
    pass
if __name__ == "__main__":
    # 示例：可在此处修改 n 以测试
    main(120)