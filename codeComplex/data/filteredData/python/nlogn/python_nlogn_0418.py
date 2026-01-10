def main(n):
    # Deterministically generate n intervals [left[i], right[i]]
    # Example pattern: non-overlapping intervals of length 2, shifted by 1
    left = [2 * i for i in range(n)]
    right = [2 * i + 1 for i in range(n)]

    left.sort()
    right.sort()

    i = 0
    j = 0
    count = 1
    ans = [0] * (n + 1)
    max_right = right[-1]
    left.append(max_right + 1)
    right.append(max_right + 2)

    while (i < n) and (j < n):
        while left[i + 1] <= right[j]:
            ans[count] += (left[i + 1] - left[i])
            count += 1
            i += 1
        ans[count] += (right[j] - left[i] + 1)
        i += 1
        count -= 1

        while ((i == n) or (right[j + 1] < left[i])) and (j < n - 1):
            ans[count] += (right[j + 1] - right[j])
            count -= 1
            j += 1
        ans[count] += (left[i] - right[j] - 1)
        j += 1
        count += 1

    for k in range(1, n + 1):
        print(ans[k], end=" ")
    print()


if __name__ == "__main__":
    main(5)