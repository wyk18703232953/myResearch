def main(n):
    # Deterministically generate l and r based on n
    # Input structure: two integer lists of length n
    l = [i % 3 for i in range(n)]
    r = [(n - 1 - i) % 3 for i in range(n)]

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
        # print("YES")
        pass
        for x in ans:
            # print(x, end=' ')
            pass
        # print()
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)