def main(n):
    # n 表示列表长度
    if n <= 1:
        print(0)
        return

    # 构造一个确定性的长度为 n 的整数列表
    # 这里使用一个简单的模式：每个数字出现两次，方便触发 index 和 remove
    # 示例：n=6 -> [0,0,1,1,2,2]
    l = [(i // 2) for i in range(n)]

    ans = 0
    while len(l) > 0:
        a = l[0]
        l = l[1:]
        if a in l:  # 原代码假设一定存在 a，这里保持逻辑安全
            ans += l.index(a)
            l.remove(a)
    print(ans)


if __name__ == "__main__":
    main(10)