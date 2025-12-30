import random

def main(n):
    # 随机生成初始 s（时间），范围可根据需要调整
    s = random.randint(1, 1000)
    ans = s

    # 随机生成 n 组 (f, t)，模拟原输入数据
    # 这里假设 f, t 都是非负整数，且范围适中
    flights = []
    for _ in range(n):
        f = random.randint(0, s + 500)   # 出发时间或某种时间刻度
        t = random.randint(0, 1000)      # 所需等待或延迟时间
        flights.append((f, t))

    # 原算法逻辑
    for f, t in flights:
        if t > (s - f):
            diff = t - (s - f)
            ans += diff
            s += diff

    print(ans)


if __name__ == "__main__":
    # 可以在此处指定规模 n 测试
    main(5)