mod = int(1000000007)

def somaPa(nSteps):
    if nSteps == 0:
        return 0
    return (1 + nSteps) * nSteps / 2


def diminui(step):
    return (pow(2, step, mod) - 2) % mod


x, k = map(int, raw_input().split())

if x == 0:
    print(0)
else:
    pot = pow(2, k + 1, mod)
    inv = pow(2, mod - 2, mod)


    big = (x * pot) % mod
    small = (big - diminui(k + 1) ) % mod

    print(int((( ( (big + small) % mod)  * inv ) % mod)))


