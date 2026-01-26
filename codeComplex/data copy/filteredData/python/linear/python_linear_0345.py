from operator import itemgetter

def main(n):
    if n <= 0:
        # print("")
        pass
        return

    m = n
    a = []
    for i in range(m):
        l = i % n
        r = (l + (i * 3 + 1) % n) % n
        if l > r:
            l, r = r, l
        a.append((l, r))

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