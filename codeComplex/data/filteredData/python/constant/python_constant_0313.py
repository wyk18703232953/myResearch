import random

def main(n):
    # 由于原题逻辑是对长度固定为 14 的数组进行操作，
    # 这里 n 作为生成测试数据的“规模因子”，
    # 但核心逻辑仍然是对长度为 14 的数组进行计算。
    # 若希望完全参数化长度，需要重写算法，这里保持原算法含义不变。

    # 生成长度为 14 的测试数据，元素范围可根据 n 调整
    # 例如：元素在 [0, n] 区间内
    A = [random.randint(0, n) for _ in range(14)]

    ans = 0
    for i in range(14):
        if A[i] == 0:
            continue
        B = A + A
        B[i + 14] = 0
        q, r = divmod(B[i], 14)
        for j in range(1, 15):
            if j <= r:
                B[i + j] += (q + 1)
            else:
                B[i + j] += q

        temp = 0
        for j in range(i + 1, i + 15):
            if B[j] % 2 == 0:
                temp += B[j]
        ans = max(ans, temp)

    print(ans)


if __name__ == "__main__":
    # 示例调用，规模参数可自行调整
    main(100)