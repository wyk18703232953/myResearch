def main(n):
    # Define k as a simple deterministic function of n
    k = max(1, n // 2)

    # Generate lst1: n distinct integers
    lst1 = [i for i in range(n)]

    # Generate lst2: k integers, overlapping with lst1 in a deterministic pattern
    # First half overlaps with lst1, second half are outside the range of lst1
    overlap = min(k, n)
    lst2 = [i for i in range(overlap)] + [n + i for i in range(k - overlap)]

    # Original core logic
    lst3 = {}
    ans = []
    for i in lst2:
        if i in lst1:
            lst3[i] = lst1.index(i)
    for i in sorted(lst3, key=lst3.get):
        ans.append(i)
    # print(*ans, sep=" ")
    pass
if __name__ == "__main__":
    main(10)