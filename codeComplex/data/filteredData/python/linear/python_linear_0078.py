def main(n):
    # Generate deterministic binary strings based on n
    # Let first string length be n, second string length be 2n (as a scalable choice)
    len_first = n
    len_second = 2 * n

    # Construct first: repeating pattern "01"
    first = [i % 2 for i in range(len_first)]
    # Construct second: repeating pattern "0011"
    pattern = [0, 0, 1, 1]
    second = [pattern[i % 4] for i in range(len_second)]

    pref_dists = [
        [0] + [int(0 != c) for c in second],
        [0] + [int(1 != c) for c in second]
    ]
    for i in range(1, len(second) + 1):
        pref_dists[0][i] += pref_dists[0][i - 1]
        pref_dists[1][i] += pref_dists[1][i - 1]

    total = 0
    for i, c in enumerate(first):
        end = len(second) - (len(first) - i)
        total += pref_dists[c][end + 1] - pref_dists[c][i]

    # print(total)
    pass
if __name__ == "__main__":
    # Example deterministic call
    main(5)