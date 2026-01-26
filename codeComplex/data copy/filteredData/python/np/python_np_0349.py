from itertools import combinations

MOD = 1000000007


def out1(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return 0
    if a == 1 and b == 0 and c == 0:
        return 1
    return a * (out2(a - 1, b, c) + out3(a - 1, b, c))


def out2(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return 0
    if a == 0 and b == 1 and c == 0:
        return 1
    return b * (out1(a, b - 1, c) + out3(a, b - 1, c))


def out3(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return 0
    if a == 0 and b == 0 and c == 1:
        return 1
    return c * (out2(a, b, c - 1) + out1(a, b, c - 1))


def column(matrix, i):
    return [row[i] for row in matrix]


def main(n):
    # 生成规模为 n 的测试数据
    # N = n，T 为所有第一列之和的一半（向下取整），确保有部分子集可满足
    N = n
    A = []
    for i in range(N):
        # 第一列从 1 到 N
        first_col = i + 1
        # 第二列在 {1,2,3} 中循环
        second_col = (i % 3) + 1
        A.append([first_col, second_col])
    T = sum(row[0] for row in A) // 2

    s = 0
    for i in range(1, N + 1):
        comb = combinations(A, i)
        for x in comb:
            if sum(column(x, 0)) == T:
                a = column(x, 1).count(1)
                b = column(x, 1).count(2)
                c = column(x, 1).count(3)
                s += (out1(a, b, c) + out2(a, b, c) + out3(a, b, c))
    # print(s % MOD)
    pass
if __name__ == "__main__":
    # 示例：以 n = 5 运行
    main(5)