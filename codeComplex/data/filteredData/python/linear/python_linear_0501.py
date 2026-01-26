def main(n):
    if n <= 0:
        return

    # Deterministically generate input array a of length n
    # Pattern: a[i] = (i * 2 + 3) % 7 - 3  (any fixed formula is fine)
    a = [(i * 2 + 3) % 7 - 3 for i in range(n)]

    res = []
    if n == 1:
        # print(1)
        pass
        return

    i = 0
    if a[0] < a[1]:

        if i >= n - 2:
            res = [1]
            cur = 2

        else:
            if a[i + 1] < a[i + 2]:
                res = [1]
                cur = 2
            elif a[i + 1] > a[i + 2]:
                res = [1]
                cur = 5

            else:
                res = [1]
                cur = 2

    elif a[0] > a[1]:

        if i >= n - 2:
            res = [5]
            cur = 4

        else:
            if a[i + 1] < a[i + 2]:
                res = [5]
                cur = 1
            elif a[i + 1] > a[i + 2]:
                res = [5]
                cur = 4

            else:
                res = [5]
                cur = 4

    else:
        if i >= n - 2:
            res.append(1)
            cur = 2

        else:
            if a[i + 1] < a[i + 2]:
                res.append(2)
                cur = 1
            elif a[i + 1] > a[i + 2]:
                res.append(4)
                cur = 5

            else:
                res.append(2)
                cur = 3

    for i in range(1, n - 1):
        if not (1 <= cur <= 5):
            # print(-1)
            pass
            return
        res.append(cur)
        if a[i] > a[i + 1]:

            if i >= n - 2:
                cur -= 1

            else:
                if a[i + 1] < a[i + 2]:
                    cur = min(cur - 1, 1)
                elif a[i + 1] > a[i + 2]:
                    cur -= 1

                else:
                    cur -= 1

        elif a[i] < a[i + 1]:

            if i >= n - 2:
                cur += 1

            else:
                if a[i + 1] < a[i + 2]:
                    cur += 1
                elif a[i + 1] > a[i + 2]:
                    cur = max(cur + 1, 5)

                else:
                    cur += 1

        else:
            if i >= n - 2:
                if cur != 3:
                    cur = 3

                else:
                    cur = 2

            else:
                if a[i + 1] < a[i + 2]:
                    if cur == 1:
                        cur = 2

                    else:
                        cur = 1
                elif a[i + 1] > a[i + 2]:
                    if cur == 5:
                        cur = 4

                    else:
                        cur = 5

                else:
                    if cur != 3:
                        cur = 3

                    else:
                        cur = 2
    if not (1 <= cur <= 5):
        # print(-1)
        pass
        return
    res.append(cur)
    # print(*res)
    pass
if __name__ == "__main__":
    # Example deterministic run for n = 10
    main(10)