def main(n):
    i = n
    s = [str(k % 3) for k in range(1, i + 1)]

    l = []
    for j in s:
        if not l or int(j) % 2 != l[-1]:
            l.append(int(j) % 2)

        else:
            l.pop()

    if len(l) < 2:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)