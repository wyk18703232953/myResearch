def main(n):
    # 生成确定性的 s 和 t，长度为 n
    # s: 递增字母序列，从 'a' 开始循环
    # t: 在 s 的基础上做一次相邻交换，保证通常可通过相邻交换恢复
    if n <= 0:
        # print(0)
        pass
        return

    s = [chr(ord('a') + (i % 26)) for i in range(n)]
    t = s[:]  # 先复制
    # 做一次确定性的相邻交换，如果可能的话
    if n > 1:
        # 在位置 pos 和 pos+1 交换
        pos = (n // 2) - 1  # 中间靠左的位置
        if pos < 0:
            pos = 0
        if pos + 1 < n:
            t[pos], t[pos + 1] = t[pos + 1], t[pos]

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
    # 示例调用：可根据需要修改 n
    main(10)