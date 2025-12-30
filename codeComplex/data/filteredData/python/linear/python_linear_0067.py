import random

def main(n):
    # 随机生成总时间 s
    s = random.randint(1, 10**5)

    ans = s
    for _ in range(n):
        # 随机生成 f, t（可根据需要调整范围）
        f = random.randint(0, 10**4)
        t = random.randint(0, 10**4)
        ans = max(ans, t + f)

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)