def main(n):
    # n 表示数组长度，k 为窗口大小，这里设为 n//2（至少为 1）
    if n <= 0:
        return
    k = max(1, n // 2)

    # 确定性生成 arr1 和 arr2
    # arr1: 1, 2, 3, ..., n
    arr1 = [i + 1 for i in range(n)]
    # arr2: 0 和 1 的确定性模式，例如 i % 3 == 0 时为 0，否则为 1
    arr2 = [0 if i % 3 == 0 else 1 for i in range(n)]

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

    # print(mx + ans)
    pass
if __name__ == "__main__":
    main(10)