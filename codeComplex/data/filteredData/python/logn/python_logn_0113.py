import random

def main(n):
    # 生成测试数据：根据规模 n 生成 [0, 2^n - 1] 范围内的 l, r，保证 l <= r
    if n <= 0:
        n = 1
    if n > 60:  # 原程序只循环到 60 位
        n = 60
    l = random.randint(0, (1 << n) - 1)
    r = random.randint(l, (1 << n) - 1)

    # 原逻辑开始
    ans = 0

    # 原代码中 R 其实没有被使用
    # R = len(bin(r)) - 2

    for i in range(61):
        if (l & (1 << i)) ^ (r & (1 << i)):
            ans = (1 << (i + 1)) - 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要调整 n
    main(10)