def comp(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] in arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[::-1]


def main(n):
    t = n
    arr = []
    # 生成确定性的字符串数组，长度为 t
    # 使用不同模式构造字符串，确保有包含关系与非包含关系
    for i in range(t):
        base = i // 3 + 1
        s = "a" * base + "b" * (i % 5) + "c" * (base % 4)
        arr.append(s)

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
    main(10)