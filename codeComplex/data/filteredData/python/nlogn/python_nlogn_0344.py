def main(n):
    # 生成确定性字符串数组：第 i 个字符串为重复字符 'a' * (i+1)
    # 为了能出现 NO 的情况，当 n > 1 时，把最后一个字符串改为与前一个无包含关系
    arr = ["a" * (i + 1) for i in range(n)]
    if n > 1:
        # 修改倒数第二个和最后一个字符串，使其不具备包含关系
        arr[-1] = "b" * len(arr[-1])
        if len(arr) >= 2 and len(arr[-2]) == len(arr[-1]):
            arr[-2] = "c" * len(arr[-2])

    arr.sort(key=lambda x: len(x))
    flag = False
    for i in range(n - 2, -1, -1):
        if arr[i] not in arr[i + 1]:
            flag = True
            break

    if flag:
        print("NO")
    else:
        print("YES")
        for s in arr:
            print(s)


if __name__ == "__main__":
    main(5)