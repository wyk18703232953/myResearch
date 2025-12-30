import random

def main(n):
    # 生成测试数据：随机 T 组，每组随机 n、k 和字符串 s
    # 为了符合原逻辑，n 为规模；我们让字符串长度在 [n, n+5] 之间浮动
    T = 5  # 测试数据组数，可按需调整
    random.seed(0)

    results = []
    for _ in range(T):
        # 随机生成本组的 n_i, k_i
        n_i = random.randint(max(1, n), max(1, n + 5))
        k_i = random.randint(1, n_i)
        # 生成长度为 n_i 的 RGB 字符串
        s = ''.join(random.choice('RGB') for _ in range(n_i))

        # 原逻辑开始（对这一组数据求最优答案）
        ans = 10 ** 9
        for i in range(n_i - k_i + 1):
            x = s[i:i + k_i]
            curr = ['R', 'G', 'B']
            for l in range(3):
                m = 0
                z = l
                for ch in x:
                    if ch != curr[z]:
                        m += 1
                    z = (z + 1) % 3
                if m < ans:
                    ans = m
        results.append(ans)

    # 输出所有结果，每行一个
    for v in results:
        print(v)


if __name__ == "__main__":
    # 示例：以 n=10 作为规模运行一次
    main(10)