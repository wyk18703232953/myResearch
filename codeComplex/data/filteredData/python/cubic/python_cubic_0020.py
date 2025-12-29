def countall(string, substring):
    total = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            total += 1
    return total


def main(n):
    # 这里根据规模 n 生成测试数据：生成长度为 n 的字符串
    # 你可以根据需要修改生成规则
    # 示例：重复 'abc' 直到长度达到 n
    base = "abc"
    s = (base * ((n // len(base)) + 1))[:n]

    allvalues = []
    for i in range(len(s)):
        for j in range(len(s) - 1, i - 1, -1):
            if countall(s, s[i:j + 1]) > 1:
                allvalues.append(j - i + 1)
                break

    try:
        print(max(allvalues))
    except ValueError:
        print(0)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)