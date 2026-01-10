def main(n):
    # Generate deterministic input array 'a' of length n
    # Example pattern: a[i] = i // 2 to introduce duplicates deterministically
    a = [i // 2 for i in range(n)]

    a.sort()
    lose = False
    pair = False
    for i in range(n - 1):
        if a[i] == a[i + 1] == 0:
            lose = True
        if a[i] == a[i + 1]:
            if pair:
                lose = True
            pair = True
            if i >= 1:
                if a[i] == a[i - 1] + 1:
                    lose = True
    if lose:
        print("cslnb")
    else:
        eventual = n * (n - 1) // 2
        curr = sum(a)
        if (curr - eventual) % 2 == 0:
            print("cslnb")
        else:
            print("sjfnb")


if __name__ == "__main__":
    main(10)