from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def main(n):
    # n controls the size of the list
    if n <= 0:
        print(0)
        return

    # Deterministic generation of parameters and list
    l = n
    r = 3 * n
    x = max(1, n // 3)

    # Generate list of length n with deterministic values
    ll = [(i * 2 + 1) for i in range(n)]

    subsets = powerset(ll)
    res = 0
    for subset in subsets:
        if len(subset) >= 2 and l <= sum(subset) <= r and max(subset) - min(subset) >= x:
            res += 1
    print(res)

if __name__ == "__main__":
    main(10)