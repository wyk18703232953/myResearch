def main(n):
    # 生成确定性输入：长度为 n 的整数数组
    # 例如：a[i] = (i % 5) + 1，保证有一定重复和变化
    a = [(i % 5) + 1 for i in range(n)]

    # 原始逻辑开始
    a.sort()
    if a[n - 1] == 1:
        a[n - 1] += 1

    else:
        a[n - 1] = 1
    a.sort()
    # print(*a)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行规模实验
    main(10)