#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(n):
    # 依据 n 确定性构造三元组 (k1, k2, k3)，再套用原算法逻辑
    # 让规模 n 直接映射到数值大小，保证可规模化
    k1 = max(1, n)
    k2 = max(1, n + 1)
    k3 = max(1, n + 2)
    k1, k2, k3 = sorted((k1, k2, k3))

    if (
        1 == k1
        or (2 == k1 and 2 == k2)
        or (3 == k1 and 3 == k2 and 3 == k3)
        or (k1 == 2 and k2 == 4 and k3 == 4)
    ):
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行时间复杂度实验
    main(5)