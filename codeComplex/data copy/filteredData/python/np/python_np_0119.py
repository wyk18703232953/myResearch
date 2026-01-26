import os

def generate_input(n):
    # n is the number of elements (original n)
    # First number is n itself, followed by n integers
    # Deterministic pattern: a simple arithmetic sequence with bit-mixed values
    nums = [n]
    for i in range(n):
        # Construct some varied integers using only deterministic arithmetic/bit ops
        val = (i * 37) ^ (i << 3) ^ (i >> 1)
        nums.append(val)
    return nums

def core_algorithm(numbs):
    n = numbs.pop(0)

    base = []
    out = []

    for i in range(n):
        x = numbs[i]
        how = 0

        for b, rep in base:
            if x.bit_length() == b.bit_length():
                x ^= b
                how ^= rep

        if x:
            how |= 1 << i

            a = 0
            b = len(base)
            while a < b:
                c = a + b >> 1
                if base[c][0] > x:
                    a = c + 1
                else:
                    b = c
            base.insert(a, (x, how))

            out.append(0)
        else:
            outind = len(out)
            out.append(-1)

            y = bin(how).encode('ascii')
            ylen = len(y)
            for i in range(2, len(y)):
                if y[i] == 49:
                    out.append(ylen - 1 - i)
            out[outind] = len(out) - 1 - outind

    return out

def main(n):
    numbs = generate_input(n)
    out = core_algorithm(numbs)
    os.write(1, b'\n'.join(str(x).encode('ascii') for x in out))

if __name__ == "__main__":
    # Example: run with a fixed size for reproducible experiment
    main(10)