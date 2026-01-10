def main(n):
    # Deterministically generate permutation p of size n
    # Example: p[i] = (i + 1) % n (a single n-cycle)
    p = [ (i + 1) % n for i in range(n) ]

    visited = [False] * n
    loops = []

    for x in range(n):
        if not visited[x]:
            visited[x] = True
            start = x
            l = [x]
            cur = p[x]
            while cur != start:
                visited[cur] = True
                l.append(cur)
                cur = p[cur]
            loops.append(len(l) - 1)

    tot = sum(loops)

    if n % 2 == 1:
        if tot % 2 == 1:
            print('Petr')
        else:
            print('Um_nik')
    else:
        if tot % 2 == 0:
            print('Petr')
        else:
            print('Um_nik')


if __name__ == "__main__":
    main(10)