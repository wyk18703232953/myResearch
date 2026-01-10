def main(n):
    from heapq import heappush, heappop

    # Deterministic data generation based on n
    # Interpret n as the length of arrays plst and clst
    # Also define k deterministically as n // 2
    if n <= 0:
        return

    k = n // 2

    # Generate plst: a non-decreasing sequence with some repeats
    # Example pattern: plst[i] = i // 3
    plst = [i // 3 for i in range(n)]

    # Generate clst: some varying costs based on simple arithmetic
    # Example pattern: clst[i] = (i * 7) % 1000
    clst = [(i * 7) % 1000 for i in range(n)]

    if k == 0:
        print(*clst)
        return

    pc = sorted(((p, c, i) for i, (p, c) in enumerate(zip(plst, clst))), key=lambda t: (t[0], t[2]))
    res = [0] * n
    pq = []
    pq_sum = 0
    pq_size = 0

    for p, c, i in pc:
        if i > 0 and plst[i] == plst[i - 1]:
            res[i] = res[i - 1]
        else:
            res[i] = pq_sum + c

        if pq_size < k:
            heappush(pq, c)
            pq_sum += c
            pq_size += 1
        else:
            alt = heappop(pq)
            if alt < c:
                heappush(pq, c)
                pq_sum += c - alt
            else:
                heappush(pq, alt)

    print(*res)


if __name__ == "__main__":
    main(10)