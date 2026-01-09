def main(n):
    # Interpret n as the length of both l1 and l2
    m = n

    # Deterministic generation of l1 and l2
    l1 = [i for i in range(n)]
    l2 = [(i * 2) % (n + 1) for i in range(m)]

    # Core logic from original code
    l3 = []
    for i in range(n):
        for j in range(m):
            if l1[i] == l2[j]:
                if l1[i] is not l3:
                    l3.append(l1[i])

    # Output
    if l3:
        # print(*l3)
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(10)