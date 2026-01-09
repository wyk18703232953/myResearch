mod = 998244353
bits = ['00', '01', '10', '11']
pat = [[0, 1, 1, 1],
       [0, 0, 2, 0],
       [0, 2, 0, 0],
       [1, 1, 1, 0]]

add = lambda a, b: (a % mod + b % mod) % mod


def solve(n, k):
    mem = [[[0 for _ in range(4)] for _ in range(k + 1)] for _ in range(2)]

    for i in range(4):
        val = min(bits[i].count('0'), 1) + min(bits[i].count('1'), 1)
        if val <= k:
            mem[0][val][i] = 1

    for i in range(1, n):
        for j in range(1, k + 1):
            for k1 in range(4):
                for k2 in range(4):
                    val = j + pat[k1][k2]
                    if val <= k:
                        mem[i & 1][val][k2] = add(mem[(i - 1) & 1][j][k1],
                                                  mem[i & 1][val][k2])

        for j in range(1, k + 1):
            for k1 in range(4):
                mem[(i - 1) & 1][j][k1] = 0

    return sum(mem[(n - 1) & 1][k]) % mod


def main(n):
    # 根据规模 n 生成测试数据：这里令 k = n
    k = n
    ans = solve(n, k)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)