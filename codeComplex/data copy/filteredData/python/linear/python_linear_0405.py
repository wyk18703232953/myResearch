from math import ceil

def main(n):
    # Deterministic generation of inputs based on n
    # p: number of test cases (fixed to 1 since original code reads once)
    p = 1
    # total_wgt grows linearly with n
    total_wgt = n * 10 + 100
    r1 = total_wgt

    # Generate lift and land arrays:
    # Use different deterministic patterns but keep same length n
    # Ensure all values > 1.0 to avoid division issues in test()
    lift = [(i % 7) + 2 for i in range(n)]
    land = [(i % 5) + 3 for i in range(n)]
    ans = 1e20

    # Extend arrays as in original code
    lift_ext = lift + [lift[0]]
    land_ext = land + [land[0]]

    def test(f):
        nonlocal r1, lift_ext, land_ext, n
        for i in range(n):
            if (r1 + f) > f * lift_ext[i]:
                return 0
            f -= (r1 + f) / lift_ext[i]
            if (r1 + f) > f * land_ext[i + 1]:
                return 0
            f -= (r1 + f) / land_ext[i + 1]
        return 1

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
    main(10)