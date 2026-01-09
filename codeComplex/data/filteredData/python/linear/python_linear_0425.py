def main(n):
    # Deterministic generation of x and set a of size n
    x = n  # scale x with n deterministically
    a = set((i * 2 + (i // 3)) for i in range(1, n + 1))
    # ensure size is exactly n (it already is by construction for n>=1)

    if len(a) < n:
        # print(0)
        pass

    else:
        d = set()
        p = 0
        for i in a:
            val = i & x
            d.add(val)
            if val != i and val in a:
                # print(1)
                pass
                p = 1
                break
        if len(d) < n and p == 0:
            # print(2)
            pass
        elif p != 1:
            # print(-1)
            pass
if __name__ == "__main__":
    # example call for time complexity experiments
    main(10)