import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里假设：
    # r 在 [3, 3 + 10*n] 内随机生成，l 在 [1, r] 内随机生成
    if n <= 0:
        return

    r = random.randint(3, 3 + 10 * n)
    l = random.randint(1, r)

    # 原逻辑开始
    if l % 2 != 0:
        l += 1
    if l + 2 > r:
        print(-1)
    else:
        print(l, l + 1, l + 2)


if __name__ == "__main__":
    # 示例：调用 main，规模可根据需要调整
    main(10)