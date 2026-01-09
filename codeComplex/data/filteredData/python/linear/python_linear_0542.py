def main(n):
    # n: length of the array
    if n <= 0:
        return

    # Deterministic data generation
    # Example: mix of negative and positive values
    arr = [((i * 3) // 2) - n for i in range(n)]

    k = min(arr)
    h = max(arr)
    s = 0
    for i in arr:
        if i >= 0:
            s += i

        else:
            s -= i

    if n == 1:
        # print(arr[0])
        pass
    elif (k < 0 and h >= 0):
        # print(s)
        pass

    else:
        if k >= 0:
            # print(s - 2 * k)
            pass

        else:
            # print(s + 2 * h)
            pass
if __name__ == "__main__":
    main(10)