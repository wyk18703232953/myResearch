#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(n: int):
    # 这里直接使用传入的 n 作为规模
    above = n // 3
    below = n - above
    for i in range(above):
        # print(2 * i + 1, 3)
        pass
    for i in range(below):
        # print(i, 0)
        pass
if __name__ == "__main__":
    # 示例：可在此处指定 n 进行测试
    main(10)