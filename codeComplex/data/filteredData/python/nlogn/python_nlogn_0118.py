def main(n):
    # 生成确定性数组：长度为 n，元素有重复和打乱顺序
    arr = [(i * 7 + 3) % (max(1, n // 2 + 1)) for i in range(n)]

    arr2 = sorted(arr)
    count = 0
    a = 0
    for i in range(n):
        if arr[i] != arr2[i]:
            count += 1
            k = arr[i]
            arr[i] = arr2[i]
            z = arr.index(arr2[i])
            arr[z] = k

        if count > 2:
            a = 1
            break
    if a == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(10)