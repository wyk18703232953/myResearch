import math
import random

def main(n: int):
    # 根据 n 生成测试数据，本质上该算法要求 n 为正整数
    # 这里假定 n 为第 n 位数字的位置（1-based），故直接使用传入的 n
    # 如需随机生成，可用：n = random.randint(1, n)
    # 为尽量不改变原语义，这里直接使用参数 n

    a = [9]
    for i in range(2, 20):
        a.append(10 ** i - 10 ** (i - 1))

    b = [0]
    for i in range(1, 20):
        b.append(b[-1] + i * a[i - 1])

    for i in range(20):
        if n <= b[i]:
            break

    p = b[i - 1]
    k = n - p
    ans = 10 ** (i - 1) - 1 + math.ceil(k / i)

    if k % i == 0:
        print(('0' + str(ans))[i])
    else:
        print(('0' + str(ans))[k % i])


# 示例调用
if __name__ == "__main__":
    # 随机生成一个规模为 1..10^6 范围内的位置作为测试
    test_n = random.randint(1, 10 ** 6)
    main(test_n)