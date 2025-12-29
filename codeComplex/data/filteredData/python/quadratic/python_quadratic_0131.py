import random

def main(n: int) -> None:
    # 随机生成 m（1 到 n 之间）
    m = random.randint(1, n)
    # 随机生成 m 个 1..n 的整数，模拟原来 input 的第二行
    nums = [random.randint(1, n) for _ in range(m)]

    # 原逻辑开始
    q = {i: 0 for i in range(1, n + 1)}
    for x in nums:
        if 1 <= x <= n:
            q[x] += 1
    print(min(q.values()))


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)