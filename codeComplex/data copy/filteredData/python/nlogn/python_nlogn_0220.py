def main(n):
    # Deterministically generate N, U, and E based on n
    # Let N = max(3, n), U = n
    N = max(3, n)
    U = n

    # Generate a non-decreasing sequence E of length N
    # Example: E[i] = i + (i // 3) to ensure some gaps but deterministic
    E = [i + (i // 3) for i in range(N)]

    maxu = -1
    j = 2
    if N < 3:
        # print(-1)
        pass
        return
    for i in range(N - 2):
        j = max(i + 2, j)
        if E[j] - E[i] > U:
            continue
        while j < N and E[j] - E[i] <= U:
            j += 1
        j -= 1
        if E[j] != E[i]:
            value = (E[j] - E[i + 1]) / (E[j] - E[i])
            if value > maxu:
                maxu = value
    # print(maxu)
    pass
if __name__ == "__main__":
    main(10)