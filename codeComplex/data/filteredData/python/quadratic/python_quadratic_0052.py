def inv_cnt(b):
    c = 0
    visited = set()
    for i in range(len(b)):
        if i + 1 in visited:
            continue
        visited.add(i + 1)
        path = [i + 1]
        while b[path[-1] - 1] != path[0]:
            visited.add(b[path[-1] - 1])
            path.append(b[path[-1] - 1])
        c += len(path) - 1
    return c % 2


def solve(n):
    # n controls the size of the permutation and the number of queries
    if n <= 0:
        return
    # permutation of size n: a[i] = (i+1) % n + 1 (a single n-cycle for n>1)
    if n == 1:
        a = [1]

    else:
        a = [(i + 1) % n + 1 for i in range(n)]
    x = inv_cnt(a)
    # number of queries proportional to n
    m = n
    for q in range(1, m + 1):
        # deterministic query ranges depending on q and n
        l = (q * 2 - 1) % n + 1
        r = (q * 3) % n + 1
        if l > r:
            l, r = r, l
        x = (x + (r - l + 1) // 2) % 2
        if x:
            # print("odd")
            pass

        else:
            # print("even")
            pass


def main(n):
    solve(n)


if __name__ == "__main__":
    main(10)