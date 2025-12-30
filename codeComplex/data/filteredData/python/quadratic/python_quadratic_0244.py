import random

def main(n):
    # 生成测试数据：n 为规模，随机生成 a, b
    if n < 2:
        n = 2
    a = random.randint(1, n)
    b = random.randint(1, n)

    c = max(a, b)
    if a != 1 and b != 1:
        print('NO')
        return
    elif n == 2 and c == 1:
        print('NO')
        return
    elif n == 3 and c == 1:
        print('NO')
        return
    else:
        if a == 1:
            g = [[1] * n for _ in range(n)]
            for i in range(n):
                g[i][i] = 0
            for i in range(c - 1, n - 1):
                g[i][i + 1] = g[i + 1][i] = 0
        else:
            g = [[0] * n for _ in range(n)]
            for i in range(c - 1, n - 1):
                g[i][i + 1] = g[i + 1][i] = 1
        print('YES')
        for r in g:
            print(''.join(str(x) for x in r))


if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)