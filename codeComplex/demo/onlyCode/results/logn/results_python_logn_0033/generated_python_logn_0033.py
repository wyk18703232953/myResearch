import math
import random

def maxXor(l, r):
    if l == r:
        return 0
    xor = l ^ r
    twoPows = math.log(xor, 2)
    return 2 ** int(math.floor(twoPows) + 1) - 1

def main(n):
    # 根据规模 n 生成测试数据，这里生成 n 对 (l, r)
    # l, r 范围可根据需要调整，这里设置为 [0, 2^20)
    upper_bound = 1 << 20
    test_cases = []
    for _ in range(n):
        a = random.randint(0, upper_bound - 1)
        b = random.randint(0, upper_bound - 1)
        l, r = min(a, b), max(a, b)
        test_cases.append((l, r))

    # 对每个测试用例运行 maxXor 并打印结果
    for l, r in test_cases:
        print(maxXor(l, r))

if __name__ == "__main__":
    # 示例：运行 main，规模为 5
    main(5)