def main(n):
    # Interpret n as the length of arr, with fixed k
    k = 20
    if n <= 0:
        return

    # Generate a deterministic array arr of length n with values in [0, 259]
    # Ensure values are within bounds used in original code (0..259)
    arr = [(i * 7 + 3) % 260 for i in range(n)]

    par = [i for i in range(260)]
    path = [-1 for _ in range(260)]

    for i in range(n):
        j = arr[i]
        if path[j] >= 0:
            par[j] = par[path[j]]
            continue
        jump = 1
        while j > 0 and path[j] == -1 and jump < k:
            path[j] = arr[i]
            j -= 1
            jump += 1
        if arr[i] - par[j] + 1 <= k:
            par[arr[i]] = par[j]
            path[j] = arr[i]

        else:
            par[arr[i]] = par[j + 1]

    for i in range(n):
        # print(par[arr[i]], end=' ')
        pass
    # print()
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(1000)