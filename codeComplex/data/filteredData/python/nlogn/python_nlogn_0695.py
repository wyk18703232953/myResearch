import random

def main(n):
    # 生成规模为 n 的测试数据，这里生成 [-10, 10] 范围内的整数
    a = [random.randint(-10, 10) for _ in range(n)]

    # 原逻辑开始
    for i, x in enumerate(a):
        if x >= 0:
            a[i] = -x - 1

    cnt_neg = 0
    for x in a:
        if x < 0:
            cnt_neg += 1

    b = sorted((abs(x), i) for i, x in enumerate(a))
    if cnt_neg % 2 == 1:
        ind = b[n - 1][1]
        a[ind] = -a[ind] - 1

    print(' '.join(map(str, a)))


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)