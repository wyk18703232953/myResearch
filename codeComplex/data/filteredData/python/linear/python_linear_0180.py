def main(n):
    # Interpret n as the length of the arrays; choose k as a deterministic function of n
    if n <= 0:
        return 0

    # Deterministic choice of k: about 1/3 of n, at least 1 and at most n
    k = max(1, min(n, n // 3 if n // 3 > 0 else 1))

    # Deterministic data generation based on n
    # arr1: simple increasing sequence with a wrap pattern
    arr1 = [(i * 2 + 1) % 1000 for i in range(n)]
    # arr2: pattern of 0s and 1s
    arr2 = [i % 2 for i in range(n)]

    ans = 0
    new_arr = [0] * n

    for i in range(n):
        if arr2[i] == 0:
            new_arr[i] = arr1[i]

        else:
            ans += arr1[i]

    total = sum(new_arr[:k])
    mx = total

    j = 0
    for i in range(k, n):
        total -= new_arr[j]
        total += new_arr[i]
        if total > mx:
            mx = total
        j += 1

    result = mx + ans
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic call
    main(10)