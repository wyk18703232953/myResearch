import sys

def main(n):
    # n 控制列表长度和数值范围
    if n <= 0:
        return
    N = n
    M = float(n)

    # 生成长度为 N 的整数列表 A 和 B
    # 所有元素 >= 2，避免 c-1 为 0
    A = [2 + (i % max(1, n)) for i in range(N)]
    B = [2 + ((i * 3) % max(1, n)) for i in range(N)]

    # 保持原有 B 的旋转逻辑
    B = B[1:] + [B[0]]

    C = []
    for a, b in zip(A[::-1], B[::-1]):
        C.append(b)
        C.append(a)

    if 1 in C:
        # print(-1)
        pass

    else:
        M0 = M
        for c in C:
            M += M / (c - 1)
        # print(M - M0)
        pass
if __name__ == "__main__":
    main(10)