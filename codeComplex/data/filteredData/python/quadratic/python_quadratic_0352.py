def main(n):
    # 生成确定性输入数据
    # s 和 t 为长度为 n 的字符列表，构造方式保证两者不同但可通过相邻交换变换
    # s: 'a', 'b', 'c', 'a', 'b', 'c', ...
    # t: 'b', 'c', 'a', 'b', 'c', 'a', ...
    base = ['a', 'b', 'c']
    s = [base[i % 3] for i in range(n)]
    t = [base[(i + 1) % 3] for i in range(n)]

    cnt = 0
    ans = []
    f1 = 0
    for i in range(n):
        if s[i] == t[i]:
            continue
        f = 0
        for j in range(i + 1, n):
            if s[j] == t[i]:
                f = 1
                for k in range(j, i, -1):
                    s[k - 1], s[k] = s[k], s[k - 1]
                    ans.append(k)
                break
        if f == 0:
            # print(-1)
            pass
            return

    # print(len(ans))
    pass

    if ans:
        # print(*ans)
        pass
if __name__ == "__main__":
    main(10)