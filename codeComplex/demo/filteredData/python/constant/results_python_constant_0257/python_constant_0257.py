def main(n):
    # Interpret n as the upper bound for all parameters
    # Generate deterministic parameters based on n
    if n < 4:
        n_use = 4

    else:
        n_use = n

    pos = n_use // 2
    l = max(1, pos - (n_use // 4))
    r = min(n_use, pos + (n_use // 4))
    if l >= r:
        r = min(n_use, l + 1)

    result = abs(pos - l) + r - l + 2
    if l == 1:
        temp = abs(pos - r) + 1
        if temp < result:
            result = temp
    if r == n_use:
        temp = abs(pos - l) + 1
        if temp < result:
            result = temp
    if l == 1 and r == n_use:
        result = 0
    temp = abs(pos - r) + r - l + 2
    if temp < result:
        result = temp
    # print(result)
    pass
if __name__ == "__main__":
    main(10)