def main(n):
    # 生成确定性的字符串输入（原代码未使用其内容，仅保持结构）
    s = "unused_input_string_of_length_" + str(n)

    # 生成长度为 n 的整数列表，元素为 i % 10 + 1（1 到 10 的循环）
    l = [(i % 10) + 1 for i in range(n)]

    # 原始逻辑开始
    l.sort(reverse=True)
    s_val = sum(l)
    x = 0
    c = 0
    for i in l:
        if x <= s_val:
            c += 1
            x += i
            s_val -= i

        else:
            break
    # print(c)
    pass
if __name__ == "__main__":
    # 示例：输入规模 n = 10
    main(10)