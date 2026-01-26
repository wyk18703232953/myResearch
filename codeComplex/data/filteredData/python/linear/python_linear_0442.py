def main(n):
    # n is the input scale: the original program reads a single integer n
    if n <= 0:
        # print()
        pass
        return

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
        for v in arr:
            ans.append(v)
    # print(*ans)
    pass
if __name__ == "__main__":
    # example deterministic call; adjust n to change scale
    main(10)