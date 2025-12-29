import random

def main(n):
    # 根据 n 生成测试数据，这里生成 n 个 1~10 之间的随机整数
    arr = [random.randint(1, 10) for _ in range(n)]

    # 原逻辑开始
    arr = sorted(arr)
    if arr[-1] == 1:
        arr[-1] = 2
    else:
        arr = [1] + arr[:n-1]
    # 原逻辑结束

    print(*arr)


if __name__ == "__main__":
    # 示例：运行时可自行修改 n
    main(5)