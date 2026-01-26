def main(n):
    if n < 2:
        # print("No")
        pass
        return

    d = {}

    # 构造确定性的树结构：1-2-3-...-n
    for i in range(1, n):
        a = i
        b = i + 1
        if a in d:
            d[a].append(b)

        else:
            d[a] = [b]
        if b in d:
            d[b].append(a)

        else:
            d[b] = [a]

    # 构造确定性的访问数组 array（长度为 n）
    # 这里选择 array = [1, 2, ..., n]
    array = [i for i in range(1, n + 1)]

    flag = 0

    if array[0] == 1:
        i = 1
        j = 0
        while j < n and i < n:
            if array[i] in d.get(array[j], []):
                i += 1

            else:
                j += 1
        if j == n and i != n:
            flag = 1

    else:
        flag = 1

    if flag == 1:
        # print("No")
        pass

    else:
        # print("Yes")
        pass
if __name__ == "__main__":
    # 示例：以 n = 10 作为规模调用
    main(10)