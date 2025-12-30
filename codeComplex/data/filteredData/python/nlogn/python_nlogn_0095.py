from random import randint

def main(n):
    # 生成参数 a, b（题意中 b 需要满足 1 <= b < n）
    if n < 2:
        # 原逻辑中访问 s[b] 和 s[b-1]，故需 n>=2
        raise ValueError("n must be at least 2")
    a = randint(1, n)      # a 在原程序中未使用，这里随便生成
    b = randint(1, n - 1)  # 保证 b < n，避免 s[b] 越界

    # 根据 n 生成测试数据：n 个整数
    # 数值范围可自行调整，这里设为 [-10^6, 10^6]
    s = [randint(-10**6, 10**6) for _ in range(n)]

    # 原逻辑
    s.sort()
    if s[b - 1] == s[b]:
        print(0)
    else:
        print(s[b] - s[b - 1])


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)