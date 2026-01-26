def main(n):
    # 生成长度为 n 的确定性字符串 s，由 '+' 和 '-' 组成
    # 规则：索引为偶数的位置为 '+'，索引为奇数的位置为 '-'
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))

    b = 0
    for ch in s:
        if ch == '+':
            b += 1

        else:
            b -= 1
            b = max(b, 0)
    # print(b)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 进行调用
    main(10)