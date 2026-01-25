def main(n):
    # 生成确定性输入：n 和长度为 n 的整数数组 a
    # 这里选择 a[i] = i % 3 + 1，保证既有 1 也有大于 1 的值
    if n <= 0:
        return
    a = [(i % 3) + 1 for i in range(n)]

    if sum(a) < (2 * n) - 2:
        print("NO")
    else:
        one = []
        rst = []
        for i in range(0, n):
            if a[i] > 1:
                rst.append(i)
            else:
                one.append(i)
        ans = []
        for i in range(1, len(rst)):
            ans.append((rst[i], rst[i - 1]))
            a[rst[i]] -= 1
            a[rst[i - 1]] -= 1
        for i in range(1, len(one)):
            for j in range(0, len(rst)):
                if a[rst[j]] > 0:
                    a[rst[j]] -= 1
                    ans.append((rst[j], one[i]))
                    break
        if len(one):
            for i in range(len(rst) - 1, -1, -1):
                if a[rst[i]] > 0:
                    ans.append((rst[i], one[0]))
                    break
        siz = min(len(one) + len(rst), 2 + len(rst)) - 1
        print("YES", siz)
        print(len(ans))
        for u, v in ans:
            print(u + 1, v + 1)


if __name__ == "__main__":
    main(10)