def main(n):
    # Interpret n as: number of test cases q = n, each with size increasing with index
    # For test case t (1-based), let:
    #   k = t
    #   string length len_s = 2 * t
    #   s is a deterministic pattern of 'R','G','B' repeated
    q = n
    results = []
    for t in range(1, q + 1):
        k = t
        len_s = 2 * t
        l1 = ["R", "G", "B"]
        s = "".join(l1[i % 3] for i in range(len_s))
        m = 10 ** 4
        for j in range(len_s):
            if j + k <= len_s:
                m1 = m2 = m3 = 0
                for i in range(j, j + k):
                    if l1[(i - j) % 3] != s[i]:
                        m1 += 1
                for i in range(j, j + k):
                    if l1[(i + 1 - j) % 3] != s[i]:
                        m2 += 1
                for i in range(j, j + k):
                    if l1[(i + 2 - j) % 3] != s[i]:
                        m3 += 1
                m = min(m, m1, m2, m3)

            else:
                break
        results.append(m)
    for value in results:
        # print(value)
        pass
if __name__ == "__main__":
    main(5)