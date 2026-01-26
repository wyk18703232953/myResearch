import math


def solve_naive(n, k):
    taken = set()
    current_cap = 0
    found = False
    while current_cap != n:
        for c in range(k, 1, -1):
            found = False
            if current_cap == 0:
                if c <= n:
                    current_cap += c
                    taken.add(c)
                    found = True
                    break

            else:
                if c not in taken and c - 1 <= n - current_cap:
                    current_cap += c - 1
                    taken.add(c)
                    found = True
                    break
        if not found:
            break
    return len(taken) if found else -1


def solve(n, k):
    if n == 1:
        return 0
    if k >= n:
        return 1

    else:
        if (3 - 2 * k) ** 2 - 8 * (n - k) < 0:
            return -1
        t = (-math.sqrt((3 - 2 * k) ** 2 - 8 * (n - k)) + (2 * k) - 3) / 2
        if t == 0.0:
            return 2
        if t % 1 == 0:
            return 1 + int(t)

        else:
            return 2 + int(t)


def main(n):
    results = []
    for i in range(1, n + 1):
        cur_n = i
        cur_k = i // 2 + 1
        res = solve(cur_n, cur_k)
        results.append(res)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)