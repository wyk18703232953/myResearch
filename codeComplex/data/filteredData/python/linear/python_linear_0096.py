def main(n):
    # Generate deterministic string S of length n over a fixed alphabet
    if n <= 0:
        # print(0)
        pass
        return

    alphabet = "abcde"
    k = len(alphabet)
    S = "".join(alphabet[i % k] for i in range(n))

    M = {}
    N = n

    s = set()
    for c in S:
        s.add(c)
        M[c] = 0

    i = 0
    j = -1
    aux = 0
    ans = 10**10

    while j < N - 1:
        j += 1

        M[S[j]] += 1
        if M[S[j]] == 1:
            aux += 1
        while M[S[i]] > 1:
            M[S[i]] -= 1
            i += 1

        if aux == len(s):
            ans = min(ans, j - i + 1)

    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)