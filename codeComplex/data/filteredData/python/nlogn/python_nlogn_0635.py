from collections import namedtuple

HS = namedtuple('HS', 'x1 x2 y')

def main(n):
    # Interpret n as total input scale; split into n verticals and n horizontals
    # Ensure at least 1 element in each list
    n_v = max(1, n // 2)
    n_h = max(1, n - n_v)

    vs = [i * 2 + 1 for i in range(n_v)]
    # Generate hs so that some have x1 == 1 and some do not; y is unused
    hs = []
    for i in range(n_h):
        if i % 3 == 0:
            x1 = 1
            # Alternate between infinite (10**9) and finite x2
            if i % 2 == 0:
                x2 = 10**9
            else:
                x2 = (i + 1) * 3
        else:
            x1 = 2
            x2 = (i + 1) * 5
        y = i  # dummy, not used in logic
        hs.append(HS(x1, x2, y))

    vs.sort()

    hr = len([s for s in hs if s.x1 == 1 and s.x2 == 10**9])
    hs_filtered = [s.x2 for s in hs if s.x1 == 1 and s.x2 < 10**9]
    hs_filtered.sort()

    r = hc = len(hs_filtered)
    vi = 0
    for hi in range(hc):
        while vi < n_v and hs_filtered[hi] >= vs[vi]:
            vi += 1
        c = (hc - hi - 1) + vi
        if c < r:
            r = c

    result = r + hr
    print(result)
    return result

if __name__ == "__main__":
    main(10)