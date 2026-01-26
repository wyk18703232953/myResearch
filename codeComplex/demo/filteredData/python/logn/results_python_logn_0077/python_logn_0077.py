from math import *

def main(n):
    # 确定性生成一对 (l, r)，使得输入规模与 n 相关
    # 令 l 与 r 为相近的大整数，以触发 l^r 的位运算逻辑
    l = n * n + 1
    r = l + n  # r > l，且差为 n
    if l != r:
        x = l ^ r
        if x == 0:
            result = 0

        else:
            k = floor(log2(x))
            result = (2 << k) - 1

    else:
        result = 0
    # print(result)
    pass
if __name__ == "__main__":
    main(10)