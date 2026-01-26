def ask(x, y, rev, a, b):
    if rev == 1:
        x, y = y, x
    # Simulate the judge: returns sign of (a^x) - (b^y)
    val = (a ^ x) - (b ^ y)
    if rev == 1:
        return -int(val)

    else:
        return int(val)

def main(n):
    # Interpret n as bit-length of hidden integers a and b (up to 30 as in original code)
    max_bits = 30
    bits = min(max_bits, max(1, n))

    # Deterministically construct hidden a and b using simple patterns
    # Example: a has 1s at even bit positions < bits, b has 1s at odd bit positions < bits
    a = 0
    b = 0
    for i in range(bits):
        if i % 2 == 0:
            a |= (1 << i)

        else:
            b |= (1 << i)

    comp = ask(0, 0, 0, a, b)
    nowa = 0
    nowb = 0
    rev = 0
    for i in range(29, -1, -1):
        if comp < 0:
            rev ^= 1
            nowa, nowb = nowb, nowa
            comp = -comp
        if comp >= 0:
            comp = ask(nowa | (1 << i), nowb | (1 << i), rev, a, b)
            if comp < 0:
                nowa |= 1 << i
                comp = ask(nowa, nowb, rev, a, b)

            else:
                tmp = ask(nowa | (1 << i), nowb, rev, a, b)
                if tmp < 0:
                    nowa |= 1 << i
                    nowb |= 1 << i
    if rev == 1:
        nowa, nowb = nowb, nowa

    # Output the reconstructed values and the hidden values for verification
    # print(nowa, nowb, a, b)
    pass
if __name__ == "__main__":
    main(10)