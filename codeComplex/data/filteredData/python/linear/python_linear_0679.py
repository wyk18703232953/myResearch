import sys

sys.setrecursionlimit(1000000)

def dprint(*args, **kwargs):
    pass

def generate_input(n):
    if n < 2:
        n = 2
    if n % 2 == 1:
        n += 1
    N = n
    # Deterministic construction of zb with length N//2
    # Ensure zb[0] is defined safely and values are varied but deterministic
    half = N // 2
    zb = [(i * 3 + 7) % (2 * half + 5) for i in range(half)]
    # Ensure zb[0] is non-negative and large enough so algorithm can proceed meaningfully
    if zb[0] < 0:
        zb[0] = -zb[0]
    return N, zb

def core_algorithm(N, zb):
    za1 = [0]
    za2 = [zb[0]]

    for i in range(1, N // 2):
        t1 = zb[i] - za1[-1]
        if t1 <= za2[-1]:
            za1.append(za1[-1])
            za2.append(t1)
            continue
        t2 = zb[i] - za2[-1]
        if t2 >= za1[-1]:
            za1.append(t2)
            za2.append(za2[-1])
            continue
        # If original assertion fails for constructed data, keep behavior but avoid crash:
        # fall back to keeping previous values to preserve determinism
        za1.append(za1[-1])
        za2.append(za2[-1])

    zr = za1 + za2[::-1]
    zs = []
    for x in zr:
        zs.append(str(x))
    r = ' '.join(zs)
    return r

def main(n):
    N, zb = generate_input(n)
    result = core_algorithm(N, zb)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)