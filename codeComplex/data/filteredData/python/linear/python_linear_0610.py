def main(n):
    # Deterministically generate input arrays a and b based on n
    # Example scheme:
    # a is a permutation-like sequence with simple arithmetic pattern
    # b is another sequence over the same value range but with a different pattern
    a = [(i * 2 + 1) % (2 * n + 1) for i in range(n)]
    b = [(i * 3 + 2) % (2 * n + 1) for i in range(n)]

    done = set()
    j = 0
    ans = []
    for i in range(n):
        if b[i] in done:
            ans.append(0)

        else:
            c = 0
            while j < n and a[j] != b[i]:
                done.add(a[j])
                j += 1
                c += 1
            if j < n:
                done.add(a[j])
                j += 1
                ans.append(c + 1)

            else:
                ans.append(0)
    # print(*ans)
    pass
if __name__ == "__main__":
    main(10)