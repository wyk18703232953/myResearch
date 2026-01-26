def main(n):
    # n controls number of test cases and string length deterministically
    T = max(1, n // 5)
    k = max(1, n // 3)
    length_s = max(k, n)

    def generate_string(idx, length):
        chars = ['R', 'G', 'B']
        return ''.join(chars[(i + idx) % 3] for i in range(length))

    results = []
    for case in range(T):
        s = generate_string(case, length_s)

        rq1 = ''
        rq2 = ''
        rq3 = ''
        for i in range(k):
            if i % 3 == 0:
                rq1 += 'R'
                rq2 += 'G'
                rq3 += 'B'
            elif i % 3 == 1:
                rq1 += 'G'
                rq2 += 'B'
                rq3 += 'R'

            else:
                rq1 += 'B'
                rq2 += 'R'
                rq3 += 'G'

        ans = 10**18
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

    for x in results:
        # print(x)
        pass
if __name__ == "__main__":
    main(10)