import sys

def ask(x, y, rev, A, B):
    if rev == 1:
        x, y = y, x
    # Original interactive behavior was: return sign(A^x - (B^y))
    ax = A ^ x
    by = B ^ y
    if ax > by:
        return 1
    elif ax < by:
        return -1

    else:
        return 0

def solve(A, B):
    comp = ask(0, 0, 0, A, B)
    nowa = 0
    nowb = 0
    rev = 0
    for i in range(29, -1, -1):
        if comp < 0:
            rev ^= 1
            nowa, nowb = nowb, nowa
            comp = -comp
        if comp >= 0:
            comp = ask(nowa | (1 << i), nowb | (1 << i), rev, A, B)
            if comp < 0:
                nowa |= 1 << i
                comp = ask(nowa, nowb, rev, A, B)

            else:
                tmp = ask(nowa | (1 << i), nowb, rev, A, B)
                if tmp < 0:
                    nowa |= 1 << i
                    nowb |= 1 << i
    if rev == 1:
        nowa, nowb = nowb, nowa
    return nowa, nowb

def main(n):
    # Input scale n controls the bit-length of A and B
    bits = max(1, n)
    # Deterministically generate A and B using simple arithmetic patterns
    # Limit to 30 bits because original algorithm loops 0..29
    bits = min(bits, 30)
    A = 0
    B = 0
    for i in range(bits):
        if i % 2 == 0:
            A |= (1 << i)
        if i % 3 == 0:
            B |= (1 << i)
    a_ans, b_ans = solve(A, B)
    # Final output of the reconstructed program
    # print("A", A)
    pass
    # print("B", B)
    pass
    # print("! %d %d" % (a_ans, b_ans))
    pass
if __name__ == "__main__":
    main(10)