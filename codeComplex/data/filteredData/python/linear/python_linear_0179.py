def main(n):
    if n <= 0:
        return 0

    k = max(1, n // 2)

    arr1 = [i + 1 for i in range(n)]
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
    print(result)
    return result


if __name__ == "__main__":
    main(10)