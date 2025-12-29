import random

def main(n):
    # 随机生成 n 组测试数据，每组两个正整数 a, b
    # 可根据需要调整数据范围
    test_data = []
    for _ in range(n):
        # 生成范围在 1~10^6 的随机整数
        a = random.randint(1, 10**6)
        b = random.randint(1, 10**6)
        test_data.append((a, b))

    # 按照原逻辑处理每组数据并输出结果
    for a, b in test_data:
        if a > b:
            a, b = b, a
        ans = 0
        while a > 0:
            ans += b // a
            b %= a
            a, b = b, a
        print(ans)


if __name__ == "__main__":
    # 示例：运行时可修改这里的 n
    main(5)