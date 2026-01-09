def main(n):
    # n is the input size corresponding to the original single integer input
    x = int(n ** 0.5)
    i = 0
    y = n
    ans = []
    while i < n:
        arr = []
        for _ in range(x):
            if y == 0:
                break
            arr.append(y)
            y -= 1
            i += 1
            if y == 0:
                break
        arr = arr[::-1]
        for j in arr:
            ans.append(j)
    # Keep original behavior: print the permutation
    # print(*ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale the experiment
    main(10)