def main(n):
    # 生成长度为 n 的列表，元素在 0..(n//2) 之间重复出现
    if n <= 1:
        # print(0)
        pass
        return
    l = [(i * 2) % (max(1, n // 2)) for i in range(n)]
    ans = 0
    while len(l) > 0:
        a = l[0]
        l = l[1:]
        if a in l:
            ans += l.index(a)
            l.remove(a)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)