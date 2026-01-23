def comp(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] in arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[::-1]


def main(n):
    # n 表示字符串数量 t
    t = max(1, n)

    # 生成确定性的字符串数组：
    # 第 i 个字符串为从 1 到 i 的数字连接，如:
    # i=1 -> "1"
    # i=2 -> "12"
    # i=3 -> "123"
    arr = ["".join(str(k) for k in range(1, i + 1)) for i in range(1, t + 1)]

    ans = 1

    arr = comp(arr)

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
    # 示例调用，可根据需要更改 n 以做规模实验
    main(5)