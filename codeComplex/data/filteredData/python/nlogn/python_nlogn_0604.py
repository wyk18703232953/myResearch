def main(n):
    # Interpret n as the size of the array
    # Construct deterministic m and arr based on n
    m = n  # original code reads n, m but uses only n and arr; we link them deterministically

    # Generate a deterministic array of length n with positive integers
    # Pattern: arr[i] = (i % 7) + 1 to avoid zeros
    arr = [(i % 7) + 1 for i in range(n)]

    # Core logic from original program (with generated n, m, arr)
    arr = sorted(arr, reverse=True)
    arr.append(0)
    isum = sum(arr)
    ans = []
    top = arr[0]
    for i in range(n):
        if arr[i] == 1:
            ans.append(1)
            arr[i + 1] = 1
            continue
        if arr[i + 1] > arr[i]:
            arr[i + 1] = arr[i]
        if arr[i] - arr[i + 1] == 0:
            ans.append(1)
            h = 1

        else:
            ans.append(arr[i] - arr[i + 1])
            h = arr[i] - arr[i + 1]

        top = arr[i] - h
        arr[i + 1] = top

    # print(isum - sum(ans))
    pass
if __name__ == "__main__":
    # Example deterministic call
    main(10)