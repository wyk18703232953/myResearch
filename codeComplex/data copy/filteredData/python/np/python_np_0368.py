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


def run_single_case(N, M):
    # deterministic matrix generation: A[i][j] = (i + 1) * (j + 2)
    matrix = [[(i + 1) * (j + 2) for j in range(M)] for i in range(N)]

    elements = []
    for n in range(N):
        for m in range(M):
            elements.append((matrix[n][m], m))

    elements.sort(reverse=True)

    candidates = []
    for val, col in elements:
        if col not in candidates:
            candidates.append(col)
            if len(candidates) == N:
                break

    simplified = []
    for n in range(N):
        row = []
        for m in candidates:
            row.append(matrix[n][m])
        simplified.append(row)

    ans = solve(simplified, 0, N, min(N, M))
    return ans


def main(n):
    # map n to number of test cases and matrix size
    if n <= 0:
        return
    T = n
    results = []
    for t in range(T):
        N = max(1, t + 1)
        M = max(1, n - t)
        res = run_single_case(N, M)
        results.append(res)
        print(res)
    return results


if __name__ == "__main__":
    main(5)