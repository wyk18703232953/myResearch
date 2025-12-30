def main(n):
    # 这里根据 n 自动生成测试数据
    # 生成一个长度为 n 的字符串 t，例如循环使用小写字母
    import string
    letters = string.ascii_lowercase
    t = ''.join(letters[i % len(letters)] for i in range(n))

    # 这里设定 k 的值（可根据需要调整生成规则）
    # 示例：令 k = n，规模一致
    k = n

    if n == 1:
        print(t * k)
    else:
        i = len(t) - 1
        while i > 0 and t[-i:] != t[:i]:
            i -= 1
        t2 = t[i:]
        print(t + t2 * (k - 1))


# 示例调用
if __name__ == "__main__":
    # 例如用 n = 5 进行测试
    main(5)