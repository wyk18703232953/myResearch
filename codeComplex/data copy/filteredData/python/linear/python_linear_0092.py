def main(n):
    # n 作为字符串长度规模
    if n <= 0:
        return

    # 构造一个确定性的字符串 s，字符周期为 26 个小写字母
    # 确保对于较大 n 时有多个不同字符，能体现算法逻辑
    base_chars = [chr(ord('a') + i) for i in range(26)]
    s_list = [base_chars[i % 26] for i in range(n)]
    s = "".join(s_list)

    u_set = set()
    for ch in s:
        u_set.add(ch)
    u_cnt = len(u_set)

    d = {}
    j = 0
    ans = 10**9
    for i in range(n):
        while len(d.keys()) < u_cnt and j < n:
            d[s[j]] = d.get(s[j], 0) + 1
            j += 1

        if len(d.keys()) == u_cnt:
            if j - i < ans:
                ans = j - i
        elif j == n:
            break

        d[s[i]] -= 1
        if d[s[i]] == 0:
            del d[s[i]]

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 以做规模实验
    main(10)