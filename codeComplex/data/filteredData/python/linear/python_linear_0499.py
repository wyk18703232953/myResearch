def main(n):
    # Generate deterministic input array 'ar' of length n based on n
    # Pattern: strictly increasing, decreasing, equal segments, all from simple arithmetic
    if n <= 0:
        return
    ar = []
    for i in range(n):
        # Construct a piecewise pattern to exercise all branches:
        # segment 1: increasing
        if i < n // 3:
            ar.append(i)
        # segment 2: equal
        elif i < 2 * n // 3:
            ar.append(n // 3)
        # segment 3: decreasing
        else:
            ar.append(2 * n // 3 - (i - 2 * n // 3))
    # Core logic from original program
    if n == 1:
        print(1)
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
                    print(-1)
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
                    print(-1)
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
        print(-1)
    else:
        print(*li)


if __name__ == "__main__":
    main(10)