def main(n):
    # Interpret n as number of events
    # Deterministically generate k and (h, m) pairs
    k = n // 2 + 1  # simple deterministic function of n

    r = 0
    for i in range(n):
        h = i % 24
        m = (i * 7) % 60
        t = 60 * h + m
        if t > r + k:
            break
        r = t + k + 1

    # print(r // 60, r % 60)
    pass
if __name__ == "__main__":
    main(10)