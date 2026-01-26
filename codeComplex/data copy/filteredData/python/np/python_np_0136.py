def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def run_algorithm(n, l, c):
    a = {0: 0}
    b = [0]
    for i in range(n):
        for p in b[:]:
            d = gcd(p, l[i])
            cost = a[p] + c[i]
            if d not in a:
                a[d] = cost
                b.append(d)
            elif a[d] > cost:
                a[d] = cost
    if 1 not in a:
        a[1] = -1
    return a[1]

def main(n):
    if n <= 0:
        print(-1)
        return
    l = [i + 2 for i in range(n)]
    c = [i % 5 + 1 for i in range(n)]
    result = run_algorithm(n, l, c)
    print(result)

if __name__ == "__main__":
    main(10)