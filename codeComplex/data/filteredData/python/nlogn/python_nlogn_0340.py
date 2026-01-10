def comp(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] in arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[::-1]


def main(n):
    # n 表示字符串数量 t
    t = max(1, n)
    # 构造确定性的字符串数组：
    # 第 i 个字符串为从 0 到 i 的数字连接，如 "0", "01", "012", ...
    arr = ["".join(str(k % 10) for k in range(i + 1)) for i in range(t)]

    arr = comp(arr)

    ans = 1
    for j in range(0, t - 1):
        if arr[j] not in arr[j + 1]:
            ans = 0
            break

    if ans == 0:
        print("NO")
    else:
        print("YES")
        for j in arr:
            print(j)


if __name__ == "__main__":
    main(5)