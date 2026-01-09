def main(n):
    # Interpret n as the initial value of the original variable n, m is unused
    m = n  # kept for structural similarity, though not used

    a = []
    b = []
    cur = n
    while cur >= 0:
        a.append(4)
        cur -= 4
        b.append(5)

    a.append(5)
    b.append(5)

    # print(*a, sep="")
    pass
    # print(*b, sep="")
    pass
if __name__ == "__main__":
    main(10)