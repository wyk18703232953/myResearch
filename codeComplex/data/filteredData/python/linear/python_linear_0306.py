def main(n):
    # Deterministically generate input array of length n
    arr = [(i * 3 + 7) for i in range(n)]

    # Core logic from original program
    for i in range(n):
        arr[i] = (arr[i] - i) // n + (1 if (arr[i] - i) % n > 0 else 0)
    result = arr.index(min(arr)) + 1

    # print(result)
    pass
if __name__ == "__main__":
    main(10)