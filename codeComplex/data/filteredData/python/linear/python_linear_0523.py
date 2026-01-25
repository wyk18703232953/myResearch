def main(n):
    if n < 2:
        print("No")
        return

    # 构造一棵确定性的树，根为 1，依次连接成链 1-2-3-...-n
    dict1 = {}
    for i in range(1, n):
        x = i
        y = i + 1
        if y in dict1:
            dict1[y].append(x)
        else:
            dict1[y] = [x]
        if x in dict1:
            dict1[x].append(y)
        else:
            dict1[x] = [y]

    # 构造一个确定性的访问序列 arr，满足原程序的典型使用场景：
    # 以 BFS 顺序：1,2,3,...,n
    arr = list(range(1, n + 1))

    if arr[0] != 1:
        print("No")
    else:
        j = 0
        i = 1
        flag = 0
        while i < n and j < n:
            if arr[i] in dict1.get(arr[j], []):
                i += 1
            else:
                j += 1
        if i != n and j == n:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main(10)