def main(n):
    # 生成确定性的输入字符串，长度为 n，字符为 0-9 循环
    s = ''.join(str(i % 10) for i in range(n))

    ans = 0
    r, c = 0, 0
    for ch in s:
        digit = int(ch)
        r += digit
        c += 1
        if digit % 3 == 0 or r % 3 == 0 or c == 3:
            ans += 1
            r, c = 0, 0
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值
    main(10)