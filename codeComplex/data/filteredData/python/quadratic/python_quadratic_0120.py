def main(n):
    # Deterministically generate 'useless' based on n
    useless = n // 2

    # Generate array 'arr' of length n deterministically
    # Example pattern: arr[i] = (i % (n // 3 + 1)) + 1 to create repetitions
    if n <= 0:
        # print(0)
        pass
        return

    mod_base = n // 3 + 1
    arr = [(i % mod_base) + 1 for i in range(n)]

    for x in range(1, n + 1):
        if x not in arr:
            # print(0)
            pass
            break

    else:
        # print(arr.count(min(arr, key=lambda x: arr.count(x))))
        pass
if __name__ == "__main__":
    main(10)