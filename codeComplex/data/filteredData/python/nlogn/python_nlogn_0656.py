def main(n):
    # Generate deterministic input:
    # Original program:
    # n = int(input())
    # a = list(map(int, input().split()))
    #
    # Here we map n to:
    # - list length = n
    # - a[i] = (i % 3) + 1 to avoid trivial all-zero / all-same cases
    if n <= 0:
        return
    a = [(i % 3) + 1 for i in range(n)]

    a = [[i, a[i]] for i in range(n)]
    a.sort(key=lambda x: x[1], reverse=True)

    ans = []

    index = 0
    cnt = 0
    right_bool = False
    left_bool = False

    for i in range(1, n):
        if a[index][1] == 0:
            print('NO')
            return
        if a[i][1] >= 2:
            ans.append([a[i - 1][0], a[i][0]])
            cnt += 1
            a[i - 1][1] -= 1
            a[i][1] -= 1
        else:
            if not right_bool:
                ans.append([a[i - 1][0], a[i][0]])
                a[i - 1][1] -= 1
                a[i][1] -= 1
                cnt += 1
                right_bool = True
            else:
                ans.append([a[index][0], a[i][0]])
                a[index][1] -= 1
                a[i][1] -= 1
                if not left_bool:
                    cnt += 1
                    left_bool = True
                if a[index][1] == 0:
                    index += 1

    print('YES', cnt)
    print(n - 1)
    for i in range(n - 1):
        print(ans[i][0] + 1, ans[i][1] + 1)


if __name__ == "__main__":
    # example deterministic run for time-complexity experiments
    main(10)