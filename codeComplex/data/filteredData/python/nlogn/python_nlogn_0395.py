import heapq


def main(n):
    # Ensure n is at least 1
    if n <= 0:
        return

    # Define k as a deterministic function of n
    k = n // 3

    # Deterministic generation of p and c based on n
    # p: some permutation-like increasing pattern with wrap-around
    p = [(i * 2 + 3) % (2 * n + 1) for i in range(n)]
    # c: strictly increasing values
    c = [i * 5 + 1 for i in range(n)]

    # Original logic starts here
    p_pairs = sorted([(x, i) for i, x in enumerate(p)], key=lambda x: x[0])

    ans = []
    top_k = []

    cur_gold = 0
    for i, t in enumerate(p_pairs):
        if k == 0:
            ans.append((c[t[1]], t[1]))

        else:
            if i < k:
                cur_gold += c[t[1]]
                ans.append((cur_gold, t[1]))
                heapq.heappush(top_k, c[t[1]])

            else:
                smallest = heapq.nsmallest(1, top_k)[0]
                if smallest < c[t[1]]:
                    cur_gold += c[t[1]]
                    ans.append((cur_gold, t[1]))
                    heapq.heappop(top_k)
                    heapq.heappush(top_k, c[t[1]])
                    cur_gold -= smallest

                else:
                    ans.append((cur_gold + c[t[1]], t[1]))

    ans = sorted(ans, key=lambda x: x[1])
    # print(" ".join(map(lambda x: str(x[0]), ans)))
    pass
if __name__ == "__main__":
    main(10)