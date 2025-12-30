import math
import random

# 原程序中的质数表，最多支持 m <= 8
P = [2, 3, 5, 7, 11, 13, 17, 19]


def ya(x):
    xr = math.ceil(math.sqrt(x))
    res = []
    for i in range(1, xr + 1):
        if x % i == 0:
            res.append(i)
            res.append(x // i)
    return res


def main(n):
    """
    n 为规模参数，用于构造测试数据。
    这里构造：
      - m = 3（列数，可按需修改，但需 <= len(P)）
      - A 为 n 行 m 列的随机整数矩阵
    函数最后返回 (ANS1+1, ANS2+1)
    """

    # 设置列数 m（可按需调整，但不能超过 len(P)）
    m = min(3, len(P))

    # 生成测试数据 A：n 行 m 列，元素取值范围 1..100
    random.seed(0)
    A = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

    # 以下逻辑与原程序保持一致，只是用生成的 A 替代输入

    # 坐标压缩
    SET = set()
    for a in A:
        SET |= set(a)

    compression_dict = {a: ind for ind, a in enumerate(sorted(SET))}

    for i in range(n):
        A[i] = [compression_dict[a] for a in A[i]]

    OK = 0
    NG = len(compression_dict)
    ANS = [1, 1]
    B = [0] * n  # 原代码中 B = [set()]*n 实际上只是容器，这里用整数列表即可
    Q = 1
    for j in range(m):
        Q *= P[j]

    # 二分查找
    while NG > OK + 1:
        mid = (OK + NG) // 2
        SET = set()

        for i in range(n):
            NOW = 1
            for j in range(m):
                if A[i][j] >= mid:
                    NOW *= P[j]
            B[i] = NOW
            SET.add(NOW)

        flag = 0

        for s in SET:
            for l in ya(s):
                if Q // l in SET:
                    flag = 1
                    OK = mid
                    break
            if flag:
                break
        else:
            NG = mid

    # 用最终的 OK 重算 B 与 SET
    SET = set()
    for i in range(n):
        NOW = 1
        for j in range(m):
            if A[i][j] >= OK:
                NOW *= P[j]
        B[i] = NOW
        SET.add(NOW)

    # 找 ANS1
    flag = 0
    ANS1 = 0
    for i in range(n):
        for l in ya(B[i]):
            if Q // l in SET:
                ANS1 = i
                flag = 1
                break
        if flag:
            break

    # 用 B[ANS1] 的因子构造 SET
    LIST = ya(B[ANS1])
    SET = set(LIST)

    # 找 ANS2
    ANS2 = 0
    for i in range(n):
        if Q // B[i] in SET:
            ANS2 = i

    # 输出与原程序行为一致的结果
    print(ANS1 + 1, ANS2 + 1)
    return ANS1 + 1, ANS2 + 1


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)