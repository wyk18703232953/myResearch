def main(n):
    # Interpret n as the size of both boy and girl arrays; set m = n
    if n <= 0:
        return

    m = n

    # Deterministic data generation
    # bmin: increasing sequence
    bmin = [i for i in range(1, n + 1)]
    # gmax: another increasing sequence offset by 2
    gmax = [i + 2 for i in range(1, n + 1)]

    bmin.sort()
    gmax.sort()

    max_boy = bmin[-1]
    min_girl = gmax[0]

    if max_boy > min_girl:
        out = -1
    elif max_boy == min_girl:
        bmin.pop()
        out = sum(gmax) + sum(x * m for x in bmin)

    else:
        bmin.pop()
        out = sum(gmax) - min_girl + max_boy
        out += min_girl + bmin[-1] * (m - 1)
        bmin.pop()
        out += sum(x * m for x in bmin)

    # print(out)
    pass
if __name__ == "__main__":
    main(10)