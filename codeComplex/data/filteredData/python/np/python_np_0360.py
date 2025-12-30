from random import randint

def main(n, m=None):
    # 若未指定 m，则设为与 n 相同的量级
    if m is None:
        m = n

    # 生成测试数据：n 行 m 列的随机整数矩阵 A
    # 可根据需要调整数值范围
    A = [[randint(0, 1000) for _ in range(m)] for _ in range(n)]

    ans = 0
    for _ in range(100):
        for j in range(m):
            x = randint(0, n - 1)
            if x:
                B = []
                for i in range(n):
                    B.append(A[i][j])
                B = B[x:] + B[:x]
                for i in range(n):
                    A[i][j] = B[i]
        c = 0
        for i in range(n):
            c += max(A[i])
        ans = max(ans, c)

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n=5，m 未指定则与 n 同规模
    main(5)