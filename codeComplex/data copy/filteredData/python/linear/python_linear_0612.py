def main(n):
    # deterministic input generation
    a = list(range(1, n + 1))
    b = [((i * 2) % n) + 1 for i in range(n)]

    ha = {}
    for i in range(n):
        ha[a[i]] = i
    removed = 0
    out = ""
    for i in range(n):
        if ha[b[i]] < removed:
            out += "0 "

        else:
            out += str(ha[b[i]] - removed + 1) + " "
            removed = ha[b[i]] + 1
    # print(out[:-1])
    pass
if __name__ == "__main__":
    main(10)