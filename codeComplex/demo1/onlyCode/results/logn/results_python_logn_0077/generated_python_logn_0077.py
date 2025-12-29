from math import log2, floor
import random

def main(n):
    # 根据规模 n 生成两个非负整数 l, r
    # 这里让它们的范围与 n 相关，可以按需要调整策略
    max_val = max(1, n)
    l = random.randint(0, max_val)
    r = random.randint(0, max_val)

    # 原逻辑：求 l^r 的最高位以下全 1 的数
    if l != r:
        res = (2 << floor(log2(l ^ r))) - 1
    else:
        res = 0

    print(res)

if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)