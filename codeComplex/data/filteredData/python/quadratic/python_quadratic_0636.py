def main(n):
    # Generate deterministic test data of size n
    # Original program expects:
    #   first line: n
    #   second line: n integers (arr)
    # We deterministically construct arr based on n.
    # Example pattern: arr[i] = i % 7 + 1, ensuring positive integers.
    arr = [(i % 7) + 1 for i in range(n)]

    arr.sort()
    tmp = [-1] * n
    c = 1
    for i in range(n):
        if tmp[i] != -1:
            continue
        x = arr[i]
        for j in range(i, n):
            if arr[j] % x == 0:
                tmp[j] = c
        c += 1

    # print(c - 1)
    pass
if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)