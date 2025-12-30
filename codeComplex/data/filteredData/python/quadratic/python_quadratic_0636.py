import random


def main(n):
    # 生成规模为 n 的测试数据，这里生成 1~10*n 的随机正整数
    arr = [random.randint(1, 10 * n) for _ in range(n)]

    arr.sort()
    tmp = [-1] * n
    c = 1
    for i in range(n):
        if tmp[i] != -1:
            continue
        x = arr[i]
        for j in range(i, n):
            if arr[j] % x == 0:
                tmp[j] = c
        c += 1

    # 输出原程序逻辑的结果
    print(c - 1)


if __name__ == "__main__":
    # 示例：调用 main(10)，真实使用时由外部代码指定 n
    main(10)