def main(n):
    # 生成确定性的输入数据
    # n 表示数组长度
    a = [(i * 2 + 3) % (n // 2 + 1 if n > 1 else 2) for i in range(n)]
    # 原逻辑开始
    a = set(a)
    a = list(sorted(list(a)))
    if len(a) == 1:
        print("NO")
    else:
        print(a[1])


if __name__ == "__main__":
    main(10)