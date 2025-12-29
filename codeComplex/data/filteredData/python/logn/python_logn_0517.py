from math import floor
import random

CONST = 9

def solve(k):
    i = 0
    while k > CONST * (10 ** i) * (i + 1):
        k -= floor(CONST * (10 ** i)) * (i + 1)
        i += 1
    num_digits = i + 1
    num = floor((k - 1) / num_digits)
    num += floor(10 ** i)
    print(('{}'.format(num))[(k - 1) % num_digits])

def main(n):
    # 根据规模 n 生成 n 个测试数据，数值范围可按需调整
    # 这里生成 1 到 10**12 之间的随机整数作为 k
    test_data = [random.randint(1, 10**12) for _ in range(n)]
    for k in test_data:
        solve(k)

if __name__ == '__main__':
    # 示例：运行规模为 5
    main(5)