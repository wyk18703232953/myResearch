from heapq import heappush, heappop

def main(n):
    # n: size of input, here used as the length of the array aa
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministic generation of aa based on n
    aa = [(i * 3 + 1) % 5 for i in range(n)]

    inf = 10 ** 9
    dp1 = [[-1] * (n + 1) for _ in range(n)]
    to = [[i + 1] for i in range(n)]
    for i in range(n):
        dp1[i][i + 1] = aa[i]
    for w in range(2, n + 1):
        for l in range(n - w + 1):
            r = l + w
            for m in range(l + 1, r):
                if dp1[l][m] != -1 and dp1[l][m] == dp1[m][r]:
                    dp1[l][r] = dp1[l][m] + 1
                    to[l].append(r)
    hp = []
    heappush(hp, (0, 0))
    dist = [-1] * (n + 1)
    while hp:
        d, i = heappop(hp)
        if i == n:
            # print(d)
            pass
            break
        if dist[i] != -1:
            continue
        dist[i] = d
        for j in to[i]:
            if dist[j] != -1:
                continue
            heappush(hp, (d + 1, j))

if __name__ == "__main__":
    main(10)