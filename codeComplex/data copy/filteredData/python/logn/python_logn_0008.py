def main(n):
    # Interpret n as upper bound r, and choose a deterministic l <= r
    # For example: l = n // 2, r = n
    l = n // 2
    r = n

    bitafter = -1
    for i in range(60, -1, -1):
        if (l & (1 << i)) != (r & (1 << i)):
            bitafter = i
            break
    res = 0
    while bitafter >= 0:
        res += 1 << bitafter
        bitafter -= 1
    # print(res)
    pass
if __name__ == "__main__":
    # Example scale
    main(10**6)