def main(n):
    # Deterministically generate a string of length n
    # Use repeating lowercase letters pattern
    if n <= 0:
        # print(0)
        pass
        return
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    m = len(alphabet)
    line = "".join(alphabet[i % m] for i in range(n))

    n_len = len(line)
    temp = [0]
    for i in range(1, n_len):
        for j in range(n_len - i):
            for k in range(1, n_len - i - j + 1):
                if line[j:j + i] == line[j + k:j + k + i]:
                    temp.append(i)
    # print(max(temp))
    pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)