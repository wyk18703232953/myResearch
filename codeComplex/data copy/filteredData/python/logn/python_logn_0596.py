def main(n):
    # Deterministically map n to original (n, k)
    # Ensure k is within a reasonable range related to n
    k = (n * (n + 1) // 4) % (n * (n + 1) // 2 + 1)

    low = 1
    high = n
    result = None

    while low <= high:
        mid = (low + high) // 2
        val = mid * (mid + 1) // 2 - (n - mid)
        if val > k:
            high = mid - 1
        elif val == k:
            result = n - mid
            break

        else:
            low = mid + 1

    # For time-complexity experiments, always produce some output
    # If no exact match found, output -1
    if result is None:
        result = -1
    # print(result)
    pass
if __name__ == "__main__":
    # Example scalable call; adjust n as needed for experiments
    main(10**5)