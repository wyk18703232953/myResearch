import random

def main(n):
    # 生成测试数据：根据 n 构造 a, b
    # 这里给出一种简单策略，你可按需修改：
    # - 绝大多数情况下满足至少一个为 1
    # - 偶尔生成 a > 1 且 b > 1 的情况测试 NO 分支
    if n <= 1:
        # 对于非常小的 n，强制 a=1,b=n 作为示例
        a, b = 1, max(1, n)
    else:
        if random.random() < 0.2:
            # 20% 概率生成 a>1 且 b>1
            a = random.randint(2, max(2, n))
            b = random.randint(2, max(2, n))
        else:
            # 至少有一个是 1
            if random.random() < 0.5:
                a = 1
                b = random.randint(1, max(1, n))
            else:
                b = 1
                a = random.randint(1, max(1, n))

    # 以下是原逻辑，只是搬进 main(n)，使用生成的 a, b

    if a > 1 and b > 1:
        print('NO')
        return

    if n in [2, 3] and a == 1 and b == 1:
        print('NO')
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

    print('YES')
    for row in matrix:
        print("".join('1' if x else '0' for x in row))


if __name__ == '__main__':
    # 示例：调用 main(5)，你可以在外部按需调用不同的 n
    main(5)