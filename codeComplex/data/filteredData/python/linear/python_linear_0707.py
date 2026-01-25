def main(n):
    # 生成长度为 n 的由'-'和'+'组成的字符串
    # 奇偶位置交替，保证确定性
    s = ''.join('-' if i % 2 == 0 else '+' for i in range(n))

    ans = 10000
    for i in range(0, 105):
        f = True
        x = i
        for c in s:
            if c == '-':
                x -= 1
            else:
                x += 1
            if x < 0:
                f = False
        if f:
            ans = min(ans, x)
    print(ans)


if __name__ == "__main__":
    main(10)