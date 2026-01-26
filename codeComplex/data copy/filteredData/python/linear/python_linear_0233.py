from itertools import groupby

def main(n):
    # n 表示字符串长度
    length = max(1, n)
    # 构造一个确定性的字符串：周期模式 "abxx"
    pattern = "abxx"
    s_chars = [pattern[i % len(pattern)] for i in range(length)]
    s = "".join(s_chars)

    x = [len(list(group)) for key, group in groupby(s) if key == "x"]
    ans = sum(max(0, l - 3 + 1) for l in x)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 的值
    main(10)