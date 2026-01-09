def main(n):
    columns = [i for i in range(1, n + 1)]
    modcolumns = [i % 2 for i in columns]

    previouslist = []

    for i in range(n):
        if len(previouslist) == 0:
            previouslist.append(modcolumns[i])
        elif modcolumns[i] == previouslist[-1]:
            previouslist.pop()

        else:
            previouslist.append(modcolumns[i])

    if len(previouslist) <= 1:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)