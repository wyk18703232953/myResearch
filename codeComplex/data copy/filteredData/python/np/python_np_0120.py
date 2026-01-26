import os

def main(n):
    # n: number of input integers
    # Deterministically generate input integers.
    # Example scheme: x_i = i ^ (i << 1)
    numbs = [n]
    numbs.extend(i ^ (i << 1) for i in range(n))

    n_val = numbs.pop(0)

    base = []
    out = []

    for i in range(n_val):
        x = numbs[i]
        how = 0

        for b, rep in base:
            if x.bit_length() == b.bit_length():
                x ^= b
                how ^= rep

        if x:
            how |= 1 << i

            a = 0
            b_len = len(base)
            while a < b_len:
                c = a + b_len >> 1
                if base[c][0] > x:
                    a = c + 1
                else:
                    b_len = c
            base.insert(a, (x, how))

            out.append(0)
        else:
            outind = len(out)
            out.append(-1)

            y = bin(how).encode('ascii')
            ylen = len(y)
            for j in range(2, len(y)):
                if y[j] == 49:  # ord('1') == 49
                    out.append(ylen - 1 - j)
            out[outind] = len(out) - 1 - outind

    os.write(1, b'\n'.join(str(x).encode('ascii') for x in out))


if __name__ == "__main__":
    # Example: run with a chosen n for experimentation
    main(10)