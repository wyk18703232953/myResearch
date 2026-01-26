def main(n):
    # Generate two deterministic sequences of strings based on n
    # First sequence: s_i = "A" + str(i % 5)
    seq1 = ["A" + str(i % 5) for i in range(n)]
    # Second sequence: s_i = "A" + str((i + 2) % 5)
    seq2 = ["A" + str((i + 2) % 5) for i in range(n)]

    a_dicts = [{}, {}]
    # Simulate original input structure using the generated sequences
    for j in range(2):
        current_seq = seq1 if j == 0 else seq2
        for i in range(n):
            x = current_seq[i]
            if x in a_dicts[j]:
                a_dicts[j][x] += 1

            else:
                a_dicts[j][x] = 1
            if x not in a_dicts[1 - j]:
                a_dicts[1 - j][x] = 0

    c = 0
    for k in a_dicts[0]:
        c += abs(a_dicts[0][k] - a_dicts[1][k])
    return c // 2


if __name__ == "__main__":
    # Example deterministic calls for experimentation
    for n in [1, 5, 10, 100]:
        # print(n, main(n))
        pass