def main(n):
    # n represents the size of input list
    # generate a deterministic list of integers based on n
    a = [(i // 2) % max(1, (n // 3) + 1) for i in range(n)]
    r = 0
    a = a[:]  # work on a copy
    while a:
        c = a[0]
        del a[0]
        # find first index with same value as c
        for i in range(len(a)):
            if c == a[i]:
                break
        # if not found, i will be len(a)-1 due to loop structure;
        # but original code assumes at least one equal element exists.
        # to preserve behavior, ensure there is at least one element.
        if i >= len(a):
            i = len(a) - 1
        del a[i]
        r += i
    # print(r)
    pass
if __name__ == "__main__":
    # example call; you can change n for different scales
    main(10)