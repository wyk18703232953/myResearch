def main(n):
    # Deterministically generate nums and costs based on n
    # Example: nums is a simple increasing sequence with some modulation,
    # costs is a derived sequence to keep structure non-trivial but deterministic
    nums = [(i * 3) % (n + 7) for i in range(n)]
    costs = [(i * 5 + 2) % (n + 11) + 1 for i in range(n)]

    k = -1

    for i in range(n):
        kc = -1
        for c in range(i + 1, n):
            if nums[i] < nums[c] and (kc == -1 or kc > costs[c]):
                if kc == -1:
                    kc = costs[c]
                kc = costs[c]

        if kc > -1:
            nat = kc
            kc = -1
            for c in range(i):
                if nums[i] > nums[c] and (kc == -1 or kc > costs[c]):
                    if kc == -1:
                        kc = costs[c]
                    kc = costs[c]

            if kc > -1:
                if k == -1:
                    k = nat + kc + costs[i]
                k = min(nat + kc + costs[i], k)

    # print(k)
    pass
if __name__ == "__main__":
    main(10)