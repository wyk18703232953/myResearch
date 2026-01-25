def main(n):
    # 为了保持原程序的输入结构：
    # 第一行：两个整数 n, k
    # 第二行：字符串 s
    #
    # 这里把参数 n 解释为字符串 s 的长度
    # k 设为一个与 n 有关的确定性值，例如 k = n
    # 字符串 s 确定性生成为周期串，增加可重复结构以保证前后缀匹配存在
    if n <= 0:
        return ""

    k = n  # 将输入规模映射为重复次数

    # 构造一个确定性的周期串，长度至少为 1
    base = "abc"
    s_chars = [base[i % len(base)] for i in range(n)]
    s = "".join(s_chars)

    p = len(s) - 1
    while p > 0 and s[:p] != s[-p:]:
        p -= 1

    # 当 p 变为 0 时，s[:0] == s[-0:] == ""，循环会终止
    # 与原程序逻辑保持一致
    result = s + s[p:] * (k - 1)
    print(result)
    return result


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)