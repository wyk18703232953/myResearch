def main(n):
    if n <= 0:
        print(-1)
        return

    # Deterministic generation of nums and costs based on n
    nums = [i % 7 + (i // 3) for i in range(n)]
    costs = [i % 5 + 1 for i in range(n)]

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

    print(k)


if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)