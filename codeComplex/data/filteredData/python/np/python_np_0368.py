import random

def solve(matrix, col, N, M):
    if col == M:
        ans = 0
        for row in matrix:
            if len(row) == 1:
                ans += row[0]
            else:
                ans += max(*row)
        return ans

    if N == 1:
        return solve(matrix, col + 1, N, M)

    ans = solve(matrix, col + 1, N, M)
    for _ in range(N - 1):
        tmp = matrix[0][col]
        for n in range(1, N):
            matrix[n - 1][col] = matrix[n][col]
        matrix[N - 1][col] = tmp

        local_ans = solve(matrix, col + 1, N, M)
        if local_ans > ans:
            ans = local_ans

    return ans


def main(n):
    """
    n: 问题规模，用作 N 和 M 的尺寸上界，并生成一组随机测试数据。
    为简单起见，令 N = M = n，矩阵元素随机生成在 [1, 100]。
    """
    N = n
    M = n

    # 生成随机测试数据矩阵
    random.seed(0)
    matrix = [
        [random.randint(1, 100) for _ in range(M)]
        for _ in range(N)
    ]

    elements = []
    for i in range(N):
        for j in range(M):
            elements.append((matrix[i][j], j))

    elements.sort(reverse=True)

    candidates = []
    for val, col in elements:
        if col not in candidates:
            candidates.append(col)
            if len(candidates) == N:
                break

    simplified = []
    for i in range(N):
        row = []
        for c in candidates:
            row.append(matrix[i][c])
        simplified.append(row)

    ans = solve(simplified, 0, N, min(N, M))
    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 4 运行
    main(4)