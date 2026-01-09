def main(n):
    # Generate deterministic input of size n
    # Original structure:
    # n: integer
    # a: list of n integers
    # Here we generate a list whose behavior is deterministic for analysis.
    a = [(i % 5) + 1 for i in range(1, n + 1)]

    a.sort(reverse=True)

    cnt = 0
    while a:
        f = a.pop()
        rm = []
        for x in a:
            if x % f == 0:
                rm.append(x)
        for x in rm:
            a.remove(x)
        cnt += 1

    # print(cnt)
    pass
if __name__ == "__main__":
    main(1000)