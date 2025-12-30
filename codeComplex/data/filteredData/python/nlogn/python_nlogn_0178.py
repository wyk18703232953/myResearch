import random

def main(n):
    # 根据 n 生成测试数据：n 个 (x, w) 对
    # 这里简单生成 [-10^9, 10^9] 范围内的整数
    segments = []
    for _ in range(n):
        x = random.randint(-10**9, 10**9)
        w = random.randint(0, 10**9)
        segments.append((x + w, x - w))  # (end, start)

    segments.sort()

    ans = 0
    t = segments[0][1]
    for end, start in segments:
        if t <= start:
            ans += 1
            t = end

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)