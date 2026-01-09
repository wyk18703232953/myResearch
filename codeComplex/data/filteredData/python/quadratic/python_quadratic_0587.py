def main(n):
    # Interpret n as:
    # T: number of test cases = n
    # For test case t (0-based): length of string nt = t + 1 + n, window size kt = (t % (nt)) + 1
    # Generate deterministic strings of 'R', 'G', 'B'
    T = n
    results = []

    for t in range(T):
        length = t + 1 + n
        k = (t % length) + 1
        # Generate s deterministically: cycle through 'R', 'G', 'B'
        chars = ['R', 'G', 'B']
        s = ''.join(chars[i % 3] for i in range(length))

        rq1 = ''
        rq2 = ''
        rq3 = ''

        for i in range(k):
            if i % 3 == 0:
                rq1 = rq1 + 'R'
                rq2 = rq2 + 'G'
                rq3 = rq3 + 'B'
            elif i % 3 == 1:
                rq1 = rq1 + 'G'
                rq2 = rq2 + 'B'
                rq3 = rq3 + 'R'
            elif i % 3 == 2:
                rq1 = rq1 + 'B'
                rq2 = rq2 + 'R'
                rq3 = rq3 + 'G'

        ans = 1000000000000000000

        for i in range(0, len(s) - k + 1):
            a1 = 0
            a2 = 0
            a3 = 0

            for j in range(i, i + k):
                if s[j] != rq1[j - i]:
                    a1 += 1
                if s[j] != rq2[j - i]:
                    a2 += 1
                if s[j] != rq3[j - i]:
                    a3 += 1

            ans = min(ans, min(a1, a2, a3))

        results.append(ans)

    # Combine outputs similar to original multiple print calls
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(5)