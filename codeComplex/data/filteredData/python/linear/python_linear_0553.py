def main(n):
    # 根据 n 确定性生成长度为 n 的数组 a
    # 这里生成一个包含 0 到 n-1 的递增序列
    a = [i for i in range(n)]

    s = 0
    for j, i in enumerate(a):
        if i > s:
            print(j + 1)
            return
        if i == s:
            s += 1
    print(-1)


if __name__ == "__main__":
    # 示例调用，使用 n = 10
    main(10)