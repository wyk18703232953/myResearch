def main(n):
    # Deterministically generate input array of size n
    # Example pattern: arr[i] = i % 50  to keep values bounded and allow duplicates
    arr = [(i * 3) % 100 for i in range(n)]
    
    arr.sort()
    s = set(arr)
    flag = False

    # Original logic: first try to find triplet
    for ele in arr:
        for i in range(31):
            if (ele - (1 << i)) in s and (ele + (1 << i)) in s:
                ans = [ele, ele - (1 << i), ele + (1 << i)]
                flag = True
                break
        if flag:
            break

    if flag:
        print(3)
        print(*ans)
        return

    # If no triplet, try to find pair
    for ele in arr:
        for i in range(31):
            if (ele + (1 << i)) in s:
                ans = [ele, ele + (1 << i)]
                flag = True
                break
        if flag:
            break

    if flag:
        print(2)
        print(*ans)
    else:
        print(1)
        print(arr[0])


if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(1000)