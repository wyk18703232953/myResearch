def main(n):
    # n 表示测试用例数量
    results = []
    for i in range(n):
        # 确定性生成一对 (a, b)，保证 a <= b 且随 i 变化
        a = i
        b = i * 2 + 3

        a1 = a
        if a % 2 == 0:
            a1 += 1
        b1 = b
        if b % 2 == 0:
            b1 -= 1
        s1 = 0
        if a1 <= b1:
            num = (b1 - a1) // 2 + 1
            s1 = num * (b1 + a1) // 2
            s1 *= -1
        b2 = b
        a2 = a
        if a % 2 == 1:
            a2 += 1
        if b % 2 == 1:
            b2 -= 1
        s2 = 0
        if a2 <= b2:
            num = (b2 - a2) // 2 + 1
            s2 = num * (b2 + a2) // 2
        results.append(s1 + s2)
    # 输出所有结果，便于计时实验时有可见输出规模
    for x in results:
        # print(x)
        pass
if __name__ == "__main__":
    main(10)