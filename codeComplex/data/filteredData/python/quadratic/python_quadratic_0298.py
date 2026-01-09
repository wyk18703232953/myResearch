def main(n):
    # Generate deterministic list of integers of length n
    # Pattern: lst[i] = i % (max(1, n//3)) ensures duplicates for index() usage
    if n <= 0:
        # print(0)
        pass
        return

    base = max(1, n // 3)
    lst = [i % base for i in range(n)]

    c = 0
    while len(lst) != 0:
        p = lst[0]
        del lst[0]
        i = lst.index(p)
        c += i
        del lst[i]
    # print(c)
    pass
if __name__ == "__main__":
    main(10)