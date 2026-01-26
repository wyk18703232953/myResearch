def main(n):
    # 输入结构：
    # 第一行: n, k
    # 第二行: 括号字符串 s
    #
    # 映射规则：
    # - k = n
    # - s 的长度 = max(1, 2 * n)
    # - s 按确定性模式生成: 奇数位 '('，偶数位 ')'，再做简单变换

    if n < 1:
        n = 1

    k = n
    length = 2 * n
    if length < 1:
        length = 1

    # 生成确定性括号串 s
    # 基础模式: "()()()..."
    base = [('(' if i % 2 == 0 else ')') for i in range(length)]
    # 再做一个可重复的确定性置换：根据下标做简单翻转
    for i in range(length):
        if (i * 3 + 1) % 5 == 0:
            base[i] = '(' if base[i] == ')' else ')'
    s = base  # list of characters

    if len(s) > k:
        p = ['('] * (k // 2)
        c = 0
        # 模拟原逻辑：按索引遍历 s，遇到 ')' 就在对应位置插入
        for i in range(len(s)):
            if s[i] == ')':
                if i <= len(p):
                    p.insert(i, ')')

                else:
                    p.append(')')
                c += 1
                if c == k // 2:
                    break
        # print("".join(p))
        pass

    else:
        # print("".join(s))
        pass
if __name__ == "__main__":
    # 示例调用，可按需要修改 n
    main(10)