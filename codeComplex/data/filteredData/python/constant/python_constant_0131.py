import random
import math

def main(n):
    # 生成测试数据：随机选择 m，1 <= m <= n 且 m != 0
    if n <= 0:
        return 0

    # 保证 m 在 [1, n] 中随机
    m = random.randint(1, n)

    a = 0
    x, y = n, m
    while y:
        a += x // y
        x, y = y, x % y

    print(a)

if __name__ == "__main__":
    # 示例：可修改 n 测试规模
    main(100)