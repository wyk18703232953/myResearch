def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main(n):
    n = max(1, int(n))
    l = [i + 1 for i in range(n)]
    c = [i % 5 + 1 for i in range(n)]

    a = {0: 0}
    for i in range(n):
        b = a.copy()
        for g, cost_now in a.items():
            d = gcd(g, l[i])
            cost = cost_now + c[i]
            if d not in b or b[d] > cost:
                b[d] = cost
        a = b.copy()

    if 1 not in a:
        a[1] = -1
    print(a[1])

if __name__ == "__main__":
    main(10)