def main(n):
    # 生成确定性的输入字符串 s，长度与 n 相关
    # 使用循环模式 'abc' 保证有足够的变化
    base_chars = ['a', 'b', 'c']
    if n <= 0:
        s = ""
    else:
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
    print(result)
    return result


if __name__ == "__main__":
    main(10)