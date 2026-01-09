def main(n):
    # 构造确定性字符串 s，长度为 n
    # 使用循环字符集 'abc'，保证有重复字符分布
    chars = ['a', 'b', 'c']
    s = ''.join(chars[i % 3] for i in range(n))

    c = set(s)
    ln = [0] * n
    for d in c:
        last = -1
        for i, v in enumerate(s):
            if v == d:
                last = i
            if last == -1:
                ln[i] = int(1e9)

            else:
                ln[i] = max(ln[i], i - last + 1)
    # print(min(ln))
    pass
if __name__ == "__main__":
    # 示例规模调用，可按需修改做实验
    main(1000)