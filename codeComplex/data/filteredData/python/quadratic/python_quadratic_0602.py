import copy
import random

def main(n):
    # 生成测试数据：
    # 为了演示，这里设：
    #   m 在 [1, n] 内随机取值
    #   k 在 [1, 10] 内随机取值
    #   A 为长度为 n 的整数数组，每项在 [-10, 10] 内随机取值
    if n <= 0:
        return 0

    m = random.randint(1, n)
    k = random.randint(1, 10)
    A = [random.randint(-10, 10) for _ in range(n)]

    ANS = 0

    for i in range(m):
        B = copy.deepcopy(A)
        for j in range(i, n, m):
            B[j] -= k

        NOW = 0
        for j in range(i, n):
            if j % m == i:
                NOW = max(NOW + B[j], B[j])
            else:
                NOW += B[j]
            ANS = max(ANS, NOW)

    print(ANS)
    return ANS