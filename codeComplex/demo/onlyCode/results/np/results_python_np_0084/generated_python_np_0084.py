def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

def n_choose_k(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def solve(diff, u):
    pluses = u + 1
    n = 2 ** u
    for i in range(unknown, -unknown - 1, -2):
        pluses -= 1
        if diff == i:
            k = n_choose_k(u, pluses)
            return k / n
    return 0

def main(n):
    global unknown
    s1 = '+' * n
    s2 = '+' * (n // 2) + '?' * (n - n // 2)
    k = 0
    correct_p = 0
    pred_p = 0
    unknown = 0
    for c in s1:
        correct_p += 1 if c == '+' else -1
    for c in s2:
        if c in '+-':
            pred_p += 1 if c == '+' else -1
        else:
            unknown += 1
    p = 1 if unknown == 0 and correct_p == pred_p else solve(correct_p - pred_p, unknown)
    print('{0:.9f}'.format(p))
    return p

if __name__ == "__main__":
    main(10)