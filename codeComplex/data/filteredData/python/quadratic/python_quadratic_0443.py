def main(n):
    if n <= 0:
        return

    # Deterministic generation of A based on n
    # Pattern: A[i] = (i * 2 + (i // 3)) % 7
    A = [(i * 2 + (i // 3)) % 7 for i in range(n)]

    dp = [[1 for _ in range(5)] for _ in range(n)]
    Prev = [[-1 for _ in range(5)] for _ in range(n)]

    for i in range(1, n):
        for j in range(5):
            for finger in range(5):
                if dp[i - 1][finger] == 1:
                    if (A[i - 1] < A[i] and finger < j) or (A[i - 1] > A[i] and finger > j) or (A[i - 1] == A[i] and finger != j):
                        dp[i][j] = 1
                        Prev[i][j] = finger
                        break

            else:
                dp[i][j] = 0

    finger = 0
    found = False
    for j in range(5):
        if dp[-1][j] == 1:
            finger = j
            path = [finger]
            for i in range(n - 1, 0, -1):
                finger = Prev[i][finger]
                path.append(finger)
            path = path[::-1]
            for i in range(n):
                # print(path[i] + 1, end=' ')
                pass
            found = True
            break
    if not found:
        # print(-1)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)