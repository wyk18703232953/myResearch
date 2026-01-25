def main(n):
    # 保证 n 至少为 1
    if n <= 0:
        n = 1

    # 确定性生成 l 和 r：
    # l[i] = i % 3, r[i] = (n - i - 1) % 3
    l = [i % 3 for i in range(n)]
    r = [(n - i - 1) % 3 for i in range(n)]

    flag = True
    ans = [n for _ in range(n)]
    check_l = [0 for _ in range(n)]
    check_r = [0 for _ in range(n)]

    for i in range(n):
        ans[i] -= l[i] + r[i]

    for i in range(n):
        cl, cr = 0, 0
        for j in range(i):
            if ans[j] > ans[i]:
                cl += 1
        for j in range(i + 1, n):
            if ans[j] > ans[i]:
                cr += 1
        if cl != l[i] or cr != r[i]:
            flag = False
            break

    mini = min(ans) - 1
    for i in range(n):
        ans[i] -= mini

    if flag:
        print("YES")
        for i in ans:
            print(i, end=' ')
        print()
    else:
        print("NO")


if __name__ == "__main__":
    main(10)