def main(n):
    # Deterministically generate initial list a of length n
    a = ["str_" + str(i % (n // 2 + 1)) for i in range(n)]
    # Generate n query strings t; some will match elements in a
    ts = ["str_" + str((i * 2) % (n // 2 + 1)) for i in range(n)]

    # Core logic from original program
    for t in ts:
        if t in a:
            a.remove(t)
    # print(len(a))
    pass
if __name__ == "__main__":
    main(10)