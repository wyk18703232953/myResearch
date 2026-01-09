def main(n):
    # Interpret n as both array size and number of queries
    # Generate deterministic test data
    # ai: a permutation-like sequence with some structure
    ai = [(i * 3 + 1) % (n + 7) for i in range(n)]
    if len(set(ai)) < n:
        # ensure there is a clear maximum distinct from others, at the last position
        max_val = max(ai) + 1
        ai[-1] = max_val
    q = n

    ar = []
    ar3 = []
    num = 1
    nummm = max(ai)
    if ai[0] != nummm:
        num2 = ai[0]
        for i in range(1, n):
            ar3 += [[num2, ai[i]]]
            if ai[i] == nummm:
                ar += [num2]
                num = i + 1
                break
            if ai[i] > num2:
                ar += [num2]
                num2 = ai[i]

            else:
                ar += [ai[i]]
    ar2 = []
    for i in range(num, n):
        ar2 += [ai[i]]
    for i in range(len(ar)):
        ar2 += [ar[i]]
    num_pairs = len(ar3)

    # Deterministically generate q queries
    # Use pattern that spans small and large m relative to num_pairs
    queries = []
    if num_pairs == 0:
        # if no pairs, all queries go to the "else" branch
        queries = [i + 1 for i in range(q)]

    else:
        for i in range(q):
            if i % 3 == 0:
                # within range of num_pairs, if possible
                m = (i % num_pairs) + 1

            else:
                # beyond num_pairs
                m = num_pairs + 1 + (i % (n if n > 1 else 1))
            queries.append(m)

    # Run the original query logic
    for m in queries:
        if m <= num_pairs:
            # print(ar3[m - 1][0], ar3[m - 1][1])
            pass

        else:
            m -= num_pairs
            m -= 1
            # print(nummm, ar2[m % (n - 1)])
            pass
if __name__ == "__main__":
    main(10)