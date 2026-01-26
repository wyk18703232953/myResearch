def main(n):
    # Deterministic data generation for a and b based on n
    # a_str: ascending digits cycling 1-9, length n
    a = [str((i % 9) + 1) for i in range(n)]
    # b_str: descending digits cycling 9-1, length n
    b = [str(9 - (i % 9)) for i in range(n)]

    n_local = len(a)
    a.sort()

    def listtostring(li: list):
        return ''.join(li)

    for i in range(0, n_local):
        for j in range(0, n_local):
            t = a.copy()
            t[i], t[j] = t[j], t[i]
            if (int(listtostring(t)) >= int(listtostring(a))) and (int(listtostring(t)) <= int(listtostring(b))):
                a[i], a[j] = a[j], a[i]

    # print(listtostring(a))
    pass
if __name__ == "__main__":
    main(5)