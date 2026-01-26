def suma_o_resta(a, b):
    return (a & (1 << b))

def diferencia(s1, d):
    if s1:
        s1.sort()
        if s1[-1] - s1[0] >= d:
            return s1
        else:
            s1.pop()
            return diferencia(s1, d)
    return s1

def no_sets(v, n, l, r, d):
    s = []
    cont = 0
    for x in range(1 << n):
        for i in range(n):
            if suma_o_resta(x, i) > 0:
                s.append(v[i])
        s = diferencia(s, d)
        if s:
            ssum = sum(s)
            if l <= ssum <= r:
                cont += 1
        s = []
    return cont

def generate_inputs(n):
    if n <= 0:
        return 0, 0, 0, 0, []
    # n is the number of elements
    # l, r, x are generated deterministically from n
    l = n
    r = 3 * n
    x = max(1, n // 3)
    v = [i * 2 + (i % 3) for i in range(n)]
    return n, l, r, x, v

def main(n):
    n, l, r, x, v = generate_inputs(n)
    result = no_sets(v, n, l, r, x)
    print(result)

if __name__ == "__main__":
    main(5)