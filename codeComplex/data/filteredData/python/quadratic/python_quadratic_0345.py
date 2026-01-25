def main(n):
    # n 表示字符串长度
    if n <= 0:
        print(-1)
        return

    # 确定性生成两个长度为 n 的小写字母串
    # s: 周期 "abcd"
    # d: 周期 "bcda"
    base_s = "abcd"
    base_d = "bcda"
    s = [base_s[i % 4] for i in range(n)]
    d = [base_d[i % 4] for i in range(n)]

    if sorted(s) != sorted(d):
        print(-1)
        return
    else:
        ans = []
        for i in range(n):
            if s[i] != d[i]:
                ind = -1
                for u in range(i + 1, n):
                    if s[u] == d[i]:
                        ind = u
                        break
                if ind == -1:
                    print(-1)
                    return
                cnt = abs(ind - i)
                s.pop(ind)
                s.insert(i, d[i])
                for _ in range(cnt):
                    if ind > 0:
                        ans.append(ind)
                    else:
                        ans.append(1)
                    ind -= 1
        print(len(ans))
        if ans:
            print(*ans)


if __name__ == "__main__":
    # 示例：用 n=10 运行一次
    main(10)