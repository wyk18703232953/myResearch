def main(n):
    # Ensure n is at least 1
    if n < 1:
        return 0

    # Deterministically construct n and p
    # n is the array length
    # Choose m deterministically as:
    # m = n//2 + 1 (always in [1, n])
    m = n // 2 + 1

    # Construct a permutation of 1..n that depends only on n and is deterministic
    # Pattern: odds in increasing order, then evens in increasing order
    odds = [i for i in range(1, n + 1) if i % 2 == 1]
    evens = [i for i in range(1, n + 1) if i % 2 == 0]
    p = odds + evens

    # Original algorithm logic
    mindex = p.index(m)
    ldict = {}
    rdict = {}
    diff = 0
    ans = 0
    ldict[0] = 1
    rdict[0] = 1

    for i in range(mindex - 1, -1, -1):
        if p[i] < m:
            diff -= 1

        else:
            diff += 1
        if diff in ldict:
            ldict[diff] += 1

        else:
            ldict[diff] = 1

    diff = 0
    for i in range(mindex + 1, n):
        if p[i] < m:
            diff -= 1

        else:
            diff += 1
        if diff in rdict:
            rdict[diff] += 1

        else:
            rdict[diff] = 1

    for num in ldict.keys():
        if -num in rdict:
            ans += ldict[num] * rdict[-num]
        if -num + 1 in rdict:
            ans += ldict[num] * rdict[-num + 1]

    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)