import sys

def core_logic(n, a, b, l):
    c, d = {}, {}
    r = 0
    for _, x, y in l:
        i, j = a * x - y, (x, y)
        r += c.get(i, 0) - d.get(j, 0)
        c[i] = c.get(i, 0) + 1
        d[j] = d.get(j, 0) + 1
    return 2 * r

def generate_data(n):
    # Deterministically generate a, b, and list l of length n
    # a, b are non-zero integers depending on n
    a = n + 1
    b = n + 2
    # l is a list of triplets (id, x, y)
    # Use simple arithmetic patterns based on i and n
    l = [(i, i % (n + 3), (i * 2) % (n + 5)) for i in range(1, n + 1)]
    return a, b, l

def main(n):
    if n <= 0:
        print(0)
        return
    a, b, l = generate_data(n)
    result = core_logic(n, a, b, l)
    print(result)

if __name__ == "__main__":
    # Example deterministic call; change n as needed for experiments
    main(10)