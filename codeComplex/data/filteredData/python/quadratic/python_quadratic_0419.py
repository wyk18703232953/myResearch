def main(n):
    # 解释输入结构映射：
    # 原程序输入：
    # 1) 一行："n k"
    # 2) 一行：长度为 n 的字符串 s
    #
    # 这里将参数 n 映射为原程序中的字符串长度 n
    # 为了定义 k 的规模，我们令 k = max(1, n // 2)
    # 字符串 s 则用一个确定性模式构造：周期为 3 的 'abc'
    if n <= 0:
        return

    k = max(1, n // 2)
    s = "".join(chr(ord('a') + (i % 3)) for i in range(n))

    m = -1
    for i in range(0, n - 1):
        ff = 0
        for j in range(0, i + 1):
            if s[j] != s[n - i - 1 + j]:
                ff = 1
                break
        if ff == 0:
            m = i

    # 原程序的输出逻辑
    print(s, end="")
    for _ in range(1, k):
        for j in range(m + 1, n):
            print(s[j], end="")

if __name__ == "__main__":
    # 示例调用：可以根据需要调整 n
    main(10)