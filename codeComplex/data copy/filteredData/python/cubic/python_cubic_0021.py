def main(n):
    # Deterministically generate a string of length n over a small alphabet
    # Pattern: repeating "abcde"
    base = "abcde"
    string = "".join(base[i % len(base)] for i in range(n))

    n_len = len(string)
    count1 = []
    long = 0
    for s_i in range(n_len):
        for end_i in range(s_i + 1, n_len + 1):
            sub = string[s_i:end_i]
            if sub not in count1:
                count1.append(sub)

            else:
                if len(sub) > long:
                    long = len(sub)
    # print(long)
    pass
if __name__ == "__main__":
    main(10)