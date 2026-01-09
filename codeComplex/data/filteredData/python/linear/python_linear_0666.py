def main(n):
    # n: input size
    # Generate deterministic data:
    # a: list of n integers
    # b: string of length n over {'W','G','L'}
    a = [(i % 7) + 1 for i in range(n)]
    chars = ['W', 'G', 'L']
    b_list = [chars[i % 3] for i in range(n)]
    b = ''.join(b_list)

    sol = 0
    e = 0
    big = 0
    g = 0
    for i in range(n):
        if b[i] == "W":
            big = 1
            sol += 3 * a[i]
            e += a[i]
        if b[i] == "G":
            sol += 5 * a[i]
            e += a[i]
            g += 2 * a[i]
        if b[i] == "L":
            sol += a[i]
            e -= a[i]
            if e < 0:
                if big:
                    sol -= 3 * e

                else:
                    sol -= 5 * e
                e = 0
        g = min(e, g)
    if e:
        sol -= 2 * g
        sol -= (e - g)
    return int(sol)


if __name__ == "__main__":
    # example deterministic call for scale n
    # print(main(10))
    pass