def main(n):
    import heapq

    MOD_NUM = 10**9 + 7

    # Deterministic generation of x, y based on n
    x = n + 3
    y = (2 * n + 5)

    # Generate n intervals deterministically
    # l increases with i, r = l + something
    events = dict()
    for i in range(1, n + 1):
        l = i
        r = i + (i % 7) + 1
        if l not in events:
            events[l] = []
        events[l].append(r)

    tv = []
    pq = []
    cost = 0

    for t in sorted(events):
        while tv and tv[0] < t:
            heapq.heappush(pq, -(x + heapq.heappop(tv) * y))

        for ri in sorted(events[t], reverse=True):
            if pq and -pq[0] > t * y:
                val = -heapq.heappop(pq)
                rj = (val - x) // y
                cost += (ri - rj) * y
                heapq.heappush(tv, ri)
            else:
                cost += x + (ri - t) * y
                heapq.heappush(tv, ri)
        cost %= MOD_NUM

    print(cost)
    return cost


if __name__ == "__main__":
    main(10)