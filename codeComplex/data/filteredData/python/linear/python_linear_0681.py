# -*- coding: utf-8 -*-

import random

def main(n):
    # 生成测试数据 A（长度为 n 的非负整数数组）
    # 为保证与原逻辑兼容，分奇偶分别处理
    if n % 2 == 0:
        A = [0] * n
        # 随机生成左半部分
        for i in range(n // 2):
            A[i] = random.randint(0, 10)
        # 复制镜像到右半部分，确保存在合法 B
        for i in range(n // 2):
            A[n - 1 - i] = A[i]
    else:
        A = [0] * n
        mid = n // 2
        # 随机生成左半部分和中间
        for i in range(mid + 1):
            A[i] = random.randint(0, 10)
        # 复制镜像到右半部分
        for i in range(mid):
            A[n - 1 - i] = A[i]

    # 根据 A 构造 B
    # B[i] = A[i] + A[n-1-i]
    B = [A[i] + A[n - 1 - i] for i in range(n)]

    # 以下为原算法逻辑，根据 B 还原 A'
    N = n
    A_res = [0] * N

    i, j = N // 2 - 1, N // 2
    A_res[i] = B[-1] // 2
    A_res[j] = B[-1] // 2 if B[-1] % 2 == 0 else B[-1] // 2 + 1
    l, r = A_res[i], A_res[j]
    for bi in range(len(B) - 2, -1, -1):
        b = B[bi]
        i -= 1
        j += 1

        if b - l >= A_res[j - 1]:
            A_res[i] = l
            A_res[j] = b - l
            r = b - l
        else:
            A_res[j] = r
            A_res[i] = b - r
            l = b - r

    # 输出生成的 B 和恢复得到的 A_res，便于测试
    print("B:", ' '.join(map(str, B)))
    print("A_res:", ' '.join(map(str, A_res)))


if __name__ == "__main__":
    # 示例：调用 main(6)
    main(6)