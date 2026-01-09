def main(n):
    # Interpret n as both the number count and the range of possible values
    m = n
    # Deterministically generate daf1 of length m with values in [1, n]
    if n <= 0:
        # print(0)
        pass
        return
    daf1 = [(i % n) + 1 for i in range(m)]
    daf2 = dict()
    for i in range(n):
        daf2[i + 1] = 0
    for v in daf1:
        if v in daf2:
            daf2[v] += 1
    # print(min(daf2.values()))
    pass
if __name__ == "__main__":
    main(10)