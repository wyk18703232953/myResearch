def main(n):
    # 确定性生成字符串 s，长度约为 n，由 '1' 和 '2' 组成
    if n <= 0:
        s = ""

    else:
        chars = []
        for i in range(n):
            chars.append('1' if i % 2 == 0 else '2')
        s = ''.join(chars)

    # 原始逻辑开始
    ans = s.replace('1', '') + '2'
    t = ans.find('2')
    # 当 s 中没有 '2' 时，ans 为 "2"，t 为 0，ans[t:-1] 为空串
    result = ans[:t] + '1' * s.count('1') + ans[t:-1]
    # print(result)
    pass
if __name__ == "__main__":
    main(10)