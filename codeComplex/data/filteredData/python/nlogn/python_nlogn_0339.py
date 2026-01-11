def main(n):
    # 生成确定性字符串列表，长度为 n
    # 第 i 个字符串为由字符 'a' 和 'b' 构成，模式可重复扩展
    base_strings = []
    for i in range(1, n + 1):
        # 使字符串长度随 i 增长，保持多样性但确定性
        s = ("ab" * i)[:i + 1]
        base_strings.append(s)

    l = base_strings
    s = sorted(l, key=len)
    for i in range(1, n):
        if s[i - 1] not in s[i]:
            # print("NO")
            pass
            return
    # print("YES")
    pass
    for i in s:
        # print(i)
        pass
if __name__ == "__main__":
    main(5)