import math


def generate_queries(n):
    queries = []
    if n <= 0:
        return queries
    for i in range(1, n + 1):
        k = i
        s = ''.join('RGB'[(j + i) % 3] for j in range(k + (i % 5)))
        queries.append((len(s), k, s))
    return queries


def solve_single(n, k, s):
    sf = 'RGB' * (k + 2)
    max_s = 0
    for i in range(n - k + 1):
        for j in range(3):
            count = 0
            for b in range(k):
                if sf[j + b] == s[i + b]:
                    count += 1
            if count > max_s:
                max_s = count
    return k - max_s


def main(n):
    queries = generate_queries(n)
    results = []
    for n_i, k_i, s_i in queries:
        res = solve_single(n_i, k_i, s_i)
        results.append(res)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(5)