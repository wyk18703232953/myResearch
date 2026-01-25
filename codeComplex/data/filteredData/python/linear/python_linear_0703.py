def main(n):
    # 生成长度为 n 的只含 '-' 和 '+' 的字符串
    # 偶数位为 '+', 奇数位为 '-'
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    a = [ch for ch in s]

    x = 0
    for ch in a:
        if ch == '-':
            x = max(0, x - 1)
        else:
            x += 1
    return x


if __name__ == "__main__":
    # 示例调用
    print(main(10))