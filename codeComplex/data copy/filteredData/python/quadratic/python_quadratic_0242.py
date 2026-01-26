def main(n):
    # 确定性生成 a, b，保证 1 <= a, b <= n
    if n < 2:
        # 对于过小的 n，构造一个退化案例
        a, b = 1, 1

    else:
        a = 1 + (n % n)           # 恒为 1
        b = 1 + ((n // 2) % n)    # 对于 n>=2，恒为 1 或 2

    if a > 1 and b > 1:
        # print('NO')
        pass
        return

    if n in [2, 3] and a == 1 and b == 1:
        # print('NO')
        pass
        return

    matrix = [[i in [j + 1, j - 1] for i in range(n)] for j in range(n)]

    a, b = n + 1 - a, n + 1 - b
    if a != n:
        matrix = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i < a and j < a and i != j:
                    matrix[i][j] = True
    elif b != n:
        matrix = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i >= b or j >= b:
                    matrix[i][j] = True
                if i == j:
                    matrix[i][j] = False

    # print('YES')
    pass
    for row in matrix:
        # print("".join('1' if x else '0' for x in row), flush=False)
        pass
if __name__ == "__main__":
    # 示例调用：可调整 n 进行规模实验
    main(5)