import math
import random

def maxXor(l, r):
    if l == r:
        return 0
    xor = l ^ r
    twoPows = math.log(xor, 2)
    return 2 ** int(math.floor(twoPows) + 1) - 1

def main(n):
    # 生成测试数据：
    # 约定：n 为生成测试数据的上界规模，l 与 r 在 [0, n] 范围内
    l = random.randint(0, n)
    r = random.randint(0, n)
    if l > r:
        l, r = r, l

    print(maxXor(l, r))

if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)