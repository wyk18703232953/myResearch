def main(n):
    # Generate a deterministic tree with n nodes
    # We'll connect node i to node i//2 for i>=2, forming a rooted tree
    dict1 = {}
    for i in range(2, n + 1):
        x = i
        y = i // 2
        if y in dict1:
            dict1[y].append(x)

        else:
            dict1[y] = [x]
        if x in dict1:
            dict1[x].append(y)

        else:
            dict1[x] = [y]

    # Generate a deterministic array "arr" representing some visitation order
    # Use a simple pattern based on n: [1,2,3,...,n]
    arr = list(range(1, n + 1))

    if n == 0:
        # print("No")
        pass
        return

    if arr[0] != 1:
        # print("No")
        pass

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
            # print("No")
            pass

        else:
            # print("Yes")
            pass
if __name__ == "__main__":
    main(10)