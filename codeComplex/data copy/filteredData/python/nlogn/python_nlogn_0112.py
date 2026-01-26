def main(n):
    # 生成确定性输入：长度为 n 的整数列表
    # 这里使用简单的算术构造：a[i] = (i * 3 + 1) % (n + 7)
    l = [(i * 3 + 1) % (n + 7) for i in range(n)]

    m = l[:]
    m.sort()
    f = 1
    c = 0
    for i in range(n):
        if l[i] != m[i]:
            c += 1
        if c > 2:
            f = 0
            break
    if f == 0:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
if __name__ == "__main__":
    main(10)