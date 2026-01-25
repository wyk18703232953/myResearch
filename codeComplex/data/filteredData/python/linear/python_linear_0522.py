def main(n):
    if n <= 1:
        print("No")
        return

    # 构造一棵确定性的树：1-2-3-...-n（链式）
    dict1 = {}
    for i in range(1, n + 1):
        dict1[i] = []
    for x in range(1, n):
        y = x + 1
        dict1[y].append(x)
        dict1[x].append(y)

    # 构造确定性的访问序列 arr，长度为 n
    # 这里设定为从 1 开始的顺序访问：1,2,...,n
    arr = list(range(1, n + 1))

    if arr[0] != 1:
        print("No")
    else:
        j = 0
        i = 1
        flag = 0
        while i < n and j < n:
            if arr[i] in dict1[arr[j]]:
                i += 1
            else:
                j += 1
        if i != n and j == n:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的取值做规模化实验
    main(10)