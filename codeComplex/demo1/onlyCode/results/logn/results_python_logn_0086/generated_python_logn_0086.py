from operator import xor
import random

def main(n: int):
    # 1. 生成测试数据：两个在 [0, 2^n - 1] 范围内的整数
    upper = (1 << n) - 1
    a = random.randint(0, upper)
    b = random.randint(0, upper)

    # 2. 原逻辑
    r0, r1 = a, b
    ms = xor(r0, r1)

    max_val = 0
    s = 1

    while ms > 0:
        ms >>= 1
        max_val += s
        s <<= 1

    print(max_val)

if __name__ == "__main__":
    # 示例调用：n=10，可按需修改
    main(10)