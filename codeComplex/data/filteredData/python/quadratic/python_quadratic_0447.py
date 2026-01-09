def main(n):
    # Deterministic generation of input array 'ar' based on n
    # Pattern: mix of increasing, decreasing, and equal segments
    ar = []
    for i in range(n):
        if i % 3 == 0:
            ar.append(i)
        elif i % 3 == 1:
            ar.append(i - 1)

        else:
            ar.append(i - 1)

    if n == 0:
        return

    if n == 1:
        # print(1)
        pass
        return

    if ar[1] > ar[0]:
        li = [1]
    elif ar[1] < ar[0]:
        li = [5]

    else:
        li = [3]

    c = 1
    while c != n:
        j = 0

        if ar[c] > ar[c - 1]:
            while c != n and ar[c] > ar[c - 1]:
                c += 1
                j += 1
            for _ in range(j - 1):
                li.append(li[-1] + 1)
                if li[-1] == 6:
                    # print(-1)
                    pass
                    return
            if c != n and ar[c] == ar[c - 1]:
                li.append(li[-1] + 1)

            else:
                li.append(5)

        elif ar[c] < ar[c - 1]:
            while c != n and ar[c] < ar[c - 1]:
                c += 1
                j += 1
            for _ in range(j - 1):
                li.append(li[-1] - 1)
                if li[-1] == 0:
                    # print(-1)
                    pass
                    return
            if c != n and ar[c] == ar[c - 1]:
                li.append(li[-1] - 1)

            else:
                li.append(1)

        else:
            while c != n and ar[c] == ar[c - 1]:
                c += 1
                j += 1
            for _ in range(j):
                if li[-1] > 3:
                    li.append(li[-1] - 1)

                else:
                    li.append(li[-1] + 1)
            if c != n and ar[c] > ar[c - 1]:
                if li[-2] == 1:
                    li[-1] = 2

                else:
                    li[-1] = 1
            elif c != n and ar[c] < ar[c - 1]:
                if li[-2] == 5:
                    li[-1] = 4

                else:
                    li[-1] = 5

    if max(li) > 5 or min(li) < 1:
        # print(-1)
        pass

    else:
        # print(*li)
        pass
if __name__ == "__main__":
    main(10)