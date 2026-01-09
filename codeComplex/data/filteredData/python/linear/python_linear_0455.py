def main(n):
    # 生成测试数据：长度为 n 的括号串，其中前 n//2 个为 '('，剩余为 ')'
    k = n // 2
    s = '(' * k + ')' * (n - k)

    a = (n - k) // 2
    s1 = s.replace('(', '', a)
    s2 = s1.replace(')', '', a)
    # print(s2)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)