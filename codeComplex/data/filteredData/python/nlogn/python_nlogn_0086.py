import random

def main(n: int):
    # 生成测试数据：
    # k: 1 ~ n
    k = random.randint(1, n)

    # scores, times：这里假设分数和时间为 0~100 的随机整数
    scores = [random.randint(0, 100) for _ in range(n)]
    times = [random.randint(0, 100) for _ in range(n)]

    # 原逻辑开始
    sorted_scores = sorted(
        zip(scores, times),
        key=lambda y: (y[0], -y[1]),
        reverse=True
    )

    ans = 1
    i = k - 2
    while i >= 0 and (sorted_scores[i] == sorted_scores[k - 1]):
        ans += 1
        i -= 1

    i = k
    while i < n and (sorted_scores[i] == sorted_scores[k - 1]):
        ans += 1
        i += 1

    print(ans)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的取值进行测试
    main(10)