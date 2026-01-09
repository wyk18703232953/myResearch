def main(n):
    # Deterministically generate arrays based on n
    # arr will be a permutation of 1..n
    # brr will be a sequence of length n with values in 1..n (cyclic pattern)
    arr = [i for i in range(1, n + 1)]
    # For some structure, reverse second half
    if n > 1:
        mid = n // 2
        arr[mid:] = reversed(arr[mid:])

    brr = [(i % n) + 1 for i in range(n)]

    numb = [0 for _ in range(n + 1)]
    for i in range(len(arr)):
        numb[arr[i]] = i + 1

    ind = 0
    outputs = []
    for c in brr:
        total = 0
        num = numb[c]
        if num > ind:
            total = num - ind
            ind = num
        outputs.append(str(total))

    # print(" ".join(outputs))
    pass
if __name__ == "__main__":
    main(10)