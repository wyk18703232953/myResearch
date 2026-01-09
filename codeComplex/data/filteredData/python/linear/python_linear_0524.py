def main(n):
    # Ensure n >= 2 for a tree-like structure
    if n < 2:
        n = 2

    d = {}

    # Deterministic generation of a tree: a simple chain 1-2-3-...-n
    for i in range(1, n):
        a = i
        b = i + 1
        if a in d:
            d[a].append(b)

        else:
            d[a] = [b]
        if b in d:
            d[b].append(a)

        else:
            d[b] = [a]

    # Deterministic generation of array of length n
    # Example: a permutation pattern depending on n
    # First element is always 1 to exercise the main branch
    array = [1] + [((i * 2) % n) + 1 for i in range(1, n)]

    flag = 0

    if array[0] == 1:
        i = 1
        j = 0

        while j < n and i < n:
            if array[i] in d.get(array[j], []):
                i += 1

            else:
                j += 1

        if j == n and i != n:
            flag = 1

    else:
        flag = 1

    if flag == 1:
        # print("No")
        pass

    else:
        # print("Yes")
        pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)