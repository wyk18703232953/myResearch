def main(n):
    # Interpret n as:
    # q: number of test cases
    # For test i:
    #   length of string n_i = i + 3 (at least 3)
    #   k_i = max(1, n_i // 2)
    # String s_i deterministically generated from pattern "RGB"
    q = n
    results = []
    for i in range(q):
        length = i + 3
        k = max(1, length // 2)
        # generate deterministic string of length 'length'
        base = "RGB"
        s = "".join(base[j % 3] for j in range(length))
        a = k
        for j in range(length - k + 1):
            a1, a2, a3 = 0, 0, 0
            for jj in range(k):
                ch = s[j + jj]
                mod = jj % 3
                if mod == 0:
                    if ch == "R":
                        a2 += 1
                        a3 += 1
                    elif ch == "G":
                        a1 += 1
                        a3 += 1

                    else:
                        a1 += 1
                        a2 += 1
                elif mod == 1:
                    if ch == "R":
                        a1 += 1
                        a2 += 1
                    elif ch == "G":
                        a2 += 1
                        a3 += 1

                    else:
                        a3 += 1
                        a1 += 1

                else:
                    if ch == "R":
                        a1 += 1
                        a3 += 1
                    elif ch == "G":
                        a1 += 1
                        a2 += 1

                    else:
                        a3 += 1
                        a2 += 1
            a = min(a, a1, a2, a3)
        results.append(a)
    for x in results:
        # print(x)
        pass
if __name__ == "__main__":
    main(5)