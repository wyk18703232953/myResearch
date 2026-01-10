def main(n):
    # 生成确定性输入数据：长度为 n 的整数数组
    # 设定数组为 [i % (n // 2 + 1) for i in range(n)]，保证存在重复和可能的次小元素
    if n <= 0:
        print("NO")
        return

    a = [i % (n // 2 + 1) for i in range(n)]

    a.sort()
    ans = 0
    ok = False
    mn = a[0] if a else None
    for i in range(len(a)):
        if a[i] > mn:
            ans = a[i]
            ok = True
            break
    if ok:
        print(ans)
    else:
        print("NO")


if __name__ == "__main__":
    main(10)