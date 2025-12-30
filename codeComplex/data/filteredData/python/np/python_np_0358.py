import random

def solve_single(A):
    n = len(A)
    m = len(A[0]) if n > 0 else 0

    # 转置得到列列表 B
    B = [[A[i][j] for i in range(n)] for j in range(m)]

    # 按列最大值排序，取前 n 列
    B.sort(key=lambda x: max(x), reverse=True)
    B = B[:n]
    LEN = len(B)

    if LEN == 0:
        return 0

    if LEN == 1:
        return sum(B[0])

    if LEN == 2:
        ans = 0
        for shift1 in range(n):
            cur = 0
            for k in range(n):
                cur += max(B[0][k], B[1][(shift1 + k) % n])
            ans = max(ans, cur)
        return ans

    if LEN == 3:
        ans = 0
        for shift1 in range(n):
            for shift2 in range(n):
                cur = 0
                for k in range(n):
                    cur += max(
                        B[0][k],
                        B[1][(shift1 + k) % n],
                        B[2][(shift2 + k) % n],
                    )
                ans = max(ans, cur)
        return ans

    # LEN >= 4 的情况只用前 4 列
    LEN = min(LEN, 4)
    B = B[:LEN]

    if LEN == 4:
        ans = 0
        for shift1 in range(n):
            for shift2 in range(n):
                for shift3 in range(n):
                    cur = 0
                    for k in range(n):
                        cur += max(
                            B[0][k],
                            B[1][(shift1 + k) % n],
                            B[2][(shift2 + k) % n],
                            B[3][(shift3 + k) % n],
                        )
                    ans = max(ans, cur)
        return ans

    # 理论上不会走到这里
    return 0


def generate_test_case(n):
    # 随机生成一个 n×m 的矩阵，m 在 [1, 2n] 范围内
    m = random.randint(1, max(1, 2 * n))
    A = [[random.randint(0, 1000) for _ in range(m)] for _ in range(n)]
    return A


def main(n):
    # 这里的 n 既作为规模参数，又作为矩阵的行数
    # 可以根据需要修改测试数据规模策略
    t = 1  # 测试组数，可根据需要调整或外部传入
    for _ in range(t):
        A = generate_test_case(n)
        ans = solve_single(A)
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(3)，可根据需要修改
    main(3)