def main(n):
    # 生成确定性输入数据：长度为 n 的整数列表
    # 例如：a = [1, 2, 3, ..., n]
    a = [i + 1 for i in range(n)]
    s = sum(a)
    new = 0
    i = 0
    # 处理特殊情况：当列表为空时，避免索引错误
    if n == 0:
        # print(0)
        pass
        return
    while i < n and 2 * (new + a[i]) < s:
        new += a[i]
        i += 1
    # print(i + 1 if i < n else n)
    pass
if __name__ == "__main__":
    main(10)