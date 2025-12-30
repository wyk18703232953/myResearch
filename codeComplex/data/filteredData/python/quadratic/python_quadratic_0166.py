import random

def main(n: int):
    # 生成测试数据：
    # 1) N = n
    # 2) 选择一个相对小的 K，保证数组 A[0..255] 不越界
    # 3) 生成 N 个在 [0, 255] 范围内的随机整数作为 P
    N = n
    # 保证 K 至少为 1，且不会太大
    K = max(1, min(10, n))
    P = [random.randint(0, 255) for _ in range(N)]

    # 以下为原始逻辑
    A = [None] * 256
    A[0] = 0
    for i in range(N):
        pn = P[i]
        if A[pn] is None:
            for j in range(K - 1, -1, -1):
                if pn < j:
                    continue
                if A[pn - j] is None:
                    A[pn - j] = pn - j
                    break
                else:
                    if A[pn - j] + K - 1 >= pn:
                        break
            for jj in range(j, -1, -1):
                A[pn - jj] = A[pn - j]
    print(*[A[P[i]] for i in range(N)])


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(5)