def main(n):
    # n is the size N of the matrix (number of strings and string length)
    N = n

    # Deterministically construct m1 and m2 as lists of strings of length N
    # Use simple arithmetic / patterns so that m1 is sometimes in ms and sometimes not,
    # but always deterministically derived from n.
    # Base string pattern: 'a', 'b', 'c', ... wrapping after 'z'
    def make_matrix(offset):
        return [
            ''.join(
                chr(ord('a') + ((i + j + offset) % 26))
                for j in range(N)
            )
            for i in range(N)
        ]

    # Let m2 be a base matrix
    m2 = make_matrix(0)

    # For m1, choose either m2 or a slightly modified version based on n
    # This keeps behavior deterministic.
    if n % 2 == 0:
        m1 = [row for row in m2]  # identical when n is even

    else:
        # modify one position deterministically when n is odd
        m1 = m2[:]
        if N > 0:
            row0 = m1[0]
            c = row0[0]
            # change first character deterministically
            c2 = chr(ord('a') + ((ord(c) - ord('a') + 1) % 26))
            m1[0] = c2 + row0[1:]

    ms = [
        m2,
        [x[::-1] for x in m2],
        [x for x in reversed(m2)],
    ]

    a = []
    for m in ms:
        a.append(m)
        a.append([x[::-1] for x in reversed(m)])
        a.append([''.join(m[j][i] for j in range(N - 1, -1, -1)) for i in range(N)])
        a.append([''.join(m[j][i] for j in range(N)) for i in range(N - 1, -1, -1)])

    ms = a
    # print(['NO', 'YES'][m1 in ms])
    pass
if __name__ == "__main__":
    # Example call; change n as needed for experiments
    main(5)