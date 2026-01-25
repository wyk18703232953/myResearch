def main(n):
    # 根据 n 构造确定性输入：长度为 n 的整数数组 ar
    # 构造方式：ar[i] = (i * 2 - 3) // 3，保证有升有降有相等
    if n <= 0:
        return
    ar = [(i * 2 - 3) // 3 for i in range(n)]

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
    # 示例调用：可以根据需要调整 n
    main(10)