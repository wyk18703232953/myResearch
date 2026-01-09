def main(n):
    # Interpret n as the size of the arrays and window k = max(1, n//2)
    if n <= 0:
        return
    k = max(1, n // 2)

    # Deterministic generation of arr1 and arr2
    # arr1: increasing sequence with some variation
    arr1 = [(i * 3 + 7) % 1000 for i in range(n)]
    # arr2: pattern of 0 and 1 based on index
    arr2 = [1 if (i % 3 == 0) else 0 for i in range(n)]

    ans = 0
    new_arr = [0] * n

    for i in range(n):
        if arr2[i] == 0:
            new_arr[i] = arr1[i]

        else:
            ans += arr1[i]

    k = min(k, n)
    total = sum(new_arr[:k])
    mx = total

    j = 0
    for i in range(k, n):
        total -= new_arr[j]
        total += new_arr[i]
        if total > mx:
            mx = total
        j += 1

    # print(mx + ans)
    pass
if __name__ == "__main__":
    main(10)