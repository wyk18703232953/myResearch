def main(n):
    # 映射：n 为两个字符串的长度，分别为 n 和 n
    # 生成确定性字符串 s1 和 s2
    # s1: 循环 'a' 到 'z'
    s1 = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    # s2: 循环 'z' 到 'a' 反向
    s2 = ''.join(chr(ord('z') - (i % 26)) for i in range(n))

    ans = 'z' * 21
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            candidate = s1[:i] + s2[:j]
            if candidate < ans:
                ans = candidate
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)