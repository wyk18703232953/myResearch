import random

def main(n):
    # 随机生成初始 s
    s = random.randint(0, 100)
    ans = s

    # 随机生成 n 对 (f, t)
    for _ in range(n):
        f = random.randint(0, 100)
        t = random.randint(0, 100)
        if t > (s - f):
            ans += t - (s - f)
            s += t - (s - f)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要调整 n
    main(5)