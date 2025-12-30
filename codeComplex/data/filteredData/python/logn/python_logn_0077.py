from math import log2, floor
import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里生成两个 0 到 2^n-1 之间的随机整数 l, r
    max_val = (1 << n) - 1
    l = random.randint(0, max_val)
    r = random.randint(0, max_val)

    # 保留原始逻辑
    if l != r:
        ans = (2 << floor(log2(l ^ r))) - 1
    else:
        ans = 0

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改
    main(10)