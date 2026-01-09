def main(n):
    # 生成一个长度为 n 的确定性字符串
    # 字符由 'a' 到 'z' 循环构成
    string = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    mx = 0

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            m = 0
            while j + m < len(string) and string[i + m] == string[j + m]:
                m += 1
            mx = max(mx, m)

    return mx


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小做时间复杂度实验
    result = main(1000)
    # print(result)
    pass