def main(n):
    # 生成确定性字符串列表，长度为 n
    # 第 i 个字符串为 "s" + "a"*i ，保证有长度层次和包含关系
    a = ["s" + "a" * i for i in range(1, n + 1)]

    if n == 1:
        print("YES")
        print(a[0])
    else:
        a.sort(key=len)
        for i in range(1, n):
            if a[i - 1] not in a[i]:
                print("NO")
                break
        else:
            print("YES")
            for s in a:
                print(s)


if __name__ == "__main__":
    main(5)