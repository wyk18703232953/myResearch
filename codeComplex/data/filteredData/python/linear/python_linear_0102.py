def main(n):
    # 生成确定性的字符串 a 和 b，长度与 n 相关
    # 保证 a 非空，避免与原逻辑不符
    if n <= 0:
        n = 1
    a = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    b = ''.join(chr(ord('z') - (i % 26)) for i in range(max(1, n // 2)))
    b0 = b[0]

    li = []
    for i in range(len(a)):
        li.append(a[:i + 1] + b0)
    li.sort()
    # print(li[0])
    pass
if __name__ == "__main__":
    main(10)