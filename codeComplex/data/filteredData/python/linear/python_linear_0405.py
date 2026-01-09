from math import ceil

def main(n):
    # Deterministically generate inputs based on n
    # p: an unused parameter in the original program; keep it for structure
    p = n

    # total_wgt (r1): use n as the weight scale
    total_wgt = n
    r1 = total_wgt

    # Generate lift and land arrays:
    # Make them length n, positive and > 1 to avoid trivial failures.
    # Example pattern: lift[i] = 2 + (i % 5), land[i] = 2 + ((i * 2) % 7)
    lift = [2 + (i % 5) for i in range(n)]
    land = [2 + ((i * 2) % 7) for i in range(n)]

    # Keep behavior consistent with original code
    def test(f):
        for i in range(local_n):
            if (local_r1 + f) > f * local_lift[i]:
                return 0
            f -= (local_r1 + f) / local_lift[i]
            if (local_r1 + f) > f * local_land[i + 1]:
                return 0
            f -= (local_r1 + f) / local_land[i + 1]
        return 1

    # Bind variables as in original code
    local_lift = lift[:]
    local_land = land[:]
    local_n = len(local_land)
    local_r1 = r1

    local_lift += [local_lift[0]]
    local_land += [local_land[0]]

    l = 0.0
    r = 1e20

    for _ in range(1000):
        mid = (l + r) / 2.0
        if test(mid):
            r = mid

        else:
            l = mid

    if r < 1e19:
        # print('%.17f' % r)
        pass

    else:
        # print(-1.0)
        pass
if __name__ == "__main__":
    # Example deterministic call; change n to scale the input
    main(10)