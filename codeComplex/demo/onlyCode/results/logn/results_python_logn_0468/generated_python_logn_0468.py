def main(n):
    import random
    import sys
    max_bit = 30
    A = random.randint(0, (1 << max_bit) - 1)
    B = A ^ n

    def ask(x, y, rev):
        if rev == 1:
            return -((B - A) if True else 0)
        return (A - B) if True else 0

    comp = ask(0, 0, 0)
    nowa = 0
    nowb = 0
    rev = 0
    for i in range(29, -1, -1):
        if comp < 0:
            rev ^= 1
            nowa, nowb = nowb, nowa
            comp = -comp
        if comp >= 0:
            comp = ask(nowa | (1 << i), nowb | (1 << i), rev)
            if comp < 0:
                nowa |= 1 << i
                comp = ask(nowa, nowb, rev)
            else:
                tmp = ask(nowa | (1 << i), nowb, rev)
                if tmp < 0:
                    nowa |= 1 << i
                    nowb |= 1 << i
    if rev == 1:
        nowa, nowb = nowb, nowa
    print("! %d %d" % (nowa, nowb))
    return nowa, nowb

if __name__ == "__main__":
    main(10)