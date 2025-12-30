import random

def main(n):
    # 随机生成测试数据：
    # t：测试组数，1 <= t <= 10
    # 对于每组：随机生成 1 <= k <= n 的 k，随机生成长度为 n 的字符串 s（只含 'R','G','B'）
    t = random.randint(1, 10)
    rgb = 'RGB' * 1000

    for _ in range(t):
        k = random.randint(1, n)
        s = ''.join(random.choice('RGB') for _ in range(n))

        ans = 3000
        # 遍历三个可能的起点偏移 w
        for w in range(3):
            # 枚举所有长度为 k 的子串起点
            for e in range(n - k + 1):
                temp = 0
                for i in range(k):
                    if s[e + i] != rgb[w + i]:
                        temp += 1
                if temp < ans:
                    ans = temp
        print(ans)


if __name__ == "__main__":
    # 示例调用，n 为规模，可按需修改
    main(10)