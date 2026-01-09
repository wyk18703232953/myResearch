def main(n):
    num = n
    layne = [(i * 2 + 3) % (3 * n + 7) + 1 for i in range(num)]
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