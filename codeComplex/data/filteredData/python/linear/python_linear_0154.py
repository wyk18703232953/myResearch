def main(n):
    # Deterministic generation of p and list1 based on n
    if n <= 0:
        return 0
    p = n * 2 + 1
    list1 = [(i * 3 + 7) % p for i in range(n)]

    mx = 0
    curr = 0
    nxt = sum(list1)
    for i in range(n - 1):
        curr += list1[i]
        nxt -= list1[i]
        mx = max(mx, curr % p + nxt % p)
    # print(mx)
    pass
    return mx

if __name__ == "__main__":
    main(10)