reduced = 1

def algorithm(n, m, k, p):
    reduced = 1
    p = list(p)
    p.reverse()
    cnt = 0
    while len(p):
        cnt1 = 1
        first = p.pop()
        fack = ((first - reduced) // k) * k
        while len(p) and p[-1] - fack - reduced < k:
            cnt1 += 1
            p.pop()
        reduced += cnt1
        cnt += 1
    return cnt

def generate_input(n):
    if n <= 0:
        n = 1
    m = max(1, n * 3)
    k = max(1, n // 2 + 1)
    p = [i * 2 + (i // 3) for i in range(1, m + 1)]
    return n, m, k, p

def main(n):
    n_val, m, k, p = generate_input(n)
    result = algorithm(n_val, m, k, p)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)