import math
EPS = 1e-6

hhh = None

def out_of_solution_bounds(n, M):
    return M < 2 * n - 1 or (n * (n + 1)) // 2 < M

def get_min_H_given_b(n, b):
    if b == 1:
        return (n * (n + 1)) // 2
    m = math.floor(math.log((b - 1) * n + 1) / math.log(b) + EPS)
    nl = round((b ** m - 1) / (b - 1))
    return (m * b ** (m + 1) - (m + 1) * b ** m + 1) // (b - 1) ** 2 + (m + 1) * (n - nl)

def find_optimal_b(n, M):
    begin = 1
    end = n
    while begin != end:
        mid = (begin + end) // 2
        if get_min_H_given_b(n, mid) <= M:
            end = mid

        else:
            begin = mid + 1
    b = end
    return b

def uniform_height_distribution(n, b):
    h = [0 for _ in range(n)]
    h[0] = 1
    i = 0
    to_fill = n - 1
    while to_fill > 0:
        i += 1
        h[i] = min(b * h[i - 1], to_fill)
        to_fill -= h[i]
    return h

def locally_increase_H(h, M, b):
    i = 1
    while not (b * (h[i - 1]) >= (h[i] - 1) and b * (h[i] - 1) >= (h[i + 1] + 1)):
        i += 1

    H = sum(i * x for i, x in enumerate(h, 1))
    while H < M:
        if b * (h[i - 1] - 1) >= (h[i] + 1):
            i -= 1

        else:
            while not b * (h[i] - 1) >= (h[i + 1] + 1):
                i += 1
        h[i] -= 1
        h[i + 1] += 1
        H += 1

    return h

def fast_find_optimal_height_distribution(n, M, b):
    begin = 0
    end = n + 1
    H_fn = lambda L: (L * (L + 1)) // 2 + get_min_H_given_b(n - L, b) + (L > 0) * (n - L)

    while begin != end:
        mid = (begin + end) // 2
        if H_fn(mid) <= M:
            begin = mid + 1

        else:
            end = mid
    L = begin - 1

    if L == n:
        return [1 for _ in range(n)]

    unif_branch_h = uniform_height_distribution(n - L, b)
    if L == 0:
        h = unif_branch_h

    else:
        h = [int(i < L) for i in range(n)]
        for i, x in enumerate(unif_branch_h, 1):
            h[i] += x

    return locally_increase_H(h, M, b)

def build_tree(n, b, h):
    p = [None for _ in range(n)]
    p[0] = 1

    i = 1
    j = 0
    for k in range(1, n):
        if j == h[i]:
            i += 1
            j = 0
        p[k] = k - j - h[i - 1] + (j // b) + 1
        j += 1
    return p

def solve_for_instance(n, M):
    if out_of_solution_bounds(n, M):
        return 'No', []
    b = find_optimal_b(n, M)
    heights = fast_find_optimal_height_distribution(n, M, b)
    parents = build_tree(n, b, heights)
    return 'Yes', parents[1:]

def main(n):
    results = []
    # Define M deterministically from n; use a range of M around the lower bound
    for k in range(1, n + 1):
        nn = n
        base_M = 2 * nn - 1
        extra = k % max(1, nn)
        M = base_M + extra
        status, parents = solve_for_instance(nn, M)
        results.append((nn, M, status, parents))
    # Simple deterministic output for experiments
    for nn, M, status, parents in results:
        # print(nn, M, status, *parents)
        pass
if __name__ == "__main__":
    main(10)