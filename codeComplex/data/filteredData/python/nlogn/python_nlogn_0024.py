def main(n):
    # 生成确定性输入：列表长度为 n
    # 元素构造：i % (n//2 + 1)，保证有重复，以及可能出现不同值数量少于 n 的情况
    l = [(i * 2 + 3) % (n // 2 + 1) for i in range(n)]

    l = set(l)
    l = list(l)

    if len(l) <= 1:
        print("NO")
        return

    l.sort()
    print(l[1])


if __name__ == "__main__":
    main(10)