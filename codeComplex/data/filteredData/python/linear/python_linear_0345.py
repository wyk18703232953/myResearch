from operator import itemgetter

def main(n):
    m = n
    a = []
    for i in range(m):
        x = i % n
        y = (i * 2 + 3) % n
        if x > y:
            x, y = y, x
        a.append((x, y))
    a = sorted(a, key=itemgetter(0, 1))

    ans = [-1] * n
    for l, r in a:
        if ans[l] == -1:
            flag = 1
            for i in range(l, r + 1):
                if flag:
                    ans[i] = 1

                else:
                    ans[i] = 0
                flag ^= 1

        else:
            flag = 1
            x = ans[l]
            for i in range(l, r + 1):
                if flag:
                    ans[i] = x

                else:
                    ans[i] = x ^ 1
                flag ^= 1

    for i in range(n):
        if ans[i] == -1:
            ans[i] = 0

    ans = map(str, ans)
    # print(''.join(ans))
    pass
if __name__ == "__main__":
    main(10)