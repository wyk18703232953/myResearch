import random

def main(n):
    # 生成测试数据：
    # n: 字符串长度
    # k: 窗口大小，取 1..n 中的一个值
    # s: 长度为 n 的随机 RGB 字符串
    k = random.randint(1, n)
    s = ''.join(random.choice('RGB') for _ in range(n))

    text = 'RGB' * 2222
    ans = 2222

    for i in range(3):
        p = text[i: k + i]
        for j in range(n - k + 1):
            diff = 0
            for l in range(j, j + k):
                if s[l] != p[l - j]:
                    diff += 1
            ans = min(ans, diff)

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次测试运行
    main(10)