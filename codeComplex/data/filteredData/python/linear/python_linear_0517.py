def main(n):
    # 确保 n 至少为 1，避免空字符串访问越界
    if n <= 0:
        n = 1

    # 构造两个长度为 n 的字符串 a 和 b
    # a: 周期为 3 的 'A','B','C' 模式
    # b: 在 a 的基础上，每隔 4 位翻转一次为 'X','Y','Z' 模式
    a = ''.join(chr(ord('A') + (i % 3)) for i in range(n))
    b = ''.join(
        (chr(ord('X') + (i % 3)) if (i % 4 == 0) else a[i])
        for i in range(n)
    )

    k = True
    result = 0
    z = None  # 原程序中使用到 z，但未初始化，这里补上确定性初始化
    for i in range(n):
        if a[i] == b[i]:
            if k == False:
                result += 1
            k = True
        else:
            if k == False and z != a[i]:
                result += 1
                k = True
            elif k == False and z == a[i]:
                result += 1
            else:
                k = False
                z = a[i]
    if k == False:
        result += 1
    print(result)


if __name__ == "__main__":
    # 示例：使用 n=10 进行一次确定性运行
    main(10)