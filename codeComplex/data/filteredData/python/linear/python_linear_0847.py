def main(n):
    # Deterministically generate input array of size n
    # Example pattern: arr[i] = (i * 3 + 7) % (n + 5)
    arr = [(i * 3 + 7) % (n + 5) for i in range(n)] if n > 0 else []

    if n == 0:
        # print("NO")
        pass
        return

    maxval = max(arr)
    maxindex = -1
    for i in range(n):
        if arr[i] == maxval:
            maxindex = i
            break

    flag = 0
    temp = maxval
    for i in range(maxindex - 1, -1, -1):
        if temp <= arr[i]:
            flag = 1
            break

        else:
            temp = arr[i]

    temp = maxval
    for i in range(maxindex + 1, n):
        if arr[i] >= temp:
            flag = 1
            break

        else:
            temp = arr[i]

    if flag == 0:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)