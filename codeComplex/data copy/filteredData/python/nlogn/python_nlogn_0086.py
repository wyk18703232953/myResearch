def main(n):
    # Interpret n as the number of (score, time) pairs.
    # Deterministically generate data:
    # scores: increasing with some repetition
    # times: pattern based on index to ensure ties exist
    scores = [(i // 3) for i in range(n)]
    times = [(n - i) // 2 for i in range(n)]

    # Choose k deterministically, in range [1, n]
    if n <= 0:
        return
    k = max(1, n // 2)
    if k > n:
        k = n

    sorted_scores = sorted(zip(scores, times), key=lambda y: (y[0], -y[1]), reverse=True)

    ans = 1
    i = k - 2
    while i >= 0 and (sorted_scores[i] == sorted_scores[k - 1]):
        ans = ans + 1
        i = i - 1

    i = k
    while i < n and (sorted_scores[i] == sorted_scores[k - 1]):
        ans = ans + 1
        i = i + 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)