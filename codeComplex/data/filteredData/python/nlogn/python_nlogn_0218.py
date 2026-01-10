def main(n):
    # Interpret n as the length of arr
    # Deterministically generate arr and u
    if n < 2:
        print(-1)
        return

    # Example deterministic construction:
    # arr is a non-decreasing sequence with some repeated and spaced values
    arr = [i * (i % 3 + 1) for i in range(n)]
    # Ensure there is some spread; choose u relative to n
    u = max(1, n // 3)

    j, i = 1, 0
    maxi = -1
    flag = 0
    for i in range(n - 1):
        if arr[i + 1] - arr[i] <= u:
            flag = 1
    if flag == 0:
        print("-1")
        return
    i = 0
    while i < n - 2:
        while 1:
            if j >= n:
                j = n - 1
                break
            if arr[j] - arr[i] > u:
                j -= 1
                break
            j += 1
        if i == j:
            j += 1
        elif arr[j] == arr[i]:
            pass
        elif arr[j] - arr[i] <= u:
            maxi = max(maxi, (arr[j] - arr[i + 1]) / (arr[j] - arr[i]))
        i += 1
    if maxi == 0:
        print("-1")
    else:
        print(maxi)


if __name__ == "__main__":
    main(10)