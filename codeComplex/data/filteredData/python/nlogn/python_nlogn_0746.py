def main(n):
    # Deterministically generate input of size n
    # Original expects: integer n and an array arr of length n
    # We map n -> length of arr
    arr = [(i // 2) for i in range(n)]  # deterministic pattern, includes duplicates in a controlled way

    tmp = 0
    for i in range(len(arr)):
        tmp += (arr[i] - i)

    arr.sort()
    c = 0
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            c += 1
        if i != 1 and arr[i] == arr[i - 1] and arr[i - 1] == arr[i - 2] + 1:
            print("cslnb")
            return

    if c > 1 or (len(arr) >= 2 and arr[0] == arr[1] == 0):
        print("cslnb")
        return

    print("cslnb" if tmp % 2 == 0 else "sjfnb")


if __name__ == "__main__":
    # example deterministic call; adjust n for different scales
    main(10)