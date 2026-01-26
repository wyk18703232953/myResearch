def main(n):
    # Interpret n as the list length; original code used `num` as both count and divisor
    num = n if n > 0 else 1

    # Deterministically generate the list `layne` of length `num`
    # Use a simple arithmetic pattern that depends only on `num`
    layne = [(i * i + num) for i in range(num)]

    mx = max(layne)
    dorf = mx * 2 * num
    indx = 1
    for i in range(num):
        dor = (layne[i] // num) * num
        if (layne[i] % num) - i > 0:
            dor = dor + num + i + 1

        else:
            dor = dor + i + 1
        if dor < dorf:
            dorf = dor
            indx = i + 1
    # print(indx)
    pass
if __name__ == "__main__":
    main(10)