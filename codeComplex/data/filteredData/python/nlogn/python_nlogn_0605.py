import random

def main(n: int):
    # 生成测试数据：m = n，a 为长度为 n 的正整数数组
    m = n
    # 例如生成 1~10*n 范围内的随机整数
    a = [random.randint(1, 10 * n) for _ in range(m)]

    # 原逻辑开始
    # 原代码中是：a = [0] + list(map(int, input().split()))
    a = [0] + a
    a.sort()
    ans = 0
    h = a[-1]
    for i in range(n, 0, -1):
        if a[i - 1] < h - 1:
            ans = ans + a[i] - h + a[i - 1]
            h = a[i - 1]
        else:
            ans = ans + a[i] - 1
            h = h - 1
    print(ans)


if __name__ == "__main__":
    # 示例运行
    main(10)