def main(n):
    # n 表示字符串长度
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    ans = 0
    for ch in s:
        if ch == '+':
            ans += 1

        else:
            ans -= 1
        if ans < 0:
            ans = 0
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)