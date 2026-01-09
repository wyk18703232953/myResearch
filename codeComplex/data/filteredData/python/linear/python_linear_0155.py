def main(n):
    # Define p deterministically based on n, ensure p != 0
    p = n + 1

    # Generate list1 deterministically with size n
    list1 = [(i * 2 + 3) for i in range(n)]

    mx = 0
    curr = 0
    nxt = sum(list1)
    for i in range(n - 1):
        curr += list1[i]
        nxt -= list1[i]
        mx = max(mx, curr % p + nxt % p)
    # print(mx)
    pass
if __name__ == "__main__":
    main(10)