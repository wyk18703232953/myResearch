def main(n):
    # Deterministically generate input list c of length n
    # Example pattern: c is made of repeated pairs [0,1,2,...,k-1,0,1,2,...]
    # ensuring enough duplicates for the algorithm to work similarly
    if n <= 0:
        # print(0)
        pass
        return

    # generate list with many duplicates
    base = max(1, n // 4)
    c = [(i % base) for i in range(n)]

    ans = 0
    # simulate original behavior; need a working copy since we pop
    c_work = c[:]
    # original loop uses range(n) but c is shrinking; stop when less than 2 left
    steps = min(n, len(c_work) // 2)
    for _ in range(steps):
        f = c_work.pop(0)
        g = c_work.index(f)
        c_work.pop(g)
        ans += g

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)