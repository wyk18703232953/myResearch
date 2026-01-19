from itertools import chain, combinations

def powerset(iterable):
    xs = list(iterable)
    return list(chain.from_iterable(combinations(xs, n) for n in range(2, len(xs) + 1)))

def main(n):
    if n < 2:
        print(0)
        return

    # Deterministic generation of parameters
    l = n
    r = 3 * n
    x = max(1, n // 3)

    # Deterministic generation of list "sett" of size n
    sett = [(i * 2 + 1) % (4 * n + 3) for i in range(n)]

    psett = powerset(sett)
    count = 0
    for subset in psett:
        k = sorted(subset)
        j = sum(k)
        if l <= j <= r and k[-1] - k[0] >= x:
            count += 1
    print(count)

if __name__ == "__main__":
    main(5)