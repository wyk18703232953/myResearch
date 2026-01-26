def main(n):
    # 生成一个确定性的二进制字符串，长度为 n
    # 使用周期模式 '1010...' 以保证包含 '1' 和其他字符
    s = ''.join('1' if i % 2 == 0 else '0' for i in range(n))

    # 原程序逻辑开始
    ans = s.replace('1', '') + '2'
    t = ans.find('2')
    result = ans[:t] + '1' * s.count('1') + ans[t:-1]
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n
    main(10)