def main(n):
    # 生成一个确定性的字符串 s，长度为 n
    # 这里使用循环周期为 26 的小写字母序列
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    n = len(s)
    d = {}
    for i in range(n):
        r = ""
        for j in range(i, n):
            r += s[j]
            if r not in d:
                d[r] = 1

            else:
                d[r] += 1
    maxi = 0
    for key in d:
        if d[key] >= 2:
            maxi = max(maxi, len(key))
    # print(maxi)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小做复杂度实验
    main(10)