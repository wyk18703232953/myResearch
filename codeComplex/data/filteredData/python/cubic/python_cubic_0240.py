def main(n):
    # Map n to sizes of three arrays: r, g, b
    # Use roughly equal partition; ensure at least 1 for non-zero n
    if n <= 0:
        # print(0)
        pass
        return
    r = n
    g = n
    b = n

    # Deterministic data generation
    # Example pattern: increasing positive integers with simple offsets
    R = [i + 1 for i in range(r)]
    G = [2 * (i + 1) for i in range(g)]
    B = [3 * (i + 1) for i in range(b)]

    R = sorted(R, reverse=True)
    G = sorted(G, reverse=True)
    B = sorted(B, reverse=True)

    dp = []
    for i in range(r + 1):
        sdp = [[0] * (b + 1) for _ in range(g + 1)]
        dp.append(sdp)

    answer = 0
    for nb_taken in range(r + g + b):
        if nb_taken % 2:
            continue
        for i in range(nb_taken + 1):
            if i > r:
                break
            j_start = nb_taken - i - b
            j_end = nb_taken - i
            for j in range(j_start, j_end + 1):
                if j < 0:
                    continue
                if j > g:
                    break
                k = nb_taken - i - j
                if k < 0 or k > b:
                    continue
                if i + j < k or i + k < j or j + k < i:
                    continue
                if i < r and j < g:
                    val = dp[i][j][k] + R[i] * G[j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                    if dp[i + 1][j + 1][k] > answer:
                        answer = dp[i + 1][j + 1][k]
                if i < r and k < b:
                    val = dp[i][j][k] + R[i] * B[k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                    if dp[i + 1][j][k + 1] > answer:
                        answer = dp[i + 1][j][k + 1]
                if j < g and k < b:
                    val = dp[i][j][k] + G[j] * B[k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                    if dp[i][j + 1][k + 1] > answer:
                        answer = dp[i][j + 1][k + 1]

    # print(answer)
    pass
if __name__ == "__main__":
    # Example deterministic call
    main(5)