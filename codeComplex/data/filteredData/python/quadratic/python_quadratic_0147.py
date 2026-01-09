def main(n):
    # Generate deterministic input data
    # Original structure:
    # n
    # then 4 blocks, each with n lines of length n (0/1 chars), separated by a blank line (ignored)
    # Here we construct 4 n x n boards deterministically from n, i, j, k
    boards = []
    for k in range(4):
        block = []
        for i in range(n):
            # Each character is '0' or '1' deterministically derived from (i, j, k, n)
            row = []
            for j in range(n):
                val = (i + j + k + n) % 2
                row.append(str(val))
            block.append(''.join(row))
        boards.append(block)

    c = [0] * 4
    for k in range(4):
        for i in range(n):
            s = boards[k][i]
            for j in range(n):
                if (i + j) % 2 != int(s[j]):
                    c[k] += 1
    c.sort()
    result = c[0] + c[1] + 2 * n * n - c[2] - c[3]
    # print(result)
    pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)