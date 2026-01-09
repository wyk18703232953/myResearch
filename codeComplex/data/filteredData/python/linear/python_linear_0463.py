def main(n):
    # 生成确定性字符串，长度由 n 决定
    # 使用循环模式 'abc'，长度为 n
    base_chars = ['a', 'b', 'c']
    s = ''.join(base_chars[i % 3] for i in range(n))
    s = s * 3
    n_len = len(s)
    m, curr = 1, 1
    for i in range(n_len - 1):
        if s[i] != s[i + 1]:
            curr += 1
            if curr > m:
                m = curr

        else:
            curr = 1
    result = min(m, n_len // 3)
    return result

if __name__ == "__main__":
    # 示例调用
    # print(main(10))
    pass