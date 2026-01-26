def main(n):
    # Generate deterministic binary strings based on n
    # Let length of first be n, length of second be 2n (at least 1)
    if n < 1:
        n = 1
    first_len = n
    second_len = 2 * n

    # first: pattern 0,1,0,1,...
    first = [i % 2 for i in range(first_len)]
    # second: pattern 0,0,1,1,0,0,1,1,...
    second = [(i // 2) % 2 for i in range(second_len)]

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
    # Example deterministic call; change n for different scales
    main(5)