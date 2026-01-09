def main(n):
    # Deterministically generate k and p based on n
    if n <= 0:
        return

    # Define k as a function of n to control "window" size
    k = max(1, n // 4)

    # Generate p as a deterministic list of integers in [0, 255]
    # Use simple modular arithmetic
    p = [(i * 37 + 13) % 256 for i in range(n)]

    arr = [[] for _ in range(256)]
    ans = []

    for i in p:
        j = i
        if len(arr[i]) == 0:
            c = 0
            while c < k and j >= 0:
                if len(arr[j]) + c > k:
                    break
                if len(arr[j]) != 0:
                    arr[i].extend(arr[j])
                    break
                arr[j] = arr[i]
                arr[j].append(j)
                j -= 1
                c += 1
            arr[i].sort()
        ans.append(arr[i][0])

    # Keep the original behavior: print the answers space-separated
    # print(*ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)