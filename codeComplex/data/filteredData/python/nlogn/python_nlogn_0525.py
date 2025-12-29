import random

def solve_case(a):
    # Core logic from original code, for a single test case with array a
    if len(set(a)) == 1:
        v = a[0]
        return f"{v} {v} {v} {v}"
    a.sort()
    g1 = False
    d = {}
    mx = 10001
    for x in a:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
        if d[x] == 4:
            g1 = True
            if x < mx:
                mx = x
    if g1:
        return f"{mx} {mx} {mx} {mx}"
    else:
        res = []
        for k in d:
            if d[k] >= 2:
                res.append(k)
        m = len(res)
        minj = 0
        # assume m >= 2 for meaningful answer (test data should ensure this)
        for j in range(m - 1):
            if res[j] * res[j + 1] * (res[minj] ** 2 + res[minj + 1] ** 2) > \
               res[minj] * res[minj + 1] * (res[j] ** 2 + res[j + 1] ** 2):
                minj = j
        return f"{res[minj]} {res[minj]} {res[minj + 1]} {res[minj + 1]}"

def main(n):
    """
    n: problem size parameter, interpreted here as:
       - number of test cases t = n
       - each test has array length len_a = max(4, n) (ensures at least one rectangle)
       - elements are random integers between 1 and 10000
    The function prints the outputs for all test cases.
    """
    random.seed(0)
    t = n
    len_a = max(4, n)
    for _ in range(t):
        # Ensure that there is at least one value with frequency >= 4 or
        # at least two values with frequency >= 2, to make the logic meaningful.
        # Strategy: pick two base values and sprinkle remaining randomly.
        base1 = random.randint(1, 10000)
        base2 = random.randint(1, 10000)
        while base2 == base1:
            base2 = random.randint(1, 10000)

        # Guarantee at least two occurrences of base1 and base2
        a = [base1, base1, base2, base2]
        while len(a) < len_a:
            a.append(random.randint(1, 10000))
        random.shuffle(a)

        print(solve_case(a))

if __name__ == "__main__":
    main(5)