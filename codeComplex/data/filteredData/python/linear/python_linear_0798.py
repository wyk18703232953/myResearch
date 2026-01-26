def main(n):
    # 构造一个确定性的字符串 s，长度至少为 8
    # 格式类似原始程序中使用的 "dxc_xx_xx"（两位块、含数字和字符）
    # 使用 n 来控制可扩展规模：当 n 增大时，字符串中的模式分布变化
    # 基础长度为 8，多余位置按简单规则填充以保持确定性
    base = []
    for i in range(max(8, n)):
        # 位置为偶数时放数字，奇数时放小写字母
        if i % 2 == 0:
            base.append(str((i // 2) % 10))

        else:
            base.append(chr(ord('a') + (i // 2) % 26))
    s = ''.join(base[:max(8, n)])

    ans = 2
    s1 = s[0:2]
    s2 = s[3:5]
    s3 = s[6:8]

    def func(inp):
        ans_inner = 2
        num = int(inp[0])
        c = inp[1]
        ans_inner = min(ans_inner, 2 - int(s.find(str(num + 1) + c) != -1) - int(s.find(str(num + 2) + c) != -1))
        ans_inner = min(ans_inner, 2 - int(s.find(str(num + 1) + c) != -1) - int(s.find(str(num - 1) + c) != -1))
        ans_inner = min(ans_inner, 2 - int(s.find(str(num - 1) + c) != -1) - int(s.find(str(num - 2) + c) != -1))
        ans_inner = min(ans_inner, 3 - s.count(inp))
        return ans_inner

    ans = min(ans, func(s1))
    ans = min(ans, func(s2))
    ans = min(ans, func(s3))
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)