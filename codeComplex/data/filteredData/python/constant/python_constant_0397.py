def main(n):
    # n is the length of each of the two strings
    # Deterministic generation of two rows of '0'/'1'
    # Example pattern: first row: alternating "0"/"1", second row: periodic blocks
    row0 = [str(i % 2) for i in range(n)]
    row1 = [str((i // 2) % 2) for i in range(n)]

    s = [row0, row1]
    cnt = 0
    for i in range(n - 1):
        if s[0][i] == s[1][i] == s[0][i + 1] == "0":
            cnt += 1
            s[0][i] = s[1][i] = s[0][i + 1] = "X"
        elif s[0][i] == s[1][i] == s[1][i + 1] == "0":
            cnt += 1
            s[0][i] = s[1][i] = s[1][i + 1] = "X"
        elif s[0][i] == s[1][i + 1] == s[0][i + 1] == "0":
            cnt += 1
            s[0][i] = s[1][i + 1] = s[0][i + 1] = "X"
        elif s[0][i + 1] == s[1][i] == s[1][i + 1] == "0":
            cnt += 1
            s[0][i + 1] = s[1][i] = s[1][i + 1] = "X"
    # print(cnt)
    pass
if __name__ == "__main__":
    # Example deterministic call for testing / benchmarking
    main(1000)