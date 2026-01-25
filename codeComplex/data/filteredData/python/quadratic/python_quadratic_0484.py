def main(n):
    # Interpret n as the length of the arrays
    if n <= 0:
        return

    left = [i % n for i in range(n)]
    right = [((n - 1 - i) * 2) % n for i in range(n)]
    res = [0] * n
    val = n

    if all(not left[i] and not right[i] for i in range(n)):
        print("YES")
        print(' '.join(['1'] * n))
        return

    while not all(not left[i] and not right[i] for i in range(n)):
        zeroSet = set()
        for i in range(n):
            if not left[i] and not right[i] and res[i] == 0:
                zeroSet.add(i)
                res[i] = val
        for v in zeroSet:
            for i in range(v + 1, n):
                if i not in zeroSet and res[i] == 0:
                    left[i] -= 1
            for i in range(v):
                if i not in zeroSet and res[i] == 0:
                    right[i] -= 1
        val -= 1
        if not zeroSet:
            print("NO")
            return

    for i in range(n):
        if not res[i]:
            res[i] = str(val)
        else:
            res[i] = str(res[i])
    if any(i == '0' for i in res):
        print("NO")
        return
    print("YES")
    print(' '.join(res))


if __name__ == "__main__":
    main(10)