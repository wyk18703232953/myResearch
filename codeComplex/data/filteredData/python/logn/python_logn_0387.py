def main(n):
    # n is the length of the hidden array and must be even (according to original logic)
    # Deterministically construct an array a of length n
    # Example pattern: a[i] = (i % 7) - (i % 5)
    if n % 2 != 0:
        # The original problem assumes even n; for odd n we just print -1 and return
        # print("! -1")
        pass
        return

    a = [(i % 7) - (i % 5) for i in range(n)]

    ask_count = 0

    def ask(num):
        nonlocal ask_count
        ask_count += 1
        # original code is 1-based; convert to 0-based index
        return a[num - 1]

    def ans(num):
        # print("! " + str(num))
        pass

    def opposite(num):
        return num + n // 2

    low = 1
    high = opposite(low)
    lval = ask(low)
    hval = ask(high)
    prev_l_less_h = (lval < hval)

    while high - low > 1:
        mid = (low + high) // 2

        lval = ask(mid)
        hval = ask(opposite(mid))
        l_less_h = (lval < hval)

        if abs(lval - hval) % 2 == 1:
            ans(-1)
            return
        elif hval == lval:
            ans(mid)
            return

        else:
            if l_less_h == prev_l_less_h:
                low = mid

            else:
                high = mid
    ans(-1)


if __name__ == "__main__":
    # example deterministic call; adjust n for scaling experiments
    main(1000)