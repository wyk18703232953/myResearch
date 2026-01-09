def main(n):
    # Interpret n as the size of arr1 and arr2
    m = n

    # Deterministically generate arr1 and arr2
    # arr1: [0, 1, 2, ..., n-1]
    arr1 = list(range(n))
    # arr2: [n//2, n//2+1, ..., n-1, 0, 1, ..., n//2-1]
    arr2 = list(range(n // 2, n)) + list(range(0, n // 2))

    # Core logic preserved
    result = sorted([x for x in arr2 if x in arr1], key=lambda k: arr1.index(k))
    if result:
        # print(*result)
        pass

    else:
        # print()
        pass
if __name__ == "__main__":
    main(10)