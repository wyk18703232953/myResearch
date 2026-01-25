def main(n):
    # n is both the array size and the target value to search for
    if n <= 0:
        return

    # Deterministically construct an array of length n that always contains n
    # First part: non-decreasing sequence ending at position n-1
    arr = [i for i in range(1, n + 1)]
    # Ensure the target value n is present
    if n not in arr:
        arr[-1] = n

    idx = arr.index(n)
    ok = 1
    for i in range(1, idx):
        if arr[i] < arr[i - 1]:
            ok = 0
    for i in reversed(range(idx, n - 1)):
        if arr[i] < arr[i + 1]:
            ok = 0
    if ok:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(10)