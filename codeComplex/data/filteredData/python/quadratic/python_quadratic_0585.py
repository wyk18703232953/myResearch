def main(n):
    # n controls the number of test cases and their sizes deterministically
    # We will create t = n test cases.
    # For each i in [1..n], create:
    #   k = max(1, i % (i + 2)) -> always 1 (since i % (i+2) == i, but we ensure k <= n by formula below)
    # To have varying k and n, define:
    #   length = i + 2
    #   k = (i % length) + 1  -> 1 <= k <= length
    #   s is an RGB-like string of length "length".
    t = n
    results = []
    for i in range(1, t + 1):
        length = i + 2
        k = (i % length) + 1
        # deterministic RGB pattern for s
        base = "RGB"
        s = "".join(base[j % 3] for j in range(length))

        mini = length

        test = "RGB" * (k // 3 + 5)
        for start in range(length - k + 1):
            count = 0
            for j in range(k):
                if s[start + j] != test[j]:
                    count += 1
            if count < mini:
                mini = count

        test = "GBR" * (k // 3 + 5)
        for start in range(length - k + 1):
            count = 0
            for j in range(k):
                if s[start + j] != test[j]:
                    count += 1
            if count < mini:
                mini = count

        test = "BRG" * (k // 3 + 5)
        for start in range(length - k + 1):
            count = 0
            for j in range(k):
                if s[start + j] != test[j]:
                    count += 1
            if count < mini:
                mini = count

        results.append(mini)

    # For an experiment, we might not want huge output, but requirement is to keep printing as original did.
    for res in results:
        print(res)


if __name__ == "__main__":
    # example deterministic call
    main(5)