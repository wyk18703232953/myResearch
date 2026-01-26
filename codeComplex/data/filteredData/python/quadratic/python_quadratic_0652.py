def main(n):
    # 生成确定性输入：长度为 n 的整数数组
    # 这里使用简单的构造：a[i] = i + 1
    a = [i + 1 for i in range(n)]

    a.sort()
    ans = 0
    while len(a) > 0:
        k = a.pop(0)
        a = [i for i in a if i % k != 0]
        ans += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)