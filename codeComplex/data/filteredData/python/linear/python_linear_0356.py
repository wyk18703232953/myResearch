def main(n):
    # 解释：n 表示输入字符串的长度
    # 构造一个确定性的数字字符串，周期为 0-9
    s = ''.join(str(i % 10) for i in range(n))
    ans = 0
    r, c = 0, 0
    for ch in s:
        r += int(ch)
        c += 1
        if int(ch) % 3 == 0 or r % 3 == 0 or c == 3:
            ans += 1
            r, c = 0, 0
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 以进行规模实验
    main(10000)