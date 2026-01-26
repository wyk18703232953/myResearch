def main(n):
    # n controls the length of the sequence of c values
    a = [0 for _ in range(256)]

    # deterministically define k based on n, keeping it in a safe range
    # ensure 1 <= k <= 128
    k = (n % 128) + 1

    # deterministically generate a list of c values in [0, 255]
    # use simple modular arithmetic; avoid out-of-bounds for a
    c_values = [(i * 37 + 11) % 256 for i in range(n)]

    output_parts = []
    for c in c_values:
        if a[c] != 0:
            output_parts.append(str(a[c] - 1))

        else:
            for x in range(c, c - k, -1):
                if x < 0:
                    break
                if a[x] == 0:
                    i = x

                else:
                    if c - a[x] + 1 < k:
                        i = a[x] - 1
                    break
                if x == 0:
                    break
            for x in range(int(i), c + 1):
                a[x] = i + 1
            output_parts.append(str(i))

    # print(" ".join(output_parts))
    pass
if __name__ == "__main__":
    main(10)