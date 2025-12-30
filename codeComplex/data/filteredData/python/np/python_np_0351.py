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
    # 生成测试数据：
    # N = n，T = n
    # A 为 N 行，每行 [value, type]
    # value 从 1..n 循环，type 在 1,2,3 中循环
    N = n
    T = n
    A = []
    for i in range(N):
        value = (i % n) + 1
        t = (i % 3) + 1
        A.append([value, t])

    s = 0
    for i in range(1, N + 1):
        comb = list(combinations(A, i))
        for x in comb:
            if sum(column(x, 0)) == T:
                a = column(x, 1).count(1)
                b = column(x, 1).count(2)
                c = column(x, 1).count(3)
                s += (out1(a, b, c) + out2(a, b, c) + out3(a, b, c))
    print(s % MOD)

if __name__ == "__main__":
    # 示例：规模 n=5
    main(5)