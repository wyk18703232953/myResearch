import random

def main(n: int):
    # 生成测试数据：随机选择 s，范围为 [0, 10^6 * n]
    # 可根据需要调整生成策略
    s = random.randint(0, 10**6 * max(1, n))

    ans = s // n
    s %= n
    if s != 0:
        ans += 1
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n 的值
    main(10)