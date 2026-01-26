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
    """
    n: 规模参数，作为 N 使用。
    测试数据生成规则：
      - N = n
      - T = n
      - A 为 N 行，每行为 [value, label]
        * value = i+1 (1..N)
        * label = (i % 3) + 1 在 {1,2,3} 之间循环
    """
    N = n
    T = n

    A = []
    for i in range(N):
        value = i + 1
        label = (i % 3) + 1  # 1,2,3 循环
        A.append([value, label])

    s = 0
    for i in range(1, N + 1):
        comb = combinations(A, i)
        for x in comb:
            if sum(column(x, 0)) == T:
                a = column(x, 1).count(1)
                b = column(x, 1).count(2)
                c = column(x, 1).count(3)
                s += (out1(a, b, c) + out2(a, b, c) + out3(a, b, c))
                s %= MOD

    # print(s % MOD)
    pass
if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(5)