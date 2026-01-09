def main(n):
    # 生成确定性的输入数组 a，规模为 n
    # 这里使用简单的算术构造：a[i] = i % (n // 2 + 1)
    if n <= 0:
        a = []

    else:
        mod_base = n // 2 + 1
        a = [i % mod_base for i in range(n)]

    d = set(a)
    if 0 in a:
        result = len(d) - 1

    else:
        result = len(d)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以做时间复杂度实验
    main(10)