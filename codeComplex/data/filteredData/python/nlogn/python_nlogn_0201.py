def check(k, b, T):
    c = [e for e in b if e[0] >= k]

    if len(c) < k:
        return False, None

    first_k_probs = c[:k]
    s = sum(e[1] for e in first_k_probs)

    if s > T:
        return False, None

    return True, first_k_probs


def solve(n, T, a, t):
    b = []

    for i in range(n):
        b.append((a[i], t[i], i + 1))

    b.sort(key=lambda x: x[1])

    low, high = 0, n
    result = 0
    final_probs = []

    while low <= high:
        mid = (low + high) // 2

        possible, probs = check(mid, b, T)
        if possible:
            result, final_probs = mid, probs
            low = mid + 1

        else:
            high = mid - 1

    return result, [e[2] for e in final_probs]


def main(n):
    if n <= 0:
        return

    T = 2 * n * n

    a = [(i % n) + 1 for i in range(1, n + 1)]
    t = [((i * 3) % (2 * n)) + 1 for i in range(1, n + 1)]

    point, probs = solve(n, T, a, t)
    # print(point)
    pass
    # print(len(probs))
    pass

    if len(probs) > 0:
        # print(" ".join(str(x) for x in probs))
        pass
if __name__ == "__main__":
    main(10)