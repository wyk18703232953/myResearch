def main(n):
    # Deterministically generate input array 'a' of length n
    # Example pattern: a[i] = i // 2 to create some duplicates and structure
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
        # print("cslnb")
        pass

    else:
        eventual = n * (n - 1) // 2
        curr = sum(a)
        if (curr - eventual) % 2 == 0:
            # print("cslnb")
            pass

        else:
            # print("sjfnb")
            pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)