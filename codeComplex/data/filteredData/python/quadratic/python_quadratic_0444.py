def main(n):
    # n: length of lst
    if n <= 0:
        return
    # Deterministically construct lst based on n
    # Pattern: increasing-decreasing-equal cycles for richer behaviour
    lst = []
    for i in range(n):
        if i % 3 == 0:
            lst.append(i // 3)
        elif i % 3 == 1:
            lst.append(i // 3 + 2)

        else:
            lst.append(i // 3 + 2)
    # Core logic from original program
    cur = 1
    if n == 1:
        # print(1)
        pass
        return
    if lst[cur] > lst[cur - 1]:
        a = [1]
    elif lst[cur] < lst[cur - 1]:
        a = [5]

    else:
        a = [3]
    while cur != n:
        cnt = 0
        if lst[cur] > lst[cur - 1]:
            while cur != n and lst[cur] > lst[cur - 1]:
                cnt += 1
                cur += 1
            for _ in range(cnt - 1):
                a.append(a[-1] + 1)
                if a[-1] >= 5:
                    # print(-1)
                    pass
                    return
            if n != cur and lst[cur] == lst[cur - 1]:
                a.append(a[-1] + 1)

            else:
                a.append(5)
        elif lst[cur] < lst[cur - 1]:
            while cur != n and lst[cur] < lst[cur - 1]:
                cnt += 1
                cur += 1
            for _ in range(cnt - 1):
                a.append(a[-1] - 1)
                if a[-1] <= 1:
                    # print(-1)
                    pass
                    return
            if n != cur and lst[cur] == lst[cur - 1]:
                a.append(a[-1] - 1)

            else:
                a.append(1)

        else:
            while cur != n and lst[cur] == lst[cur - 1]:
                cnt += 1
                cur += 1
            for _ in range(cnt - 1):
                if a[-1] < 3:
                    a.append(a[-1] + 1)

                else:
                    a.append(a[-1] - 1)
            if cur != n and lst[cur] > lst[cur - 1]:
                if a[-1] == 1:
                    a.append(2)

                else:
                    a.append(1)

            else:
                if a[-1] == 5:
                    a.append(4)

                else:
                    a.append(5)
    # print(*a)
    pass
if __name__ == "__main__":
    main(10)