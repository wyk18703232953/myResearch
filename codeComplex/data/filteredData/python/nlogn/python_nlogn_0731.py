from collections import Counter

def main(n):
    # Deterministically generate input tiles as strings like "s1", "p2", "m3"
    # We map n to the number of tiles; cycle through suits and ranks deterministically.
    suits = ['s', 'p', 'm']
    tiles = []
    for i in range(n):
        s = suits[i % 3]
        r = (i % 9) + 1  # ranks 1..9
        tiles.append(s + str(r))

    # Original logic using generated tiles instead of input()
    ts = Counter(''.join(reversed(t)) for t in tiles)
    t0 = None
    run = 0
    ans = 3
    for t, c in sorted(ts.items()):
        if t0 is None or t[0] != t0[0] or int(t[1]) != int(t0[1]) + 1:
            run = 0
        t0 = t
        run += 1
        ans = min(ans, 3 - max(c, run))
    for s in 'spm':
        for r in range(1, 10):
            if s + str(r - 1) in ts and s + str(r + 1) in ts:
                ans = min(ans, 1)
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)