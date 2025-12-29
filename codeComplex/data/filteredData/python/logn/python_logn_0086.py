from operator import xor
import random

def main(n):
    # 根据规模 n 生成两个非负整数，控制在 n 位二进制以内
    # 例如 n=10，则最多生成小于 2^10 的随机数
    if n <= 0:
        return

    upper = 1 << n  # 2^n
    a = random.randrange(upper)
    b = random.randrange(upper)

    r = [a, b]

    ms = xor(r[0], r[1])

    max_val = 0
    s = 1

    while ms > 0:
        ms >>= 1
        max_val += s
        s <<= 1

    print(max_val)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)