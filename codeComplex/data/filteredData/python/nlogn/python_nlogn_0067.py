def main(n):
    # 根据 n 生成确定性的输入数组 a，规模为 n
    # 例如：a[i] = (i * 3 + 1) % (n + 5) + 1，保证都是正整数
    a = [((i * 3 + 1) % (n + 5)) + 1 for i in range(n)]

    b = sorted(a, reverse=True)
    total = sum(a)
    gain = 0
    num = 0
    for x in range(len(b)):
        gain += b[x]
        num += 1
        if gain > total / 2:
            break
    print(num)


if __name__ == "__main__":
    main(10)