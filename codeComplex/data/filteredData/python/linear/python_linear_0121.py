def main(n):
    if n < 1:
        print("NO")
        return

    t = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        v = (i % n) + 1
        t[v].append(i + 2)

    flag = True
    for l in t:
        if l != []:
            cnt = 0
            for ele in l:
                if t[ele] == []:
                    cnt += 1
            if cnt < 3:
                flag = False
                break

    if flag:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(10)