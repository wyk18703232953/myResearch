from collections import Counter

def solve(n, ribbons):
    L = len(ribbons[0])
    a = [Counter(r).most_common(1)[0][1] for r in ribbons]

    r = sorted([(x, i) for i, x in enumerate(a)], reverse=True)

    if n == 1:
        c = Counter(a)
        if c[L - 1] == 1:
            for i in range(3):
                if a[i] == L - 1:
                    return i
        if c[L - 1] > 1:
            return 3
        if c[L] + c[L - 2] == 1:
            for i in range(3):
                if a[i] == L or a[i] == L - 2:
                    return i
        if c[L] + c[L - 2] > 1:
            return 3

    if r[1][0] == r[0][0]:
        return 3
    if r[1][0] + n >= L:
        return 3
    return r[0][1]


def generate_ribbons(L):
    # deterministic generation of 3 ribbons of length L over 'K','S','T'
    chars = ['K', 'S', 'T']
    ribbons = []
    for j in range(3):
        s = []
        for i in range(L):
            s.append(chars[(i + j) % 3])
        ribbons.append(''.join(s))
    return ribbons


def main(n):
    # interpret n as the length of each ribbon; ensure minimum length 1
    L = max(1, n)
    ribbons = generate_ribbons(L)

    # use n as original parameter n as well; if original problem expects n>=1
    param_n = max(1, n)

    cats = ('Kuro', 'Shiro', 'Katie', 'Draw')
    k = solve(param_n, ribbons)
    # return instead of print to make it suitable for experiments
    return cats[k]


if __name__ == "__main__":
    # example deterministic call
    result = main(10)
    # print(result)
    pass