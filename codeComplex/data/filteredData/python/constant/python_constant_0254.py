import math
import random

def main(n):
    # 生成测试数据：
    # 规模 n 用作第一行的 n
    # 第二行的 m 随机设置为 [1, 2^(n+2)] 范围内的整数，保证有足够大规模测试
    m = random.randint(1, 2 ** (n + 2))

    # 原逻辑
    if n <= math.log2(m):
        result = m % (2 ** n)
    else:
        result = m

    print(result)


if __name__ == '__main__':
    # 示例：可以在此处修改固定的 n 来测试
    main(10)