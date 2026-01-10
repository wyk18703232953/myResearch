def main(n):
    # Interpret n as the length of the list a; m is not actually used in the logic
    # Deterministically generate m and a based on n
    m = n  # m is unused in the original algorithm, just keep same scale
    a = [(i * 3 + 1) % (n + 5) for i in range(n)]  # deterministic integer list

    # Core algorithm from original program (with input removed)
    ll = sorted(a)
    mx = ll[n - 1] - 1
    cc = 0
    for i in range(n - 2, -1, -1):
        if ll[i] == 0:
            continue
        if mx == 0:
            cc += ll[i] - 1
            continue

        if ll[i] >= mx:
            cc += 1
            mx -= 1
            cc += ll[i] - 1
            ll[i] = 1
        else:
            mx = ll[i]
            cc += 1
            mx -= 1
            cc += ll[i] - 1
            ll[i] = 1

    # For complexity experiments, returning the result is better than printing
    return cc


if __name__ == "__main__":
    # Example deterministic call for testing / benchmarking
    result = main(10)
    print(result)