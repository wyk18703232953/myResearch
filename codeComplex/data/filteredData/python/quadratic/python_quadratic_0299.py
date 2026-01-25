def main(n):
    # n 表示数组长度
    a = [i % 10 for i in range(n)]
    ans = 0
    # 使用列表下标模拟原始的 pop(0) 行为
    while len(a) > 0:
        c = a[0]
        del a[0]
        i = a.index(c)
        ans += i
        del a[i]
    print(ans)


if __name__ == "__main__":
    main(10)