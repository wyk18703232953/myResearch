def main(n):
    # 解释输入结构：
    # 原程序读取：n, k 以及一个长度为 n 的括号串 s
    # 用 n 作为字符串长度，令 k 为 n//2，保证 0 <= k <= n
    # 生成确定性测试数据：前半部分为 '('，后半部分为 ')'
    k = n // 2
    s = ''.join('(' if i < n // 2 else ')' for i in range(n))
    a = (n - k) // 2
    s1 = s.replace('(', '', a)
    s2 = s1.replace(')', '', a)
    # print(s2)
    pass
if __name__ == "__main__":
    main(10)