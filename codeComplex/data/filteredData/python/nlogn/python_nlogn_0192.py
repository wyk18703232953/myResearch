import random

def main(n: int):
    # 生成测试数据：n 个 [-10, 10] 之间的随机整数
    b = [random.randint(-10, 10) for _ in range(n)]

    cnt = {}
    ans = 0

    for i in range(n):
        ans += b[i] * i + (-b[i]) * (n - i - 1)

    for i in range(n):
        if (b[i] - 1) in cnt:
            ans -= cnt[b[i] - 1]
        if (b[i] + 1) in cnt:
            ans += cnt[b[i] + 1]
        if b[i] in cnt:
            cnt[b[i]] += 1
        else:
            cnt[b[i]] = 1

    print(ans)


if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(10)