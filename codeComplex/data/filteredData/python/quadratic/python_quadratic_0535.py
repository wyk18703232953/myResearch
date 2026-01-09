def main(n):
    # Scale interpretation:
    # Use n as base, let m = n for simplicity, so total length is 2n
    # Original input structure:
    #   n, m
    #   x: length n + m
    #   t: length n + m (values 0 or 1)
    #
    # Deterministic generation rules:
    #   n = n
    #   m = n
    #   x[i] = (i * 3) % (2*n + 1)
    #   t[i] = 0 if i % 3 == 0 else 1
    #
    # This preserves enough zeros and ones to exercise all branches.
    m = n
    total = n + m

    x = [(i * 3) % (total + 1) for i in range(total)]
    t = [0 if i % 3 == 0 else 1 for i in range(total)]

    arr = []
    pep = {}
    for i in range(total):
        if t[i] == 0:
            arr.append(i)
            pep[x[i]] = 0

        else:
            for j in arr:
                pep[x[j]] = i
            arr = []
    for i in range(total - 1, -1, -1):
        if t[i] == 0:
            arr.append(i)

        else:
            for j in arr:
                if abs(x[j] - x[i]) <= abs(x[pep[x[j]]] - x[j]):
                    pep[x[j]] = i
            arr = []
    ans = []
    for i in range(total):
        if t[i]:
            ans.append(1)

        else:
            ans.append(0)
    for i in pep:
        ans[pep[i]] += 1
    for i in ans:
        if i:
            # print(i - 1, end=' ')
            pass
if __name__ == "__main__":
    main(10)