def main(n):
    # Deterministic data generation: original code expects:
    # n: number of elements
    # b: list of n integers
    # Here we define b as a simple arithmetic sequence based on n
    b = [(i * 2 + 1) for i in range(n)]  # odd numbers: 1,3,5,...

    ff = []
    ss = []
    for i in b[::-1]:
        q = i
        f = q // 2
        if q % 2:
            s = f + 1

        else:
            s = f
        if len(ff) == 0:
            ff = [f]
            ss = [s]

        else:
            if f > ff[-1] or s < ss[-1]:
                d = max(f - ff[-1], ss[-1] - s)
                f -= d
                s += d
            ff.append(f)
            ss.append(s)
    # print(*(ff[::-1] + ss))
    pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(5)