from bisect import bisect_left


if __name__ == "__main__":
    n, m = map(int, raw_input().split())
    verticals = [int(raw_input()) for _ in range(n)]
    h = [map(int, raw_input().split()) for _ in range(m)]
    horizontals = [t[1] for t in h if t[0] == 1] 

    verticals.sort()
    horizontals.sort()
    verticals.append(10**9)
    min_blockers = n + m
    for i, v in enumerate(verticals):
        cur_blockers = len(horizontals) - bisect_left(horizontals, v) + i
        min_blockers = min(min_blockers, cur_blockers)

    print(min_blockers)
