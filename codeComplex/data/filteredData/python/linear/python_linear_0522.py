def main(n):
    # Generate a deterministic tree with n nodes: a simple path 1-2-3-...-n
    dict1 = {}
    for i in range(1, n):
        x, y = i, i + 1
        if y not in dict1:
            dict1[y] = [x]

        else:
            dict1[y].append(x)
        if x not in dict1:
            dict1[x] = [y]

        else:
            dict1[x].append(y)

    # Generate a deterministic BFS-like traversal array
    # For a path 1-2-3-...-n, the natural BFS from 1 is [1,2,3,...,n]
    arr = list(range(1, n + 1))

    if arr[0] != 1:
        # print("No")
        pass
        return

    j = 0
    i = 1
    while i < n and j < n:
        if arr[i] in dict1.get(arr[j], []):
            i += 1

        else:
            j += 1

    if i != n and j == n:
        # print("No")
        pass

    else:
        # print("Yes")
        pass
if __name__ == "__main__":
    main(10)